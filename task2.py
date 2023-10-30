import sys
import random

G=[]

print("Задайте количество вершин графа: ")
n=int(input())
print("Граф матрицей смежности: ")

# nn=[]
# for i in range(n):
#     nn=input().split()
#     if len(nn)!=n:
#         print("Матрица должна быть квадратной!")
#         input("Нажмите клавишу Enter, чтобы продолжить...")
#         sys.exit()
#     for j in range(len(nn)):
#         nn[j] = int(nn[j])
#         if (nn[j]!=1 and nn[j]!=0):
#             print("Матрица должна состоять только из 1 и 0!")
#             input("Нажмите клавишу Enter, чтобы продолжить...")
#             sys.exit()
#     G.append(nn)


k=0
for i in range(n):
    G.append([0]*n)
    for j in range(i,n):
        if i==j:
            G[i][j]=0
            continue
        G[i][j]=random.randint(0,1)
    for j in range(i):
        G[i][j]=G[j][i]
    if 1 not in G[i] and i+1!=n:
        k=random.randint(i,n-1)
        G[i][k]=1

for i in range(n):
    for j in range(n):
        print(str(G[i][j]), end=' ')
    print()

print()
print("Введите обход графа по алгоритму обхода в глубину: ")
check=[int(i)-1 for i in input().split()]

used=[check[0]]
help=0
allvisited=[-1]


start=check[0]
i=1

if len(check)!=n:
    print("Неверно!")
    input("Нажмите клавишу Enter, чтобы продолжить...")
    sys.exit()

while(True):
    ok = -1
    if start!=allvisited[-1]:  #список каждого захода в вершины, по которому возвращаемся назад, если зашли в тупик
        allvisited.append(start)

    if G[start][check[i]]==1 and check[i] not in used:  #происходит углубление если есть таков путь от вершины
        used.append(check[i])
        start = check[i]
        i=i+1
        help=1
    if help==0:
        for j in range(len(G)):
            if G[start][j]==1 and j not in used:  #если есть смежная вершина в которой еще не были
                ok=j
        if ok!=check[i] and ok!=-1:   #проверяем данная вершина не тупиковая, но пользователь поднимается дальше вверх по цепочке вершин
            print("Неверно!")
            input("Нажмите клавишу Enter, чтобы продолжить...")
            sys.exit()
    if i==len(check):
        break
    if help==0:
        if start==used[0]:  #если начальная вершина с тупиком, то выходим
            break
        start=allvisited[-2] #возвращаемся на одну вершину, пройденную ранее
        del allvisited[-1]
    help=0


if (check == used):
    print("Верно!")
else:
    print("Неверно!")
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()
