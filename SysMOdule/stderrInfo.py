"""This is similar to sys.stdout because it also prints directly to the Console. But the difference is that it only prints Exceptions and Error messages. (Which is why it is called Standard Error).
    """

import sys

stdout_fileno = sys.stdout
stderr_fileno = sys.stderr

sample_input = ['Hi', 'Hello from AskPython', 'exit']

for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')
    # Tries to add an Integer with string. Raises an exception
    try:
        ip = ip + 100
    # Catch all exceptions
    except:
        stderr_fileno.write('Exception Occurred!\n')

# Print string value to stderr
print("This is standard error", file=sys.stderr)


# Print string variable to stderr
errmessage = "This is standard error"
print(errmessage, file=sys.stderr)


# Print list variable to stderr
errmessage = ["Error", "Number", 123]
print(errmessage, file=sys.stderr)
