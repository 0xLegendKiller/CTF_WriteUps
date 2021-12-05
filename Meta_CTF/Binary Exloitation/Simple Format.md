### Problem
```text
I seem to have forgotten my flag ... Can you guess it for me? I get pretty forgetful of what I type so I made sure to always remind myself if I make a mistake so I don't send the same data twice.
The service is located at host1.metaproblems.com 5470. You can use a tool like nc or netcat to access it.
Here's the compiled binary.
Hint: %s is a useful format indeed, but are there other ways to display data as well?
```

### Solution
```bash
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ wget https://metaproblems.com/f632e5ca07b55b84f0bd5edc7ffb2201/fundamentals
--2021-12-05 02:20:08--  https://metaproblems.com/f632e5ca07b55b84f0bd5edc7ffb2201/fundamentals
Resolving metaproblems.com (metaproblems.com)... 35.173.187.102
Connecting to metaproblems.com (metaproblems.com)|35.173.187.102|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16888 (16K)
Saving to: ‘fundamentals’

fundamentals                            100%[============================================================================>]  16.49K  --.-KB/s    in 0s      

2021-12-05 02:20:10 (53.6 MB/s) - ‘fundamentals’ saved [16888/16888]

                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ file fundamentals   
fundamentals: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=fac9d3a9b0e15abd6bb17bcd1d3ac6e84d04a5d4, for GNU/Linux 3.2.0, not stripped
                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ chmod +x fundamentals 
                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ ./fundamentals 
What is your guess?
145
Wow you actually guessed it
```

#### Tried ltrace then --> 100 A's as input
```bash
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ ltrace ./fundamentals
setvbuf(0x7f800c5756c0, 0, 2, 0)                                                                 = 0
setvbuf(0x7f800c5749a0, 0, 2, 0)                                                                 = 0
puts("What is your guess?"What is your guess?
)                                                                      = 20
open("./flag.txt", 0, 00)                                                                        = -1
read(-1 <no return ...>
error: maximum array length seems negative
, "", 100)                                                                                       = -1
read(0lol
, "lol\n", 100)                                                                            = 4
strlen("")                                                                                       = 0
strncmp("lol\n", "", 0)                                                                          = 0
puts("Wow you actually guessed it"Wow you actually guessed it
)                                                              = 28
+++ exited (status 0) +++
                                                                                                                                                           
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ echo "lol" > lol.txt                                                                  
                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$ ./fundamentals      
What is your guess?
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA cat lol.txt
Wow you actually guessed it
                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/meta_ctf/binary]
└─$  cat lol.txt
lol
```
The last command get self executed, so we can assume some sort of command exec on our side.

#### Trying to connect via netcat to get flag.txt
```bash
┌──(kali㉿kali)-[~/ctf/meta_ctf/crypto]
└─$ nc host1.metaproblems.com 5470
What is your guess?
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%s
Your guessed wrong with 
```
Seems like data is getting printed (due to open("./flag.txt", 0, 00) function).
How do we get the flag to our end  ????

---- Incomplete----

