#!/usr/bin/python3

import sys

"""
This script counts and lists the command-line arguments passed to it,
excluding the script name.

It performs the following steps:
1. Counts the number of arguments provided.

2. Displays a message based on the number of arguments:
   - If no arguments are provided, it prints "0 arguments."
   - If exactly one argument is provided, it prints "1 argument:".
   - If multiple arguments are provided,
   it prints "<n> arguments:" where <n> is the count.

3. For each argument, it prints the argument number and its value in
the format:"<position>: <argument>".
"""


length = len(sys.argv) - 1

if length == 0:
    print("{} arguments.".format(length))

elif length == 1:
    print("{} argument:".format(length))

else:
    print("{} arguments:".format(length))


for argument in range(1, len(sys.argv)):

    print("{}: {}".format(argument, sys.argv[argument]))
