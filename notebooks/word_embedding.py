from gensim.models import word2vec
import logging
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.PathLineSentences(sys.argv[1])
model = word2vec.Word2Vec(sentences, sg=1, size=100)
model.save(sys.argv[2])

# model = word2vec.Word2Vec.load(sys.argv[1])
# results = model.most_similar(positive='猫', topn=10)