import pandas as pd
from prompt_var import *
from langchain.chains import LLMChain
from prompt_temp import llm,few_shot_prompt,chain
from word_extension import read_word_document
from split_insert import make_changes


###define the path for word document
word_file_path = "path for standard word document"
excel_file_path = "path for your excel file here"

def generate(excel_file_path,word_file_path):
    try:
        df = pd.read_excel(excel_file_path)
        for row in df.itertuples():
            query = (row[1::])
            section=chain.run(query)
            make_changes(section,word_file_path,row[0])



    except Exception as e:
        print("Error:", e)


