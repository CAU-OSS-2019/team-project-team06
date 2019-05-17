class keywordfunction:
    def __init__(self, StringBox):
        self._StringBox = StringBox

    def MakeKeyword(self):
        # corpus 전체 말뭉치
        corpus = []
        text_num = []
        number = 0
        for i in self._StringBox:
            corpus.append(i)
            text_num.append(number)
            number += 1

        num_docs = len(corpus)

        
