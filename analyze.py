from janome.tokenizer import Tokenizer
import openai
import os
import sys

if "OPENAI_API_KEY" not in os.environ:
    print("ERROR: OPENAI_API_KEY environment variable not found.")
    sys.exit(1)

openai.api_key = os.environ["OPENAI_API_KEY"]

TO_FUWAFUWA_PROMPT = """

"""

def analyze_text(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    result = []
    slander_list = []
    # MeCabで形態素解析を行う
    for token in tokens:
        print(token.surface)
        result.append(token)

        #ここで悪口かどうか判断
        with open("black_word_list.txt","r") as f:
            black_word = f.readlines()
            for i in range(len(black_word)):
                black_word[i] = black_word[i].replace("\n","")
            print(black_word)
            if token.surface in black_word:
                slander_list.append(token.surface)
                print(token)

    return slander_list
    
def openAI():
    # プロンプト
    prompt = '''
    '''

    # 推論
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": '次の日本語を言い換えてください: “チー牛"'}
    ]
    )
    print(response["choices"][0]["message"]["content"])

def IsIronic(text):
    # OpenAI GPT-3のコンプリーションモードにより、皮肉を検出するための文の作成
    prompt = f"以下の文章が皮肉であるか判断してください: \n\n {text} \n\n 答え:"

    # OpenAI APIによる皮肉検出
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print("呼び出せてるよ")
    # OpenAI APIからの応答を文字列に変換
    response_text = response["choices"][0]["message"]["content"]
    print(response_text)


def ProfanityFilter(text:str):
    with open("black_word_list.txt","r") as f:
        black_word = f.readlines()
        for i in range(len(black_word)):
            target = black_word[i].replace("\n","")
            if target in text:
                print(target)
                return True,target
        
    return False