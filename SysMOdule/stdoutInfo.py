"""For the output file object, we use sys.stdout. It is similar to sys.stdin, but it directly displays anything written to it to the Console.
    """

import sys

stdout_fileno = sys.stdout

sample_input = ['Hi', 'Hello from AskPython', 'exit']

for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')
