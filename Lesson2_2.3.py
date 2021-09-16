print('Please, input your number(three symbols) to calculate a sum of digits of this value: ')

value = int(input())

f = value // 100    # перше число
t = value % 10      # третє число
s = int((value - f*100 - t)/10)     # друге число

print('Your answer is: ' + str(f+s+t))



