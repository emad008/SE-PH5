from .model import Model
from .medical_info_type_treatment_process_rel import MedicalInfoTypeTreatmentProcessRelation
from typing import List


class MedicalInfo(Model):
    def __init__(self, patient_id: int, medical_information_type_id: int, data: str, id: int = None) -> None:
        self.patient_id = patient_id
        self.medical_information_type_id = medical_information_type_id
        self.data = data
        super().__init__(id)

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),   
            patient_id=self.patient_id,
            medical_information_type_id=self.medical_information_type_id,
            data=self.data
        )

    # @classmethod
    # def list_by_treatment_process_id(cls, treatment_process_id: int) -> List["MedicalInfo"]:
    #     return [
    #         cls.repo.get(
    #             id=rel.medical_info_type_id
    #         )
            
    #         for rel in MedicalInfoTypeTreatmentProcessRelation.list_by_treatment_process_id(
    #             treatment_process_id=treatment_process_id
    #         )
    #     ]

    def __str__(self) -> str:
        return f"""name: {self.name}, type: {self.type}"""
