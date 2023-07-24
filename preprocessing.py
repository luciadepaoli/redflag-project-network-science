words = set(nltk.corpus.words.words()) #the last two lines serve to download the corpus of standard English language words
stop_words = set(nltk.corpus.stopwords.words("english")) #taking the stop words from English language
tag_map = defaultdict(lambda : wn.NOUN) #here we define that wn.NOUN is the default value for the dict
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

path="./DATA/"
path_to_protocol5=path+"Tweets/REDFLAG_2021_09_01_to_2021_12_31.pkl"
with open(path_to_protocol5, "rb") as fh:
    tweets_df = pickle.load(fh)

tweets_df.columns = ['Datetime', 'Tweet Id', 'Text', 'Username', "Hashtags"]
tweets_df = tweets_df[tweets_df["Datetime"] < "2021-12-1"]
tweets_filtered = tweets_df.copy()

tweets_filtered["clean_text"] = tweets_filtered["Text"].map(cleaner)
tweets_filtered["clean_text"] = tweets_filtered["clean_text"].map(cleanu)

unique_hashtags = {}

for idx, row in tweets_filtered.iterrows():
    hashtag_list = []
    for hashtag in row["Hashtags"]:
        hashtag = hashtag.lower()
        if hashtag == "redflags":
            hashtag = "redflag"
        if hashtag == "redflags" or hashtag == "trending" :
            hashtag = "redflag"
        elif hashtag == "redflagtrend" or hashtag == "redflagstrend":
            hashtag = "redflag"
        elif  hashtag == "redflagschallenge" or hashtag == "redflagchallenge" or hashtag=="redflagwarning":
            hashtag = "redflag"
            
        unique_hashtags.setdefault("#"+hashtag, 0)
        unique_hashtags['#'+hashtag] += 1
        hashtag_list.append(hashtag)
        tweets_filtered.at[idx, "hashtags"] = hashtag_list
unique_hashtags.pop('#redflag') # remove redflag