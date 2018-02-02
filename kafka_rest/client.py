from urllib import request
from urllib import parse
import json
import logging

logger = logging.getLogger(__name__)


class Consumer:

    def __init__(self, url, group_name, format='avro'):
        logger.info('Setting internal veriables')
        self.url = url
        self.group_name = group_name
        self.format = format
        self.accept_header = 'application/vnd.kafka.{}.v2+json'.format(format)
        self.content_type_header = 'application/vnd.kafka.v2+json'

        # register the consumer
        logger.info('Registering consumer')
        data = {'format': self.format,
                'auto.offset.reset': 'earliest'}
        data = json.dumps(data)
        data = data.encode()
        headers = {'Content-Type': self.content_type_header}
        req = request.Request(self.url + '/consumers/' + self.group_name, data, headers)
        with request.urlopen(req) as f:
            response = f.read()
            response = response.decode()
            response = json.loads(response)
        self.instance_id = response['instance_id']
        self.base_uri = response['base_uri']
        logger.debug('Using base URI: {} and instance id: {}'.format(self.base_uri, self.instance_id))

    def subscribe(self, topics):
        logger.info('Subscribing to topics')
        data = {'topics': topics}
        data = json.dumps(data)
        data = data.encode()
        headers = {'Content-Type': self.content_type_header}
        req = request.Request(self.base_uri + '/subscription/', data, headers, method='POST')
        with request.urlopen(req) as f:
            response = f.read()

    def get_subscriptions(self):
        headers = {'Accept': self.content_type_header}
        req = request.Request(self.base_uri + '/subscription', headers=headers)
        with request.urlopen(req) as f:
            response = f.read()
            response = response.decode()
            response = json.loads(response)
            return response['topics']

    def poll(self, timeout=None):
        logger.info('Polling')
        uri = self.base_uri + '/records'
        if timeout:
            query = parse.urlencode({'timeout':  str(timeout)})
            uri += "?" + query
        logger.info(uri)

        headers = {'Accept': self.accept_header}
        req = request.Request(uri, headers=headers)
        with request.urlopen(req) as f:
            response = f.read()
            response = response.decode()
            response = json.loads(response)
            return response
