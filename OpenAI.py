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
    model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
    lst = model.most_similar(positive=[word],negative=[""])