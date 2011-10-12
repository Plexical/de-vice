from device import useragent

from .user_agents import user_agents

def pytest_generate_tests(metafunc):

    if "agent" in metafunc.funcargnames:
        for agent in user_agents:
            metafunc.addcall(funcargs={'agent': agent})

def test_create_simplest():
    assert useragent.Analyzer()

def test_calculate_poc():
    analyzer = useragent.Analyzer()
    info = analyzer.analyze('Dummy')
    assert info['type'] == 'unknown'
    info['digest'] in analyzer.cache

def test_uaencode():
    assert (useragent.uaencode("Opera/5.0 (SunOS 5.8 sun4u; U) [en]") ==
            "Opera/5.0_(SunOS_5.8_sun4u*_U)_[en]")

def test_analysis(agent):
    analyzer = useragent.Analyzer() # XXX Lame, learn to use funcargs instead
    agent, attrs = agent # XXX Also lame, same reason
    info = analyzer.analyze(agent)
    assert info['complete']
    for attr, expected in attrs.iteritems():
        assert info[attr] == expected
        
