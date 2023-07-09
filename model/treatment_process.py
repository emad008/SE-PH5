from .model import Model
from .medical_info_type import MedicalInfoType
from typing import List


class TreatmentProcess(Model):
    def __init__(self, name: str, approvement_status: str, description: str, price: int, reject_reason: str = None, id: int = None) -> None:
        super().__init__(id)
        self.name = name
        self.approvement_status = approvement_status
        self.description = description
        self.reject_reason = reject_reason
        self.price = price

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),
            name=self.name,
            approvement_status=self.approvement_status,
            reject_reason=self.reject_reason,
            description=self.description,
            price=self.price
        )

    def list_medical_info(self) -> List[MedicalInfoType]:
        return MedicalInfoType.list_by_treatment_process_id(
            self.id
        )

    def __str__(self) -> str:
        return f"""
        id: {self.id}
        name: {self.name}
        approvement: {self.approvement_status}
        reject_reason: {self.reject_reason}
        description: {self.description}
        price: {self.price}
        """
