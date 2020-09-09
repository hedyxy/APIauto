from conf.setting import CASE_PATH,CASE_EG,PY_PATH
import os
class GetCase(object):
	def creat_py(self):
		base_case_str = open(CASE_EG,encoding='utf-8').read()
		for f in os.listdir(CASE_PATH):
			if f.endswith('.yml') or f.endswith('.yaml'):
				abs_path = os.path.join(CASE_PATH,f)
				class_name = 'Test'+ f.replace('.yml','').replace('.yaml','').capitalize()
				new_case_str = base_case_str%(class_name,abs_path)
				py_file_path = os.path.join(PY_PATH,class_name)
				open('%s.py'%py_file_path,'w',encoding='utf-8').write(new_case_str)





