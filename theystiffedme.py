import subprocess
import time
from colorama import Fore, Back

# define the command to run the bomber.py script
command = "python3 bomber.py --sms=100 -c=1 -T=10 -v -V"

while True:
    # read the list of phone numbers from the file
    with open("numbers.txt", "r") as f:
        numbers = f.read().splitlines()

    # loop through the list of numbers and run the bomber.py script for each one
    for number in numbers:
        # format the command with the current number
        formatted_command = f'{command} {number}'

        # start the subprocess and capture the output in a log file
        with open("output.txt", "a") as log_file:
            p = subprocess.Popen(formatted_command, shell=True,
                                 stdout=log_file, stderr=subprocess.STDOUT)

            # wait for the program to finish
            p.wait()

               # print the output to the terminal
        with open("output.txt", "r") as log_file:
            output = log_file.read()
            lines = output.splitlines()

            # print the colored output for each line
            for line in lines:
                if "success" in line.lower():
                    print(Back.GREEN + Fore.BLACK + line)
                else:
                    print(Back.RED + Fore.BLACK + line)


        # wait for 5 minutes before moving on to the next number
        time.sleep(220)

    # wait for 3 hours before starting the loop again
    time.sleep(10800)
