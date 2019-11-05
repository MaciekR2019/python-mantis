from model.project import Project
import string
import random


def random_string(maxlen):
    letters = string.ascii_letters + " "* 10
    chosen_letters = "".join([random.choice(letters) for i in range(random.randrange(7, maxlen))])
    return chosen_letters


def project_name(maxlen):
    prefix = "Projekt nr: "
    numbers = string.digits
    name = prefix + "".join([random.choice(numbers) for i in range(random.randrange(5, maxlen))])
    return name

testdata = [Project(name=project_name(20), description=random_string(30))]
