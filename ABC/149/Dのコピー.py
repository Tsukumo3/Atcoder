class Hand:

    def __init__(self,r,s,p,k):
        self._R = r#ぐ
        self._S = s#ch
        self._P = p#pa

        self._K = k

        self.flag_r = False
        self.flag_s = False
        self.flag_p = False

    def get_flag(self,str):

        if str == "r":
            return self.flag_r

        elif str == "s":
            return self.flag_s

        elif str == "p":
            return self.flag_p

    def get_point(self,str):

        if str == "r":
            return self._P

        elif str == "s":
            return self._R

        elif str == "p":
            return self._S


if __name__ == '__main__':

    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())
    #print(T)


    aHand = Hand(R,S,P,K)
    ans = 0

    for i in range(len(T)):

        #k回前のじゃんけん
        try:
            if T[i] == T[i-K]:
                print("match")
                continue
            else:
                ans += aHand.get_point(T[i])

        except:
            print(T[i])
            print(aHand.get_point(T[i]))
            ans += aHand.get_point(T[i])

    print(ans)
