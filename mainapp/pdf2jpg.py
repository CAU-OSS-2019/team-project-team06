import argparse
import asyncio
import logging
import os
from pdf2image import convert_from_path
from .keywordfunction import keywordfunction

from .detect import detect_text

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
            texts = detect_text(page) #OCR
            full_text += texts[0].description
            current_page = i + 1
            logging.info('Processing page: {}'.format(current_page))
        r = keywordfunction(full_text)
        print(r.MakeKeyword())
    except Exception as e:
        logging.warning('Error: {}'.format(e))

    #키워드 추출
    text_list =[full_text]
    #print(r.MakeKeyword())

def convert(path='input', dpi=200):
    try:
        files = list_pdfs(path)
        print("tq")
        if len(files) > 0:
            for file in files:
                print("PPPP")
                file_path = os.path.join(path, file)
                convert_resume_to_text(file_path, dpi=dpi)
                asyncio.sleep(0.01)
                print("~~~")
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
    #convert('media',200)