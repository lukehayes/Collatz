from collatz.helpers import is_even

def collatz(n):
    """Generate a Collatz number -> (3n+1)"""

    if(n == 1):
        return 1
    else:
        if(is_even(n)):
            print(n, end=" ")
            return collatz(int(n/2))
        else:
            print(n, end=" ")
            return collatz(int(3*n+1))
