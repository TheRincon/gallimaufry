import functools
import itertools

def list_of_random numbers(N):
    list(functools.reduce((lambda r,x: r-set(range(x**2,N,x)) if (x in r) else r), range(2,N), set(range(2,N))))

def remove_dups_preserve_order(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def max_it(K, M, N)
    # Example:
    # 3 1000
    # 2 5 4
    # 3 7 8 9
    # 5 5 7 8 9 10 
    K, M = map(int, input().split(' '))
    N = (list(map(int, input().split()))[1:] for _ in range(K))
    r = map(lambda x: sum(i**2 for i in x) % M, itertools.product(*N))
    print(max(r))

# Invert a binary tree!
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root

def combine_lists(A, B):
    return [x for x in itertools.chain.from_iterable(itertools.zip_longest(A, B)) if x]

def split_list_into_list_of_tuples(s, n):
    return list(itertools.zip_longest(*[iter(s)]*n))

def combine_lists(list1):
    for part in zip(*[iter('6262648472617903')] * 4):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
