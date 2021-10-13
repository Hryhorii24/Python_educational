# 1

a = (input("Number 1: "))
b = (input("Number 2: "))

try:
    a = float(a)
    b = float(b)
except ValueError:
    print(str(a) + str(b))
else:
    print(a + b)



# 2.1

def is_a_number():
    suspected = input('Enter a number: ')
    while True:
        try:
            suspected = float(suspected)
        except ValueError:
            suspected = input('Try again: ')
        else:
            return suspected


# print(is_a_number())



# 2.2

def word():
    suspected_string = input('Enter a string: ')
    suspected_string = suspected_string.lstrip()
    suspected_string = suspected_string.rstrip()
    for i in suspected_string:
        if " " in suspected_string:
            suspected_string = input('Try again: ')
        else:
            return suspected_string


print(word())



# 2.3

def is_a_triangle():
    a = is_a_number()
    b = is_a_number()
    c = is_a_number()
    while True:
        if a + b <= c or a + c <= b or b + c <= a:
            print('Not a triangle. Please, try again')
            a = is_a_number()
            b = is_a_number()
            c = is_a_number()
            continue
        elif a == b == c:
            print('Equilateral triangle')
        elif a == b or b == c or a == c:
            print('Isosceles triangle')
        else:
            print('Versatile triangle')
        return a, b, c


print(is_a_triangle())



# 2.4

def distance():
    print('Input x1')
    x1 = is_a_number()
    print('Input y1')
    y1 = is_a_number()
    print('Input x2')
    x2 = is_a_number()
    print('Input y2')
    y2 = is_a_number()
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


print(f'Distance is: {distance()}')



# 2.5

def remove_chars():
    string = input('enter string: ')
    chars = '''!,()-[]{};?@#$%:'"\,./^&;*_'''
    for i in string:
        if i in chars:
            string = string.replace(i, '')
    return string


print(remove_chars())



# 3

def song(a=3, b=3, c=0):
    d = ''
    e = ''
    if c == 0:
        f = '.'
    elif c == 1:
        f = '!'
    while a > 1:
        a -= 1
        e = 'la-'*b
        d = d + e[:-1] + '\n'
        if a == 1:
            d = d + e[:-1] + f
    return d


print(song())
