import time
import sys

def welcome_message():
    messages = ["Welcome to the terminal!", "Enjoy your stay!", "Hello, world!", "Python is awesome!"]
    while True:
        for message in messages:
            sys.stdout.write("\r{} - {}".format(time.strftime("%H:%M:%S"), message))
            sys.stdout.flush()
            time.sleep(2)  # Change message every 2 seconds

if __name__ == "__main__":
    welcome_message()
