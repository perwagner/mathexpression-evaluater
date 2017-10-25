# Simple Math Expression evaluated
Evaluates simple math expressions which contains integers and operators
(+, -, *, /). The evaluator deals with rational numbers by implementing
a special Nom class which contains a numerator and denominator. The 
math expression should be input as a string and output will likewise be
a string.

## Installation
There is not installer provided. You must import the function
from the file /evaluator/eval.py. The function's name is eval.

The function was developed and tested on Python 3.6, but should work for any
Python 3 version.

## Usage
(assuming your file is in the parent dir to the root directory)

```commandline
>> python3
Python 3.6.1 (default, May 27 2017, 16:10:34) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from evaluator.eval import eval
>>> eval('5+3')
'8'
```

## Notes
In order to keep the code base as small and simple as possible, you should be 
aware of the following:

* The input expression should be as 'clean' as possible (no special characters).
The function does only do a minimum of input validation
* When the function outputs (returns) fractions ('6/8'), these are not
simplified, eg. 6/8 == 3/4, but '6/8' would still be the output by the function.
* Error reporting is minimal and no logging has been implemented.
* The input expression must be correcly formed, otherwise the correctness of 
the output is not quarenteed. Ex: eval('1+2(1+2)') would not evaluate to 
a meaningful result (correct would be "1+2*(1+2)")



## Testing
Install the dependencies from requirements.txt into your environment (use 
a virtual environment).

```commandline
>> virtualenv venv -p python3
>> source venv/bin/activate
>> pip install -r requirements.txt
``` 
Run the tests with py.test
```commandline
>> pytest evaluator/
```
More verbose output can be achieved with
```commandline
>> pytest evaluator -v
```

Get coverage and coverage report:
```commandline
>> py.test --cov=evaluator evaluator
>> py.test --cov=evaluator evaluator --cov-report html
```
Coverage report will be put in the directory: /coverage_html_report

```commandline
----------- coverage: platform linux, python 3.6.1-final-0 -----------
Name                     Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------
evaluator/Nom.py            30      3      4      0    91%
evaluator/__init__.py        0      0      0      0   100%
evaluator/eval.py           87      2     24      2    96%
evaluator/test_Nom.py       15      0      0      0   100%
evaluator/test_eval.py     121      0      0      0   100%
----------------------------------------------------------
TOTAL                      253      5     28      2    98%
```

## TODO
* Make a package
* Better input validation (maybe some 'auto correction')
* Support for variables (x, y, z)
