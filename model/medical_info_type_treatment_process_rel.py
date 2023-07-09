from .model import Model
from typing import List


class MedicalInfoTypeTreatmentProcessRelation(Model): 
    def __init__(self, medical_info_type_id: int, treatment_process_id: int, id: int = None) -> None:
        self.medical_info_type_id = medical_info_type_id
        self.treatment_process_id = treatment_process_id
        super().__init__(id)

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),   
            medical_info_type_id=self.medical_info_type_id,
            treatment_process_id=self.treatment_process_id,
        )

    @classmethod
    def list_by_treatment_process_id(cls, treatment_process_id: int) -> List["MedicalInfoTypeTreatmentProcessRelation"]:
        return cls.repo.list(
            treatment_process_id=treatment_process_id
        )
