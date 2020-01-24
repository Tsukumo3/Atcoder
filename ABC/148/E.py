class FactCounter:
    def __init__(self):
        self.counter5 = 0

    def factrize5(self,n):

        if n%5 == 0:
            self.counter5 += 1
            self.factrize5(n/5)
        else:
            return


    def even_function_num5(self,n):

        if n < 2:
            return
        else:
            self.factrize5(n)
            self.even_function_num5(n-2)
        return

    def is_odd(self,n):

        if not n %2 == 0:
            return True
        else:
            return False

        return None

if __name__ == '__main__':

    N = int(input())

    Count = FactCounter()

    ans = 0

    if Count.is_odd(N):
        pass
    else:
        Count.even_function_num5(N)
        ans = Count.counter5

    print(ans)
