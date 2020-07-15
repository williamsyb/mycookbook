import unittest
import time
from observer import Observer, Observable


class Account(Observable):
    def __init__(self):
        super().__init__()
        self.name = 'orientsec'
        self.__latest_ip = {}
        self.__latest_region = {}

    def login(self, name, ip, time_):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            self.notify_observers({'name': name, 'ip': ip, 'region': region, 'time': time_})
        self.__latest_region[name] = region
        self.__latest_ip[name] = ip

    def __get_region(self, ip):
        ip_region = {
            '101.47.18.9': '上海市',
            '67.218.147.69': '美国洛杉矶'
        }
        region = ip_region.get(ip)
        return '' if region is None else region

    def __is_long_distance(self, name, region):
        latest_region = self.__latest_region.get(name)
        return latest_region is not None and latest_region != region


class SmsSender(Observer):
    def update(self, observable, obj):
        print(f'[短信发送] {obj["name"]} 您好！检测到您的账户可能登陆异常。最近一次登陆信息：\n'
              f'登陆地区：{obj["region"]} 登陆IP:{obj["ip"]} '
              f'登陆时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(obj["time"]))}')


class MailSender(Observer):
    def update(self, observable, obj):
        print(f'[邮件发送] {obj["name"]} 您好！检测到您的账户可能登陆异常。最近一次登陆信息：\n'
              f'登陆地区：{obj["region"]} 登陆IP:{obj["ip"]} '
              f'登陆时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(obj["time"]))}')


class TestAccountMonitor(unittest.TestCase):
    def test_account(self):
        account = Account()
        account.add_observer(SmsSender())
        account.add_observer(MailSender())
        account.login('William', '101.47.18.9', time.time())
        account.login('William', '67.218.147.69', time.time())


if __name__ == '__main__':
    unittest.main()
