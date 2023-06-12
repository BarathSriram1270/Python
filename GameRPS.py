import random
def res():
    return random.randint(0,2)
def game(m):
    a=res()
    b=res()
    if a==b:
        return 't'
    elif a==0 and b==1:
        print("Round ",m,":A is rock B is paper B won")
        return 'b'
    elif a==1 and b==0:
        print("Round ",m,":A is paper B is rock A won")
        return 'a'
    elif a==1 and b==2:
        print("Round ",m,":A is paper B is scissors B won")
        return 'b'
    elif a==2 and b==1:
        print("Round ",m,":A is scissors B is paper A won")
        return 'a'
    elif a==2 and b==0:
        print("Round ",m,":A is scissors B is rock B won")
        return 'b'
    else:
        print("Round ",m,":A is rock B is scissors A won")
        return 'a'
n=int(input("Enter how rounds"))
awin=0
bwin=0
m=0
x=int(input("Do you want to consider tie?\nIf yes enter 1 If not enter 0"))
if x==1:
    for i in range(n):
        m=m+1
        result = game(m)
        if result=='a':
            awin=awin+1
        elif result=='b':
            bwin=bwin+1
        while result =='t':
            result=game(m)
            if result=='a':
                awin=awin+1
            elif result=='b':
                bwin=bwin+1
    print("A won:",awin,"B won:",bwin)
elif x==0:
    for i in range(n):
        m=m+1
        result = game(m)
        if result=='a':
            awin=awin+1
        elif result=='b':
            bwin=bwin+1
    print("A won:",awin,"B won:",bwin)