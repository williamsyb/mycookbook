from abc import ABCMeta, abstractmethod


class Context(metaclass=ABCMeta):
    def __init__(self):
        self.__states = []
        self.__cur_state = None
        self.__state_info = 0

    def add_state(self, state):
        """在初始化子类时，可以一把把状态都先添加好"""
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        """函数为了在设置state_info时自动切换状态"""
        if state is None:
            return False
        if self.__cur_state is None:
            print('初始化为'.format(state.get_name()))
        else:
            print('由 {} 转为 {}'.format(self.__cur_state.get_name(),
                                      state.get_name()))

        self.__cur_state = state
        self.add_state(state)
        return True

    def _set_state_info(self, state_info):
        """关键的私有方法，在设置状态信息（基类中的私有变量）的同时，切换了状态"""
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def get_state_info(self):
        """为了让子类访问藏在Context基类中的私有变量"""
        return self.__state_info

    def get_state(self):
        """为了让子类获取当前的状态state，用来执行behavior"""
        return self.__cur_state


class State:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, state_info):
        return False

    @abstractmethod
    def behavior(self, context):
        pass
