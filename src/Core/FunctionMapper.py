# map recognized text to respective functions

import pickle
import sys
from unittest import result
sys.path.append(".")
sys.path.append("./")
from src.Utils.to_tokens import sentence_pipeline,create_corpa
class FunctionMapper:
    def __init__(self) -> None:
        try:                                        #load corpa
            with open('src/tokens', 'rb') as f:     
                df, tfidf_df, tfidf = pickle.load(f)
        except:
            create_corpa()
            df, tfidf_df, tfidf = pickle.load(f)
    def return_function(self,text):
        query_terms = ["what",
                "where",
                "how",
                "who",
                "why",
                "which",
                "when",
                "whose",
                "at"]
        try:                                        #load corpa
            with open('src/tokens', 'rb') as f:     
                df, tfidf_df, tfidf = pickle.load(f)
        except:
            create_corpa()
            _ , tfidf_df, tfidf = pickle.load(f)
        result=  sentence_pipeline(text , tfidf , tfidf_df)
        try:
            _ = text.split(" ")[0]
            if(_ == "surf"):
                result = 8
        except:
            pass
        try:
            _ = text.split(" ")[0]
            if(_ in query_terms and result !=4 and result!=5 and result!=2):
                result = 9
        except:
            pass
        try:
            _ = text.split(" ")[0]
            if(_ == "info"):
                result = 10
        except:pass
        try:
            _ = text.split(" ")[0]
            if(_ == "solve"):
                result = 7
        except:pass
        print(result)
        
        return result

if __name__ == "__main__":
    fc = FunctionMapper()
    print(fc.return_function('open youtube'))