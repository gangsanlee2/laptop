dan = 2
while dan <10:
    val = 1
    while val <10:
        print('%d * %d = %d' %(dan, val, dan*val), end='   ')
        val += 1
    print()
    dan += 1