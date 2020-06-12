x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
#ヘロン公式
a = pow( pow(abs(x_a - x_b),2) + pow(abs(y_a - y_b), 2), 0.5)
b = pow( pow(abs(x_b - x_c),2) + pow(abs(y_b - y_c), 2), 0.5)
c = pow( pow(abs(x_c - x_a),2) + pow(abs(y_c - y_a), 2), 0.5)
s = (a+b+c)/2
ans = pow(s*(s-a)*(s-b)*(s-c), 0.5)
print(ans)
