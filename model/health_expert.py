from .model import Model
from .medical_info_type import MedicalInfoType
from .medical_info import MedicalInfo


class HealthExpert(Model):
    def __init__(self, first_name: str, last_name: str, is_busy: bool = False, id: int = None) -> None:
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.is_busy = is_busy

    @classmethod
    def find_non_busy_health_expert(cls) -> "HealthExpert":
        non_busy_health_experts = cls.repo.list(is_busy=False)

        if len(non_busy_health_experts) <= 0:
            raise Exception("all health experts are busy")
        
        return non_busy_health_experts[0]

    def you_have_been_assigned(self):
        self.is_busy = True
        self.save()

    def serialize(self) -> dict:
        return dict(
            **super().serialize(),   
            first_name=self.first_name,
            last_name=self.last_name,
            is_busy=self.is_busy
        )
