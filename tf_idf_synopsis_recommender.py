import pandas as pd
import numpy as np
import json
import itertools
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

n = len(sys.argv)
if n < 2:
    print("Please input an anime name")
    sys.exit()

path_in_str = 'data/anime_list_final_231.json'
json_file = open(path_in_str)
data = json.load(json_file)
anime_df_raw = pd.DataFrame.from_dict(data, orient='index')
anime_df_raw = anime_df_raw[anime_df_raw['error'] != 'not_found']
anime_df = anime_df_raw[['id', 'title', 'mean', 'genres', 'statistics', 'num_episodes', 'synopsis']]
anime_df = anime_df.dropna()

anime_df['genres_name'] = anime_df['genres'].apply(lambda x : [a['name'] for a in x])
anime_df['genres_id'] = anime_df['genres'].apply(lambda x : [a['id'] for a in x])

anime_df['watching'] = anime_df['statistics'].apply(lambda x : x['status']['watching'])
anime_df['num_list_users'] = anime_df['statistics'].apply(lambda x : x['num_list_users'])
anime_df['completed'] = anime_df['statistics'].apply(lambda x : x['status']['completed'])
anime_df['plan_to_watch'] = anime_df['statistics'].apply(lambda x : x['status']['plan_to_watch'])
anime_df['dropped'] = anime_df['statistics'].apply(lambda x : x['status']['dropped'])
anime_df['on_hold'] = anime_df['statistics'].apply(lambda x : x['status']['on_hold'])

anime_df.drop(['genres', 'statistics'], axis=1, inplace=True)

anime_df.rename({'id': 'anime_id'}, axis=1, inplace=True)

nltk.download('wordnet', quiet = True)
nltk.download('stopwords', quiet = True)
nltk.download('averaged_perceptron_tagger', quiet = True)
nltk.download('punkt', quiet = True)
  
  
  
stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

verbs = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

def extract_tokens(text):
    text = text.lower()

    sentence =[]
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)

    i = 0
    for token in tokens:
        if tags[i][1] not in verbs: 
            lemma_tag = lemmatizer.lemmatize(token)
        else:
            lemma_tag = lemmatizer.lemmatize(token, 'v')


        if lemma_tag not in stop_words:
            if lemma_tag.isalpha():
                sentence.append(lemma_tag)
        i = i+1
            
    lemma_sentence = ' '.join(sentence)
    lemma_sentence = lemma_sentence.replace("'s", " is")
    lemma_sentence = lemma_sentence.replace("'ve", " have")
    lemma_sentence = lemma_sentence.replace("'ll", " will")
    lemma_sentence = lemma_sentence.replace("'m", " am")
    lemma_sentence = lemma_sentence.replace("n't", " not")
    lemma_sentence = lemma_sentence.replace("'d", " would")
    lemma_sentence = lemma_sentence.replace("'re", " are")
    return lemma_sentence
  
anime_df["lemma_synopsis"]= anime_df["synopsis"].apply(extract_tokens)
anime_df.head()


  
tf_idf_vectorizer = TfidfVectorizer()
tf_idf_anime_id = tf_idf_vectorizer.fit_transform((anime_df["lemma_synopsis"]))
  
cos_sim = cosine_similarity(tf_idf_anime_id, tf_idf_anime_id)
tf_idf_vectorizer.get_feature_names_out()

anime_df['anime_id'] = anime_df['anime_id'].astype(int)
anime_names = pd.Series(np.array(anime_df['title']))

  
def recommend_anime(title, max_reco = 10, cosine_sim = cos_sim):
    recommended_animes = []
    index = anime_names[anime_names == title].index[0]
    # print(index)
    # print(anime_df.iloc[index])
    
    similar_scores = pd.Series(cosine_sim[index]).sort_values(ascending = False)
    
    top_animes = list(similar_scores.iloc[1:max_reco+1].index)
    for anime_index in top_animes:
        anime_row = anime_df.iloc[anime_index]
        anime_name = anime_row['title']
        recommended_animes.append(anime_name)
    return recommended_animes

for i in range(1, n):
    print("Anime recommendations for: "+sys.argv[i])

    try:
        print(recommend_anime(sys.argv[i]))
    except:
        print("Invalid anime name according to MyAnimeList, please enter a valid name")