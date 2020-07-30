# -*- coding UTF-8 -*-
# @project : python03
# @Time    : 2020/7/8 10:39
# @Author  : Yibin Sun
# @Email   : sunyibin@orientsec.com.cn
# @File    : consumer02.py
# @Software: PyCharm
from kombu import Queue, Exchange, Connection, Consumer


def cb_1(body, message):
    print(body)
    print("my_consume_1")
    message.ack()


def cb_2(body, message):
    print(message)
    print("my_consume_2")


def cb_3(body, message):
    print("my_consume_3")


with Connection('amqp://alpha:y2iaciej@10.46.0.39:5672/rapid_alpha_dev') as connection:
    with connection.channel() as channel:
        kombu_queue = Queue(name='kombu_queue',
                            exchange=Exchange('kombu_queue', type='direct'),
                            routing_key='kombu_queue',
                            durable=False,
                            channel=channel,
                            )
        kombu_queue_1 = Queue(name='kombu_queue_1',
                              exchange=Exchange('kombu_queue_1', type='direct'),
                              routing_key='kombu_queue_1',
                              durable=False,
                              channel=channel,
                              max_priority=10,  # 优先级
                              )
        # 消费
        consumer = Consumer(channel,
                            queues=[kombu_queue, kombu_queue_1],  # 多个队列
                            accept=['json', 'pickle', 'msgpack', 'yaml'],  # 多种类型
                            callbacks=[cb_1, cb_2, cb_3]  # 多个回调
                            )
        consumer.consume()

        while True:
            import time

            connection.drain_events()
