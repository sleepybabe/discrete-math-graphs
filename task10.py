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

code=[]
def Prufer(G,code):
    ind=-1
    curind=-1
    for i in range(n):
        check=0
        for j in range(n):
            if G[i][j]==1:   #проверяем, лист ли это или нет
                check+=1
        if check==1:  #если лист, то сохраняем индексы данной вершины
            ind = G[i].index(1)
            curind=i
            break

    G[curind][ind]=0
    G[ind][curind]=0
    code.append(ind+1)
    if len(code)==n-2:
        return code
    else:
        return Prufer(G,code)

print()
code=Prufer(G,code)

print("Код Прюфера: ", *code)
print()
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()