import math

def isPrime(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  # nの平方根まで計算する
  m = math.floor(math.sqrt(n)) + 1
  for p in range(3, m, 2):
      if n % p == 0:
        return False
  return True

if __name__ == '__main__':
    X = int(input())

    while(True):

        if isPrime(X):
            print(X)
            break
        else:
            X += 1
