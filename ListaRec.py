def sumalista(n):
    suma = 0
    for x in range(len(n)):
        suma = suma + n[x]
    return suma

def slista_rec(n):
    x = 0
    for i in n: 
        x += i
    return x        

def main ():

    n = ([3,9,6,7])
    print(sumalista(n))
    print(slista_rec(n))

main()
