def sumalista(n):
    suma = 0
    for x in range(len(n)):
        suma = suma + n[x]
    return suma

def slista_rec(n):
    
    for x in range(len(n)):
        return slista_rec(n[x]) + n[x]

def main ():

    n = ([3,9,6,7])
    print(sumalista(n))
    print(slista_rec(n))

main()
