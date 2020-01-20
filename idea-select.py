import os
import random
import subprocess
import re

subject = ' PRODUCT DESIGN & DEVELOPMENT '

_, width = subprocess.check_output(['stty', 'size']).decode().split()
width = int(width)
title = subject.center(width, "-")


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
        line = input("> ")
        if line:
            lines.append(line)
        else:
            lines.append(line)
            print("! Press enter once more to exit")
            line = input("> ")
            if line:
                lines.append(line)
            else:
                break
    text = '\n'.join(lines)

    os.system('clear')

    print(" QUESTION ".center(width, "-"))
    print("")
    print(questions[selected])
    print("")

    print(" YOUR ANSWER ".center(width, "-"))
    print("")
    print(text)

    print(" NOTES ".center(width, "-"))
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
    input("Press enter to continue... ")
