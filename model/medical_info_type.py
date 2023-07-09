from .model import Model
from .medical_info_type_treatment_process_rel import MedicalInfoTypeTreatmentProcessRelation
from typing import List


class MedicalInfoType(Model):
    def __init__(self, name: str, type: str, id: int = None) -> None:
        self.name = name
        self.type = type
        super().__init__(id)

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),   
            name=self.name,
            type=self.type,
        )

    @classmethod
    def get_by_name(cls, name: str) -> "MedicalInfoType":
        return cls.repo.get(name=name)

    @classmethod
    def list_by_treatment_process_id(cls, treatment_process_id: int) -> List["MedicalInfoType"]:
        return [
            cls.repo.get(
                id=rel.medical_info_type_id
            )
            
            for rel in MedicalInfoTypeTreatmentProcessRelation.list_by_treatment_process_id(
                treatment_process_id=treatment_process_id
            )
        ]

    def __str__(self) -> str:
        return f"""name: {self.name}, type: {self.type}"""
