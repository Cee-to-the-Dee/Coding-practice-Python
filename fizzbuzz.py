store = {3:'fizz', 5:'buzz', 7:'kangooroo'}
for i in range(1,101):
    output = ''
    for x in store:
        if (i % x == 0):
            output += store[x]
    if (output == ''):
        output = i
    print(output)
