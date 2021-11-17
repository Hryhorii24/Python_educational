import unittest
import requests

# def hypoten(Cathet1, Cathet2):
#     return (Cathet1 ** 2 + Cathet2 ** 2) ** 0.5
#
#
# class OurTestClass(unittest.TestCase):
#
#     def test_method_1(self):
#         res = hypoten(3, 4)
#         self.assertEqual(res, 5)
#
#     def test_method_2(self):
#         res = hypoten(0, 0)
#         self.assertEqual(res, 1)
#
#
# if __name__ == '__main__':
#     unittest.main


from Lesson3 import is_year_leap, is_triangle
from HW4 import triangle_type
from HW5 import ITEmployee1
from HW6 import book1
from HW6 import role1


class TestYearLeap(unittest.TestCase):
    def test_pos1(self):
        res = is_year_leap(2000)
        self.assertEqual(res, 'YES')

    def test_pos2(self):
        res = is_year_leap(1111)
        self.assertEqual(res, 'NO')

    def test_neg1(self):
        res = is_year_leap(2004)
        self.assertEqual(res, 'YES')

    def test_neg2(self):
        res = is_year_leap(880)
        self.assertEqual(res, 'YES')



class TestTriangle(unittest.TestCase):
    def test_tr1(self):
        res = is_triangle(1, 1, 1)
        self.assertEqual(res, 'TRUE')

    def test_tr2(self):
        res = is_triangle(1, 0, 1)
        self.assertEqual(res, 'FALSE')

    def test_tr3(self):
        res = is_triangle(3, 4, 5)
        self.assertEqual(res, 'TRUE')

    def test_tr4(self):
        res = is_triangle(0, 0, 0)
        self.assertEqual(res, 'FALSE')


class TestType(unittest.TestCase):
    def test_not_triangle(self):
        res = triangle_type(5, 2, 2)
        self.assertEqual(res, 'Not a triangle. Please, try again')

    def test_equilateral_triangle(self):
        res = triangle_type(2, 2, 2)
        self.assertEqual(res, 'Equilateral triangle')

    def test_isosceles_triangle(self):
        res = triangle_type(1, 2, 2)
        self.assertEqual(res, 'Isosceles triangle')

    def test_versatile_triangle(self):
        res = triangle_type(5, 4, 2)
        self.assertEqual(res, 'Versatile triangle')


class TestITEmployee(unittest.TestCase):
    def test_1empty_list(self):
        res = ITEmployee1.skills
        self.assertEqual(res, [])

    def test_add_role(self):
        ITEmployee1.add_skill("Tests writing")
        res = ITEmployee1.skills
        self.assertEqual(res, ["Tests writing"])

    def test_second_role(self):
        ITEmployee1.add_skill("SQL")
        res = ITEmployee1.skills
        self.assertEqual(res, ["Tests writing", "SQL"])


class TestBook(unittest.TestCase):
    def test_create_book(self):
        res = book1.create_book()
        self.assertEqual(res, 201)
        self.assertNotEqual(res, 404)

    def test_check_book(self):
        res = book1.check_book()
        self.assertEqual(res, {'id': book1.get_my_book_id(), 'title': 'Roflinky', 'author': 'ARTHAS'})

    def test_update_book(self):
        book1.put_book(title='TbOOk', author='wiper')
        res = book1.check_book()
        self.assertEqual(res, {'id': book1.get_my_book_id(), 'title': 'TbOOk', 'author': 'wiper'})

    def test_delete_book(self):
        res = book1.delete_book()
        self.assertEqual(res, 204)


class TestRoles(unittest.TestCase):

    def setUp(self):
        book1.create_book()
        self.BookID = book1.get_my_book_id()
        role1.create_role()
        self.RoleID = role1.check_role()

    def test_id_filter(self):
        res = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?book_id={self.BookID}').status_code
        cnt = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?book_id={self.BookID}').json()
        print(cnt)
        self.assertEqual(res, 200)
        self.assertEqual(cnt, [{'id': self.RoleID, 'name': 'Big G', 'type': 'Worker', 'level': 80, 'book': self.BookID}])

    def test_role_types_filter(self):
        type_key = "User"
        # res = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?type={type_key}').status_code
        cnt = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?type={type_key}').json()
        for i in cnt:
            self.assertEqual(i.get("type"), type_key)

    def test_role_lvls_filter(self):
        role_lvl = 80
        # res = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?level={type_lvl}').status_code
        cnt = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/?level={role_lvl}').json()
        for i in cnt:
            self.assertEqual(i.get("level"), role_lvl)

























if __name__ == '__main__':
    unittest.main()
