from math import sqrt, ceil, floor
class Solution:
    # special number = square of prime
    # just count all primes in range [sqrt(l), sqrt(r)]
    # [l, x^2, r] -> [sqrt(l), x, sqrt(r)] where x is prime number

    def nonSpecialCount(self, l: int, r: int) -> int:
        sl, sr = ceil(sqrt(l)), floor(sqrt(r))
        cnt = 0
        for i in range(sl, sr + 1):
            if self.isprime(i):
                cnt += 1
        return r - l + 1 - cnt
    
    def isprime(self, k):
        if k == 2:
            return True
        if k % 2 == 0 or k <= 1:
            return False

        for i in range(2, int(sqrt(k))+1):
            if k % i == 0:
                return False
        return True