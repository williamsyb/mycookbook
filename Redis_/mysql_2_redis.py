import json
import os
import sys
import MySQLdb
import redis
import hashlib

reload(sys)
sys.setdefaultencoding('utf-8')


class mysql2redis():
    def __init__(self, mysqlip, mysqluser, mysqlpwd, redisip, redisauth):
        self.mysqlip = mysqlip
        self.mysqluser = mysqluser
        self.mysqlpwd = mysqlpwd
        self.redisip = redisip
        self.redisauth = redisauth
        self.domain=None

    def domain2md5(self, domains):
        for domain in domains:
            m = hashlib.md5()
            m.update(domain)
            self.domain = domain
            self.read4mysql(m.hexdigest())

    def read4mysql(self, site_uuid):
        print("%s processing..." % self.domain)
        db = MySQLdb.connect(self.mysqlip, self.mysqluser, self.mysqlpwd, "lxserver")
        cursor = db.cursor()
        sql = """SELECT a.reply_type,a.module,b.parent_key,a.user_id,a.type,a.site_uuid,b.connect_key,a.`mode`,a.has_get_file,
		a.city,a.ip,a.create_time,a.is_connect,a.area,a.root_path,a.`name`,a.connect_url,a.province,a.site_id,a.industry_id,a.harm_level,b.rc4_key 
		FROM lx_site a,lx_user b WHERE a.site_uuid = '%s' AND a.user_id = b.user_id""" % site_uuid
        cursor.execute(sql)
        data = cursor.fetchall()
        self.processData(data)
        db.close()

    def processData(self, data):
        for row in data:
            siteid = row[18]
            v = "{'replyType':%s,'module':'%s','parentKey':'%s','userid':%s,'type':'%s','siteUuid':'%s','connectkey':'%s','mode':%s,'hasgetfile':%s,'city':'%s','ip':'%s','createtime':%s,'isconnect':%s,'area':'%s','rootpath':'%s','name':'%s','connecturl':'%s','province':'%s','siteid':'%s','industryid':%s,'harmlevel':%s,'rc4key':'%s'}" % (
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                row[12],
                row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21])
            value = json.dumps(v, ensure_ascii=False)
            is_connect = row[12]
            self.write2redis(siteid, is_connect, value)
        print("%s OK" % self.domain)

    def write2redis(self, siteid, score, value):
        # print(siteid)
        # print(score)
        # print(value)
        pool = redis.ConnectionPool(host=self.redisip, port=6379, password=self.redisauth)
        r = redis.Redis(connection_pool=pool)
        dic = {siteid: value}
    # r.hmset("lxsitehashin", dic)
    # r.zadd("lxsitesetin", score, siteid)


if __name__ == '__main__':
    domains = ['http://aa.com', 'http://bb.com', 'http://cc.com', 'http://dd.com', 'http://ee.com', 'http://ff.com']
    mysqlip = "mysql.*.iaiot.com"
    mysqluser = "root"
    mysqlpwd = "rootpwd"
    redisip = "127.0.0.1"
    redisauth = "redispwd"
    mysql2redis(mysqlip, mysqluser, mysqlpwd, redisip, redisauth).domain2md5(domains)

os.system("pause")
