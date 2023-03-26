from janome.tokenizer import Tokenizer
import openai
import os
import sys
import gensim   

if "OPENAI_API_KEY" not in os.environ:
    print("ERROR: OPENAI_API_KEY environment variable not found.")
    sys.exit(1)

openai.api_key = os.environ["OPENAI_API_KEY"]

def ToFuwafuwa(word:str):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user","content":f"「{word}」を攻撃性の低い文章に変換してください"}
        ]
    )

    answer = response["choices"][0]["message"]["content"]
    print(f"攻撃性の低い文章 : {answer}")

    # response = openai.ChatCompletion.create(
    #     model = "gpt-3.5-turbo",
    #     messages = [
    #     {"role":"user","content":"以下の文章をポジティブに変換してください"},
    #     {"role":"assistant","content":word}
    #     ]
    # )

    # answer = response["choices"][0]["message"]["content"]

    # print(f"ポジティブに変換 : {answer}" )

    return answer

def ToMoreFuwafuwa(text:str):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
        {"role":"user","content":"以下の文章をポジティブに変換してください"},
        {"role":"assistant","content":text}
        ]
    )

    answer = response["choices"][0]["message"]["content"]

    print(f"ポジティブに変換 : {answer}" ) 
    return answer


def ToFuwafuwa2(text):
    MESSAGE = ""
    with open("black_word_list.txt","r") as f:
        black_word = f.readlines()
        for i in range(len(black_word)):
            target = black_word[i].replace("\n","")
            MESSAGE += f"{target},"

    MESSAGE += """
    はネガティブな言葉です．それを踏まえて以下の文章を攻撃性の低い言い方に変換してください．
    """

    print(MESSAGE)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
        {"role":"user","content":MESSAGE},
        {"role":"assistant","content":text}
        ],
        top_p = 0.6
    )

    answer = response["choices"][0]["message"]["content"]

    print(f"第一変換 : {answer}" )

    

    return answer 
