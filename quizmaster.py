#! /usr/bin/env python3
"""
quizmaster.py

Test your knowledge using questions saved in `[subject]/`.
Designed to help with exam revision.
Probably only works on macOS and Linux.

Question format:
[subject]/[question_title].txt

# [question: one line]
[answer: all other lines]

XDGFX, 2019
"""

import argparse
import os
import random
import re
import readline
import subprocess
import sys
import textwrap


def wrap_print(text, width):
    """
    Format text to a certain width by wrapping the words.
    """
    text = '\n'.join(['\n'.join(textwrap.wrap(line, width,
                                              break_long_words=False, replace_whitespace=False))
                      for line in text.splitlines()])
    print(text)


def clear_line():
    """
    Clear the current line in the terminal.
    """
    sys.stdout.write("\033[F")
    print(" " * width)
    sys.stdout.write("\033[F")


def safe_filename(input_filename):
    """
    Make a file name that only contains safe charaters
    """
    safechars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -_."
    filename = "".join(
        [character for character in input_filename if character in safechars])
    filename = filename.replace(" ", "_")
    return filename


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Get subject to test on
parser = argparse.ArgumentParser(
    description="quizzmaster - test yourself on different topics")
parser.add_argument(
    'subject', help='the subject (name of the folder) to ask questions from')

args = parser.parse_args()
subject = f" {args.subject.upper().rstrip('/')} "

readline.parse_and_bind('set horizontal-scroll-mode on')
readline.parse_and_bind('set history-size 0')

# Check width of terminal
_, width = subprocess.check_output(['stty', 'size']).decode().split()
width = int(width)
title = subject.center(width, "-")

title = title.replace(subject, bcolors.HEADER + subject + bcolors.ENDC)

question_files = [name for name in os.listdir(
    args.subject) if os.path.isfile(os.path.join(args.subject, name))]
i = len(question_files)

with open('motivation.txt', 'r') as m:
    motivations = m.read().splitlines()


# Main loop
while True:
    # Check which questions have already been asked
    counter_file = f'.counter_{safe_filename(args.subject)}'
    try:
        with open(counter_file, 'r+') as f:
            done = f.read().splitlines()
            if len(done) == i:  # Incase all questions done, clear file
                msg = " ALL QUESTIONS COMPLETE! "
                msg_print = msg.center(width, "-")
                msg_print = msg_print.replace(
                    msg, bcolors.HEADER + msg + bcolors.ENDC)
                input("Press enter to restart... ")
                f.truncate(0)
                done = []

    # Program has not yet been run, need to create a counter file
    except FileNotFoundError:
        open(counter_file, 'w')
        done = []

    selected = random.randint(0, i - 1)

    question_filename = os.path.join(
        args.subject, os.listdir(args.subject)[selected])

    # Reselect question if already completed
    while question_filename in done:
        selected = random.randint(0, i - 1)
        question_filename = os.path.join(
            args.subject, os.listdir(args.subject)[selected])

    question_body = open(question_filename, "r").readlines()

    question = [line for line in question_body if line.startswith("#")][0]
    question_body.remove(question)
    if not question_body[0].strip():
        del question_body[0]
    answer = "".join(question_body)

    os.system('clear')

    print(title)
    print("")
    wrap_print(question, width)
    print("")

    print("Type your answer below:")
    print("")

    lines = []
    while True:
        line = input(bcolors.OKBLUE + "> " + bcolors.ENDC)

        clear_line()

        wrap_print(bcolors.OKBLUE + "> " + bcolors.ENDC + line, width)

        if line:
            lines.append(line)
        else:
            lines.append(line)

            line = input(bcolors.WARNING + "> " + bcolors.ENDC)

            clear_line()

            wrap_print(bcolors.OKBLUE + "> " + bcolors.ENDC + line, width)

            if line:
                lines.append(line)
            else:
                break
    text = '\n'.join(lines)

    os.system('clear')

    print(" QUESTION ".center(width, "-").replace("QUESTION",
                                                  bcolors.HEADER + "QUESTION" + bcolors.ENDC))
    print("")
    wrap_print(question, width)
    print("")

    print(" YOUR ANSWER ".center(width, "-").replace("YOUR ANSWER",
                                                     bcolors.HEADER + "YOUR ANSWER" + bcolors.ENDC))
    print("")
    wrap_print(text, width)
    print("")

    print(" NOTES ".center(width, "-").replace("NOTES",
                                               bcolors.HEADER + "NOTES" + bcolors.ENDC))
    print("")

    # for _, _, files in os.walk(args.subject):
    #     for question in files:
    #         identifier = re.search("^(\\d.+?-)", question)

    #         if identifier:
    #             filename = re.search(
    #                 "(\\b" + str(selected + 1) + " )", identifier.group(1))

    #             if filename:
    #                 with open(question, 'r') as f:
    #                     wrap_print(f.read(), width)
    wrap_print(answer, width)

    print("")
    print("-" * width)
    print("")

    wrap_print(bcolors.OKGREEN + random.choice(motivations) +
               bcolors.ENDC, width)

    print("")
    print(bcolors.OKBLUE +
          "[↪] to continue.\n[x] to put question back into pool.\n[e] to edit the question file.\n[a] to add a new question.\n[q] to quit.\n" + bcolors.ENDC)

    while True:
        response = input(bcolors.OKBLUE + "> " + bcolors.ENDC)

        if response == "e":
            clear_line()
            subprocess.call(["vim", question_filename])

        elif response == "a":
            clear_line()
            filename = os.path.join(args.subject, input("Filename: "))

            while os.path.isfile(filename):
                filename = os.path.join(args.subject, input(
                    "File already exists! Enter new filename: "))

            subprocess.call(["vim", filename])

        elif response == "x":
            break

        elif response == "q":
            raise SystemExit

        elif response == "":
            with open(counter_file, 'a+') as f:
                f.write(question_filename + "\n")
            break

        else:
            clear_line()
