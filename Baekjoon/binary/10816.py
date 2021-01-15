import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

hashmap = {}
for n in N_list:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(" ".join(str(hashmap[m]) if m in hashmap else '0' for m in M_list))
