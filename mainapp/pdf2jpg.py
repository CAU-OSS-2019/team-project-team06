import argparse
import asyncio
import logging
import os
from pdf2image import convert_from_path
import mainapp.keywordfunction as kf

from mainapp.detect import detect_text
from mainapp.highlight import highlight

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
    returnvalue = []
    texts_list = []
    page_count = 0
    try:
        logging.info('No. of pages: {}'.format(len(pages)))
        page_len = len(pages)
        for i, page in enumerate(pages):
            texts = detect_text(page) #OCR
            texts_list.append(texts)
            full_text += texts[0].description
            page_count += 1
            current_page = i + 1
            logging.info('Processing page: {}'.format(current_page))

        returnvalue.append(texts_list)
        returnvalue.append(full_text)
        returnvalue.append(pages)
        returnvalue.append(page_count)
        return returnvalue
    except Exception as e:
        logging.warning('Error: {}'.format(e))


def convert(path='input', dpi=200, color='YELLOW'):
    full_text_list = []
    full_texts_info = []
    full_page_list = []
    try:
        files = list_pdfs(path)
        if len(files) > 0:
            for file in files:
                file_path = os.path.join(path, file)
                convert_data = convert_resume_to_text(file_path, dpi=dpi)
                full_texts_info.append(convert_data[0])
                full_text_list.append(convert_data[1])
                full_page_list.append(convert_data[2])
                page_count = convert_data[3]
                asyncio.sleep(0.01)
            r = kf.keywordfunction(full_text_list)
            print(r.MakeKeyword())
            highlight(full_page_list, full_texts_info, r.MakeKeyword(), color)

    except Exception as e:
        logging.warning('Error: {}'.format(e))


async def main(path, dpi=200):
    await asyncio.wait([
        convert(path=path, dpi=dpi, color='YELLOW')
    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDF to JPG')
    parser.add_argument('-i', '--input', required=True,
                        help="Input dir containing PDF files")

    ap = vars(parser.parse_args())
    resume_dir = ap['input']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(resume_dir))
    # convert('media',200)
