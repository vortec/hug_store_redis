import os
import pytest
import redis


@pytest.fixture()
def connection():
    host = os.environ.get('REDIS_HOST', 'localhost')
    port = int(os.environ.get('REDIS_PORT', 6379))
    db = int(os.environ.get('REDIS_DB', 0))

    return redis.StrictRedis(host=host, port=port, db=db)
