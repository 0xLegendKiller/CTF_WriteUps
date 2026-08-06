──╼ [★]$ python3 solve.py                                                                                                                                                                                                                                                      
[+] Connecting to 154.57.164.65:31038                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                
======================================================================                                                                                                                                                                                                          
Welcome to the HTB Space Center.                                                                                                                                                                                                                                                
This is your first step into mission operations,so we must start by testing your basics.                                                                                                                                                                                        
Below you'll receive pairs of TLEs for some of our satelites, and locations of some of our groundstations.                                                                                                                                                                      
Your job is to determine the time windows when the satellite will be visible.                                                                                                                                                                                                   
Input the rise and set times for the next 24h (you can skip the current window)                                                                                                                                                                                                 
Input your answers as space separated timestamps,starting with the first time the spacecraft is visible. e.g.:                                                                                                                                                                  
2026-08-06T16:12:45Z 2026-08-06T16:16:36Z 2026-08-06T17:53:01Z 2026-08-06T17:56:35Z 2026-08-06T19:32:48Z 2026-08-06T19:36:39Z 2026-08-07T14:25:16Z 2026-08-07T14:28:54Z                                                                                                         
                                                                                                                                                                                                                                                                                
Assume that a satellite is visible if it is above 30 degrees in the horizon.                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                
Challenge Sat 1                                                                                                                                                                                                                                                                 
TLE:                                                                                                                                                                                                                                                                            
DIGITWIN HTB                                                                                                                                                                                                                                                                    
1 01337U 00000A   26218.60741088+.00000000  00000-0  67580-4 0 708  5                                                                                                                                                                                                           
2 01337  53.9036 114.7006 0024570 300.4786 161.0079 15.62648043 47023                                                                                                                                                                                                           
Station location:                                                                                                                                                                                                                                                               
(Lat,Long): 56.38846919566821,52.18673517172777                                                                                                                                                                                                                                 
                                             
When will it be visible next?>                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                
[+] TLE:                                                                                                                                                                                                                                                                        
1 01337U 00000A   26218.60741088+.00000000  00000-0  67580-4 0 708  5                                                                                                                                                                                                           
2 01337  53.9036 114.7006 0024570 300.4786 161.0079 15.62648043 47023                                                                                                                                                                                                           
[+] Station: 56.38846919566821, 52.18673517172777                                                                                                                                                                                                                               
[+] Search start: 2026-08-06T14:33:59.590066+00:00                                                                                                                                                                                                                              
[+] Passes:                                                                                                                                                                                                                                                                     
    2026-08-07T11:58:07Z -> 2026-08-07T12:00:33Z                                                                                                                                                                                                                                
    2026-08-07T13:33:38Z -> 2026-08-07T13:36:05Z                                                                                                                                                                                                                                
[+] Sending:                                                                                                                                                                                                                                                                    
2026-08-07T11:58:07Z 2026-08-07T12:00:33Z 2026-08-07T13:33:38Z 2026-08-07T13:36:05Z                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                
======================================================================                                                                                                                                                                                                          
Correct!                                                                                                                                                                                                                                                                        
Challenge Sat 2                                                                                                                                                                                                                                                                 
TLE:                                                                                                                                                                                                                                                                            
DIGITWIN HTB                                                                                                                                                                                                                                                                    
1 01337U 00000A   26218.60746065+.00000000  00000-0  22417-5 0 308  2                                                                                                                                                                                                           
2 01337  51.2104 249.7867 0088755  78.0451 193.5500 15.18383532 51299                                                                                                                                                                                                           
Station location:                                                                                                                                                                                                                                                               
(Lat,Long): -36.92876697734215,-12.34838597773717                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                
When will it be visible next?>                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                
[+] TLE:                                                                                                                                                                                                                                                                        
1 01337U 00000A   26218.60746065+.00000000  00000-0  22417-5 0 308  2                                                                                                                                                                                                           
2 01337  51.2104 249.7867 0088755  78.0451 193.5500 15.18383532 51299                                                                                                                                                                                                           
[+] Station: -36.92876697734215, -12.34838597773717                                                                                                                                                                                                                             
[+] Search start: 2026-08-06T14:34:03.964043+00:00                                                                                                                                                                                                                              
[+] Passes:                                                                                                                                                                                                                                                                     
    2026-08-06T17:52:26Z -> 2026-08-06T17:56:28Z                                                                                                                                                                                                                                
    2026-08-07T10:54:40Z -> 2026-08-07T10:58:35Z                                                                                        
[+] Sending:                                                        
2026-08-06T17:52:26Z 2026-08-06T17:56:28Z 2026-08-07T10:54:40Z 2026-08-07T10:58:35Z                                                     


======================================================================
Correct!
Challenge Sat 3
TLE:
DIGITWIN HTB
1 01337U 00000A   26218.60752662+.00000000  00000-0  16479-3 0 385  6
2 01337  97.6648 132.8885 0036167 122.3992  24.7822 15.12167613424370
Station location:
(Lat,Long): 38.012245998331544,129.467941753621



When will it be visible next?>

[+] TLE:
1 01337U 00000A   26218.60752662+.00000000  00000-0  16479-3 0 385  6
2 01337  97.6648 132.8885 0036167 122.3992  24.7822 15.12167613424370
[+] Station: 38.012245998331544, 129.467941753621
[+] Search start: 2026-08-06T14:34:09.645116+00:00
[+] Passes:
    2026-08-06T16:07:26Z -> 2026-08-06T16:08:59Z
    2026-08-07T02:46:37Z -> 2026-08-07T02:50:15Z
[+] Sending:
2026-08-06T16:07:26Z 2026-08-06T16:08:59Z 2026-08-07T02:46:37Z 2026-08-07T02:50:15Z

======================================================================
Correct!
HTB{s4tell1735_4r3_4_d15h_b357_53rv3d_c0ld!}

[!] Parsing error: Could not parse TLE/station from:
Correct!
HTB{s4tell1735_4r3_4_d15h_b357_53rv3d_c0ld!}

