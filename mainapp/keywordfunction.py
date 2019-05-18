import math
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import gc
from collections import Counter
from nltk.tag import pos_tag

class keywordfunction:
    def __init__(self, StringBox):
        self._StringBox = StringBox

    def MakeKeyword(self):
        # corpus 전체 말뭉치
        corpus = []
        text_num = []
        number = 0
        for i in self._StringBox:
            corpus.append(i.replace("\n", " "))
            text_num.append(number)
            number += 1

        num_docs = len(corpus)

        # 문서집합에서 단어토 생성 후 토큰 빈도 수 세고 인코딩 벡터 만들
        v = CountVectorizer(ngram_range=(1, 2), binary=True, stop_words='english', min_df=1)

        vf = v.fit_transform(corpus)

        # min_df는 단어장에 포함되기 위한 최소 빈도
        # fit변환계수 추정, transform

        terms = v.get_feature_names()
        freqs = np.asarray(vf.sum(axis=0).ravel())[0]
        idfs = [math.log10(num_docs / f) for f in freqs]
        custom_weight1 = np.array([1 + math.log10(f) for f in freqs])

        keywords1 = []
        interval = 100
        cur_index = 0

        while cur_index < len(corpus):
            v = CountVectorizer(ngram_range=(1, 2), stop_words='english', vocabulary=terms, min_df=1)
            vf = v.fit_transform(corpus[cur_index:cur_index + interval])
            a = vf.toarray()

            for data in a:
                x = np.copy((np.log10(data + 1) * idfs * custom_weight1).argsort()[-20:][::-1])
                keywords1.append(x)

            del v
            del vf
            del a
            gc.collect()
            cur_index += interval
        # 메모리문제때문에 키워드 100간격씩 추출하고 메모리 해제

        x1 = np.array(keywords1).flatten()

        # 중복 없애기->집합생성
        dummy = x1.copy().tolist()

        # 중복된거지워주기

        occ = Counter(dummy)
        # 동일한 값의 자료가 몇개인지 파악

        for wid in list(occ.keys()):
            if occ[wid] < 1:
                del occ[wid]
        # 15개 이하로 나온건 다 제거

        # survived 최종 남은 키워드
        survived = {}
        for word in list(occ.keys()):
            for i, k in enumerate(keywords1):
                # 열거해서 정렬
                if word in k:
                    if text_num[i] not in survived:
                        survived[text_num[i]] = [word]
                    else:
                        survived[text_num[i]].append(word)


        survived_articles = list(survived.keys())
        survived_articles.sort()

        finalkeyword = []
        for s in survived_articles[:30]:
            output = [terms[x] for x in survived[s]]
            finalkeyword.append(output)

        tagged_list = []
        for i in finalkeyword:
            tagged_list.append(pos_tag(i))
        #print(tagged_list)

        return finalkeyword
