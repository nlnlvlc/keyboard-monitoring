import pynput
from pynput.keyboard import Key, Listener
import time

#holds time when keys are pressed
start_time = []
#holds time when keys are released
end_times = []

#average duration of key presses
avg_press = 0
#average delay between key presses
avg_delay = 0
#it takes to type 1 character, on average
#based on 40 wpm, at 4.7 cpw, low end average
tpc_low_avg = 60 / (40 * 4.7)
#based on 60 wpm, at 4.7 cpw, high end average
tpc_high_avg = 60 / (60 * 4.7)
#upper bound of typing realistic typing speed
tpc_upper_bound = 60 / (120 * 4.7)

#holds keys pressed
#uncomment keys for testing
#keys = []

#when key press is registered
def on_press(key):
    global start_time
    #record time key is pressed
    start_time.append(time.time())
    #keys.append(key)

#when key release is registered
def on_release(key):
    global end_times
    #record time key is released
    end_times.append(time.time())
    #type the escape key to exit program
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def flag():

    suspicious = False
    # find duration of each key press, in seconds
    key_press_duration = [end_times[i] - start_time[i] for i in range(len(end_times))]
    # find input delay/speed between key press
    delays = [start_time[i] - start_time[i - 1] for i in range(1, len(start_time))]

    # find average key press duration
    if len(key_press_duration) > 1:
        avg_press = sum(key_press_duration) / len(key_press_duration)
    elif len(key_press_duration) == 1:
        avg_press = key_press_duration[0]
    # find average input delay duration
    if len(delays) > 1:
        avg_delay = sum(delays) / len(delays)
    elif len(delays) == 1:
        avg_delay = delays[0]

    print(f"\nAverage Delay: {avg_delay} \nDelays: {delays}\n"
          f"\nAverage Key Press Duration: {avg_press} \nDuration: {key_press_duration}\n"
          f"\nLow Average Typing Speed: {tpc_low_avg} \nHigh Average Typing Speed: {tpc_high_avg}"
          f"\nUpperbound: {tpc_upper_bound}\n")

    if avg_delay < tpc_high_avg and avg_delay > tpc_upper_bound:
        print(f"This input of {avg_delay} appears to be faster than the expected {tpc_high_avg}")
    elif avg_delay > tpc_low_avg:
        print(f"This input of {avg_delay} appears to be slower than expected {tpc_low_avg}.")
    elif avg_delay <= tpc_low_avg and avg_delay >= tpc_high_avg:
        print(f"This input of {avg_delay} appears to be as fast as expected")
    elif avg_delay < tpc_upper_bound:
        print(f"Input speed of {avg_delay} is too fast.")
        suspicious = True

    print(f"Suspicious activity has {'not ' if suspicious == False else ''}been detected")

if __name__ == '__main__':
    flag()

