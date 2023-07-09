from typing import List
from model import Patient, TreatmentProcess, MedicalInfoType, MedicalInfoTypeTreatmentProcessRelation, \
    HealthExpert


class DataSource:
    def get_patients(self) -> List[Patient]:
        return [
            Patient(
                first_name="emad",
                last_name="emami",
                balance=100000                
            ),
            Patient(
                first_name="hosein",
                last_name="bayati",
                balance=100                
            ),
            Patient(
                first_name="sepehr",
                last_name="modir",
                balance=1000                
            ),
        ]

    def get_treatment_processes(self) -> List[TreatmentProcess]:
        return [
            TreatmentProcess(
                name="Diabetes Treatment",
                approvement_status="APPROVED",
                description="""Diabetes is a chronic condition characterized by high levels of sugar (glucose) in the blood, 
                which can lead to a range of complications affecting various organs and systems in the body.""",
                price=10000,
                id=1
            ),
            TreatmentProcess(
                name="Appendicitis Treatment",
                approvement_status="APPROVED",
                description="""Appendicitis is a condition in which the appendix becomes inflamed and swollen, causing pain and 
                tenderness in the lower right abdomen.""",
                price=10,
                id=2
            ),
        ]

    def get_medical_info_types(self) -> List[MedicalInfoType]:
        return [
            MedicalInfoType(
                name="blood-sugar",
                type="string",
                id=1
            ),
            MedicalInfoType(
                name="gender",
                type="string",
                id=2
            )
        ]

    def get_medical_info_type_treatment_process_relations(self) -> List[MedicalInfoTypeTreatmentProcessRelation]:
        return [
            MedicalInfoTypeTreatmentProcessRelation(
                medical_info_type_id=1,
                treatment_process_id=2
            )
        ]

    def get_health_experts(self) -> List[HealthExpert]:
        return [
            HealthExpert(
                first_name="mamad",
                last_name="araghi"
            )
        ]
