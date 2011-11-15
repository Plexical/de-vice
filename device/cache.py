class DummyCache(dict):
    """
    A stupid kind of cache: cache directly to memory. Mostly
    intended for testing.
    """

    "Retrieves data by key"
    retreive = lambda s, k: s.get(k, None)

    "Cache data by key"
    def store(self, key, data):
        self[key] = data
