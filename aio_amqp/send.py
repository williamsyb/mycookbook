import asyncio
import aioamqp


async def send():
    transport, protocol = await aioamqp.connect(host='192.168.220.128', port=5672, login='sunyibin',
                                                password='y2iaciej',
                                                virtualhost='/',login_method='PLAIN')
    channel = await protocol.channel()

    await channel.queue_declare(queue_name='hello')

    await channel.basic_publish(
        payload='Hello World!',
        exchange_name='',
        routing_key='hello'
    )

    print(" [x] Sent 'Hello World!'")
    await protocol.close()
    transport.close()


asyncio.get_event_loop().run_until_complete(send())
