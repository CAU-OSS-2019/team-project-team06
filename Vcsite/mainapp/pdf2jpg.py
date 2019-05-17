import argparse
import asyncio
import logging
import os
from pdf2image import convert_from_path

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
 
