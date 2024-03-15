from common.utils import get_float, print_remaining, print_taken, write_dosebook
from common.calc import taken, remaining
from model.dose import Dose
from model.dosebook import DoseBook


def dose():
    amount = get_float(input('\tamount: '))
    comment = input('\tcomment: ')
    return Dose(amount, comment)

def log_dose(dosebook):
    dosebook.doses.append(dose())
    print_taken(dosebook)
    print_remaining(dosebook)

def print_dosebook(dosebook: DoseBook):
    """The current dose logs in the working dosebook"""
    print(dosebook.medication)
    doses = dosebook.doses
    for d in doses:
        print(d)
