#a, b = map(float, input().split())

a, b = input().split()
from decimal import Decimal
import math
print(math.floor(int(a)*Decimal(b)))
