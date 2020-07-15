import aioamqp
import asyncio


async def connect():
    try:
        transport, protocol = await aioamqp.connect(host='192.168.220.128', login_method='PLAIN')  # use default parameters
        # transport, protocol = await aioamqp.connect()
    except aioamqp.AmqpClosedConnection:
        print("closed connections")
        return
    print("connected !")
    await asyncio.sleep(1)
    print("close connection")
    await protocol.close()
    transport.close()


asyncio.get_event_loop().run_until_complete(connect())
