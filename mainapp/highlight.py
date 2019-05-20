from PIL import Image
import string
from fpdf import FPDF
import os

def highlight(files, texts_list, keyword_list):
    for i,pages in enumerate(files):
        width, height = pages[0].size
        pdf = FPDF(unit="pt", format= [width,height] )
        pdf.set_auto_page_break(0)

        for j, page in enumerate(pages):
            invert_img = page.load()
            for k, word in enumerate(texts_list[i][j]):
                if k == 0:
                    pass
                else:
                    lower_word = word.description.lower().strip(string.punctuation)
                    if k == 1:#first word of page
                        for keyword in keyword_list[i]:
                            if lower_word == keyword:
                                #invert color
                                start_x = word.bounding_poly.vertices[0].x
                                start_y = word.bounding_poly.vertices[0].y
                                end_x = word.bounding_poly.vertices[2].x
                                end_y = word.bounding_poly.vertices[2].y
                                for x in range(start_x, end_x):
                                    for y in range(start_y, end_y):
                                        color = invert_img[x,y]
                                        invert_img[x,y] = (255-color[0],255-color[1],255-color[2])
                        before_word = word
                        before_lower_word = lower_word
                    else:
                        for keyword in keyword_list[i]:
                            if len(keyword.split()) == 1:
                                if lower_word == keyword:
                                    #keyword length is 1, and it matches to word. so invert color
                                    start_x = word.bounding_poly.vertices[0].x
                                    start_y = word.bounding_poly.vertices[0].y
                                    end_x = word.bounding_poly.vertices[2].x
                                    end_y = word.bounding_poly.vertices[2].y
                                    for x in range(start_x, end_x):
                                        for y in range(start_y, end_y):
                                            color = invert_img[x,y]
                                            invert_img[x,y] = (255-color[0],255-color[1],255-color[2]) 
                            else:
                                if lower_word == keyword.split()[1] and before_lower_word == keyword.split()[0]:
                                    #keyword length is 2, and it matches to before word,
                                    #and current word, so invert both colors
                                    #invert before word's color
                                    start_x = before_word.bounding_poly.vertices[0].x
                                    start_y = before_word.bounding_poly.vertices[0].y
                                    end_x = before_word.bounding_poly.vertices[2].x
                                    end_y = before_word.bounding_poly.vertices[2].y
                                    for x in range(start_x, end_x):
                                        for y in range(start_y, end_y):
                                            color = invert_img[x,y]
                                            invert_img[x,y] = (255-color[0],255-color[1],255-color[2])
                                    #invert current word's color
                                    start_x = word.bounding_poly.vertices[0].x
                                    start_y = word.bounding_poly.vertices[0].y
                                    end_x = word.bounding_poly.vertices[2].x
                                    end_y = word.bounding_poly.vertices[2].y
                                    for x in range(start_x, end_x):
                                        for y in range(start_y, end_y):
                                            color = invert_img[x,y]
                                            invert_img[x,y] = (255-color[0],255-color[1],255-color[2])
                    before_word = word
                    before_lower_word = lower_word 
            result_file_name = 'result{}-{}.png'.format(i, j)

            page.save(result_file_name)
            pdf.add_page()
            pdf.image(result_file_name)
            os.remove(result_file_name)

        pdf.output("result-{}.pdf".format(i+1),"F")

