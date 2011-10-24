from mock import patch

from device import useragent

from .user_agents import user_agents

def pytest_funcarg__analyzer(request):
    return useragent.Analyzer()

def pytest_generate_tests(metafunc):
    if "agent" in metafunc.funcargnames:
        for agent in user_agents:
            metafunc.addcall(funcargs={'agent': agent})

def test_create_simplest():
    assert useragent.Analyzer()

def test_calculate_poc(analyzer):
    info = analyzer.analyze('Dummy')
    assert info['type'] == 'unknown'
    info['digest'] in analyzer.cache

def test_uaencode():
    assert (useragent.uaencode("Opera/5.0 (SunOS 5.8 sun4u; U) [en]") ==
            "Opera/5.0_(SunOS_5.8_sun4u*_U)_[en]")

def test_calculate_unknown_queries(analyzer):
    with patch.object(analyzer, 'query') as mocked_q:
        mocked_q.return_value = {'complete': True}
        analyzer.analyze('Dummy')
    assert mocked_q.called

def test_analysis(analyzer, agent):
    agent, attrs = agent # XXX would be more elegant to separate agent, attrs
    with patch.object(analyzer, 'query') as mocked_q:
        mocked_q.return_value = {'complete': True}
        info = analyzer.analyze(agent)
    assert info['complete']
    for attr, expected in attrs.iteritems():
        assert info[attr] == expected
        
