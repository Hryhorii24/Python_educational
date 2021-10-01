d = {'title': "Gunpowder", 'price': 979, 'ingredients': ['nitrate', 'charcoal', 'sulfur']}


d['description'] = 'Gunpowder, also known as black powder to distinguish it from modern smokeless powder, is the earliest known chemical explosive'
print('4.1 ' + d['title'], d['price'], d['ingredients'], d['description'])


d.update({'price': d['price'] + 100})
print('4.2 ' + d['title'], d['price'], d['ingredients'], d['description'])


d['ingredients'].append('dry air')
print('4.3 ' + d['title'], d['price'], d['ingredients'], d['description'])


if len(d["ingredients"]) == 0:
    print(f'4.4 There is {len(d["ingredients"])} ingredient')

if len(d["ingredients"]) == 1:
    print(f'4.4 There is {len(d["ingredients"])} ingredient')

else:
    print(f'4.4 There are {len(d["ingredients"])} ingredients')


d.pop('description')
print('4.5 ' + d['title'], d['price'], d['ingredients'])
