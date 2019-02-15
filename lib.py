from pymongo import MongoClient
import logging
import time
import random


test_client = MongoClient(
    host='humor1.vip.gatech.edu',
    port=3306,
    username='comedian_monologues',
    password='BlENteRsEWROmbERaInG',
    authSource='hgp_comedian_monologues',
    authMechanism='SCRAM-SHA-1'
)


def insert_example():
    logger = logging.getLogger(__name__)

    youtube_table = \
        test_client['hgp_comedian_monologues']['youtube_monologues']

    logger.info('Content before example insert')
    for record in youtube_table.find():
        print(record)

    youtube_table.insert_one({
        'data': f'insert example {str(random.randint(1, 1000))}',
        'timestamp': int(round(time.time() * 1000))
    })

    logger.info('Content after example insert')
    for record in youtube_table.find():
        print(record)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO
    )
    insert_example()