import datetime
writer_name = input('ФИО писателя, дата рождения и дата смерти в формате: Имя Фамилия*гггг-мм-дд*гггг-мм-дд*:')

inital_data = writer_name.split('*')

name = inital_data[0]
birth_date = inital_data[1]
death_date = inital_data[2]

birth_date_1 = birth_date.split('-')
death_date_1 = death_date.split('-')

"""""
birth = int(birth_date_1[0])
death = int(death_date_1[0])
"""

birth = datetime.date(int(birth_date_1[0]), int(birth_date_1[1]), int(birth_date_1[2]))
death = datetime.date(int(death_date_1[0]), int(death_date_1[1]), int(death_date_1[2]))

age_days = death - birth
age_years = age_days/365

print(name, age_years)

