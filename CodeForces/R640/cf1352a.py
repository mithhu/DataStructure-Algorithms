Test = int(input())
for _ in range(Test):
    ip = input()
    mul = 1
    count = 0
    array = []
    for i in reversed(range(len(ip))):
        if int(ip[i]) != 0:
            res = mul*int(ip[i])
            array.append(str(res))
            count += 1
        mul = mul*10
    print(count)
    for i in range(len(array)):
        print(int(array[i]), end=" ")
