hug_store_redis
=======
[![Build Status](https://travis-ci.org/vortec/hug_store_redis.svg?branch=master)](https://travis-ci.org/vortec/hug_store_redis)
[![Coverage Status](https://coveralls.io/repos/vortec/hug_store_redis/badge.svg?branch=master&service=github)](https://coveralls.io/github/vortec/hug_store_redis?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/vortec/hug_store_redis/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/vortec/hug_store_redis/?branch=master)

**hug_store_redis** is a [Redis](http://redis.io/) store extension for the Python framework
[hug](https://github.com/timothycrosley/hug), which can be used as a session store.

Installation
------------
Install via pip:

    pip install hug_store_redis


Usage
-----
This is how you create a Redis store:

```python
from hug_store_redis import RedisStore
store = RedisStore(connection, namespace='sessions', expiration=3600)
```

The arguments are as follows:

* **connection**: A connection object to the Redis server. This module installs
  the [official redis module](https://pypi.python.org/pypi/redis), but you can
  use your client of choice thanks to Python's duck typing. If you just want to
  get started quickly, use: `import redis; connection = redis.StrictRedis()`.
* **namespace**: A prefix for the keys which will be saved in Redis. If you
  choose `sessions`, the full key will be `sessions:foobar`.
* **expiration**: Expiration time of each key in seconds. Will be reset on every
  `store.set()` call.

If you want to use this store with hug's session middleware, this is how:

```python
middleware = SessionMiddleware(store)
__hug__.http.add_middleware(middleware)
```

Remember that the `__hug__` object is only available after the first time a hug
decorator has been executed.


API
---
The API implements the hug API for external stores.

* **set(key, data)**: JSON-encode `data` and save it for the given `key`.
* **get(key)**: JSON-decode data for the given `key` and return it. Raises
  `hug.exceptions.StoreKeyNotFound` if the key does not exist.
* **exists(key)**: Return whether the given `key` exists or not.
* **delete(key)**: Delete the given `key`.

Authors
-------
**hug_store_redis** is written and maintained by Fabian Kochem.
