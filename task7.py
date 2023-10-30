#Алгоритм Прима

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

used=[]
used.append(0)
index=-1
s=0
m=0

while(True):
    ok=0
    m = max(max(G))+1
    print(m)
    for i in used:
        for j in range(len(G[i])):
            if G[i][j]!=0 and G[i][j]<m:   #находим минимум
                if j not in used:  #если вершина еще не была отмечена
                    m=G[i][j]
                    index=j
                    ok=1
                    print(m, i, index)

    used.append(index)
    print(used)
    s+=m
    if (len(used)==n):
        break


for i in range(n):
    used[i]+=1
print("Вес = ", s )
print("Минимальное остовное дерево: ", *used)


