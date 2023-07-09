from ..datasource import DataSource
from model import TreatmentProcess, Patient, MedicalInfoType, MedicalInfoTypeTreatmentProcessRelation, \
    HealthExpert


class Initializer:
    def __init__(
            self,
            datasource: DataSource
    ) -> None:
        self.datasource = datasource

    def initialize(self):
        for treatment_process in self.datasource.get_treatment_processes():
            TreatmentProcess.create(
                treatment_process
            )
        
        for patient in self.datasource.get_patients():
            Patient.create(
                patient
            )
        
        for medical_info_type in self.datasource.get_medical_info_types():
            MedicalInfoType.create(
                medical_info_type
            )
        
        for medical_info_type_treatment_process_relation in self.datasource.get_medical_info_type_treatment_process_relations():
            MedicalInfoTypeTreatmentProcessRelation.create(
                medical_info_type_treatment_process_relation
            )

        for health_expert in self.datasource.get_health_experts():
            HealthExpert.create(health_expert)
