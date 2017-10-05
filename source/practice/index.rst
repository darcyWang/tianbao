基础概念理解
==============

一些名词的解释以及自己不太明白的词语
 DFS (depth first search)


2147483647  是32位操作系统中最大的符号型整型常量


时间复杂度
空间复杂度


贪心算法
一、基本概念：
 
     所谓贪心算法是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的仅是在某种意义上的局部最优解。
     贪心算法没有固定的算法框架，算法设计的关键是贪心策略的选择。必须注意的是，贪心算法不是对所有问题都能得到整体最优解，选择的贪心策略必须具备无后效性，即某个状态以后的过程不会影响以前的状态，只与当前状态有关。
    所以对所采用的贪心策略一定要仔细分析其是否满足无后效性。

二、贪心算法的基本思路：
    1.建立数学模型来描述问题。
    2.把求解的问题分成若干个子问题。
    3.对每一子问题求解，得到子问题的局部最优解。
    4.把子问题的解局部最优解合成原来解问题的一个解。

三、贪心算法适用的问题
      贪心策略适用的前提是：局部最优策略能导致产生全局最优解。
    实际上，贪心算法适用的情况很少。一般，对一个问题分析是否适用于贪心算法，可以先选择该问题下的几个实际数据进行分析，就可做出判断。
 
四、贪心算法的实现框架
    从问题的某一初始解出发；
    while （能朝给定总目标前进一步）
    { 
          利用可行的决策，求出可行解的一个解元素；
    }
    由所有解元素组合成问题的一个可行解；
  
五、贪心策略的选择
     因为用贪心算法只能通过解局部最优解的策略来达到全局最优解，因此，一定要注意判断问题是否适合采用贪心算法策略，找到的解是否一定是问题的最优解。
 



1. doctype的作用是什么?页面中有没有它的区别是?
2. w3c标准盒模型占位宽度是如何计算的?它与IE盒模型有什么不同?
3. 请说下移动端常见的适配不同屏幕大小的方法?
4. 一个高宽未知的图片如何在一个比它大的容器内水平垂直居中?
5. label标签的作用是什么?
6. 定义链接四种状态的伪类的正确书写顺序是?
7. 你知道的css选择器有哪些?
8. 下面两个div的间距应该是多少?为什么?
<div style="margin:5px"></div><div style="margin:10px"></div>
9. png8、png24的区别是什么?
10. png和jpg这两种图片格式分别适用的场景是?
11.请介绍下你知道的前端性能优化方法?
12. 页面导入样式时，使用link和 @import有什么区别?
13.请介绍下css中针对ie6-9常用的hack方法
14. Javascript的基本数据类型有哪些?
15.请介绍下Javascript原型、原型链的特点?
16.曾经用原生Javascript实现过什么功能?
17. 请用jquery和原生Js分别实现添加、移除、移动、复制、创建和查找DOM节点
18. 实时监测用户在input内输入的字符数应该监听哪个事件?
19. 遇到疑难问题时，你通常是如何解决的？最好举例说明
20. inline、inline-block-block的区别是?


Django-celery + Redis on OSX Lion
=================================

Installation and Setup
----------------------

1. Install redis on OSX (10.7) Lion::

        $ brew install redis

2. In the project and virtualenv I wanted to use django-celery in I installed the following::

        $ pip install django-celery
        $ pip install redis

3. Add ``djcelery`` to your ``INSTALLED_APPS`` in your Django ``settings.py`` file.

4. Added the following django-celery settings toward the end of my Django ``settings.py`` file. ::

        BROKER_HOST = "localhost"
        BROKER_BACKEND="redis"
        REDIS_PORT=6379
        REDIS_HOST = "localhost"
        BROKER_USER = ""
        BROKER_PASSWORD =""
        BROKER_VHOST = "0"
        REDIS_DB = 0
        REDIS_CONNECT_RETRY = True
        CELERY_SEND_EVENTS=True
        CELERY_RESULT_BACKEND='redis'
        CELERY_TASK_RESULT_EXPIRES =  10
        CELERYBEAT_SCHEDULER="djcelery.schedulers.DatabaseScheduler"

.. note::

        If you run several sites that use Celery you will want to increment the number for ``REDIS_DB`` and ``BROKER_VHOST`` setting by 1 for each new site. Example for the next site you add, you would want to change those settings to the following::

                BROKER_VHOST = "1"
                REDIS_DB = 1

5. In your local development settings file it might be good to add ``CELERY_ALWAYS_EAGER = True``. This blocks the run tests (sans celery) that way you can test and develop easier.

6. Open a terminal window and start redis. ::

        $ redis-server /usr/local/etc/redis.conf

7. Open another terminal window and start a celery worker server for testing. ::

        $ python manage.py celeryd -l info


Example Task
------------

- Add the following code in a ``tasks.py`` file in a folder for one of your apps that's in your ``INSTALLED_APPS`` in your Django ``settings.py`` file. ::

        from celery.decorators import task

        @task()
        def add(x, y):
            return x + y

- Now you should be able to play around with Django-celery from the command line. Open another terminal window and do the following::

        $ django-admin.py shell
        >>> result = add.delay(4, 4)
        >>> result.ready() # returns True if the task has finished processing.
        False
        >>> result.result # task is not ready, so no return value yet.
        None
        >>> result.get()   # Waits until the task is done and returns the retval.
        8
        >>> result.result # direct access to result, doesn't re-raise errors.
        8
        >>> result.successful() # returns True if the task didn't end in failure.
        True