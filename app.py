from flask import Flask, render_template, request, url_for, redirect
from analyze import *
from OpenAI import *
import random
import csv

import re

COUNT_MAX = 10

app = Flask(__name__)

@app.route("/more-fuwafuwa", methods = ["GET","POST"])
def fuwafuwa():
    if request.method == "GET":
        with open("text.txt","r") as f:
            r = f.readline()
            text = r.replace("\n","")
            print(f"もっとふわふわにするテキストはこちら : {text}")
        answer_from_GPT = ToMoreFuwafuwa(text)
        return render_template("result.html",text=answer_from_GPT)

@app.route("/report", methods = ["GET","POST"])
def report():
    if request.method == "POST":
        text = request.form.get("report_text")
        print(f"ユーザーから「{text}」がちくちく言葉として報告されました")

        with open("data/report.csv","at") as f:
            writer = csv.writer(f)
            writer.writerow([text,0])

        #report 押したときの処理 (thanks.htmlを表示)
        return render_template("thanks.html")

    # report押したときの処理 (thanks.htmlを表示する?)
    with open("text.txt","r") as f:
        r = f.readline()
        text = r.replace("\n","")
        print(f"text : {text}")
    answer_from_GPT = ToFuwafuwa(text)
    return render_template("result.html",text=answer_from_GPT)


@app.route("/count", methods = ["GET","POST"])
def count():
    if request.method == "GET":
        req = request.args
        num = int(req.get("num"))
        with open('data/report.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        print(data)
        value = int(data[num][1]) + 1
        data[num][1] = value
        if value == COUNT_MAX:
            # データセット << どんな内容をCSVファイルに書くか >>
            with open("data/fine_tuning.csv","a") as f:
                writer = csv.writer(f)
                print(f"10回以上{[data[num][0]]}は「はい」が押されたよ")
                writer.writerow([data[num][0]])

        # 書き換えたデータをCSVファイルに保存する
        with open('data/report.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return render_template("index-no.html")
    else:
        # 入力されたテキストを取得する
        text = request.form.get("input_text")
        with open("text.txt","w") as f:
            f.write(text)
        answer_from_GPT = ToFuwafuwa(text)
        if "「" in answer_from_GPT:
            answer_from_GPT = re.findall("(?<=「).+?(?=」)", answer_from_GPT)[0]

        # 解析結果を表示する
        return render_template("result.html",text=answer_from_GPT) 
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 入力されたテキストを取得する
        text = request.form.get("input_text")
        with open("text.txt","w") as f:
            f.write(text)
        answer_from_GPT = ToFuwafuwa(text)
        if "「" in answer_from_GPT:
            answer_from_GPT = re.findall("(?<=「).+?(?=」)", answer_from_GPT)[0]

        # 解析結果を表示する
        return render_template("result.html",text=answer_from_GPT)
    
    else:
        targets = []
        with open("data/report.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                targets.append(row[0])
            num = random.randint(0,len(targets)-1)
            target = targets[num].replace("\n","")
            print(f"target : {target}")
            
        return render_template("index.html",target=targets[num],num=num)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)