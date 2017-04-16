x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def km(x1,y1):
    # Key subroutine for the Karatsuba multiplication algorithm
    x2 = str(x1)
    y2 = str(y1)

    #Basic case to exit recursion
    if len(x2) == 1 and len(y2) == 1:
        return x1*y1

    #Calculatung a,b,c and d
    n = max(len(x2),len(y2))
    n = n + n%2
    n2 = n // 2
    q1 = len(x2) - n2
    q2 = len(y2) - n2
    if x2[:q1] == '':
        a = 0
    else:
        a = int(x2[:q1])
    if x2[q1:] == '':
        b = 0
    else:
        b = int(x2[q1:])
    if y2[:q2] == '':
        c = 0
    else:
        c = int(y2[:q2])
    if y2[q2:] == '':
        d = 0
    else:
        d = int(y2[q2:])
    #Recursive call to calculate product of a and c
    ac = km(a,c)
    # Recursive call to calculate product of b and d
    bd = km(b,d)
    # Recursive call to calculate (a+b)*(c+d) - a*c - b*d
    sec = km(a+b,c+d) - ac - bd
    return 10**n*ac + 10**n2*sec + bd

w = x*y
w2 = km(x,y)

# print(w)
print(w2)