import sys

print("Введите код Прюфера: ")
code=[int(i)-1 for i in input().split()]
n=len(code)

G=[]*(n+2)
for i in range(n+2):
    G.append([0]*(n+2))

anticode=[]

def decode(code,k):
    take=-1
    for i in range(n+2):
        if i not in code and i not in anticode:  #находим первую вершину, которой нет в коде и антикоде
            take=i
            break
    G[take][code[0]]=1   #восстанавливаем дерево для этой вершины с параллельным элементом из code
    G[code[0]][take]=1
    anticode.append(take)  #добавление вершины в антикод
    del code[0]
    if k==n-1:  #если дошли до пустого code
        for i in range(n+2):
            if i not in anticode:   #заполняем антикод и дерево недостающими номерами вершин (проверка от 1 до n)
                G[anticode[-1]][i]=1
                G[i][anticode[-1]]=1
                anticode.append(i)
        return
    else:
        return decode(code,k+1)

decode(code,0)
print()
for i in range(len(anticode)):
    anticode[i]+=1
print("Декодирование кода Прюфера: ", *anticode)
print()
print("Полученное дерево: ")
for i in range(n+2):
    for j in range(n+2):
        print(G[i][j],end=', ')
    print(end='\n')

print()
input("Нажмите клавишу Enter, чтобы продолжить...")
sys.exit()