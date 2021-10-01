# 1
# s = str(input())
# print(s[2], s[-2], s[:6], s[:-3], s[::2], s[1::2], s[-1::-1], s[-1::-2], s[1:-1], len(s))

# 2
# s = str(input())
# print(s[len(s)//2 + 1:] + s[: len(s)//2 + 1])

# 3
# a = int(input())
# if a % 400 == 0:
#     print('YES')
# elif a % 100 == 0:
#     print('NO')
# elif a % 4 == 0:
#     print('YES')
# else:
#     print('NO')

# 4
# a = int(input('Input a: '))
# b = int(input('Input b: '))
# c = int(input('Input c: '))

# if a + b <= c:
#    print('NO')
# elif a + c <= b:
#    print('NO')
# elif b + c <= a:
#    print('NO')
# else:
#    print('YES')

# 5
# a = int(input('Input a: '))
# b = int(input('Input b: '))
# c = int(input('Input c: '))
#
# if a < b < c:
#     a, b, c = a, b, c
# elif a < c < b:
#     a, b, c = a, b, c
# elif b < a < c:
#     a, b, c = b, a, c
# elif b < c < a:
#     a, b, c = b, c, a
# elif c < a < b:
#     a, b, c = c, a, b
# elif c < b < a:
#     a, b, c = c, b, a
#
# print(f'a = {a}, b = {b}, c = {c}')

# 6
# a = int(input('Input a: '))
# b = int(input('Input b: '))
# c = int(input('Input c: '))
#
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)

# 7.1
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# 7.2
# a = 20
# while 1 <= a <= 20:
#    print(a, end=' ')
#    a -= 1

# 7.3
# a = int(input('input a: '))
# b = 0
# if a % 2 != 0:
#     print('Incorrect number')
# while a % 2 >= 0:
#     b += 1
#     print(a)
#     if a % 2 == 1:
#         print(f'The division occurred {b - 1} time(s)')
#         break
#     a = a // 2

# 8
# s = ['dfdsfs', 'dfsdf', 'sdfd', 'sdfsdfs', 'hgjgjgjgjgjg']
#
# while len(s) >= 0:
#     if len(s) == 0:
#         break
#     s.pop(0)
#     print(s)

# 9.1
# def is_year_leap(a):
#     if a % 400 == 0:
#         print('YES')
#     elif a % 100 == 0:
#         print('NO')
#     elif a % 4 == 0:
#         print('YES')
#     else:
#         print('NO')
#
#
# is_year_leap(2011)

# 9.2
# def is_triangle(a, b, c):
#     if a + b <= c:
#        print('NO')
#     elif a + c <= b:
#        print('NO')
#     elif b + c <= a:
#        print('NO')
#     else:
#        print('YES')
#
#
# is_triangle(11, 14, 5)

# 10
s = '''Praesent ullamcorper auctor, tortor at ultricies.
Suspendisse molestie dignissim tempor.
Praesent ullamcorper auctor, tortor at ultricies.
Suspendisse molestie dignissim tempor'''

print(len(s.split(' ')) + len(s.split('/n')))

