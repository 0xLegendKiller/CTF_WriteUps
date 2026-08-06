#!/usr/bin/env python3

import re
import socket
from datetime import datetime, timedelta, timezone

from skyfield.api import load, EarthSatellite, wgs84


HOST = "154.57.164.65"
PORT = 31038
ELEVATION_LIMIT = 30.0


def recv_until(sock, marker=b"When will it be visible next?>"):
    data = b""

    while marker not in data:
        chunk = sock.recv(4096)

        if not chunk:
            break

        data += chunk

    return data.decode(errors="ignore")


def parse_challenge(text):
    # TLE line 1
    m1 = re.search(
        r"^1 [^\r\n]+$",
        text,
        re.MULTILINE,
    )

    # TLE line 2
    m2 = re.search(
        r"^2 [^\r\n]+$",
        text,
        re.MULTILINE,
    )

    # Ground station
    station = re.search(
        r"\(Lat,Long\):\s*([-0-9.eE+]+)\s*,\s*([-0-9.eE+]+)",
        text,
    )

    if not m1 or not m2 or not station:
        raise ValueError(
            "Could not parse TLE/station from:\n" + text
        )

    line1 = m1.group(0).strip()
    line2 = m2.group(0).strip()

    lat = float(station.group(1))
    lon = float(station.group(2))

    return line1, line2, lat, lon


def elevation_at(satellite, station, ts, dt):
    t = ts.from_datetime(dt)

    difference = satellite - station
    topocentric = difference.at(t)

    alt, az, distance = topocentric.altaz()

    return alt.degrees


def find_crossing(satellite, station, ts, t1, t2, limit):
    """
    Binary-search a threshold crossing between t1 and t2.
    """

    e1 = elevation_at(satellite, station, ts, t1)
    e2 = elevation_at(satellite, station, ts, t2)

    for _ in range(45):
        mid = t1 + (t2 - t1) / 2

        em = elevation_at(satellite, station, ts, mid)

        if (e1 - limit) * (em - limit) <= 0:
            t2 = mid
            e2 = em
        else:
            t1 = mid
            e1 = em

    return t1 + (t2 - t1) / 2


def find_passes(line1, line2, lat, lon, start_time):
    ts = load.timescale()

    satellite = EarthSatellite(
        line1,
        line2,
        "DIGITWIN HTB",
        ts,
    )

    station = wgs84.latlon(lat, lon)

    end_time = start_time + timedelta(hours=24)

    # Sample every 10 seconds.
    step = timedelta(seconds=10)

    current = start_time
    previous_elevation = elevation_at(
        satellite,
        station,
        ts,
        current,
    )

    passes = []

    rise_time = None

    while current < end_time:
        nxt = min(current + step, end_time)

        elevation = elevation_at(
            satellite,
            station,
            ts,
            nxt,
        )

        previous_visible = previous_elevation >= ELEVATION_LIMIT
        current_visible = elevation >= ELEVATION_LIMIT

        # Rising through 30 degrees
        if not previous_visible and current_visible:
            rise_time = find_crossing(
                satellite,
                station,
                ts,
                current,
                nxt,
                ELEVATION_LIMIT,
            )

        # Setting through 30 degrees
        elif previous_visible and not current_visible:
            set_time = find_crossing(
                satellite,
                station,
                ts,
                current,
                nxt,
                ELEVATION_LIMIT,
            )

            if rise_time is not None:
                passes.append((rise_time, set_time))
                rise_time = None

        previous_elevation = elevation
        current = nxt

    return passes


def format_time(dt):
    # Challenge expects UTC ISO-8601 with Z.
    #
    # Round to nearest second.
    if dt.microsecond >= 500_000:
        dt += timedelta(seconds=1)

    dt = dt.replace(microsecond=0)

    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    print(f"[+] Connecting to {HOST}:{PORT}")

    with socket.create_connection((HOST, PORT)) as sock:

        while True:
            text = recv_until(sock)

            if not text:
                print("[!] Connection closed")
                break

            print("\n" + "=" * 70)
            print(text)

            # Detect successful completion
            if any(
                x in text.lower()
                for x in [
                    "congratulations",
                    "flag",
                    "success",
                ]
            ):
                print("[+] Challenge appears complete.")
                break

            try:
                line1, line2, lat, lon = parse_challenge(text)

                print("[+] TLE:")
                print(line1)
                print(line2)

                print(f"[+] Station: {lat}, {lon}")

            except Exception as e:
                print(f"[!] Parsing error: {e}")
                break

            # IMPORTANT:
            #
            # The challenge instance is generated dynamically.
            # Use the current UTC time as the beginning of the
            # 24-hour search window.
            #
            # If the service exposes its challenge time explicitly,
            # this can be replaced with that value.
            start_time = datetime.now(timezone.utc)

            print(
                "[+] Search start:",
                start_time.isoformat(),
            )

            passes = find_passes(
                line1,
                line2,
                lat,
                lon,
                start_time,
            )

            if not passes:
                print("[!] No passes found.")
                answer = ""
            else:
                print("[+] Passes:")

                timestamps = []

                for rise, set_ in passes:
                    rise_s = format_time(rise)
                    set_s = format_time(set_)

                    print(
                        f"    {rise_s} -> {set_s}"
                    )

                    timestamps.extend(
                        [rise_s, set_s]
                    )

                answer = " ".join(timestamps)

            print("[+] Sending:")
            print(answer)

            sock.sendall(
                (answer + "\n").encode()
            )


if __name__ == "__main__":
    main()

