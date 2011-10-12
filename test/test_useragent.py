from device import useragent

from .user_agents import user_agents

def pytest_generate_tests(metafunc):

    if "agent" in metafunc.funcargnames:
        for agent in user_agents:
            metafunc.addcall(funcargs={'agent': agent})

class DummyCache(dict):
    retreive = lambda s, k: s.get(k, None)

    def store(self, key, data):
        self[key] = data

def setup_module(mod):
    mod.cache = DummyCache()
    mod.analyzer = useragent.Analyzer(mod.cache)

def test_calculate_poc():
    info = analyzer.analyze('Dummy')
    assert info['type'] == 'unknown'
    info['digest'] in cache

def test_uaencode():
    assert (useragent.uaencode("Opera/5.0 (SunOS 5.8 sun4u; U) [en]") ==
            "Opera/5.0_(SunOS_5.8_sun4u*_U)_[en]")

def test_analysis(agent):
    user_agent, attrs = agent
    info = analyzer.analyze(user_agent)
    assert info['complete']
    for attr, expected in attrs.iteritems():
        assert info[attr] == expected
        
