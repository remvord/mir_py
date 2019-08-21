import logging, dataclasses


@dataclasses.dataclass()
class Mylogger():
    name: str
    file: str = fr'{name}.log'
    level: str = logging.INFO
    log:

    def init(self):
        __log = logging.getLogger(self.name)
        formatter = logging.Formatter(f'%(asctime)s {logging.BASIC_FORMAT}')

        fh = logging.FileHandler(r'/home/remvord/shara/App1.log')
        fh.setLevel(logging.CRITICAL)
        fh.setFormatter(formatter)
        __log.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        __log.addHandler(ch)

    def message(self, text):
        self.__log.info(text)



log.setLevel(logging.INFO)
log.critical('criticalMessage')
log.error('errorMessage')

try:
    raise Exception
except Exception as e:
    log.exception('exceptionMessage', exc_info=e)

log.warning('warningMessage')
log.info('infoMessage')
log.debug('debugMessage')
print(logging.BASIC_FORMAT)
