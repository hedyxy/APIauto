import unittest
import requests
from conf.setting import BASE_URL
from common.mysql import db
from common.redis import my_redis

class TestMore(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.url = BASE_URL
	@classmethod
	def tearDownClass(cls):
		db.execute('delete from app_myuser where username="xxx"; ')

	def Reg(self):
		url = self.url+'/api/user/reg'
		data =  {
			'username':'xxx',
			'pwd':'xx',
			'cpwd':'xx',
		}
		res = requests.post(url,data=data).text
		self.assertIn('注册成功',res)

	def Login(self):
		pass

	def testMore(self):
		userid,sign = self.Login()
		url = self.url+''
		data = {'userid':userid,'sign':sign}
		res = requests.get(url,params=data).text
		print('中奖信息：。。',res)
		self.assertTrue('product_name' in res)
		self.assertTrue('imgUrl' in res)
if __name__ == '__main__':
	unittest.main()