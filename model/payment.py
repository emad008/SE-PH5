from .model import Model
from .patient import Patient


class Payment(Model):
    def __init__(self, patient_id: int, amount: int, id: int = None) -> None:
        super().__init__(id)
        self.amount = amount
        self.patient_id = patient_id

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),
            amount=self.amount,
            patient_id=self.patient_id
        )
    
    def get_patient(self) -> Patient:
        return Patient.get_by_id(id=self.patient_id)

    def decrease_patient_balance(self):
        patient = self.get_patient()
        patient.decrease_balance(self.amount)

    def save(self):
        if self.id is None:
            self.decrease_patient_balance()
        return super().save()
