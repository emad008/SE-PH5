from typing import List
from .table import Table


class Database:
    def __init__(self, tables: List[Table] = []) -> None:
        self.tables = {
            table.name: table for table in tables
        }

    def get_table(self, table_name: str) -> Table:
        return self.tables[table_name]
