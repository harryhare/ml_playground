import pandas as pd
import numpy as np
import random

from keras.layers import Input, Embedding, Dot, Reshape, Dense
from keras.models import Model
random.seed(100)


#load dataset
user_keywords = pd.read_csv("user_keywords.csv")



def date_process(user_item):
    """user_item is a DataFrame, column=[user_id, keywords]
    1. user_item: user and item information, user_id, keywords, keyword_index
    2. user_index: user to index
    3. item_index：item to index
    """
    user_item["keywords"] = user_item["keywords"].apply(lambda x: x.split("|"))
    keyword_list = []
    for i in user_item["keywords"]:
        keyword_list.extend(i)

    # word count
    item_count = pd.DataFrame(pd.Series(keyword_list).value_counts())
    # add index to word_count
    item_count['id'] = list(range(0, len(item_count)))

    # 将word的id对应起来
    map_index = lambda x: list(item_count['id'][x])
    user_item['keyword_index'] = user_item['keywords'].apply(map_index)  # 速度太慢
    # create user_index, item_index
    user_index = {v: k for k, v in user_item["user_id"].to_dict().items()}
    item_index = item_count["id"].to_dict()
    return user_item, user_index, item_index


user_keywords, user_index, keyword_index = date_process(user_keywords)
