from typing import List, Tuple
from model import Patient, Treatment, HealthExpert, MedicalInfoType


class TreatmentController:   
    def make_new_treatment(self, patient_id: int, treatment_process_id: int, medical_informations: List[Tuple[str, str]]) -> Treatment:
        patient = Patient.get_by_id(id=patient_id)
        patient: Patient
        for medical_info in medical_informations:
            patient.add_medical_info(
                medical_info_type=MedicalInfoType.get_by_name(name=medical_info[0]),
                value=medical_info[1]
            )

        treatment = Treatment(
            patient_id=patient_id,
            treatment_process_id=treatment_process_id,
        )
        saved_treatment = treatment.save()
        saved_treatment: Treatment
        saved_treatment.assign_health_expert(health_expert=HealthExpert.find_non_busy_health_expert())
        return saved_treatment
