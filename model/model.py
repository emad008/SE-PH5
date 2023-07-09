import re

class Model:
    repo = None

    def __init__(self, id: int = None) -> None:
        self.id = id

    @staticmethod
    def camel_to_snake(camel_case):
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
        return snake_case
    
    @classmethod
    def get_table_name(cls):
        return cls.camel_to_snake(cls.__name__)

    @classmethod
    def deserialize(cls, **attrs):
        return cls(**attrs)

    def serialize(self) -> dict:
        return {
            "id": self.get_id()
        }

    @classmethod
    def create(cls, object: "Model"):
        return cls.repo.create(object)

    @classmethod
    def get_by_id(cls, id):
        return cls.repo.get(id=id)

    @classmethod
    def list_all(cls):
        return cls.repo.list()

    def get_id(self):
        return self.id
    
    def set_id(self, id: int):
        self.id = id

    def save(self):
        return self.repo.save(self)

    def __repr__(self) -> str:
        return str(self)
