import math
def isPrime(num):
    if num <= 1 or (num%2)==0:
        return False
    for check  in range(3,int(math.sqrt(num))):
        if num%check == 0:
            return False
    return True
def isPrime2(num):
    if num <= 1:
        return False
    for check in range(2,int(num/2)+1):
        if(num % check == 0):
            return False
    return True

def check(n):
    print(f"isPrume({n}) => {isPrime2(n)}")



def test_isPrime():
    assert (isPrime(2)),"fallo con 2"
    assert (isPrime(3)),"fallo con 3"
    assert (isPrime(5)),"fallo con 5"
    assert (isPrime(4)),"fallo con 4"
    assert (isPrime(6)),"fallo con 6"
    assert (isPrime(8)),"fallo con 8"
    assert (isPrime(10)),"fallo con 10"
    assert (isPrime(1)),"fallo con 1"
    assert (isPrime(0)),"fallo con 0"
    assert (isPrime(-3)),"fallo con -3"

if __name__ == "__main__":
    # check(int(input("Ingrese numero:")))
    test_isPrime()



