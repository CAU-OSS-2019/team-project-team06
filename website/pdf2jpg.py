import argparse
import asyncio

async def convert(path='input', dpi=200):
    files = list_pdfs(path)

    if len(files) > 0:
        for file in files:
            file_path = os.path.join(path, file)
           
            await asyncio.sleep(0.01)


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
 
