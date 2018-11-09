more practice and things become better
======================================

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

.. code-block:: python

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next          
                
    # use two queues
    # initialize your data structure here.
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if not self.queue2:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
        self.size += 1

    # @return nothing
    def pop(self):
        if not self.queue2:
            for _ in xrange(self.size-1):
                self.queue2.append(self.queue1.pop(0))
            self.queue1.pop(0)
        else:
            for _ in xrange(self.size-1):
                self.queue1.append(self.queue2.pop(0))
            self.queue2.pop(0)
        self.size -= 1

    # @return an integer
    def top(self):
        if not self.queue2:
            for _ in xrange(self.size-1):
                self.queue2.append(self.queue1.pop(0))
            tmp = self.queue1.pop(0)
            self.queue2.append(tmp)
            return tmp
        else:
            for _ in xrange(self.size-1):
                self.queue1.append(self.queue2.pop(0))
            tmp = self.queue2.pop(0)
            self.queue1.append(tmp)
            return tmp

    # @return an boolean
    def empty(self):
        return self.size == 0

    # use one queue   
    # initialize your data structure here.
    def __init__(self):
        self.queue = collections.deque()
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)
        for _ in xrange(self.size):
            self.queue.append(self.queue.popleft())
        self.size += 1

    # @return nothing
    def pop(self):
        self.queue.popleft()
        self.size -= 1

    # @return an integer
    def top(self):
        # queue peek operation
        return self.queue[0]

    # @return an boolean
    def empty(self):
        return self.size == 0
                
    A bit shorter and faster:

    ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
    The speed difference isn't noticeable with the given inputs, but you can see it like this (about 384 ms for the generator, about 504 ms for the filter+lambda)

    for _ in range(100):
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
    More lines but actually fewer printable characters and even faster (about 293 ms):

        ans = 0
        for x in nums:
            if x & xor & -xor:
                ans ^= x    
        
    def number(self, l):
        if l == 0:
            return 0
        if l % 2 == 0:
            return 4*(5**(l/2-1))
        elif l == 1:
            return 3
        else:
            return 3*(5**(l/2-1))*4 
        
        
    def titleToNumber(self, s):
        res = 0
        for i in s:
            res = res*26 + ord(i)-ord('A')+1
        return res  