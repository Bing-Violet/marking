# Marks
This is a mini api project.

## Getting started
You can either use the docker file to test out the code, or install django and other libraries in the requirements.txt with your virtual environment(eg. pipenv). In this case you will need to have python installed, and run '''pip install pipenv''' in your command line, see https://www.python.org/ and https://pypi.org/project/pipenv/ for more information. 

## Code Structure
'''
.
├── Dockerfile
├── README.md
├── db.sqlite3
├── docker-compose.yml
├── manage.py
├── marks
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── mark_parser.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── serializers.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── mark_parser.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20200610_0703.py
│   │   ├── 0003_auto_20200610_1231.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       ├── 0002_auto_20200610_0703.cpython-38.pyc
│   │       ├── 0003_auto_20200610_1231.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── test_files
│   │   ├── Untitled.gif
│   │   └── test.xml
│   ├── test_marks.py
│   ├── urls.py
│   └── views.py
├── marks_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
'''

## What does it do?
### Post
- It imports data from /import, and the data will be ingested with the custom-made parser, where the mark is calculated with summary marks : obtained/ available. A sample xml file may look like this:
    <mcq-test-results>
        <mcq-test-result scanned-on="2017-12-04T12:12:10+11:00">
            <first-name>Jane</first-name>
            <last-name>Austen</last-name>
            <student-number>521585128</student-number>
            <test-id>1234</test-id>
            <summary-marks available="20" obtained="13" />
        </mcq-test-result>
    </mcq-test-results>
- After being processed by the parser, data will then be stored in database. If the record with the same student id and same test id already exist in the database, the parser would compare the mark and only keep the one with higher mark, so there won't be any duplicates in the record.

### Get
- The get method take an integer parameter as the test id. So we can retrieve the aggregated data of a certain test with its id. 
- Data will be redenderedi in json format. A typical output could look like this: 
{
    "test_id": 1234,
    "count_mark": 4,
    "min_mark": {
        "mark__min": 70
    },
    "max_mark": {
        "mark__max": 95
    },
    "mean": {
        "mark__avg": 81.25
    },
    "std_mark": {
        "mark__stddev": 9.60143218483576
    },
    "percentile_25": 73.75,
    "percentile_50": 80.0,
    "percentile_75": 87.5
}

## Demo

## Limitations
It's been a hectic week and I couldn't work out a big chunk of time so my unittests are still at a premature stage. I might update the tests in the rest of the days. I fully understand the significance of TDD and apologize for my practice went the other way round this time. 




