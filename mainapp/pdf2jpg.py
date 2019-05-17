import argparse
import asyncio
import logging
import os
from pdf2image import convert_from_path

import keywordfunction as kf
from detect import detect_text 

logging.basicConfig(
     level=logging.INFO,
     format='{%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
)

def list_pdfs(path='input'):
    files = os.listdir(path)
    pdfs = [i for i in files if i.split('.')[-1] == 'pdf']
    return pdfs


def convert_resume_to_text(file_path, dpi=200):
    pages = convert_from_path(file_path, dpi)
    full_text = ""
    try:
        logging.info('No. of pages: {}'.format(len(pages)))
        page_len = len(pages)
        for i, page in enumerate(pages):
            page_text = detect_text(page) #OCR
            full_text += page_text[0].description 

            #highlighting test code
            invert_img = page.load()
            compare_string = ['important','audience','competitions','sportsmanship']
            for text in texts:
                lower_text = text.description.lower().strip(string.punctuation)
                if lower_text in compare_string:
                    start_x = text.bounding_poly.vertices[0].x
                    start_y = text.bounding_poly.vertices[0].y
                    end_x = text.bounding_poly.vertices[2].x
                    end_y = text.bounding_poly.vertices[2].y
                    for x in range(start_x, end_x):
                        for y in range(start_y, end_y):
                            color = invert_img[x,y]
                            invert_img[x,y] = (255-color[0],255-color[1],255-color[2])
            page.save("result.png")

            current_page = i + 1
            logging.info('Processing page: {}'.format(current_page))

    except Exception as e:
        logging.warning('Error: {}'.format(e))

    #키워드 추출
    text_list =[full_text]
    print(r.MakeKeyword())

async def convert(path='input', dpi=200):
    try:
        files = list_pdfs(path)
        if len(files) > 0:
            for file in files:
                file_path = os.path.join(path, file)
                convert_resume_to_text(file_path, dpi=dpi)

                await asyncio.sleep(0.01)
    except Exception as e:
        logging.warning('Error: {}'.format(e))

async def main(path, dpi=200):
    await asyncio.wait([
        convert(path=path, dpi=dpi)
    ])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='PDF to JPG')
    parser.add_argument('-i', '--input', required=True,
                        help="Input dir containing PDF files")

    ap = vars(parser.parse_args())
    resume_dir = ap['input']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(resume_dir))
