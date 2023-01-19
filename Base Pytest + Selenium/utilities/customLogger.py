import logging

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            filename='..\\Logs\\automation.log',
            filemode='w',
            level=logging.INFO,
            format='%(asctime)s: %(levelname)s: %(message)s:',
            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        return logger
