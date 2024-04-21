import json
from enum import Enum

med_types = ['mg', 'mcg', 'mg/mL', 'mcg/mL', 'drop', 'patch']

class MedicationRoute(Enum):
    PO = 'Oral'
    IV = 'Intravenous'
    IM = 'Intramuscular'
    SC = 'Subcutaneous'
    IH = 'Inhalation'
    TO = 'Topical'
    PR = 'Rectal'
    SL = 'Sublingual'

class Medication:
    def __init__(self,
                 name: str,
                 strength: float,
                 med_type: str,
                 route: str,
                 description: str,
                 qty: float):
        self.name = name
        self.strength = strength
        self.med_type = med_type
        self.route = route
        self.description = description
        self.qty = qty

    def __str__(self):
        return (f"{self.name} {self.strength} {self.med_type}(s) {self.route}\n"
                f"\tqty: {self.qty}"
                f"\t{self.description}\n")

    def to_dict(self):
        """Serializes the Medication object to a dictionary."""
        return {
            'name': self.name,
            'strength': self.strength,
            'med_type': self.med_type,
            'route': self.route,
            'description': self.description,
            'qty': self.qty
        }

    @classmethod
    def from_dict(cls, data):
        """Deserializes the Medication object from a dictionary."""
        return cls(
            name=data['name'],
            strength=data['strength'],
            med_type=data['med_type'],
            route=data['route'],
            description=data['description'],
            qty=data['qty']
        )


def list_medication_types():
    """Lists the options for medication type"""
    for med_type in med_types:
        print(med_type)

def list_medication_routes():
    """Lists the options for route of administration"""
    for name, member in MedicationRoute.__members__.items():
        print(f"{name}: {member.value}")
