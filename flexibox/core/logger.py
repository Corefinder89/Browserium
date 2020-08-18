# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Logger is to have all the generic functionality for logging
#          Can be used to generate logs for all the required functions carried out in the project
import logging
from time import sleep


class Logger(object):
    def log_info(self, informationMessage):
        logging.info(informationMessage)
        sleep(1)

    def log_error(self, errorMessage):
        logging.error(errorMessage)

    def log_debug(self, debugMessage):
        logging.debug(debugMessage)

    def log_warning(self, warningMessage):
        logging.warning(warningMessage)

    def log_critical(self, criticalMessage):
        logging.critical(criticalMessage)
