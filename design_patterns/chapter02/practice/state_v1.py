import unittest

from practice.state import Context, State


class Water(Context):
    def __init__(self):
        super().__init__()
        self.add_state(SolidState('固体'))
        self.add_state(LiquideState('液体'))
        self.add_state(GaseousState('气体'))
        self.set_temperature(24)

    def get_temperature(self):
        return self.get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def rise_temperature(self, step):
        self.set_temperature(self.get_temperature() + step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature() - step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        print('i am behavior {}'.format(str(context.get_state_info())))


class LiquideState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return 0 < state_info < 100

    def behavior(self, context):
        print('i am behavior {}'.format(str(context.get_state_info())))


class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info > 100

    def behavior(self, context):
        print('i am behavior {}'.format(str(context.get_state_info())))


class TestWater(unittest.TestCase):
    def test_water(self):
        water = Water()
        water.behavior()
        water.set_temperature(-4)
        water.rise_temperature(18)
        water.behavior()
        water.rise_temperature(110)
        water.behavior()


if __name__ == '__main__':
    unittest.main()
