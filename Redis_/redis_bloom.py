from redisbloom.client import Client

# 因为我使用的是虚拟机中docker的redis, 填写虚拟机的ip地址和暴露的端口
rb = Client(host='node01', port=6379)
rb.bfAdd('urls', 'baidu')
rb.bfAdd('urls', 'google')
print(rb.bfExists('urls', 'baidu'))  # out: 1
print(rb.bfExists('urls', 'tencent2'))  # out: 0

rb.bfMAdd('urls', 'a', 'b')
print(rb.bfMExists('urls', 'google', 'baidu', 'tencent'))  # out: [1, 1, 0]