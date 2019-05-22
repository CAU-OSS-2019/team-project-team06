
<div>
<center>
<img width='200' src="https://user-images.githubusercontent.com/43204507/57985512-f0387300-7aa3-11e9-8eea-a1cc4603d649.png">
</center>
</div>

# Highlight My Life

**Highlight My Life(HML)** is a program that highlights what is important in the pdf file of textbooks or lecture books that contain a lot of content. By highlighting, you will be able to easily understand which part of the content is important and provide convenience in studying or understanding.

Highlight My Life(HML) is an open source project developed by Chung-ang University Student Team using Google API, OCR, NLP etc..

HML is made in Python 3 version.

## Installation
---------------
To install package
```bash
    $ git clone https://github.com/CAU-OSS-2019/team-project-team06.git
    $ cd team-project-team06
    $ pip install -r requirements.txt
```
You have to get Google Cloud Vision API key for running this program.
```bash
    $ export GOOGLE_APPLICATION_CREDENTIALS="/my key location.json"
```

## Getting Started in Web
------------------------------
```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver 0.0.0.0:8000
```
<div>
<center>
Enter '127.0.0.1:8000/mainapp'
<br>
<br>
<img width = '600' src="https://user-images.githubusercontent.com/43204507/58175040-3aa33500-7cda-11e9-82fc-ba5b66133c57.png">
<br>
<br>
Press "파일선택" -> "Upload" -> "Send"
<br>
<br>
<img width = '600' src="https://user-images.githubusercontent.com/43204507/58175357-ef3d5680-7cda-11e9-96a0-4c0c45cc5663.png">
<br>
<br>
<img width = '600' src="https://user-images.githubusercontent.com/43204507/58175962-44c63300-7cdc-11e9-9485-5e7bc426d80b.png">
<br>
</center>
<p style="font-size:20px"> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspinput&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp output
</div>

## Test
-------------------

```bash
    $ cd mainapp
    $ python pdf2jpg.py -i ./input
```

## Contribute
----------------
* Issue Tracker: https://github.com/CAU-OSS-2019/team-project-team06/issues
* Source Code: https://github.com/CAU-OSS-2019/team-project-team06/

## Contribution guidelines
-----------------------
If you want to contribute to HML, be sure to review the [contribution guideline](https://github.com/CAU-OSS-2019/team-project-team06/). This project adheres to HML's code of conduct. By participating, you are expected to uphold this code.

We use GitHub issues for tracking requests and bugs.

## License
------------------------
MIT license