#раскраска графа путем нахождения степени каждой вершины и далее эти степени отсортировать от большего к меньшему

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

stepens=[]
for i in range(n):  #нахождение степеней вершин
    k=0
    for j in range(n):
        if G[i][j]==1:
            k+=1
    stepens.append(k)
sortstepens=stepens.copy()
v=[]

sortstepens.sort(reverse=True)

for i in range(n):
    v.append(stepens.index(sortstepens[i]))
    stepens[v[i]]=-1

painted={}
used=[]

def paint(v, k, used):


    for i in range(n):
        brk = 0
        help = 0
        print(v[i])
        for key, value in painted.items():  #проверяем не была ли уже добавлена эта вершина
            if v[i] in value:
                brk=1
                break
        if brk==1:
            continue
        for j in range(n):
            brk=0
            for key, value in painted.items():  #снова проверяем на добавленность
                if v[j] in value:
                    brk = 1
                    break
            if brk==1:
                continue
            if len(used)>1:  #если не смежных вершин больше одной, то проверяем что ни одна из вершин одного цвета не смежна с новой вершиной
                for d in range(len(used)):
                    if G[used[d]][v[j]]==0:
                        help+=1
                if help==len(used):
                    used.append(v[j])
                help=0
            elif G[v[i]][v[j]] == 0:
                used.append(v[j])
        painted[k]=used
        k+=1
        used=[]
        brk=0
    # prv=0
    # for key, value in painted.items():
    #     prv+=len(value)
    # if prv==n:
    return painted
    # else:
    # return paint(v,k,used)


painted=paint(v,1,used)
print("Раскраска: ")
print(painted)
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()