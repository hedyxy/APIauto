import os
BASE_PATH = os.path.dirname(
	os.path.dirname(
	os.path.abspath(__file__)
))
CASE_PATH = os.path.join(BASE_PATH,' ')
LOG_PATH = os.path.join(BASE_PATH,'logs')
REPORT_PATH = os.path.join(BASE_PATH,'report')
CASE_EG = os.path.join(BASE_PATH,'conf','base_case.eg')
PY_PATH = os.path.join(BASE_PATH,'cases')


BASE_URL ='http://192.10.0.1:8080'