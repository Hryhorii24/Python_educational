# import requests
#
#
#1
# class book_requests:
#     def __init__(self):
#         self.books_url = 'http://pulse-rest-testing.herokuapp.com/books'
#         self.title = 'Roflinky'
#         self.author = 'ARTHAS'
#         self.my_book_id = None
#
#     def create_book(self):
#         post_response = requests.post(f"{self.books_url}", data={"title": f'{self.title}', 'author': f"{self.author}"})
#         if post_response.status_code == 201:
#             print("added successfully")
#         else:
#             print("rekt!")
#
#     def check_book(self):
#         get_response = requests.get(f'{self.books_url}')
#         books = get_response.json()
#         books_ids = []
#
#         for book in books:
#             if book.get("title") == self.title and book.get("author") == self.author:
#                 books_ids.append(book.get("id"))
#
#         for book in books:
#             if book.get("id") == books_ids[-1]:
#                 self.my_book_id = books_ids[-1]
#                 print(f'This book is present! id is {self.my_book_id},'
#                       f' author is {book.get("author")} and title is {book.get("title")}')
#                 print(requests.get(f"{self.books_url}/{self.my_book_id}").json())
#                 return self.my_book_id
#
#     def put_book(self, title='TITLE', author='AUTHOR', ):
#         self.title = title
#         self.author = author
#         update_book = requests.put(f"{self.books_url}/{self.my_book_id}",
#                                    data={"title": f'{self.title}', "author": f'{self.author}'})
#         if update_book.status_code == 200:
#             print("Updated successfully")
#         else:
#             print("rekt!")
#         print(requests.get(f"{self.books_url}/{self.my_book_id}").json())
#
#     def delete_book(self):
#         deleted_book = requests.delete(f"{self.books_url}/{self.my_book_id}")
#         if deleted_book.status_code == 204:
#             print("Deleted successfully")
#         else:
#             print('rekt!')
#
#     def get_my_book_id(self):
#         return self.my_book_id
#
#
# book1 = book_requests()
# book1.create_book()
# book1.check_book()
# book1.put_book('12321', '2222')
# # book1.delete_book()
# # print(book1.get_my_book_id())



#2
# class roles:
#     def __init__(self):
#         self.roles_url = 'http://pulse-rest-testing.herokuapp.com/roles'
#         self.name = 'Big G'
#         self.type = 'User'
#         self.level = 80
#         self.book = book1.get_my_book_id()
#         self.my_role_id = None
#
#     def create_role(self):
#         post_response = requests.post(f"{self.roles_url}", data={"name": f'{self.name}', 'type': f"{self.type}",
#                                                                  'level': f"{self.level}", 'book': f"{self.book}"})
#
#         if post_response.status_code == 201:
#             print("added successfully")
#         else:
#             print("rekt!")
#
#     def check_role(self):
#         get_response = requests.get(f'{self.roles_url}')
#         roles = get_response.json()
#         roles_ids = []
#
#         for role in roles:
#             if role.get("name") == self.name and role.get("type") == self.type:
#                 roles_ids.append(role.get("id"))
#
#         for role in roles:
#             if role.get("id") == roles_ids[-1]:
#                 self.my_role_id = roles_ids[-1]
#                 print(f'This role is present! id is {self.my_role_id}, name is {role.get("name")}, '
#                       f'type is {role.get("type")}, level is {role.get("level")} and book id {role.get("book")}')
#                 print(requests.get(f"{self.roles_url}/{self.my_role_id}").json())
#                 return self.my_role_id
#
#
#     def put_book(self, name='NAME', type='TYPE', level=None):
#         self.name = name
#         self.type = type
#         self.level= level
#         update_role = requests.put(f"{self.roles_url}/{self.my_role_id}",
#                                    data={"name": f'{self.name}', "type": f'{self.type}', "level": f'{self.level}'})
#         if update_role.status_code == 200:
#             print("Updated successfully")
#         else:
#             print("rekt!")
#         print(requests.get(f"{self.roles_url}/{self.my_role_id}").json())
#
#     def delete_role(self):
#         deleted_role = requests.delete(f"{self.roles_url}/{self.my_role_id}")
#         if deleted_role.status_code == 204:
#             print("Deleted successfully")
#         else:
#             print('rekt!')
#
#
#
# role1 = roles()
# role1.create_role()
# role1.check_role()
# role1.put_book('Cina', 'Boss', 3)
# role1.delete_role()




#3
# frequency = {}
# text = open('template.txt', 'r')
# file = open('new_file.txt', 'a')
# text_string = text.read().lower()
#
# mark = ',.'
# for char in text_string:
#     if char in mark:
#         text_string = text_string.replace(char, "")
#
# sorted_words = sorted(text_string.split())
#
# for word in sorted_words:
#     count = frequency.get(word, 0)
#     frequency[word] = count + 1
#
# frequency_list = frequency.keys()
#
# for words in frequency_list:
#     file.write(f'{words} {frequency[words]}\n')
#
# text.close()
# file.close()



#4
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# server = 'smtp.gmail.com'
# user = 'mishokporoshok@gmail.com'
# password = '****'
#
# recipients = ['bukar29091999@gmail.com, grigoriy29091999@gmail.com']
# sender = 'mishokporoshok@gmail.com'
# subject = 'Check theme'
# text = 'Done by G'
# html = '<html><head></head><body><p>' + text + '</p></body></html>'
#
# msg = MIMEMultipart('alternative')
# msg['Subject'] = subject
# msg['From'] = 'Grigoriy <' + sender + '>'
# msg['To'] = ', '.join(recipients)
# msg['Reply-To'] = sender
# msg['Return-Path'] = sender
#
# part_text = MIMEText(text, 'plain')
# part_html = MIMEText(html, 'html')
#
# msg.attach(part_text)
# msg.attach(part_html)
#
# mail = smtplib.SMTP_SSL(server)
# mail.login(user, password)
# mail.sendmail(sender, recipients, msg.as_string())
# mail.quit()




#5

# def add_employee(surname='', Name='', departament='', salary=None):
#     content = open('company.txt', 'a')
#
#     table = {"Surname": surname, "Name": Name, "Departament": departament, 'Salary': salary}
#
#     content.write(f'{table}\n')
#
#     content.close()



# add_employee("B", 'G', 'Oil', 2)
# add_employee("B", 'G', 'Rust', 3)
# add_employee("B", 'G', 'Lang', 4)
# add_employee("B", 'G', 'ATM', 5)


# def count_departaments():
#     content = open('company.txt', 'r')
#     line = {content.readline()}
#     print(line.get(Surname))
#     return line
#
#
#
#
# print(count_departaments())

import re
def add_employee(surname='', name='', departament='', salary=None):
    content = open('company.txt', 'a')

    content.write(f"{surname} {name} {departament} {salary}\n")

    content.close()


def max_salary():
    file = open("company.txt")
    strings = file.read().split("\n")[:-1]
    # print(strings)
    x = []
    for emp in strings:
        value = emp.split(" ")
        x.append(value[3])

    print(max(x))

def count_departaments():
    file = open("company.txt")
    strings = file.read().split("\n")[:-1]
    # print(strings)
    x = []
    for emp in strings:
        value = emp.split(" ")
        x.append(value[2])
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    print(len(y))




# a = []
# x = 5
# while x > 0:
#     a.append("134124")
#     x -= 1
#     print(a)




# add_employee("B", 'G', 'Oil', 2)
# add_employee("B", 'G', 'Rust', 3)
# add_employee("B", 'G', 'Lang', 4)
# add_employee("B", 'G', 'ATM', 5)


count_departaments()



