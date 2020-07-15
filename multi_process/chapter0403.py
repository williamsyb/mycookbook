import asyncio
import time
from random import randint


@asyncio.coroutine
def start_state():
    print('start state called \n')
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from state2(input_value)
    else:
        result = yield from state1(input_value)
    print('Resume of the Transition: \nStart state calling ' + result)


@asyncio.coroutine
def state1(value):
    output = str(('state 1 with transition value = {}\n'.format(value)))
    input_value = randint(0, 1)
    time.sleep(1)
    print('...state1 Evaluating...')
    if input_value == 0:
        result = yield from state3(input_value)
    else:
        result = yield from state2(input_value)
    result = 'state 1 calling ' + result
    return output + str(result)


@asyncio.coroutine
def state2(value):
    output = str(('state 2 with transition value = {}\n'.format(value)))
    input_value = randint(0, 1)
    time.sleep(1)
    print('...state2 Evaluating...')
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from state3(input_value)
    result = 'state 2 calling ' + result
    return output + str(result)


@asyncio.coroutine
def state3(value):
    output = str(('state 3 with transition value = {}\n'.format(value)))
    input_value = randint(0, 1)
    time.sleep(1)
    print('...state3 Evaluating...')
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from end_state(input_value)
    result = 'state 3 calling ' + result
    return output + str(result)


@asyncio.coroutine
def end_state(value):
    output = str(('end state with transition value={}\n'.format(value)))
    print('stop computation....')
    return output


if __name__ == '__main__':
    print('finish state machine simulation with asyncio coroutine')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
