from model.dose import Dose
from model.medication import Medication


class DoseBook:
    def __init__(self,
                 medication: Medication,
                 doses: [Dose]):
        self.medication = medication
        self.doses = doses

    def __str__(self):
        doses_str = "\n".join([str(dose) for dose in self.doses])
        return (f"{self.medication}\n~~~~~~~~\n"
                f"Doses:\n========\n"
                f"{doses_str}")

    def to_dict(self):
        """Serializes the DoseBook object to a dictionary."""
        return {
            'medication': self.medication.to_dict(),
            'doses': [dose.to_dict() for dose in self.doses]
        }

    @classmethod
    def from_dict(cls, data):
        """Deserializes the DoseBook object from a dictionary."""
        medication = Medication.from_dict(
            data['medication'])  # Assuming Medication has a from_dict method
        doses = [Dose.from_dict(dose_data) for dose_data in
                 data['doses']]  # Deserialize each Dose
        return cls(medication=medication, doses=doses)
