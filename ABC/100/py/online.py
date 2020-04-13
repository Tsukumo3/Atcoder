import requests
from bs4 import BeautifulSoup

# 問題ページの URL (例)
problem_url = "https://atcoder.jp/contests/abc147/tasks/abc147_a"

# 問題ページの情報を取得
problem_html = requests.get(problem_url)
problem_soup = BeautifulSoup(problem_html.content, "html.parser")

#for i in problem_soup.find_all("pre"):
#    print(i.get_text())

# サンプルデータを取得
testcase = problem_soup.find_all("pre")

# サンプルの数
# 英語ページのサンプルも取ってきているので省く
n = len(testcase)
if n % 2 == 0:
    n = int(n / 2)

# サンプル入出力をファイルに書き込む
for i in range(1, n, 2):
    # 例
    # testcase[1] -> Sample1 の入力
    # testcase[2] -> Sample1 の出力
    case_num = int((i + 1) / 2)

    # i == 1 なら in1.txt に Sample1 の 入力を保存
    in_path = "in" + str(case_num) + ".txt"
    f_in = open(in_path, "w")
    f_in.write(testcase[i].get_text())
    f_in.close()

    # 出力例も同様
    out_path = "out" + str(case_num) + ".txt"
    f_out = open(out_path, "w")
    f_out.write(testcase[i + 1].get_text())
    f_out.close()
