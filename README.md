# Scrapy Spider

**This scrapy spider is used to scrape all the submissions from CodeForces of a particular user.
It also scrapes all the test-cases of the problem.**

![Output Image](https://github.com/revantg/scraping-codeforces/raw/master/Screenshot%20from%202018-11-25%2002-04-22.png)

# Usage / Installation

## Architecture
```bash
├── 2018-10-15 22:27:04.359764.pickle
├── codeforces
│   ├── gen_prog_file.py
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── items.cpython-36.pyc
│   │   ├── pipelines.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py
│   └── spiders
│       ├── codeforces_scraper.py
│       ├── __init__.py
│       └── __pycache__
│           ├── __init__.cpython-36.pyc
│           └── ltra_golu.cpython-36.pyc
├── scrapy.cfg
├── Screenshot from 2018-11-25 02-04-22.png
└── submission_list.json

4 directories, 18 files

```
## Installation
This section will guide you through a series of steps to setup this project on your computer.

### Requirements

Make sure you have the following installed to proceed further into the installation process

 - Python 3.5 (or above)
 - Python Package Manager - ( PIP )
 - Git 

### Install Dependencies

All the dependencies and Packages have been conveniently bundles into a `'requirements.txt'` file for a smooth installation and have the Project Up and running on your machine with minimal effort and time.
Run the following commands from the terminal .

Get a complete copy of the project by cloning into a suitable directory

    git clone https://github.com/revantg/scraping_courses.git
  
 Install all the dependencies by running the command from the terminal.

    sudo pip install -r requirements.txt

## Usage

 - For running the spider run the following command from the terminal.
```bash
scrapy crawl codeforces -a username=abhishekvr12 -a submission_id=43738235
```
### Arguments
``username`` - The codeforces handle whose submissions are to be scraped	
``submission_id`` - All the submissions submitted after this submission id will be scraped.
- Change the value of the ``path`` variable in ``pipelines.py`` file where you want your submissions to be placed.




This generates the follow	ing files

-  ```log_final.txt``` - Complete output of the scrapy spider
- ```courses_data.json``` - Scraped data of all the courses

## Output

This script generates data for a course in the following format
```json
{
  "submission_stats": [
    {
      "date_time": "2018-09-05 17:07:27",
      "submission_id": "42495359",
      "problem_name": "B - Run For Your Prize",
      "submission_link": "http://codeforces.com/contest/938/submission/42495359",
      "participant_id": "19532151",
      "contest_url": "http://codeforces.com/contest/938/problem/B",
      "submission_lang": "GNU C++14",
      "time_consumed": "46 ms",
      "memory_consumed": "400 KB",
      "submission_verdict": "OK",
      "submission_verdict_text": "Accepted",
      "problem_id": [
        "938",
        "B"
      ]
    }
  ],
  "username" : "abhishekvr12",
  "submissionid": "42495359",
  "problemname": "B - Run For Your Prize",
  "language": "GNU C++14",
  "verdict": "Accepted",
  "time_taken": [
    "46 ms"
  ],
  "memory": "396 KB",
  "submitted_time": "2018-09-05 17:07:27",
  "judged_time": "2018-09-05 17:07:27",
  "program": [
    "#include <bits/stdc++.h>\r\n\r\nusing namespace std;\r\n\r\nint main()\r\n{\r\n    int n;\r\n    scanf(\"%d\", &n);\r\n    vector<int> v(n);\r\n    for(int i=0; i<n; i++) scanf(\"%d\", &v[i]);\r\n    int ans=0;\r\n    for(int i=0; i<n; i++) ans=max(ans,min(v[i]-1,(int)1e6-v[i]));\r\n    printf(\"%d\\n\",ans);\r\n    return 0;\r\n}"
  ],
  "testcases_data": [
    {
      "test_no": "1\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "3\r\n2 3 9\r\n",
      "output_data": "8\r\n",
      "correct_answer": "8\r\n",
      "comment": "ok answer is '8'\r\n",
      "Time": ": 0 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "2\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "2\r\n2 999995\r\n",
      "output_data": "5\r\n",
      "correct_answer": "5\r\n",
      "comment": "ok answer is '5'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "3\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "100000\r\n20 35 37 70 81 83 103 106 127 137 157 162 164 178 201 204 205 212 213 217 246 254 255 265 267 282 301 312 316 321 341 343 348 364 366 388 391 420 423 426 433 436 450 459 460 479 482 492 523 528 529 538 545 551 558 566 578 584 586 598 618 619 630 645 646 647 651 672 681 684 705 711 721 722 746 764 774 783 795 823 831 835 839 843 853 859 865 870 881 888 933 942 943 948 954 968 975 999 1000 1017 1032 1048 1074 1080 1090 1099 1106 1116 1131 1132 1155 1156 1167 1171 1174 1175 1187 1191 1215 1233 1239 12...",
      "output_data": "499987\r\n",
      "correct_answer": "499987\r\n",
      "comment": "ok answer is '499987'\r\n",
      "Time": ": 31 ms, ",
      "memory": ": 396 KB"
    },
    {
      "test_no": "4\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "100000\r\n16 40 48 51 54 59 65 67 71 73 77 107 117 126 159 163 189 195 215 273 277 304 306 309 319 322 326 334 336 339 345 354 355 357 363 385 387 401 416 417 418 430 432 444 451 466 477 491 512 520 521 545 549 585 588 593 602 607 608 623 630 636 659 687 691 696 714 719 743 758 765 789 800 809 810 818 829 849 861 864 868 889 892 902 904 915 917 919 930 940 951 952 957 958 1001 1002 1008 1039 1055 1062 1073 1085 1095 1103 1116 1137 1139 1158 1181 1195 1199 1205 1213 1216 1219 1222 1239 1240 1242 1275 1301 130...",
      "output_data": "499995\r\n",
      "correct_answer": "499995\r\n",
      "comment": "ok answer is '499995'\r\n",
      "Time": ": 31 ms, ",
      "memory": ": 384 KB"
    },
    {
      "test_no": "5\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "1\r\n20\r\n",
      "output_data": "19\r\n",
      "correct_answer": "19\r\n",
      "comment": "ok answer is '19'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 4 KB"
    },
    {
      "test_no": "6\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "6\r\n2 3 500000 999997 999998 999999\r\n",
      "output_data": "499999\r\n",
      "correct_answer": "499999\r\n",
      "comment": "ok answer is '499999'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "7\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "1\r\n999999\r\n",
      "output_data": "1\r\n",
      "correct_answer": "1\r\n",
      "comment": "ok answer is '1'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "8\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "1\r\n510000\r\n",
      "output_data": "490000\r\n",
      "correct_answer": "490000\r\n",
      "comment": "ok answer is '490000'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "9\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "3\r\n2 5 27\r\n",
      "output_data": "26\r\n",
      "correct_answer": "26\r\n",
      "comment": "ok answer is '26'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "10\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "2\r\n600000 800000\r\n",
      "output_data": "400000\r\n",
      "correct_answer": "400000\r\n",
      "comment": "ok answer is '400000'\r\n",
      "Time": ": 0 ms, ",
      "memory": ": 0 KB"
    },
    ..
    ..
    {
      "test_no": "42\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "86\r\n1360 2132 2241 5214 5612 5978 7906 8770 9627 12841 14224 24279 24441 25236 26281 26331 28788 28804 29684 30908 30919 31339 32070 32268 33794 34336 35340 36580 43679 46247 47508 47752 49630 50241 51241 51456 51584 55447 56388 56467 58315 58567 58686 60170 60360 62561 62645 63061 64156 64409 64535 65251 65567 66371 66681 68528 68578 68773 72026 72270 72359 72642 73484 75306 75561 75618 76214 76931 77464 77480 79924 80561 80800 81515 82199 82203 84605 85365 86092 88193 89466 93109 95272 96041 96114 97435\r...",
      "output_data": "97434\r\n",
      "correct_answer": "97434\r\n",
      "comment": "ok answer is '97434'\r\n",
      "Time": ": 0 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "43\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "1\r\n505050\r\n",
      "output_data": "494950\r\n",
      "correct_answer": "494950\r\n",
      "comment": "ok answer is '494950'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "44\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "1\r\n753572\r\n",
      "output_data": "246428\r\n",
      "correct_answer": "246428\r\n",
      "comment": "ok answer is '246428'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 0 KB"
    },
    {
      "test_no": "45\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "2\r\n576696 760487\r\n",
      "output_data": "423304\r\n",
      "correct_answer": "423304\r\n",
      "comment": "ok answer is '423304'\r\n",
      "Time": ": 15 ms, ",
      "memory": ": 4 KB"
    },

```
with the following parameters
- `` submission_stats `` -  Contains all the details of the submission
- `` submissionid `` - ID of the submission
- `` problemname `` - Name of the problem
- `` language `` - Language of the program (eg. C++ 14, Python3 etc)
- `` verdict `` - Result of the submission - (Accepted, Wrong Answer, Time Limit Exceeded, Runtime error)
- `` time_taken `` - Total Runtime of the program
- `` memory `` - Total memory consumed by the program
- `` submitted_time ``- Time (UTC) when the program was submitted
- `` judged_time `` - Time(UTC) when the program was evaluated
- `` program `` - Program
- `` testcases_data `` - All the testcases
- `` username `` - Handle of the user 

``submission_stats`` has the following structure
```json
[{'date_time': '2018-09-05 17:07:27',
  'submission_id': '42495359',
  'problem_name': 'B - Run For Your Prize',
  'submission_link': 'http://codeforces.com/contest/938/submission/42495359',
  'participant_id': '19532151',
  'contest_url': 'http://codeforces.com/contest/938/problem/B',
  'submission_lang': 'GNU C++14',
  'time_consumed': '46\xa0ms',
  'memory_consumed': '400\xa0KB',
  'submission_verdict': 'OK',
  'submission_verdict_text': 'Accepted',
  'problem_id': ['938', 'B']}]
```

``testcases_data`` has the following structure
```json
    {
      "test_no": "42\r\n            ",
      "testcase_verdict": "Verdict: OK",
      "input_data": "86\r\n1360 2132 2241 5214 5612 5978 7906 8770 9627 12841 14224 24279 24441 25236 26281 26331 28788 28804 29684 30908 30919 31339 32070 32268 33794 34336 35340 36580 43679 46247 47508 47752 49630 50241 51241 51456 51584 55447 56388 56467 58315 58567 58686 60170 60360 62561 62645 63061 64156 64409 64535 65251 65567 66371 66681 68528 68578 68773 72026 72270 72359 72642 73484 75306 75561 75618 76214 76931 77464 77480 79924 80561 80800 81515 82199 82203 84605 85365 86092 88193 89466 93109 95272 96041 96114 97435\r...",
      "output_data": "97434\r\n",
      "correct_answer": "97434\r\n",
      "comment": "ok answer is '97434'\r\n",
      "Time": ": 0 ms, ",
      "memory": ": 0 KB"
    }
```



# Technical Details

## Items
### Submisisons Meta-Data
```python
date_time = scrapy.Field(output_processor = TakeFirst())
submission_id = scrapy.Field(output_processor = TakeFirst())
problem_name = scrapy.Field(output_processor    akeFirst())
submission_link = scrapy.Field(output_processor  =  TakeFirst())
participant_id = scrapy.Field(output_processor = TakeFirst())
contest_url = scrapy.Field(output_processor = TakeFirst())
submission_lang = scrapy.Field(output_processor  =  TakeFirst())
time_consumed = scrapy.Field(output_processor = TakeFirst())
memory_consumed = scrapy.Field(output_processor = TakeFirst())
submission_verdict = scrapy.Field(output_processor = TakeFirst())
submission_verdict_text = scrapy.Field(output_processor = TakeFirst())
problem_id = scrapy.Field()
```

### Submission Data for every ``Accepted`` submission
```python
    submission_stats = scrapy.Field()
    submissionid = scrapy.Field(
        output_processor=TakeFirst()
    )
    problemname = scrapy.Field(
        output_processor=TakeFirst()
    )
    language = scrapy.Field(
        output_processor=TakeFirst()
    )
    verdict = scrapy.Field(
        output_processor=TakeFirst()
    )
    time_taken = scrapy.Field(
        output_processsor=TakeFirst()
    )
    memory = scrapy.Field(
        output_processor=TakeFirst()
    )
    submitted_time = scrapy.Field(
        output_processor=TakeFirst()
    )
    judged_time = scrapy.Field(
        output_processor=TakeFirst()
    )
    username = scrapy.Field(
        output_processor = TakeFirst()
    )
    program = scrapy.Field()
    testcases_data = scrapy.Field()

```

## Pipelines
```python
ITEM_PIPELINES  =  {
'codeforces.pipelines.CodeforcesPipeline': 300,
}
```
- Add headers to the C++ files
```cpp
/* 
	1 A - Little C Loves 3 I 
	author : abhishekvr12 | submitted at : 2018-09-21 17:43:57
	time taken : 31 ms | memory consumed : 12 KB
*/
#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int x, a, b, c;
    cin >> x;
    if (x % 3 == 0)
        a = 1, b = 1, c = x - 2;
    if (x % 3 == 1)
        a = 1, b = 1, c = x - 2;
    if (x % 3 == 2)
        a = 1, b = 2, c = x - 3;
    cout << a << " " << b << " " << c;
}
```

- Save the program in user-defined path
## Scope
This spider can be deployed on EC2 which can run at regular user-defined interval (using ``cronjob``) and if a new solution has been submitted, it can be automatically commited to the user's github directory.



