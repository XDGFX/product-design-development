#! /usr/bin/env python3


import os
import random
import subprocess
import re
import textwrap
import readline
import sys


def wrapPrint(text, width):
    text = '\n'.join(['\n'.join(textwrap.wrap(line, width,
                                              break_long_words=False, replace_whitespace=False))
                      for line in text.splitlines()])
    print(text)


def clearLine():
    sys.stdout.write("\033[F")
    print(" " * width)
    sys.stdout.write("\033[F")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


readline.parse_and_bind('set horizontal-scroll-mode on')
readline.parse_and_bind('set history-size 0')

subject = ' PRODUCT DESIGN & DEVELOPMENT '

_, width = subprocess.check_output(['stty', 'size']).decode().split()
width = int(width)
title = subject.center(width, "-")

title = title.replace(subject, bcolors.HEADER + subject + bcolors.ENDC)


with open('_questions.txt', 'r') as q:
    questions = q.read().splitlines()
    questions = [x for x in questions if x.strip()]

with open('_motivation.txt', 'r') as m:
    motivations = m.read().splitlines()

i = len(questions)

with open('_counter.txt', 'r+') as c:
    done = c.read().splitlines()
    if len(done) == i:  # Incase all questions done, clear file
        c.truncate(0)
        done = []

print(" SETUP ".center(width, "-").replace("SETUP",
                                           bcolors.HEADER + "SETUP" + bcolors.ENDC))

print("")
print("Question pool: " + str(i))
print("")

# Main loop
while 1:

    selected = random.randint(0, i)

    while str(selected) in done:
        selected = random.randint(0, i)

    os.system('clear')

    print(title)
    print("")
    wrapPrint(questions[selected], width)
    print("")

    print("Type your answer below:")
    print("")

    lines = []
    while True:
        line = input(bcolors.OKBLUE + "> " + bcolors.ENDC)

        clearLine()

        wrapPrint(bcolors.OKBLUE + "> " + bcolors.ENDC + line, width)

        if line:
            lines.append(line)
        else:
            lines.append(line)

            line = input(bcolors.WARNING + "> " + bcolors.ENDC)

            clearLine()

            wrapPrint(bcolors.OKBLUE + "> " + bcolors.ENDC + line, width)

            if line:
                lines.append(line)
            else:
                break
    text = '\n'.join(lines)

    os.system('clear')

    print(" QUESTION ".center(width, "-").replace("QUESTION",
                                                  bcolors.HEADER + "QUESTION" + bcolors.ENDC))
    print("")
    wrapPrint(questions[selected], width)
    print("")

    print(" YOUR ANSWER ".center(width, "-").replace("YOUR ANSWER",
                                                     bcolors.HEADER + "YOUR ANSWER" + bcolors.ENDC))
    print("")
    wrapPrint(text, width)
    print("")

    print(" NOTES ".center(width, "-").replace("NOTES",
                                               bcolors.HEADER + "NOTES" + bcolors.ENDC))
    print("")

    for _, _, files in os.walk("."):
        for file in files:
            identifier = re.search("^(\\d.+?-)", file)

            if identifier:

                filename = re.search(
                    "(\\b" + str(selected + 1) + " )", identifier.group(1))

                if filename:
                    with open(file, 'r') as f:
                        wrapPrint(f.read(), width)

    print("")
    print("-" * width)
    print("")

    wrapPrint(bcolors.OKGREEN + random.choice(motivations) + bcolors.ENDC, width)

    print("")

    with open('_counter.txt', 'a') as c:
        c.write(str(selected) + "\n")

    input(bcolors.OKBLUE + "Press enter to continue... " + bcolors.ENDC)
