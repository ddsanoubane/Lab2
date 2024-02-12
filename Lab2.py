#!/usr/bin/env python3
#Description of Function: A function that uses command line arguements. This function will print two variables used, the script and then the script and variables.
import sys

def print_variables():
    script_variable = sys.argv[0]

    print('Script name: {script_variable}')

    if len(sys.argv) > 1:
        arguments = ' '.join(sys.argv[1:])
        print(f"Script and arguments: {script_variable} {arguments}")
    else:
        print("No arguments used with the script.")

print_variables()

