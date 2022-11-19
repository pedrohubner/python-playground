class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person_name(self):
        print("Olá, meu nome é ".__add__(self.name))

    def print_person_age(self):
        print("Agora a idade é " + str(self.age))

    def get_person_age_after_birthday(self):
        return self.age + 1


__nome__ = "Pedro"

person = Person("Pedro", 20)

person.print_person_age()
person.get_person_age_after_birthday()
person.print_person_age()
