n = input()

first = n[0]
length = len(n)
guess = int(''.join([first]*length))

if guess >= int(n):
    print(guess)
else:
    next = int(first)+1
    guess = int(''.join([str(next)]*length))
    print(guess)
