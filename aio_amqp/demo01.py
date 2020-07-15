import asyncio
import aioamqp


async def connect():
    try:
        transport, protocol = await aioamqp.connect()  # use default parameters
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        return

    print("connected !")
    await asyncio.sleep(1)

    print("close connection")
    await protocol.close()
    transport.close()


# asyncio.get_event_loop().run_until_complete(connect())


async def callback(channel, body, envelope, properties):
    print(body)

# channel = await protocol.channel()
# await channel.basic_consume(callback, queue_name="my_queue")
