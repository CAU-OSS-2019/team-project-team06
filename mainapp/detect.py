#!/usr/bin/env python

import argparse
import re
import io

def detect_text(image):
    #Detects text in the file.
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format='png')
    image = imgByteArr.getvalue()
    image = vision.types.Image(content=image)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    
    '''
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    '''

    return texts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    detect_path_parser=parser.add_argument('path')

    args = parser.parse_args()

    detect_text(args.path)
