# l = ['dsfdsfds', 'ddddddd', 'eeee', '33']
# suma = 0
#
# for i in l:
#     if len(i)%2 == 1:
#         suma += 1
#
#
# print(suma)

# d = {'Value1': 1, 'Value2': 2}
#
# for i in d:
#     print(i, d[i], end='\n')

i = 12

# def type_of_element(i):
#     return type(i)
#
# print(type_of_element(i))

while True:
    a = input('Input: ')
    try:
        a = float(a)
        print("Done")
    except:
        print("Error!")
        continue
    break