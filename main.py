import logging
import globalVar

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.INFO)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
a = "2222"
# a = 6
# logger.debug('A debug message')
# logger.info('An info message')
logger.warning('b: {b}'.format(b = a))
# logger.error('A Major error has happened.')
# logger.critical('Fatal error. Cannot continue')
# globalVar.test_global()