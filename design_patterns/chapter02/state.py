from abc import abstractmethod, ABCMeta


class Context(metaclass=ABCMeta):
    def __init__(self):
        self.__states = []
        self.__cur_state = None
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print(f'初始化为{state.get_name()}')
        else:
            print(f'由 {self.__cur_state.get_name()} 变为 {state.get_name()}')

        self.__cur_state = state
        self.add_state(state)
        return True

    def get_state(self):
        return self.__cur_state

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def _get_state_info(self):
        return self.__state_info


class State(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, state_info):
        return False

    @abstractmethod
    def behavior(self, context):
        pass
