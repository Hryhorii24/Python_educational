import datetime


# 1
class Person:
    '''Загальні відомості про працівника'''
    def __init__(self, full_name='', year_of_birth=None):
        '''Конструктор приймає вхідні параметри. Імя та прізвище одною строкою та рік нарордження'''
        self.full_name = full_name
        self.year_of_birth = year_of_birth
        # Тут застряг з ексепшеном
        # try:
        #     cuted_full_name = full_name.replace(' ', '')
        #     print(cuted_full_name)
        #     full_name.isalpha()
        #     print('There are numbers')
        # except True:
        #     print('Not a string')
        # print(cuted_full_name.isalpha())
    def get_name(self, name=''):
        '''Окремо ввиодить імя'''
        self.name = name
        self.name = self.full_name.split(' ')[0]
        return 'Name: ' + self.name
    def get_surname(self, surname=''):
        '''Окремо ввиодить прізвище'''
        self.surname = surname
        self.surname = self.full_name.split(' ')[1]
        return 'Surname: ' + self.surname
    def get_obj_age_in(self, year=None):
        '''Якщо нічого не подається на вхід, то виводить вік робітника, або рахує кількість років до сьогодні '''
        self.year = year
        if year == None:
            year = self.year_of_birth
        return f'Years old: {datetime.datetime.now().year - year}'
    def __str__(self):
        '''Виведення на екран через пряме звернення до обєкту'''
        return f'{self.name} {self.surname}, {self.year}'     # От тут от просто не знаходить параметри(


Person1 = Person('John Wick sdf222', 1971)
# print(Person1.get_name())
# print(Person1.get_surname())
# print(Person1.get_obj_age_in(1900))



class Employee(Person):
    '''Отримаує на вхід параметри робітника: Позиція, Досвід, Зарплатня.
    Дозволяє вивести статус працівника та підвищити зарплатню'''
    def __init__(self, Position='', Experience=None, Salary=None):
        '''Вхідні параметри'''
        self.Position = Position
        self.Experience = Experience
        self.Salary = Salary
        self.status = None
        # print(f'Experience: {Experience}, Position: {Position}, Salary: {Salary}')
    def get_status(self):
        '''Визначає статус працівника по градаціям: Джун, Мідл, Сіньйор'''
        if self.Experience < 3:
            self.status = 'Junior'
        elif 3 < self.Experience < 6:
            self.status = 'Middle'
        elif self.Experience > 6:
            self.status = 'Senior'
        return 'Status and Position: ' + self.status + ' ' + self.Position
    def increase_salary(self, addition_sum = 0):
        '''Підвищує зарплатню на вказану суму'''
        self.additon_sum = addition_sum
        self.Salary = self.Salary + addition_sum
        return self.Salary
    def __str__(self):
        '''Виведення на екран через пряме звернення до обєкту'''
        return f'{self.status}, {self.Experience}, {self.Salary}'   # Знову відображається None замість self.status
        # return f'{self.status} Salary: {self.Salary}'


Employee1 = Employee('Developer', 4, 10000)
# print(Employee1)
# print(Employee1.get_status())
# print(Employee1.increase_salary(1234))



class ITEmployee(Employee):
    '''Дає можливість присвоїти скіли певному обєкту'''
    def __init__(self, *args, **kwargs):
        '''Збирає аргументи, створює порожнійс список-заготовку'''
        Employee.__init__(self, *args, **kwargs)
        self.skills = []
    def add_skill(self, new_skill):
        '''Додає елементи в скписок скілів'''
        self.skills.append(new_skill)
    def __str__(self):
        '''Виведення'''
        return f'Skills: {self.skills}'


ITEmployee1 = ITEmployee()
# ITEmployee1.add_skill(['Bla', 'Bla-bla', 2333, "432124fdsffd"])
# print(ITEmployee1.skills)
# print(ITEmployee1)



class square:
    '''На вхід приймає два аргументи, методи можуть обраховати площу і периметр прямокутника'''
    def __init__(self, a=None, b=None):
        '''Наші дві сторони'''
        self.a = a
        self.b = b
    def get_area(self):
        '''Обраховує і повертає площу прямокутника'''
        return self.a*self.b
    def get_perimeter(self):
        '''Обраховує і повертає периметр прямокутника'''
        return self.a*2 + self.b*2
    def __str__(self):
        '''Виведення'''
        return f'{self.a * 2 + self.b * 2}'


square1 = square(10, 20)
# print(square1)
# print(square1.get_area())
# print(square1.get_perimeter())


# 2
class student:
    '''Приймаємо параметри на вхід, методи можуть: додати оцінку в список, вирахувати середню оцінку,
    скільки студент навчається'''
    def __init__(self, name_surname='', speciality='', enter_year=None, marks_list=[]):
        '''Створюємо параметри в конструкторі'''
        self.name_surname = name_surname
        self.speciality = speciality
        self.enter_year = enter_year
        self.marks_list = marks_list
    def add_mark(self, new_mark):
        '''В раніше створений список додається оцінка'''
        self.new_mark = new_mark
        self.marks_list.append(new_mark)
        return self.marks_list
    def average_mark(self):
        '''Вираховується середнє значенния в списку оцінок'''
        return sum(self.marks_list)/len(self.marks_list)
    def years_in_university(self):
        '''Обраховуємо, скільки років студент навчається в університеті, на диний момент'''
        return datetime.datetime.now().year - self.enter_year
    def __str__(self):
        return f'{self.marks_list} {sum(self.marks_list) / len(self.marks_list)} ' \
               f'{datetime.datetime.now().year - self.enter_year}'


student1 = student('Hryhorii Bukar', 'Electronic systems', 2016)
# print(student1.years_in_university())
# print(student1.add_mark(99))
# print(student1.add_mark(61))
# print(student1)



class point:
    '''На вхід приймає два аргументи, методи можуть обраховати відстань до точки від початку координат і
    відстань між дома точками'''
    def __init__(self, X=None, Y=None):
        '''Конструктор приймає два аргументи'''
        self.X = X
        self.Y = Y
        self.range = None
        self.distance = None
    def get_range(self):
        '''Геометрична формула, виводимо відстань до початку координат'''
        return ((self.X - 0)**2 + (self.Y - 0)**2)**0.5
    def get_distance(self, second_point):
        '''Геометрична формула, виводимо відстань між точками'''
        return ((self.X - second_point.X) ** 2 + (self.Y - second_point.Y) ** 2) ** 0.5
    def __str__(self):
        '''Виведення'''
        return f'{self.range}, {self.distance}'  # Знову ж не розумію, чому воно повертає None


point1 = point(0, 4)
point2 = point(0, 10)

print(point1)
print(point1.get_range())
print(point1.get_distance(point2))


