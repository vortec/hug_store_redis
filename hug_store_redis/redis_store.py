import hug
import json


class RedisStore:
    def __init__(self, connection, namespace='store', expiration=86400):
        self.connection = connection
        self.namespace = namespace
        self.expiration = expiration

    def _make_full_key(self, key):
        return '{}:{}'.format(self.namespace, key)

    def set(self, key, data):
        payload = json.dumps(data)
        full_key = self._make_full_key(key)
        self.connection.set(full_key, payload, self.expiration)

    def get(self, key):
        payload = self.connection.get(self._make_full_key(key))
        if payload is None:
            raise hug.exceptions.StoreKeyNotFound(key)
        return json.loads(payload.decode('utf-8'))

    def exists(self, key):
        return self.connection.exists(self._make_full_key(key))

    def delete(self, key):
        full_key = self._make_full_key(key)
        return self.connection.delete(full_key) == 1
