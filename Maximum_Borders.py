total_test_num = int(input())

for _ in range(total_test_num):
    row_column = list(map(int, input().split()))
    max_count = 0

    for _ in range(row_column[0]):
        row_input = input().strip()   # e.g. .....####......
        
        max_len = max(len(s) for s in row_input.split('.'))
        max_count = max(max_count, max_len)

    print(max_count)