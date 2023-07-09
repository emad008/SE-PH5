from model import Model
from storage import Database, Table
from typing import Type, List


class Repository:
    def __init__(self, storage: Database, model: Type[Model]) -> None:
        self.storage = storage
        self.model = model

    def get_table_name(self):
        return self.model.get_table_name()

    def get_table(self) -> Table:
        return self.storage.get_table(self.get_table_name())

    def save(self, object: Model) -> Model:
        if object.get_id() is None:
            return self.create(object)

        return self.model.deserialize(**self.get_table().update(object.serialize()))

    def create(self, object: Model) -> Model:
        return self.model.deserialize(**self.get_table().insert(object.serialize()))

    def list(self, **attrs) -> List[Model]:
        return [self.model.deserialize(**values) for values in self.get_table().select(**attrs)]

    def get(self, **attrs) -> Model:
        matched_rows = self.list(**attrs)

        if len(matched_rows) == 0:
            raise Exception(
                f"object of type {self.model.__name__} doest not exists"
            )
        
        if len(matched_rows) > 1:
            raise Exception(
                f"multiple objects of type {self.model.__name__} found"
            )

        return matched_rows[0]
