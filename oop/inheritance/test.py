class Person:
    def __init__(self, name, last_name, year, account):
        self.name = name
        self.last_name = last_name
        self.year = year
        self.account = account

    def get_name(self):
        print(f"Ваше имя {self.name}")

    def get_last_name(self):
        print(f"Ваше фамилия {self.last_name}")

    def get_byrthday(self):
        print(f"Ваше год рождения {self.year}")

    def get_account(self):
        print(f"Ваш аккаунт {self.account}")

    def get_person_data(self):
        print(f"Имя: {self.name} Фамилия: {self.last_name} Год рождения {self.year} аккаунт: {self.account}")

class Doctor(Person):
    profession = ''
    def __init__(self,name, last_name,year,account,profession):
        Person.__init__(name, last_name, year, account)
        self.profession = profession

    def get_person_data(self):
        print(f"Имя: {self.name} Фамилия: {self.last_name} Год рождения {self.year} аккаунт: {self.account} Профессия:")

person = Person(name="Alexander", last_name="aaa",year=1990, account="ssss@gmail.com")
person.get_name()
person.get_person_data()

doctor = Doctor(profession="Urolog", name="Doctor", last_name=" Doctors",year=1990,account="aaa@mail.ru")
doctor.get_person_data()
# doctor.name