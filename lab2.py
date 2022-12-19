import numpy as np
import math as m
import copy
from PIL import Image, ImageDraw

N = 38
LimIt = 38
path = ["original/0.png", "original/1.png", "original/2.png", "original/3.png", "original/4.png", "original/5.png", "original/6.png", "original/7.png", "original/8.png", "original/9.png"]
M=0

def remake_y(Y):
    Y_new = copy.deepcopy(Y)
    for i in range(len(Y[0])):
        if Y[0][i][0] < 0:
            Y_new[0][i][0] = -1
        else:
            Y_new[0][i][0] = 1
    return Y_new
    

def compare(Y, X):
    for j in range(len(X)):
        k = 0
        for i in range(len(Y[0])):
            if Y[0][i][0] == X[j][i][0]:
                k = k + 1
        if k == len(Y[0]):
            return True
    return False


def get_Y_i(y, Y_new):
    Y_i = []
    for i in range(38):
        y = func()
        y = y +1
        Y_i.append(y)
    if len(Y_i)==len(Y_new):
        print("Everything is okay", Y_i)
    else: 
        print("Sorry, you made a mistake")
    return Y_i


def func(Y):
    num = hypsin(Y)
    den = hypcos(Y)
    for i in range(n):
        for j in range(n):
            Y[i][j] =  num/ den 
    return Y

e=2.718282


def hypsin(Y):
    s = (pow(e, Y[i][j]) - pow(e, -Y[i][j]))/2
    return s


def hypcos(Y):
    c = (pow(e, Y[i][j]) + pow(e, -Y[i][j]))/2
    return c



def depict(path, Y):
    global N
    img = Image.new('1', (38, 38), "white")
    draw = ImageDraw.Draw(img)
    k = 0
    for i in range(N):
        for j in range(N):
            if Y[k][0] >= 0:
                color = 1
            else:
                color = 0
            k = k + 1
            draw.point((i, j), color)
    img.show()
    img.save(path)


Y_last = []


def trial(W, Y):
    global Y_last
    res= F(W@Y[0])
    Y_last.append(res)
    return Y_last


def F(Y):
    for i in range(len(Y)):
        for j in range(len(Y[i])):
            Y[i][j] = (m.exp(Y[i][j]) - m.exp(-Y[i][j])) / (m.exp(Y[i][j]) + m.exp(-Y[i][j]))
    return Y


def take_w(X):
    W = np.zeros((1444, 1444))
    for i in range(len(X)):
        first=(W@X[i]-X[i])
        second=(W@X[i]-X[i]).T
        numerator = first@second
        secFirst= X[i].T@X[i]
        secSec= X[i].T@W@X[i]
        denominator = (secFirst-secSec)
        W = W+ (numerator / denominator)
    return W


def get_M(Neur):
    global M
    global N
    if Neur==N:
        M=N/(2*m.log2(N))    
    print("Value of memory=", M)


def get_alpha(M):            
    global N
    alpha= M/N
    print("The ratio of the number of key images M that can be remembered to the number of network neurons is alpha")
    print("alpha=", alpha)


def get_E(W):
    E=0
    lenght=len(S)
    for i in range(lenght):
        for j in range(lenght):
            E += (-0.5*(S[i]@S[j]@W))
    return E


def take_img(path):
    X = []
    for a in range(len(path)):
        x = np.zeros((1444, 1))
        img = Image.open(path[a])
        pell = img.load()
        l = 0
        for i in range(N):
            for j in range(N):
                if pell[i, j][0] == 255:
                    needed_pell = 1
                else:
                    needed_pell = -1
                x[l] = needed_pell
                l = l + 1
        X.append(x)
    return X


def main():
    global path
    return path


def start(original_pic):
    show_bad_image = Image.open("bad/%s.png" % original_pic)
    show_bad_image.show()


flag = True
its = 0


def cycle(W, X):
    global flag
    global its
    Y = take_img(["bad/%s.png" % original_pic])
    while flag:
        if its >= LimIt:
            print("Can't recognize")
            break
        Y = trial(W, Y)
        Y_new = remake_y(Y)
        if compare(Y_new, X) is True:
            print("Ok, recognized picture: result/img.png")
            depict(f"result/img.png", Y[0])
            flag = False
        its = its + 1



if __name__ == "__main__":
    main()
    X = take_img(path)
    W = take_w(X)
    original_pic = input("Input number to recognize: ")
    start(original_pic)
    get_E(W)
    get_Y_i(y, Y_new)
    cycle(W, X)
    Neur= 38
    get_M(Neur)
    get_alpha(M)