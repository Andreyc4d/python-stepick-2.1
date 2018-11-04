with open('input.txt', 'r') as f:
    n=int(f.readline())
    print('n='+str(n))
    for i in range(n):
        print((f.readline().strip()))
    n=int(f.readline())
    print('n='+str(n))
    for i in range(n):
        print((f.readline().strip()))
