import sys,os
BASE_PATH = os.path.dirname(os.path.dirname(
	os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)
from common.tools import GetCase
from conf.setting import PY_PATH,REPORT_PATH
import unittest,BeautifulReport
def run():
	g = GetCase()
	g.creat_py() #生成测试文件
	suite = unittest.TestSuite()
	all_cases = unittest.defaultTestLoader.discover(PY_PATH,'Test*.py')
	[suite.addTests(case) for case in all_cases]
	report_obj = BeautifulReport.BeautifulReport(suite)
	report_obj.report(filename='apidemo',log_path=REPORT_PATH,
					  description='apidemo测试报告')
run()