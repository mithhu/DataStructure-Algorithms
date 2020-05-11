Test = int(input())
for _ in range(Test):
    n, k = map(int, input().split())
    array = []
    num = 1
    while len(array) < k:
        if num % n != 0:
            array.append(num)
        num += 1
    print(array[-1])
