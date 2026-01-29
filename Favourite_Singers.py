# Favourite Singers
total_n = int(input())
n = list(map(int, input().split()))

dict_n = {}

for i in n:
    dict_n[i] = dict_n.get(i, 0) + 1


# most frequent number
max_num =  max(dict_n.values())
output = 0
for k in dict_n.keys():
    if dict_n[k]==max_num:
        output += 1
        
print(output)