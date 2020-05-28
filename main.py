#Длина наибольшего возрастающего участка
def maxlong(sf):
    try:
        err=0
        maxlg=1 #итоговый max
        maxlgloc=1#текущий max
        f=open(sf,"r")
        s=None #указатели
        p=None
        for str in f:
            try:
                for sx in [sx for s1 in str.split(' ') for s2 in s1.split("\t") for s3 in s2.split("\n") for sx in s3.split(",") if sx!=""]:
                    try:
                        if(s==None):
                            s=int(sx)#первый эл-т
                            continue
                        p=int(sx) # второй эл-т
                        if(p>=s):
                            maxlgloc=maxlgloc+1
                        else:
                            maxlgloc=1
                        s=p
                        if(maxlgloc>maxlg):
                            maxlg=maxlgloc
                    except:
                        print(sx, "That word was ignored")
            except ValueError:
                err=-2
                print("Bad value:", str)
                maxlg=None
        f.close()
        if(maxlg == 1):
            err = -3# если взять последовательность 3 2 1, то упадёт без этого условия
        return err,maxlg
    except FileNotFoundError:
        err=-3
        print("Can't open file")
        maxlg=None
    return err, maxlg

err,maxlg=maxlong("in.txt")
if(err<0):
    print("Error")
else:
    print("Длина наибольшего возрастающего участка: ",maxlg)
