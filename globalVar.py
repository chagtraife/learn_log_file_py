import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)



def test_global():
	# Logs
	logger.debug('jjjjjA debug message')
	logger.info('llllllllAn info message')
	logger.warning('sssssssSomething is not right.')
	logger.error('A ssnksjcMajor error has happened.')
	logger.critical('   dgdggdFatal error. Cannot continue')