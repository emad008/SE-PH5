from typing import List
from .column import Column
from model import Model
import csv
import tempfile
import shutil


class Table:
    def __init__(self, name: str, columns: List[Column] = []) -> None:
        self.name = name
        self.columns = {
            column.name: column for column in columns
        }
        self.last_unused_id = 1
        self.write_columns()

    def get_file_name(self):
        return './data/' + self.name + '.csv'

    def get_column_names(self):
        return self.columns.keys()

    def write_columns(self):
        with open(self.get_file_name(), 'w') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=self.get_column_names())
            writer.writeheader()

    def insert(self, object):
        if object["id"] is None:
            object["id"] = self.last_unused_id
            self.last_unused_id += 1
        else:
            if len(self.select(id=object["id"])) > 0:
                raise Exception("object with this id already exists")

        with open(self.get_file_name(), 'a') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=self.get_column_names())
            writer.writerow(object)
        return object

    def parse_row(self, row):
        parsed_row = {}
        for attr in self.get_column_names():
            parsed_row[attr] = row[attr]
            if parsed_row[attr] == '':
                parsed_row[attr] = None
                continue
            if self.columns[attr].data_type == 'integer':
                parsed_row[attr] = int(parsed_row[attr])
            if self.columns[attr].data_type == 'boolean':
                parsed_row[attr] = parsed_row[attr] == 'True'
        
        return parsed_row

    def update(self, object):
        with open(self.get_file_name(), 'r') as input_file, tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)

            writer.writeheader()

            found = False
            for row in reader:
                row = self.parse_row(row)
                if row['id'] == object['id']:
                    writer.writerow(object)
                    found = True
                else:
                    writer.writerow(row)

            if not found:
                raise Exception("row not found")

            shutil.move(temp_file.name, self.get_file_name())
        
        return object

    def select(self, **attrs):
        with open(self.get_file_name(), 'r') as input_file:
            reader = csv.DictReader(input_file)

            result = []
            for row in reader:
                match = True
                row = self.parse_row(row)
                for attr in attrs:
                    if row[attr] != attrs.get(attr):
                        match = False

                if match:
                    result.append(row)

        return result
