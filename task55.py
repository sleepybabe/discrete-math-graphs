import sys

G=[]
nn=[]
print("Задайте количество вершин графа: ")
n=int(input())
print("Задайте граф матрицей смежности: ")
for i in range(n):
    nn=input().split()
    if len(nn)!=n:
        print("Матрица должна быть квадратной!")
        input("Нажмите клавишу Enter, чтобы продолжить...")
        sys.exit()
    for j in range(len(nn)):
        nn[j] = int(nn[j])
        if (nn[j]!=1 and nn[j]!=0):
            print("Матрица должна состоять только из 1 и 0!")
            input("Нажмите клавишу Enter, чтобы продолжить...")
            sys.exit()
    G.append(nn)


# for i in range(n):
#     for j in range(n):
#         print(str(G[i][j])+',', end=' ')
#     print()

res=[0]*n
k=1

def dfs(start):
    used=[]
    help=0
    allvisited=[-1]

    while(True):
        if start not in used:  #список обхода вершин
            used.append(start)
        if start!=allvisited[-1]:       #список каждого захода в вершины, по которому возвращаемся назад, если зашли в тупик
            allvisited.append(start)
        for j in range(len(G)):
            if G[start][j]==1 and j not in used:  #если есть смежная вершина в которой еще не были
                start=j
                help=1
                break
        if help==0:  #если тупик
            if start==used[0]:  #если начальная вершина с тупиком, то выходим
                break
            start=allvisited[-2] #возвращаемся на одну вершину, пройденную ранее
            del allvisited[-1]
        help=0
    return used

start=0
flag=0
while(True):
    used=dfs(start)
    for i in used:  #отмечаем вершины которые получились соединенными с начальной вершиной
        res[i]=k
    for j in range(len(res)):  #проверяем если остались вершины с нулевой отметкой
        if res[j]==0:  #если есть, то выполняем снова обход в глубину, прибавляя 1 к результату k
            start=j
            k=k+1
            flag=1
            break
    if flag==0:
        break
    flag=0

print("Число компонент связности: ", k)
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()