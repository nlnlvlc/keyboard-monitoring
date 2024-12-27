import pynput
from pynput.keyboard import Key, Listener
import time


class KeyTimingMonitor:
    def __init__(self):
        self.start_times = []
        self.end_times = []

    def on_press(self, key):
        self.start_times.append(time.time())

    def on_release(self, key):
        self.end_times.append(time.time())
        if key == Key.esc:
            return False

    def flag(self):
        # based on 40 wpm, at 4.7 cpw, low-end average
        TCP_LOW_AVG = 60 / (40 * 4.7)
        # based on 60 wpm, at 4.7 cpw, high-end average
        TCP_HIGH_AVG = 60 / (60 * 4.7)
        # upper bound of typing realistic typing speed
        TCP_UPPER_BOUND = 60 / (120 * 4.7)

        suspicious = False

        # Calculate duration of each key press
        key_press_duration = [self.end_times[i] - self.start_times[i] for i in range(len(self.end_times))]
        # Calculate delay between key presses
        delays = [self.start_times[i] - self.start_times[i - 1] for i in range(1, len(self.start_times))]

        # Calculate averages
        avg_press = sum(key_press_duration) / len(key_press_duration) if key_press_duration else 0
        avg_delay = sum(delays) / len(delays) if delays else 0

        print(f"\nAverage Delay: {avg_delay} \nDelays: {delays}\n"
              f"\nAverage Key Press Duration: {avg_press} \nDuration: {key_press_duration}\n"
              f"\nLow Average Typing Speed: {TCP_LOW_AVG} \nHigh Average Typing Speed: {TCP_HIGH_AVG}"
              f"\nUpperbound: {TCP_UPPER_BOUND}\n")

        if TCP_HIGH_AVG > avg_delay > TCP_UPPER_BOUND:
            print(f"This input of {avg_delay} appears to be faster than the expected {TCP_HIGH_AVG}")
        elif avg_delay > TCP_LOW_AVG:
            print(f"This input of {avg_delay} appears to be slower than expected {TCP_LOW_AVG}.")
        elif TCP_LOW_AVG >= avg_delay >= TCP_HIGH_AVG:
            print(f"This input of {avg_delay} appears to be as fast as expected")
        elif avg_delay < TCP_UPPER_BOUND:
            print(f"Input speed of {avg_delay} is too fast.")
            suspicious = True

        print(f"Suspicious activity has {'not ' if suspicious == False else ''}been detected")

    def monitor(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

        self.flag()
