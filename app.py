from flask import Flask, render_template, request
from analyze import analyze_text,openAI

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 入力されたテキストを取得する
        text = request.form.get("input_text")
        
        # MeCabで解析する
        analyzed_text = analyze_text(text)
        
        # 解析結果を表示する
        return render_template("result.html",text=analyzed_text)
    
    else:
        openAI()
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)