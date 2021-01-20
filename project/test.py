from itertools import groupby
from operator import itemgetter


lst = [
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (445952, 445953), 'idx': 0},
    {'src_name': 'node_C', 'dest_name': 'node_A', 'filename': 'file1', 'range': (222976, 445952), 'idx': 0},
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (0, 222976), 'idx': 2},
    {'src_name': 'node_C', 'dest_name': 'node_A', 'filename': 'file1', 'range': (222976, 445952), 'idx': 1},
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (445952, 445953), 'idx': 54},
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (0, 222976), 'idx': 1},
    {'src_name': 'node_C', 'dest_name': 'node_A', 'filename': 'file1', 'range': (222976, 445952), 'idx': 2},
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (0, 222976), 'idx': 3},
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (0, 222976), 'idx': 0},
    {'src_name': 'node_B', 'dest_name': 'node_A', 'filename': 'file1', 'range': (445952, 445953), 'idx': 2},
    {'src_name': 'node_C', 'dest_name': 'node_A', 'filename': 'file1', 'range': (222976, 445952), 'idx': 3},
]

res = sorted(lst, key=itemgetter('range'))
for d in res:
    print(d)

haha = groupby(res, key=lambda x: x["range"])
for k, v in haha:
    vl = list(v)
    vl_res = sorted(vl, key=itemgetter('idx'))
    for i in vl_res:
        print(k, i)