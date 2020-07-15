import asyncio
import aioamqp


async def callback(channel, body, envelope, properties):
    print(" [x] Received %r" % body)


async def receive():
    transport, protocol = await aioamqp.connect(host='192.168.220.128', port=5672,login_method='PLAIN')
    channel = await protocol.channel()

    await channel.queue_declare(queue_name='hello')

    await channel.basic_consume(callback, queue_name='hello')


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(receive())
event_loop.run_forever()
