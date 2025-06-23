# 11. Класс Persona содержит информацию о ФИО человека, дате рождения и адресе человека. Метод подсчитывает количество дней оставшихся до следующего дня рождения. По заданному ФИО человека узнать количество дней оставшихся до следующего дня рождения.

from datetime import date


class Persona:
    def __init__(self, fio, birth_date_str, address):
        self.fio = fio

        self.birth_date = date.fromisoformat(birth_date_str)
        self.address = address

    def days_to_next_birthday(self):
        """Подсчитывает количество дней до следующего дня рождения."""
        today = date.today()

        birthday_this_year = self.birth_date.replace(year=today.year)

        if birthday_this_year < today:

            next_birthday = birthday_this_year.replace(year=today.year + 1)
        else:

            next_birthday = birthday_this_year

        delta = next_birthday - today
        return delta.days


people = [
    Persona("Иванов Иван Иванович", "1990-12-25", "г. Москва"),
    Persona("Петров Петр Петрович", "1985-03-15", "г. Санкт-Петербург"),
]


search_fio = "Петров Петр Петрович"
found = False

for person in people:
    if person.fio == search_fio:
        days_left = person.days_to_next_birthday()
        print(
            f"Для человека '{person.fio}' до следующего дня рождения осталось: {days_left} дней.")
        found = True
        break

if not found:
    print(f"Человек с ФИО '{search_fio}' не найден.")
