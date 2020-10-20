import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('jawiki.word_vectors.100d.txt')

# ベクトルを取り出す
print(model['日本'])

# 類似した単語を取り出す
print(model.most_similar('日本'))
