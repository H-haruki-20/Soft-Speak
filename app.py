from flask import Flask, render_template, request
from analyze import *
from OpenAI import *

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 入力されたテキストを取得する
        text = request.form.get("input_text")
        
        result,word = ProfanityFilter(text)
        print(f"result : {result}")
        print(f"word : {word}")
        if result:
            # 悪口の部分の言い換えを行う (Chat-GPT)
            final = text.replace(word,"ペンギン")
        
        # 解析結果を表示する
        return render_template("result.html",text=final)
    
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)