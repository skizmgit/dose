from common import utils, calc
from common import command_functions as command
from model.dosebook import DoseBook
from model.medication import (
    Medication,
    MedicationRoute as Route,
    list_medication_types,
    list_medication_routes)

PROMPT = '>>: '
FILE_EXT = '.db'

dosebook = None
dosebook_name: str
strength: float
medication_name: str
med_type: str
route = Route.PO.name
description: str
qty: float


def main():
    global dosebook
    global dosebook_name
    global medication_name
    global strength
    global med_type
    global route
    global description
    global qty
    print("~~~dose v1~~~")
    while True:
        while utils.is_dosebook_empty(dosebook):
            print("Would you like to load a dosebook or create new?"
                  "\nDoseBooks:")
            utils.list_dosebooks()
            ui = input("type 'load <dosebook_name>' or 'new <dosebook_name>'\n"
                       f"{PROMPT}")
            if ui.startswith("load "):
                _, filename = ui.split(maxsplit=1)
                dosebook = utils.read_dosebook(filename + FILE_EXT)
                dosebook_name = filename
                command.print_dosebook(dosebook)
            elif ui.startswith("new "):
                _, db_name = ui.split(maxsplit=1)
                medication_name = input("What is the name of the medication?"
                                        f"\n{PROMPT}")
                qty = utils.get_float(input(f"What quantity of "
                                          f"{medication_name} do you have?"
                                          f"\n{PROMPT}"))
                list_medication_types()
                med_type = input("Select a medication type from the list, "
                                 "or enter a custom one\n"
                                 f"{PROMPT}")
                while not med_type:
                    med_type = input("Select a medication type from the list, "
                                     "or enter a custom one\n"
                                     f"{PROMPT}")
                strength = utils.get_float(input("Enter the strength of the "
                                                 f"medicine in {med_type}"
                                                 f"(s)\n{PROMPT}"))
                list_medication_routes()
                route = input("Select a route of administration from the list"
                              f"\n{PROMPT}")
                description = input("Provide a description/instructions\n"
                                    f"{PROMPT}")
                medication = Medication(medication_name, strength, med_type,
                                        route, description, qty)
                confirm = input("Is this your medication?"
                                f"\n{medication}"
                                f"\n(Y/N)"
                                f"{PROMPT}")
                if confirm.upper() == 'Y':
                    dosebook = DoseBook(medication, [])
                    dosebook_name = db_name
                    utils.write_dosebook(dosebook, dosebook_name + FILE_EXT)
            else:
                print("Syntax error.  please try again.")

        cmd = input(f"{PROMPT}")
        if cmd == "quit" or cmd == "exit" or cmd == "x":
            print("~~~dose v1~~~")
            break
        elif cmd.startswith("load "):
            _, filename = cmd.split(maxsplit=1)
            dosebook = utils.read_dosebook(filename + FILE_EXT)
            dosebook_name = filename
        elif cmd.startswith("save"):
            utils.write_dosebook(dosebook, dosebook_name + FILE_EXT)
        elif cmd.startswith("save "):
            _, filename = cmd.split(maxsplit=1)
            utils.write_dosebook(dosebook, filename + FILE_EXT)
        elif cmd.startswith("delete "):
            _, filename = cmd.split(maxsplit=1)
            utils.delete_dosebook(filename + FILE_EXT)
        elif cmd.lower() == 'list':
            utils.list_dosebooks()
        elif cmd.lower() == 'print':
            command.print_dosebook(dosebook)
        elif cmd.lower() == 'dose':
            command.log_dose(dosebook)
            utils.write_dosebook(dosebook, dosebook_name + FILE_EXT)
        elif cmd.lower() == 'taken':
            utils.print_taken(dosebook)
        elif cmd.lower() == 'rem' or cmd.lower() == 'remaining':
            utils.print_remaining(dosebook)
        else:
            dose_help()


def dose_help():
    """
    Display available commands and their description.
    """
    help_text = """
    Available Commands:
    - load <dosebook>: Load an existing dosebook from a file.
    - save: Save the current dosebook to a file.
    - save <filename>: Save the current dosebook to a new file.
    - delete <filename>: Delete a specific dosebook file.
    - list: List all available dosebooks.
    - print: Print the current dosebook's contents.
    - dose: Log a dose in the current dosebook.
    - taken: Display the total quantity of medication taken.
    - remaining or rem: Display the remaining quantity of medication.
    - quit or exit or x: Exit the application.
    """
    print(help_text)


if __name__ == '__main__':
    main()
