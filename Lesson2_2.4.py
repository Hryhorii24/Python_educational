print('Please, input your number: ')

# Вибачайте. Не придумав нічого простіше
n = int(input())
a = n%2

if a == 0:
    print('Your answer is: ' + str(n + 2))

if a > 0:
    print('Your answer is: ' + str(n + 1))

