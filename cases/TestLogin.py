import ddt
import unittest,requests
@ddt.ddt
class TestLogin(unittest.TestCase):
	@ddt.file_data(r'E:\login.yml')
	@ddt.unpack
	def test_run(self,**kwargs):
		method = kwargs.get('method')
		url = kwargs.get('url')
		data = kwargs.get('data',{})
		header = kwargs.get('header',{})
		is_json = kwargs.get('is_json',0)
		cookie = kwargs.get('cookie',{})
		check = kwargs.get('check')
		if method=='post':
			if is_json:
				r = requests.post(url,json=data,headers=header,cookies=cookie)
			else:
				r = requests.post(url,data=data, headers=header, cookies=cookie)
		else:
			r = requests.get(url,params=data,headers=header, cookies=cookie)
		for c in check:
			self.assertIn(c,r.text)