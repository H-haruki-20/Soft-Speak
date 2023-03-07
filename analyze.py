from janome.tokenizer import Tokenizer
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

def analyze_text(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    result = []
    slander_list = []
    # MeCabで形態素解析を行う
    for token in tokens:
        print(type(token))
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
        {"role": "user", "content": '次の日本語を言い換えてください: “ガリガリ"'}
    ]
    )
    print(response["choices"][0]["message"]["content"])