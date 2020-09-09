import logging
from logging import handlers
from conf.setting import LOG_PATH

class Logger(object):
	level_relations = {
		'debug': logging.DEBUG,
		'info': logging.INFO,
		'warning': logging.WARNING,
		'error': logging.ERROR,
		'crit': logging.CRITICAL
	}
	def __init__(self,filename,level='debug',
				 when='D',
				 back_count=3,
				 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
		self.logger = logging.getLogger(filename)

		format_str = logging.Formatter(fmt)
		self.logger.setLevel(self.level_relations.get(level))
		sh = logging.StreamHandler()
		sh.setFormatter(format_str)
		th = handlers.TimedRotatingFileHandler(filename=filename,when=when,
											   backupCount=back_count,encoding='utf-8')
		th.setFormatter(format_str)
		self.logger.addHandler(sh)
		self.logger.addHandler(th)


log = Logger(LOG_PATH).logger





