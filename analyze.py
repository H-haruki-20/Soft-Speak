from janome.tokenizer import Tokenizer
import openai

openai.api_key = "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"

def analyze_text(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    result = []
    # MeCabで形態素解析を行う
    for token in tokens:
        print(token)
        result.append(token)
    
    return result
    
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