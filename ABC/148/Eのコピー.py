class Solve:
    def __init__(self,n):
        self.counter5 = 0
        self._n = n

    def perform(self):

        if self.is_odd(self._n):
            return 0

        #５割り切れる値まで戻る
        while(True):

            if self._n%5 == 0:
                break
            else:
                self._n -= 2

        # 5の何乗かを考える- > 5^1で割り切れる 5^2でわれる・・・
        t = 10
        while(self._n>=t):
            self.counter5 += self._n // t
            t *= 5

        return self.counter5

    def is_odd(self,n):

        if not n %2 == 0:
            return True
        else:
            return False

        return None

if __name__ == '__main__':

    N = int(input())

    Count = Solve(N)

    ans = Count.perform()

    print(ans)
