import hug
from hug_store_redis import RedisStore
import pytest
import time
import uuid


def test_store(connection):
    store = RedisStore(connection, namespace='test')
    key = str(uuid.uuid4())
    data = {'important': True}

    # Key doesn't exist
    assert not store.exists(key)

    # Create
    store.set(key, data)
    assert store.exists(key)

    # Read
    assert store.get(key) == data

    # Update
    data['important'] = False
    store.set(key, data)
    assert store.get(key) == data

    # Delete
    store.delete(key)
    assert not store.exists(key)


def test_get_unknown_key(connection):
    store = RedisStore(connection, namespace='test')

    with pytest.raises(hug.exceptions.StoreKeyNotFound):
        store.get('this-does-not-exist')


def test_expiration(connection):
    store = RedisStore(connection, namespace='test', expiration=1)
    key = str(uuid.uuid4())
    store.set(key, True)
    assert store.exists(key)
    time.sleep(1)
    assert not store.exists(key)
