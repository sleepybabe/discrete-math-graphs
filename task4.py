import random
import sys
from math import inf



print("Задайте количество вершин графа: ")
n=int(input())
print("Задайте граф матрицей смежности: ")
G=[]
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
print("Введите обход графа по алгоритму обхода в ширину: ")
check=[int(i)-1 for i in input().split()]

if len(check)!=n:
    print("Неверно!")
    input("Нажмите клавишу Enter, чтобы продолжить...")
    sys.exit()

def getPath(v):
    d = [-1] * n
    d[v] = 0
    checklen = [inf] * n  # список расстояний от заданной вершины
    checklen[v] = 0
    ind = -1
    k = 0
    while(True):
        m = inf
        for i in range(n):
            if v==i and d[v]!=-1:   #если расстояние до вершины уже добавили в результат
                checklen[i]=None
            elif checklen[i]!= None and (G[v][i]+d[v])<checklen[i] and G[v][i]!=0:  #если путь до вершины еще не была добавлена в результат
                checklen[i]=G[v][i]+d[v]   #расстояние от искомой вершины плюсуется с расстояением новой
            if checklen[i]!=None and checklen[i]<m and checklen[i]!=0:  #находим минимум чтобы его выделить следующей вершиной и добавить в результат
                m=checklen[i]
                ind=checklen.index(m)
        v=ind
        if v==check[0]:
            return m
        d[v]=m
        for j in checklen:
            if j==None:
                continue
            else:
                k+=1
        if k==1:
            break
        k=0


r=[0]
for i in range(1,len(check)):
    r.append(getPath(check[i]))

for i in range(n-1):
    if r[i]<=r[i+1]:
        continue
    else:
        print("Неверно!")
        input("Нажмите клавишу Enter, чтобы продолжить...")
        sys.exit()
print("Верно!")
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()
