# the exercice  in the image



# EX1

def indiceMaximum(chaine , c):
    ind=-1
    for i in range(len(chaine)-1 ,0 ,-1):
        if (chaine[i]==c):
            ind = i
            break
    return (ind)

indiceMaximum ("abccc ccca",'c')



# EX2

def parenthese(chaine ):
    ouv =0
    ferm = 0
    for ch in chaine:
        if ouv < ferm :
            return False
        else:
            if ch=='(':
                ouv += 1
            elif ch == ')':
                ferm += 1
    if ouv != ferm :
        return False
    else:
        return True


parenthese("(())a)(aa()" )
