from PIL import Image
import string

def highlight(files, texts_list, keyword_list):
    for i,pages in enumerate(files):
        for j, page in enumerate(pages):
        invert_img = page.load()
        for k, word in enumerate(texts_list[i][j]):
             if k == 0:
                  pass
             else:
                 lower_word = word.description.lower().strip(string.punctuation)
                 if k == 1:#first word of page

                 else:
                                                                
