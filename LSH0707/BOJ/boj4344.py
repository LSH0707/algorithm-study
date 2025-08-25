C = int(input())
for test_case in range(1, 1+C):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    cnt = 0
    for i in range(1, arr[0]+1):
        if arr[i] > avg:
            cnt =  cnt + 1
    print('{0:.3f}'.format(cnt*100/arr[0]), end='')
    print('%')