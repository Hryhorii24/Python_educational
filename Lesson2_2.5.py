print('Please, input your number: ')

n = float(input())
z = float(n % 1)

if n > 0:
    print(f'Your answer is:  {z}')

else:
    print(f'Your answer is:  {-(1 - z)}')
