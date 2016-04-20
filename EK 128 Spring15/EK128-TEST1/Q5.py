choices= [['pie', 'latte'], ['cake', 'capucino'], ['figs', None],
    ['cake', 'cognac'], ['cake', 'cognac'], [None, None], ['apple',
    'cognac'], [None, None], ['cookies', None], ['cake',
    'capucino'], ['apple', 'cognac'], ['apple', 'capucino'], [None,
    None], [None, 'latte'], ['figs', 'capucino'], ['figs', 'tea'],
    ['figs', 'capucino'], ['strawberries', 'tea'], ['cookies',
    'coffee'], ['strawberries', None], ['figs', 'cognac'],
    ['apple', None], ['strawberries', 'latte'], ['apple', 'latte'],
    ['cookies', 'cognac'], [None, 'capucino'], ['pie', 'tea'],
    ['ice cream', 'latte'], ['ice cream', 'latte'], ['cake',
    'tea'], ['ice cream', None], ['cookies', 'latte'],
    ['strawberries', 'latte'], ['cake', 'latte'], ['cookies',
    'latte'], ['cake', 'capucino'], ['cake', 'tea'], ['cookies',
    'latte'], ['cake', 'tea'], ['cookies', None], ['cake',
    'cognac'], ['pie', None], ['cake', 'tea'], ['strawberries',
    'coffee'], ['ice cream', None], ['apple', 'tea'], ['figs',
    None], ['apple', 'cognac'], ['ice cream', 'tea'], ['cookies',
    'cognac'], [None, 'latte'], ['apple', 'latte'], [None,
    'capucino'], ['ice cream', 'coffee'], ['cookies', 'latte'],
    [None, None], [None, 'latte'], ['strawberries', 'cognac'],
    ['strawberries', 'tea'], ['pie', 'capucino'], ['cake',
    'latte'], ['cake', 'latte'], ['ice cream', 'capucino'],
    ['apple', 'capucino'], ['ice cream', 'tea'], ['ice cream',
    'coffee'], ['apple', 'coffee'], ['ice cream', 'coffee'], [None,
    'tea'], ['cake', 'tea'], ['cake', 'cognac'], [None, 'cognac'],
    ['cake', 'coffee'], ['pie', None], [None, 'coffee'], ['apple',
    'cognac'], [None, 'cognac'], ['apple', 'cognac'], ['figs',
    'coffee'], ['cake', None], [None, None], ['cookies', 'latte'],
    ['cake', 'latte'], ['cake', 'capucino'], ['apple', 'cognac'],
    [None, 'cognac'], ['strawberries', 'latte'], [None, 'latte'],
    ['cookies', 'cognac'], [None, 'tea'], ['ice cream', 'coffee'],
    ['pie', 'cognac'], ['figs', 'coffee'], ['cake', 'latte'],
    ['strawberries', 'cognac'], ['pie', 'tea'], ['figs', 'latte'],
    ['cookies', 'tea'], ['cookies', 'latte'], ['cake', None]]


desserts = {}
drinks = {}
combos = {}

count = -1
count2 = -1
comboCount = 0

for i in choices:
    for j in i:
        count2 += 1
        if j == None:
            if (count2 % 2 == 0):
                count2 = 0
                i[count2]='None'
            if (count2 % 2 != 0):
                count2 = 1
                i[count2]='None'
        count += 1
        if (count % 2 == 0):
            if j in desserts:
                desserts[j] += 1
            if j not in desserts:
                desserts[j] = 1
        if (count % 2 != 0):
            if j in drinks:
                drinks[j] += 1
            if j not in drinks:
                drinks[j] = 1
    L=', '.join(i)
    
    if L in combos:
        combos[L] += 1
    if L not in combos:
        combos[L] = 1
        print(comboCount)
        comboCount += 1


out = (desserts, drinks, comboCount, " unique combinations.")

print(out)
