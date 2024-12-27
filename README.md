# Keyboard Input Monitor

This program was included in a larger project developing keylogger spyware and detection mechanisms and runs as part of a ```keylogger detector``` program.

### Run program

Two versions of the program are included in the repository: ```key_input_monitor.py```, which can be ran independentally, and ```key_timing_monitor.py```, which has been modified to be packaged and run along another detection method.

To run ```key_input_monitor.py```:

```commandline
python key_input_monitor.py
```

### Keyboard Monitor

The Keyboard Monitor uses ```pynput``` to monitor keyboard activity, specifically the duration of a key presses and the
input delay between individual key presses. This program considers the average typing speed to determine if there is
some keyboard activity writing faster than is humanly expected or if keys are being pressed and released faster
than is standard.

The program will run into it registers an ```Esc``` key input or is manually terminated. When terminated using the 
```Esc``` key, the program will produce an output, similar to below.

```
Average Delay: 0.23482217788696289
Delays: [0.23201990127563477, 0.09738922119140625, 0.12463736534118652, 0.1830155849456787, 0.5370488166809082]

Average Key Press Duration: 0.0786575476328532
Duration: [0.08795619010925293, 0.07336735725402832, 0.06424117088317871, 0.08620810508728027, 0.07198667526245117, 0.08818578720092773]

Low Average Typing Speed: 0.3191489361702128
High Average Typing Speed: 0.2127659574468085
Upperbound: 0.10638297872340426

This input of 0.23482217788696289 appears to be as fast as expected
Suspicious activity has not been detected
```
