import os
import platform

#パス指定
file_name = "NewProjectFile(新しいファイル)"
dir_path = "../../" + str(file_name)
README_path = "../../" + str(file_name) + "/README.md"
memo_path = "../../" + str(file_name) + "/Ver1.0/実行環境.txt"

#フォルダ作成(重複時にはファイル作成をしない)
try:
    os.mkdir(dir_path)
except FileExistsError:
    print("FileExistsError:すでに同じ名前のファイルが存在しています")

os.mkdir(dir_path + "/Ver1.0")

#README作成
readme_list = ["# Title<br>",
               "## 機能<br>",
               "## ざっくりとした仕組み<br>",
               "## 動かない場合<br>",
               "・実行できない！<br>",
               "→Python実行環境がない可能性があります。Pythonの実行環境を用意してください。<br>",
               "## お問い合わせ<br>",
               "何かございましたら「shaneron@sumahotektek.com」まで連絡ください。反応は非常に遅いです。<br>",
               "### 変更履歴<br>",
               "Ver1.0:初期バージョン"]

with open (README_path, 'w', encoding = 'UTF-8') as r:
    for word in readme_list:
        r.write(word + "\n\n")

#Pythonバージョン取得→メモ帳保存
py_version = platform.python_version()

with open (memo_path, 'w', encoding = 'UTF-8') as f:
    f.write("Python " + py_version)