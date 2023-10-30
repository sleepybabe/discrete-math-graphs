import sys
from queue import Queue


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
#print(G)
allvisited = Queue()
print("Задайте начальную вершину обхода: ")
start=int(input())-1
used=[start]
allvisited.put(start)

while(True):
    start=allvisited.get() #вытаскиваем из очереди вершину и проверяем ее на наличие непройденных смежных вершин
    for j in range(len(G)):
        if G[start][j]==1 and j not in used: #если есть непройденные смежные вершины то добавляем в очередь их и затем повторяем первое действие
            used.append(j)
            allvisited.put(j)
    if len(used)==n:
        break
for i in range(n):
    used[i]+=1
print("Обход в ширину: ", *used)
print()
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()
