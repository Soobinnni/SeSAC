import logging
import argparse

logger = logging.getLogger('my-logger')

logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# logging.basicConfig(level=logging.CRITICAL)

# 로그 포맷팅
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# default handler없애기
logger.propagate = False

# 로그 옵션 동적 처리
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='로그레벨설정')
args = parser.parse_args()

# 로그 레벨 적용
log_level_args = args.log_level.upper()
logger.setLevel(log_level_args)

# 로그를 출력하는 방법
logger.debug('헬로우5') # 5
logger.info('헬로우4') # 4
logger.warning('헬로우3') # 3 
logger.error('헬로우2') # 2
logger.critical('헬로우1') # 1 