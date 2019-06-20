from PIL import Image
import string
from fpdf import FPDF
import os
from . import rgb

def highlight(files, texts_list, keyword_list):

    for i,pages in enumerate(files):
        width, height = pages[0].size
        pdf = FPDF(unit="pt", format= [width,height] )
        pdf.set_auto_page_break(0)
        for j, page in enumerate(pages):
            invert_img = page.load()
            word_location_list = []
            for k, word in enumerate(texts_list[i][j]):
                if k == 0:
                    pass
                else:
                    lower_word = word.description.lower().strip(string.punctuation)
                    if k == 1:#first word of page
                        for keyword in keyword_list[i]:
                            if lower_word == keyword:
                                #invert color
                                coordinate = [word.bounding_poly.vertices[0].x, word.bounding_poly.vertices[2].x, 
                                        word.bounding_poly.vertices[0].y, word.bounding_poly.vertices[2].y]
                                word_location_list.append(coordinate)
                        before_word = word
                        before_lower_word = lower_word
                    else:
                        for keyword in keyword_list[i]:
                            if len(keyword.split()) == 1:
                                if lower_word == keyword:
                                    #keyword length is 1, and it matches to word. so invert color
                                    coordinate = [word.bounding_poly.vertices[0].x, word.bounding_poly.vertices[2].x, 
                                            word.bounding_poly.vertices[0].y, word.bounding_poly.vertices[2].y]
                                    word_location_list.append(coordinate)
                            else:
                                if lower_word == keyword.split()[1] and before_lower_word == keyword.split()[0]:
                                    #keyword length is 2, and it matches to before word,
                                    #and current word, so invert both colors
                                    #invert before word's color
                                    coordinate = [before_word.bounding_poly.vertices[0].x, before_word.bounding_poly.vertices[2].x, 
                                            before_word.bounding_poly.vertices[0].y, before_word.bounding_poly.vertices[2].y]
                                    word_location_list.append(coordinate)
                                    #invert current word's color
                                    coordinate = [word.bounding_poly.vertices[0].x, word.bounding_poly.vertices[2].x, 
                                            word.bounding_poly.vertices[0].y, word.bounding_poly.vertices[2].y]
                                    word_location_list.append(coordinate)
                    before_word = word
                    before_lower_word = lower_word 

            for coordi in enumerate(word_location_list):
                for x in range(coordi[1][0], coordi[1][1]):
                    for y in range(coordi[1][2], coordi[1][3]):
                        color = invert_img[x, y]
                        invert_img[x, y] = apply_highlight_color(color, rgb.YELLOW)

            result_file_name = 'result{}-{}.png'.format(i, j)

            page.save(result_file_name)
            pdf.add_page()
            pdf.image(result_file_name)
            os.remove(result_file_name)

        pdf.output("result-{}.pdf".format(i+1),"F")


# mix original color with highlight color (use subtractive mixing)
def apply_highlight_color(origin_rgb, highlight_rgb=(255, 255, 0)):
    output_rgb = tuple(
        map(lambda x: max(0, min(255, int(x))),
            (
                255 - ((((255 - origin_rgb[i]) ** 2 + (255 - highlight_rgb[i]) ** 2) / 2) ** 0.5)
                for i in range(3)
            )
        )
    )

    return output_rgb
