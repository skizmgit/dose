from model.dosebook import DoseBook


def taken(dosebook: DoseBook) -> float:
    return sum([d.amount for d in  dosebook.doses])


def remaining(dosebook: DoseBook) -> float:
    return dosebook.medication.qty - taken(dosebook)

