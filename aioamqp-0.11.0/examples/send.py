"""
    Hello world `send.py` example implementation using aioamqp.
    See the documentation for more informations.

"""

import asyncio
import aioamqp


@asyncio.coroutine
def send():
    transport, protocol = yield from aioamqp.connect()
    channel = yield from protocol.channel()

    yield from channel.queue_declare(queue_name='a')

    yield from channel.basic_publish(
        payload="C:\sqlite\db\chinook.db xml",
        exchange_name='',
        routing_key='a'
    )

    print(" [x] Sent 'Hello World!'")
    yield from protocol.close()
    transport.close()



asyncio.get_event_loop().run_until_complete(send())
