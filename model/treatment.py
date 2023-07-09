from .model import Model
from .payment import Payment
from .treatment_process import TreatmentProcess
from .health_expert import HealthExpert


class Treatment(Model):
    def __init__(
            self, 
            patient_id: int, 
            treatment_process_id: int, 
            assigned_health_expert_id: int = None,
            payment_id: int = None, 
            length: int = None, 
            id: int = None
        ) -> None:
        super().__init__(id)
        self.patient_id = patient_id
        self.treatment_process_id = treatment_process_id
        self.assigned_health_expert_id = assigned_health_expert_id
        self.payment_id = payment_id
        self.length = length

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),
            patient_id=self.patient_id,
            treatment_process_id=self.treatment_process_id,
            assigned_health_expert_id=self.assigned_health_expert_id,
            payment_id=self.payment_id,
            length=self.length
        )

    def get_treatment_process(self) -> TreatmentProcess:
        return TreatmentProcess.get_by_id(id=self.treatment_process_id)

    def assign_health_expert(self, health_expert: HealthExpert):
        self.assigned_health_expert_id = health_expert.id
        health_expert.you_have_been_assigned()
        self.save()
    
    def pay(self):
        self.payment_id = Payment(
            patient_id=self.patient_id,
            amount=self.get_treatment_process().price
        ).save().id

        self.save()

    def save(self):
        if self.payment_id == None:
            self.pay()
        return super().save()

    def __str__(self) -> str:
        return f"""
        id: {self.id}
        patient_id: {self.patient_id}
        treatment_process_id: {self.treatment_process_id}
        assigned_health_expert_id: {self.assigned_health_expert_id}
        payment_id: {self.payment_id}
        length: {self.length}
        """
