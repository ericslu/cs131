def bar(tup):
    tup2 = tup
    print_tup('tup2 = tup', tup, tup2)
    tup += ('bean', 'bag')
    print_tup("tup += ('bean', 'bag')", tup, tup2)
    tup2 = ('alfredo', 'aspargus')
    print_tup("tup2 = ('alfredo', 'aspargus')", tup, tup2)
    tup = tup2
    print_tup('tup = tup2', tup, tup2)

def print_tup(instruction, tup, tup2):
    print(instruction, '\nLocal Tup: ', tup, '\nLocal Tup2: ', tup2)
    print('tup is tup2:', tup is tup2, '\n')

tup = ('apple', 'pear')
bar(tup)
print('Global tuple: ', tup)
