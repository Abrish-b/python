"""For the input file object, we use sys.stdin. This is similar to a file, where you can open and close it, just like any other file.
    """
import sys

stdin_fileno = sys.stdin

# Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
for line in stdin_fileno:
    # Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    else:
        print('Message from sys.stdin: ---> {} <---'.format(line))
