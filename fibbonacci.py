import pygal

def fibonacci(Nterms: int, N1: int, N2: int):
    Count = 0
    # check if the number of terms is valid
    if Nterms <= 0:
        print("Please enter a positive integer")

    # if there is only one term, return n1
    elif Nterms == 1:
        print("Fibonacci sequence upto",Nterms,": ")
        print(N1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while Count < Nterms:
            print(N1)
            Nth = N1 + N2
            # update values
            N1 = N2
            N2 = Nth
            Count += 1
    return N1

nterms = int(input("How many terms? "))
fibonacci(nterms, 0, 1 )
pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render()
