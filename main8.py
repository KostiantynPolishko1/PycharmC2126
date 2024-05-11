import logging

# logging.debug('DEBUG')
# logging.info('INFO')
# logging.warning('WARNING')
# logging.error('ERROR')
# logging.critical('CRITICAL')

logging.basicConfig(level=logging.DEBUG,
                    filename='logs.txt',
                    filemode='w',
                    format='LOG DATA: %(asctime)s | %(levelname)s | %(message)s')

a = '5'
b = 2

result: int
flag = False

try:
    result = a + b
except BaseException as ex:
    flag = True
    # print(ex)
    logging.exception(ex)
finally:
    if flag:
        print(f'{a} || {b} are not digit')
    else:
        print(f'{a} + {b} = {result}')

