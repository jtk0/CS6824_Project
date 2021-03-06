import tweetGenerator
import os
import pickle
from gensim import corpora
import gensim 
from gensim.corpora import Dictionary

def createWordFrequencyFile(fileLoc = "./data/wordFrequency.txt",useCache=True):
    if (useCache==True and os.path.isfile(fileLoc)):
         wf = pickle.load( open(fileLoc,'rb'))
         return wf
    tg = tweetGenerator.tweetGenerator()
    wordFreqDict = {}
    for tweet in tg:
        for word in tweet:
            if word in tg:
                wordFreqDict[word]=wordFreqDict[word]+1
            else:
                wordFreqDict[word]=1
    pickle.dump(wordFreqDict,open(fileLoc,'wb'))
    return wordFreqDict

def createDictionary(dictLoc="./data/dict",useCache=True):
    if (useCache==True and os.path.isfile(dictLoc)):
        dictionary = Dictionary.load_from_text(dictLoc)
    else:
        tg = tweetGenerator.tweetGenerator()
        wf = createWordFrequencyFile()
        dictionary = Dictionary(tg)
        dct.save_as_text(dictLoc) 
    return dictionary


#for value in vectorizedTweets():
# break
# print value


def lda():
 wf = createWordFrequencyFile()
 dic =createDictionary()
 tg = tweetGenerator.tweetGenerator()
 corpus = []
 for tweet in tg:
    corpus.append(dic.doc2bow(tweet))
 lda = gensim.models.ldamodel.LdaModel(corpus,10,dic)
 return lda
