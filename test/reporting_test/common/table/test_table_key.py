table = {}

table[(1, 2)] = 3
table[(1, 3)] = 4
print(table)

table[(1, 2)] = 5

print(table)

for k in table.keys():
    print(k[1])
    print(table[k])
