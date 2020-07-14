import functools

def list_of_random numbers(N):
    list(functools.reduce((lambda r,x: r-set(range(x**2,N,x)) if (x in r) else r), range(2,N), set(range(2,N))))

def remove_dups_preserve_order(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def combine_lists(list1)
    for part in zip(*[iter('6262648472617903')] * 4):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

if __name__ == '__main__':
