### Problem
```text
Sometimes in forensics, we run into files that have odd or unknown file extensions. In these cases, it's helpful to look at some of the file format signatures to figure out what they are. We use something called "magic bytes" which are the first few bytes of a file.
What is the ASCII representation of the magic bytes for a VMDK file? The flag format will be 3-4 letters (there are two correct answers).
```
### Solution
> https://en.wikipedia.org/wiki/List_of_file_signatures
```text
4B 44 4D	KDM	0	vmdk	VMDK files
```

![image](https://user-images.githubusercontent.com/60841283/144699870-ff406ba5-65e6-4682-9485-197776c079c8.png)

* Flag :- MetaCTF{KDM}
