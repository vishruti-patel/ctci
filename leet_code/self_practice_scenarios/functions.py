# def name():
#     print('Vishruti')
# name()


# def even_odd():
#     n = input('Enter num:')
#     n = int(n)
#     if n%2 == 0:
#         print('even')
#     else:
#         print('odd')
# even_odd()


# 3! = 3 * 2 * 1
#factorial
def fac(f):
    if  f == 0:
        return 1
    else:
        # print("fac is: ", f*fac(f-1))
        return f*fac(f-1)
print(fac(5))

# call stack - fac(5): [5*(4*3*2*1*1)]


def fact_using_for():
    n = input("Enter number:")
    n = int(n)
    r = 1
    for i in range(1, n+1):
        r =r*i
    print("Factorial is:", r)
fact_using_for()
