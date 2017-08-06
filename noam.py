import turtle


h = 0
m = 0
s = 0
def fun_time():
    global h
    global m
    global s

    if s==60:
        s= 0
        s+= 1


    if m==60:
        m= 0
        m+= 1


    if h==24:
        h= 0
        h+= 1

turtle.outime(fun_time, 1000)

