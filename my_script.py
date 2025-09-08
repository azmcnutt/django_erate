import sys
import logging
from pprint import pprint

from core.usac2 import Usac

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(module)s : %(lineno)d | %(levelname)s: %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

def main():
    logger.info('******  Starting my script  ******')
    usac = Usac()
    usac.entity.set_ben('16051395')
    ben = usac.entity.all
    ben['annexes'] = usac.annex.get_annexes(ben['entity_number'])
    pprint(ben)
    # annex = usac.annex.get_annexes('16051395')
    # pprint(annex)

    logger.info('******   Ending my script   ******')
if __name__ == "__main__":
    main()