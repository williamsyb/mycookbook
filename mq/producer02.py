# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/7/8 10:35
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : producer02.py
# @Software: PyCharm

import time
from kombu.entity import Exchange, Queue
from kombu.messaging import Producer
from kombu.connection import Connection

with Connection('amqp://alpha:y2iaciej@10.46.0.39:5672/rapid_alpha_dev') as connection:
    with connection.channel() as channel:
        for i in range(1, 10):
            science_news = Queue(name='kombu_queue',
                                 exchange=Exchange('kombu_queue', type='direct'),
                                 routing_key='kombu_queue',
                                 channel=channel,
                                 durable=False,
                                 )
            science_news.declare()
            producer = Producer(channel, serializer='json', routing_key='kombu_queue')
            producer.publish({'name': 'kombu_queue', 'size': i})

            science_news = Queue(name='kombu_queue_1',
                                 exchange=Exchange('kombu_queue_1', type='direct'),
                                 routing_key='kombu_queue_1',
                                 channel=channel,
                                 max_priority=10,  # 优先级
                                 durable=False,
                                 )
            science_news.declare()
            producer = Producer(channel, serializer='json', routing_key='kombu_queue_1')
            producer.publish({'name': 'kombu_queue_1', 'size': i}, priority=i)