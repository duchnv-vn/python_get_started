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

print(address_1.get_full_address())
