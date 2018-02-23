import logging
import argparse

from kafka_rest.client import Consumer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s')


parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL of the Kafka REST Proxy')
parser.add_argument('topic', nargs='+', help='Topic')

def main():
    args = parser.parse_args()
    logger.info(args)

    consumer = Consumer(args.url, 'bftestgroup')
    consumer.subscribe(args.topic)
    subs = consumer.get_subscriptions()
    logger.debug(subs)
    #resp = consumer.poll(1000)
    #logger.debug(resp)
    offsets = consumer.get_offsets()
    #logger.debug(offsets)
    consumer.delete()



if __name__ == '__main__':
    main()
