from op_stats.logger import LOGGER
import psutil

class Stats():

    def __init__(self):
        self.cpu_percent = 0

    @classmethod
    def get_cpu_percent(cls):
        LOGGER.info('get cpu use as a percentage')
        cpu_percent = psutil.cpu_percent()
        return cpu_percent
