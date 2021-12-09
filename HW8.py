from Lesson3 import is_year_leap, is_triangle
from HW4 import triangle_type
from HW5 import ITEmployee1
from HW6 import book1
from HW6 import role1
import requests

# Task 1

l1 = [2**n for n in range(20)]
print(l1, end="\n\n")


numbers = [212, 432432, 14124, 5325325, 1242142, 444, 3, 33, 99, 63]
numbers = [number for number in numbers if number%3==0]
numbers.sort()
print(numbers, end="\n\n")


list1 = ["vasya", 11, 0, "1243235345", 999990]
list1 = [num for num in list1 if isinstance(num, int)]
list1.sort()
print(list1, end="\n\n")

def del_num(text):
    rtrn = ''
    for i in text:
        if not i.isdigit():
            rtrn += i
    return rtrn


list1 = ["vasya", 11, 0, "124ffdgfdh3235345", 999990]
list2 = [del_num(w) for w in list1 if isinstance(w, str)]
list2.sort()
print(list2, end="\n\n")


dict1 = {"name": 'G', "surname": 'B', "age": 22, "position": 'QA', "address": 'Vyb 3', "skills": 'reading, writing'}
# print(dict1, end="\n\n")

dict2 = {k: dict1[k] for k in dict1}
print(dict2, end="\n\n")

dict3 = {k: del_num(dict1[k].lower()).strip() for k in dict1 if type(dict1[k]) == str}
print(dict3, end="\n\n")


# Task 2

import pytest


@pytest.fixture
def fixt1():
    print("\nInitialization of fixture")
    fixture = "I am a fixture"
    yield fixture
    print("\nDestroying of fixture")

def test_1(fixt1):
    print('- test_1()')
    assert fixt1

def test_2(fixt1):
    print('- test_2()')
    assert 1 == 1

def test_for_exeption_rise():
    s = "asdasd"
    with pytest.raises(ValueError):
        s.split(1)


@pytest.fixture
def fixt1():
    return is_year_leap(2000)

@pytest.fixture
def fixt2():
    return is_year_leap(1111)

@pytest.fixture
def fixt3():
    return is_year_leap(2004)

@pytest.fixture
def fixt4():
    return is_year_leap(880)


def test1(fixt1):
    print('test1')
    assert fixt1 == "YES"


def test2(fixt2):
    print('test2')
    assert fixt2 == "NO"

def test3(fixt3):
    print('test3')
    assert fixt3 == "YES"

def test4(fixt4):
    print('test4')
    assert fixt4 == "YES"



@pytest.fixture
def fixt5():
    return triangle_type(5, 2, 2)

@pytest.fixture
def fixt6():
    return triangle_type(2, 2, 2)

@pytest.fixture
def fixt7():
    return triangle_type(1, 2, 2)

@pytest.fixture
def fixt8():
    return triangle_type(5, 4, 2)


def test5(fixt5):
    print('test5')
    assert fixt5 == "Not a triangle. Please, try again"

def test6(fixt6):
    print('test6')
    assert fixt6 == "Equilateral triangle"

def test7(fixt7):
    print('test7')
    assert fixt7 == "Isosceles triangle"

def test8(fixt8):
    print('test8')
    assert fixt8 == "Versatile triangle"



@pytest.fixture
def fixt9():
    return ITEmployee1.skills

@pytest.fixture
def fixt10():
    ITEmployee1.add_skill("Tests writing")
    return ITEmployee1.skills

@pytest.fixture
def fixt11():
    ITEmployee1.add_skill("SQL")
    return ITEmployee1.skills



def test9(fixt9):
    print('test9')
    assert fixt9 == []

def test10(fixt10):
    print('test10')
    assert fixt10 == ["Tests writing"]

def test11(fixt11):
    print('test11')
    res = fixt11
    assert fixt11 == ["Tests writing", "SQL"]



@pytest.fixture
def fixt12():
    return book1.create_book()

@pytest.fixture
def fixt13():
    return book1.check_book()

@pytest.fixture
def fixt14():
    book1.put_book(title='TbOOk', author='wiper')
    return book1.check_book()

@pytest.fixture
def fixt15():
    return book1.delete_book()



def test12(fixt12):
    print('test12')
    assert fixt12 == 201
    assert fixt12 != 404

def test13(fixt13):
    print('test13')
    assert fixt13 == {'id': book1.get_my_book_id(), 'title': 'Roflinky', 'author': 'ARTHAS'}

def test14(fixt14):
    print('test14')
    assert fixt14 == {'id': book1.get_my_book_id(), 'title': 'TbOOk', 'author': 'wiper'}

def test15(fixt15):
    print('test15')
    assert fixt15 == 204
    assert fixt15 != 404



def setup_module(module):
    book1.create_book()
    role1.create_role()
    role1.check_role()


@pytest.fixture
def fixt16():
    return requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?book_id={book1.get_my_book_id()}').status_code

@pytest.fixture
def fixt17():
    return requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?book_id={book1.get_my_book_id()}').json()

@pytest.fixture
def fixt18():
    return requests.get('http://pulse-rest-testing.herokuapp.com/roles/?type=User').json()

@pytest.fixture
def fixt19():
    return requests.get('http://pulse-rest-testing.herokuapp.com/roles/?level=80').json()



def test16(fixt16):
    print('test_id_filter_response')
    assert fixt16 == 200

def test17(fixt17):
    print('test_id_filter_content')
    assert fixt17 == [{'id': role1.get_my_role_id(), 'name': 'Big G', 'type': 'Worker', 'level': 80, 'book': book1.get_my_book_id()}]

def test18(fixt18):
    print('test_role_types_filter')
    for i in fixt18:
        assert i.get('type') == "User"

def test19(fixt19):
    print('test_role_types_filter')
    for i in fixt19:
        assert i.get('level') == 80



