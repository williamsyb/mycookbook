使用Redis实现分布式锁
更新时间： 2020/07/13 GMT+08:00查看PDF分享
本节基于华为云分布式缓存服务实践所编写，用于指导您在以下场景使用DCS实现分布式锁。

场景介绍
很多互联网场景（如商品秒杀，论坛回帖盖楼等），需要用加锁的方式，以对某种资源进行顺序访问控制。如果应用服务集群部署，则涉及到对分布式应用加锁。

当前分布式加锁主要有三种方式：（磁盘）数据库、缓存数据库、Zookeeper。

使用DCS服务中Redis类型的缓存实例实现分布式加锁，有几大优势：

加锁操作简单，使用SET、GET、DEL等几条简单命令即可实现锁的获取和释放。
性能优越，缓存数据的读写优于磁盘数据库与Zookeeper。
可靠性强，DCS有主备和集群实例类型，避免单点故障。
实践指导
准备一台弹性云服务器（ECS），选择Windows系统类型。
在ECS上安装JDK1.8以上版本和Eclipse，下载jedis客户端（点此处直接下载jar包）。
在华为云控制台购买DCS缓存实例。注意和ECS选择相同虚拟私有云、子网以及安全组。
在ECS上运行Eclipse，创建一个java工程，为示例代码分别创建一个分布式锁实现类DistributedLock.java和测试类：CaseTest.java，并将jedis客户端作为libs引用到工程中。
将DCS缓存实例的连接地址、端口以及连接密码配置到示例代码文件中。注意有两处需要配置密码信息，分别在getLockWithTimeout和releaseLock两个方法中。
编译并运行得到结果。
加锁实现
须知：
以下代码实现仅展示使用DCS服务进行加锁访问的便捷性。具体技术实现需要考虑死锁、锁的检查等情况，这里不做详细说明。

package dcsDemo01;

import java.util.UUID;

import redis.clients.jedis.Jedis;

public class DistributedLock {
    private final String host = "192.168.0.220";
    private final int port = 6379;

    private static final String SUCCESS = "OK";
    private static final String SET_IF_NOT_EXIST = "NX";
    private static final String EXPIRE_TIME = "PX";

    public  DistributedLock(){}

    /*
     * @param lockName      锁名
     * @param timeout       获取锁的超时时间
     * @param lockTimeout   锁的有效时间
     * @return              锁的标识
     */
    public String getLockWithTimeout(String lockName, long timeout, long lockTimeout) {
        String ret = null;
        Jedis jedisClient = new Jedis(host, port);

        try {
            String authMsg = jedisClient.auth("******");
            if (!SUCCESS.equals(authMsg)) {
                System.out.println("AUTH FAILED: " + authMsg);
            }

            String identifier = UUID.randomUUID().toString();
            String lockKey = "DLock:" + lockName;
            long end = System.currentTimeMillis() + timeout;

            while(System.currentTimeMillis() < end) {
                String result = jedisClient.set(lockKey, identifier, SET_IF_NOT_EXIST, EXPIRE_TIME, lockTimeout);
                if(SUCCESS.equals(result)) {
                    ret = identifier;
                    break;
                }

                try {
                    Thread.sleep(2);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }finally {
            jedisClient.quit();
            jedisClient.close();
        }

        return ret;
    }

    /*
     * @param lockName        锁名
     * @param identifier    锁的标识
     */
    public void releaseLock(String lockName, String identifier) {
        Jedis jedisClient = new Jedis(host, port);

        try {
            String authMsg = jedisClient.auth("******");
            if (!SUCCESS.equals(authMsg)) {
                System.out.println("AUTH FAILED: " + authMsg);
            }

            String lockKey = "DLock:" + lockName;
            if(identifier.equals(jedisClient.get(lockKey))) {
                jedisClient.del(lockKey);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }finally {
            jedisClient.quit();
            jedisClient.close();
        }
    }
}

测试代码
假设20个线程对10台mate10手机进行抢购：

package dcsDemo01;
import java.util.UUID;

public class CaseTest {
    public static void main(String[] args) {
        ServiceOrder service = new ServiceOrder();
        for (int i = 0; i < 20; i++) {
            ThreadBuy client = new ThreadBuy(service);
            client.start();
        }
    }
}

class ServiceOrder {
    private final int MAX = 10;

    DistributedLock DLock = new DistributedLock();

    int n = 10;

    public void handleOder() {
        String userName = UUID.randomUUID().toString().substring(0,8) + Thread.currentThread().getName();
        String identifier = DLock.getLockWithTimeout("Huawei Mate 10", 10000, 2000);
        System.out.println("正在为用户：" + userName + " 处理订单");
        if(n > 0) {
            int num = MAX - n + 1;
            System.out.println("用户："+ userName + "购买第" + num + "台，剩余" + (--n) + "台");
        }else {
            System.out.println("用户："+ userName + "无法购买，已售罄！");
        }
        DLock.releaseLock("Huawei Mate 10", identifier);
    }
}

class ThreadBuy extends Thread {
    private ServiceOrder service;

    public ThreadBuy(ServiceOrder service) {
        this.service = service;
    }

    @Override
    public void run() {
        service.handleOder();
    }
}

运行结果
配置好实际的缓存实例连接地址、端口与连接密码，运行代码，得到以下结果：

正在为用户：eee56fb7Thread-16 处理订单
用户：eee56fb7Thread-16购买第1台，剩余9台
正在为用户：d6521816Thread-2 处理订单
用户：d6521816Thread-2购买第2台，剩余8台
正在为用户：d7b3b983Thread-19 处理订单
用户：d7b3b983Thread-19购买第3台，剩余7台
正在为用户：36a6b97aThread-15 处理订单
用户：36a6b97aThread-15购买第4台，剩余6台
正在为用户：9a973456Thread-1 处理订单
用户：9a973456Thread-1购买第5台，剩余5台
正在为用户：03f1de9aThread-14 处理订单
用户：03f1de9aThread-14购买第6台，剩余4台
正在为用户：2c315ee6Thread-11 处理订单
用户：2c315ee6Thread-11购买第7台，剩余3台
正在为用户：2b03b7c0Thread-12 处理订单
用户：2b03b7c0Thread-12购买第8台，剩余2台
正在为用户：75f25749Thread-0 处理订单
用户：75f25749Thread-0购买第9台，剩余1台
正在为用户：26c71db5Thread-18 处理订单
用户：26c71db5Thread-18购买第10台，剩余0台
正在为用户：c32654dbThread-17 处理订单
用户：c32654dbThread-17无法购买，已售罄！
正在为用户：df94370aThread-7 处理订单
用户：df94370aThread-7无法购买，已售罄！
正在为用户：0af94cddThread-5 处理订单
用户：0af94cddThread-5无法购买，已售罄！
正在为用户：e52428a4Thread-13 处理订单
用户：e52428a4Thread-13无法购买，已售罄！
正在为用户：46f91208Thread-10 处理订单
用户：46f91208Thread-10无法购买，已售罄！
正在为用户：e0ca87bbThread-9 处理订单
用户：e0ca87bbThread-9无法购买，已售罄！
正在为用户：f385af9aThread-8 处理订单
用户：f385af9aThread-8无法购买，已售罄！
正在为用户：46c5f498Thread-6 处理订单
用户：46c5f498Thread-6无法购买，已售罄！
正在为用户：935e0f50Thread-3 处理订单
用户：935e0f50Thread-3无法购买，已售罄！
正在为用户：d3eaae29Thread-4 处理订单
用户：d3eaae29Thread-4无法购买，已售罄！

不加锁场景
如果注释掉加锁代码，变成无锁情况，则抢购无序。

//测试类中注释两行用于加锁的代码：
public void handleOder() {
    String userName = UUID.randomUUID().toString().substring(0,8) + Thread.currentThread().getName();
    //加锁代码
    //String identifier = DLock.getLockWithTimeout("Huawei Mate 10", 10000, 2000);
    System.out.println("正在为用户：" + userName + " 处理订单");
    if(n > 0) {
        int num = MAX - n + 1;
        System.out.println("用户："+ userName + "够买第" + num + "台，剩余" + (--n) + "台");
    }else {
        System.out.println("用户："+ userName + "无法够买，已售罄！");
    }
    //加锁代码
    //DLock.releaseLock("Huawei Mate 10", identifier);
}

注释加锁代码后的运行结果，可以看出处理过程是无序的：

正在为用户：e04934ddThread-5 处理订单
正在为用户：a4554180Thread-0 处理订单
用户：a4554180Thread-0购买第2台，剩余8台
正在为用户：b58eb811Thread-10 处理订单
用户：b58eb811Thread-10购买第3台，剩余7台
正在为用户：e8391c0eThread-19 处理订单
正在为用户：21fd133aThread-13 处理订单
正在为用户：1dd04ff4Thread-6 处理订单
用户：1dd04ff4Thread-6购买第6台，剩余4台
正在为用户：e5977112Thread-3 处理订单
正在为用户：4d7a8a2bThread-4 处理订单
用户：e5977112Thread-3购买第7台，剩余3台
正在为用户：18967410Thread-15 处理订单
用户：18967410Thread-15购买第9台，剩余1台
正在为用户：e4f51568Thread-14 处理订单
用户：21fd133aThread-13购买第5台，剩余5台
用户：e8391c0eThread-19购买第4台，剩余6台
正在为用户：d895d3f1Thread-12 处理订单
用户：d895d3f1Thread-12无法购买，已售罄！
正在为用户：7b8d2526Thread-11 处理订单
用户：7b8d2526Thread-11无法购买，已售罄！
正在为用户：d7ca1779Thread-8 处理订单
用户：d7ca1779Thread-8无法购买，已售罄！
正在为用户：74fca0ecThread-1 处理订单
用户：74fca0ecThread-1无法购买，已售罄！
用户：e04934ddThread-5购买第1台，剩余9台
用户：e4f51568Thread-14购买第10台，剩余0台
正在为用户：aae76a83Thread-7 处理订单
用户：aae76a83Thread-7无法购买，已售罄！
正在为用户：c638d2cfThread-2 处理订单
用户：c638d2cfThread-2无法购买，已售罄！
正在为用户：2de29a4eThread-17 处理订单
用户：2de29a4eThread-17无法购买，已售罄！
正在为用户：40a46ba0Thread-18 处理订单
用户：40a46ba0Thread-18无法购买，已售罄！
正在为用户：211fd9c7Thread-9 处理订单
用户：211fd9c7Thread-9无法购买，已售罄！
正在为用户：911b83fcThread-16 处理订单
用户：911b83fcThread-16无法购买，已售罄！
用户：4d7a8a2bThread-4购买第8台，剩余2台