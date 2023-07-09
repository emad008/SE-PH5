from .model import Model
from .medical_info_type import MedicalInfoType
from .medical_info import MedicalInfo


class Patient(Model):
    def __init__(self, first_name: str, last_name: str, balance: int, id: int = None) -> None:
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def add_medical_info(self, medical_info_type: MedicalInfoType, value: str):
        MedicalInfo(
            patient_id=self.id,
            medical_information_type_id=medical_info_type.id,
            data=value
        ).save()

    def decrease_balance(self, amount: int):
        self.balance -= amount

        if self.balance < 0:
            raise Exception("insufficient balance")

        self.save()

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),   
            first_name=self.first_name,
            last_name=self.last_name,
            balance=self.balance
        )
