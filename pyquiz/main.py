import numpy
import difflib
import click
from inspect import isfunction, signature
from contextlib import suppress
from random import shuffle

def get_sig(f):
    with suppress(ValueError):
        return signature(f)

def print_question(question):
    click.secho(question, fg="blue")

def print_correct(question):
    click.secho(question, fg="green")

def print_incorrect(question):
    click.secho(question, fg="red")

def diff(a, b):
    return " ".join(difflib.ndiff(a, b))


def quiz_for_function(module, f, sig):
    print_question(f"Function {f.__name__}(...)")

    if (guess := click.prompt("Containing module")) == module:
        print_correct(diff(guess, module))
    else:
        print_incorrect(diff(guess, module))


def quiz_for(module):
    functions = [getattr(module, attr) for attr in dir(module) if isfunction(getattr(module, attr))]
    signatures = [(f, get_sig(f)) for f in functions]
    signatures = [(_, s) for _, s in signatures if s is not None]

    shuffle(signatures)

    for f, sig in signatures:
        quiz_for_function("numpy", f, sig)




def main():
    quiz_for(numpy)