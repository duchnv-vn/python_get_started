import csv
from datetime import datetime
from decimal import Decimal


class Person:
    """
    This string is used for document this class
    """

    first_name = ""
    last_name = ""

    def set_states(
        self,
        *,
        first_name,
        last_name,
    ):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        return f"Hello {self.first_name}"


person_1 = Person()

person_1.set_states(first_name="Duc", last_name="Huynh")


class Address:
    house_number = ""
    street_name = ""
    zone_name = ""
    province_name = ""
    city_name = ""

    def __init__(
        self,
        *,
        house_number,
        street_name,
        zone_name,
        city_name,
        province_name,
    ):
        self.house_number = house_number
        self.street_name = street_name
        self.zone_name = zone_name
        self.city_name = city_name
        self.province_name = province_name

    def get_full_address(self) -> str:
        return f"{self.house_number} {self.street_name}, {self.zone_name}, {self.city_name}, {self.province_name}"


address_1 = Address(
    house_number="123",
    street_name="Hoang Dieu 2",
    zone_name="Linh Chieu",
    city_name="Ho Chi Minh",
    province_name="Thu Duc",
)


class DataPoint:
    def __init__(self, *, date, value):
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.value = Decimal(value)


class Forex:
    def __init__(self, *, file_path: str):
        self.file_path = file_path

        self.data = self.process_data()

    @property
    def root_folder(self):
        return "section26-custom-classes/files"

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self.validate_file_path(value)

        self._file_path = f'{self.root_folder}/{value}'

    @property
    def row_number(self):
        return len(self.data)

    def __eq__(self, other: object):
        return isinstan_ce(other, self.__class__) and other.file_path == self.file_path

    def process_data(self):
        with open(self.file_path) as file:
            reader = csv.reader(file)

            next(reader)

            return [
                DataPoint(date=date, value=value)
                for date, value in reader
                if value != "."
            ]

    def validate_file_path(self, value):
        if not (isinstance(value, str)):
            raise ValueError('file_path must be string.')


forex_1 = Forex(file_path="DEXUSEU.csv")
# forex_2 = Forex(file_path="DEXUSEU.csv")

# print(forex_1 == forex_2)

print(forex_1.row_number)
print(forex_1._file_path)
print(forex_1.file_path)
