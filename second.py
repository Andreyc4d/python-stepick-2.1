DescrClass = dict() #description error class 2 dim list
AlreadySet = set()
str1 = []
with open('input.txt', 'r') as f:
    n=int(f.readline())
    for i in range(n):
        str1 = f.readline().strip().split()
        if len(str1) == 1:
            DescrClass[str1[0]] = []
        elif len(str1)>1:
            DescrClass[str1[0]] = str1[2:]
    n=int(f.readline())
    print(DescrClass)
    print(len(DescrClass['OSError']))
    print('n='+str(n))
    tmp1 = 0
    for i in range(n):
        str2 = f.readline().strip()
        for element in DescrClass[str2]:
            if element in AlreadySet:
                print(str2)
                break
        AlreadySet.add(str2)
print(AlreadySet)
