from typing import List
from model import TreatmentProcess


class TreatmentProccessController:
    def list_treatment_processes(self, patient_id: int) -> List[TreatmentProcess]:
        return TreatmentProcess.list_all()

    def get_treatment_process(self, patient_id: int, treatment_process_id: int) -> TreatmentProcess:
        return TreatmentProcess.get_by_id(id=treatment_process_id)
