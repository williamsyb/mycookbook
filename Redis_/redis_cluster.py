# https://www.cnblogs.com/yscl/p/12008471.html

from rediscluster import RedisCluster

# Requires at least one node for cluster discovery. Multiple nodes is recommended.

startup_nodes = [
    # 填写虚拟机的地址
    {"host": "192.168.12.78", "port": "7000"},
    {"host": "192.168.12.78", "port": "7001"},
    {"host": "192.168.12.78", "port": "7002"},
    {"host": "192.168.12.78", "port": "7003"},
    {"host": "192.168.12.78", "port": "7004"},
    {"host": "192.168.12.78", "port": "7005"},
]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

rc.set('test2', 'test2...')
print(rc.get('test1'))
print(rc.get('test2'))
