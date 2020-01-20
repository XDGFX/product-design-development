import os
import random
import subprocess
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


subject = ' PRODUCT DESIGN & DEVELOPMENT '

_, width = subprocess.check_output(['stty', 'size']).decode().split()
width = int(width)
title = subject.center(width, "-")

title = title.replace(subject, bcolors.HEADER + subject + bcolors.ENDC)


with open('_questions.txt', 'r') as q:
    questions = q.read().splitlines()

questions = [x for x in questions if x.strip()]

i = len(questions)

while 1:

    selected = random.randint(0, i)

    os.system('clear')

    print(title)
    print("")
    print(questions[selected])
    print("")

    print("Type your answer below:")
    print("")

    lines = []
    while True:
        line = input(bcolors.OKBLUE + "> " + bcolors.ENDC)
        if line:
            lines.append(line)
        else:
            lines.append(line)
            # print("! Press enter once more to exit")
            line = input(bcolors.WARNING + "! " + bcolors.ENDC)
            if line:
                lines.append(line)
            else:
                break
    text = '\n'.join(lines)

    os.system('clear')

    print(" QUESTION ".center(width, "-").replace("QUESTION",
                                                  bcolors.HEADER + "QUESTION" + bcolors.ENDC))
    print("")
    print(questions[selected])
    print("")

    print(" YOUR ANSWER ".center(width, "-").replace("YOUR ANSWER",
                                                     bcolors.HEADER + "YOUR ANSWER" + bcolors.ENDC))
    print("")
    print(text)

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
                        print(f.read())

    print("")
    print("-" * width)
    print("")
    input(bcolors.OKGREEN + "Press enter to continue... " + bcolors.ENDC)
