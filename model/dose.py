from datetime import datetime
from typing import Tuple


def get_datetime_tuple(iso_string):
    try:
        date_obj = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_obj.strftime("%-m/%-d/%Y")
        formatted_time = date_obj.strftime("%-I:%M %p")
        return formatted_date, formatted_time
    except ValueError as e:
        return (f"Error: {str(e)}",)


class Dose:
    def __init__(self,
                 amount: float,
                 comment: str,
                 time: tuple[str, str] = None):
        if time is None:
            time = get_datetime_tuple(datetime.now().isoformat())
        self.time = time
        self.amount = amount
        self.comment = comment

    def __str__(self):
        return (f"{self.time[0]} - {self.time[1]}\n"
                f"\tamount: {self.amount}\n"
                f"\t{self.comment}")

    def to_dict(self):
        """Serializes the Dose object to a dictionary."""
        return {
            'time': self.time,
            'amount': self.amount,
            'comment': self.comment
        }

    @classmethod
    def from_dict(cls, data):
        """Deserializes the Dose object from a dictionary."""
        return cls(
            amount=data['amount'],
            comment=data['comment'],
            time=data['time']
        )
