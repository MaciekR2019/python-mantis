from model.project import Project
import string
import random


def random_string(maxlen):
    letters = string.ascii_letters
    chosen_letters = "".join([random.choice(letters) for i in range(random.randrange(7, maxlen))])
    return chosen_letters


testdata = Project(name=random_string(15), description=random_string(30))