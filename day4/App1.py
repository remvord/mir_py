import logging

log = logging.getLogger('App1.simple')
formatter = logging.Formatter(f'%(asctime)s {logging.BASIC_FORMAT}')

fh = logging.FileHandler(r'/home/remvord/shara/App1.log')
fh.setLevel(logging.CRITICAL)
fh.setFormatter(formatter)
log.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
log.addHandler(ch)

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
