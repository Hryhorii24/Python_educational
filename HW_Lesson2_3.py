list1 = ["absorb", "boring", "world", "divide", "emotion", "cannon", "push", "sold", "mash"]

print(f'3.1 {list1[-3]}')

print(f'3.2 {list1[1][0]}')

print(f'3.3 {list1[-1][-1]}')

list1.append('COVER')
print(f'3.4 {list1}')

list1.insert(len(list1)//2, 'MESA')
print(f'3.5 {list1}')

list1.remove(list1[0])
print(f'3.6 {list1}')

list1.remove('world')
print(f'3.7 {list1}')