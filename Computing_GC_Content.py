user_name = input()
d = {}

while user_name[0] != '':
    d[user_name] = ''
    DNA = input()
    if user_name != '>':
        while DNA[0] != '>':
            d[user_name] += DNA
            DNA = input()
        user_name = DNA
    else:
        break


def make_pocent(str):
    sum = 0
    for i in str:
        if i == 'C' or i == 'G':
            sum += 1
    return round(100*sum/len(str), 7)


print(d)
del d['>']

MAX = 0
for j in d:
    if make_pocent(d[j]) > MAX:
        MAX = make_pocent(d[j])
        name = j

print(name[1:])
print(MAX)
