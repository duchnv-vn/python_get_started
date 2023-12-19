class Person:
    first_name = ""
    last_name = ""

    exec()

    def say_hello(self):
        return f"Hello {self.first_name}"


person_1 = Person("Duc", "Huynh")

print(person_1.say_hello())
