#Реализация алгоритма нахождения кратчайших путей от заданной вершины до остальных вершин графа

#Алгоритм Дейкстры

from math import inf
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
    G.append(nn)
print("Задайте начальную вершину: ")
v=int(input())-1
d=[-1]*n
d[v]=0
checklen=[inf]*n  #список расстояний от заданной вершины
checklen[v]=0
ind=-1
k=0
start=v+1

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
    #print('ch', checklen)
    v=ind
    d[v]=m
    for j in checklen:
        if j==None:
            continue
        else:
            k+=1
    if k==1:
        break
    k=0

for i in range(n):
    if i+1==start:
        continue
    print("Кратчайший путь от вершины",start, 'до', i+1, 'равно',d[i])

print()
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()

