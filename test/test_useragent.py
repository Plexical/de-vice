import types
import mock

from device import useragent

import user_agents

def pytest_funcarg__analyzer(request):
    return useragent.Analyzer()

def pytest_funcarg__fake_analyzer(request):
    analyzer = useragent.Analyzer()
    analyzer.query = types.MethodType(lambda s,
                                      ua: {'complete':True}, analyzer)
    return analyzer

def pytest_generate_tests(metafunc):
    if "agent" in metafunc.funcargnames:
        for agent in user_agents.user_agents:
            metafunc.addcall(funcargs={'agent': agent})

def test_create_simplest():
    assert useragent.Analyzer()

def test_calculate_poc(fake_analyzer):
    info = fake_analyzer.analyze('Dummy')
    assert info['type'] == 'unknown'
    info['digest'] in fake_analyzer.cache

def test_uaencode():
    assert (useragent.uaencode("Opera/5.0 (SunOS 5.8 sun4u; U) [en]") ==
            "Opera/5.0_(SunOS_5.8_sun4u*_U)_[en]")

def test_calculate_unknown_queries(analyzer):
    with mock.patch.object(analyzer, 'query') as mocked_q:
        mocked_q.return_value = {'complete': True}
        analyzer.analyze('Dummy')
    assert mocked_q.called

def test_analysis(analyzer, agent):
    agent, attrs = agent # XXX would be more elegant to separate agent, attrs
    with mock.patch.object(analyzer, 'query') as mocked_q:
        mocked_q.return_value = {'complete': True}
        info = analyzer.analyze(agent)
    assert info['complete']
    for attr, expected in attrs.iteritems():
        assert info[attr] == expected

def test_uaencode_called(analyzer):
    with mock.patch.object(analyzer, '_webservice') as ws:
        ws.return_value = {'resolution_width': 1,
                           'resolution_height': 1,
                           'complete': True}
        res = analyzer.analyze("A Dummy;browser")
    assert ws.call_args[0][0] == 'A_Dummy*browser'
    assert res['complete']

def test_webservice(analyzer):
    with mock.patch('device.useragent.requests.get') as fake_ws:
        res = mock.Mock()
        res.ok = True
        res.content = user_agents.n1_response
        fake_ws.return_value = res
        res = analyzer.analyze(user_agents.n1)
    assert res['complete']
    assert res['width'] == 480
    assert res['height'] == 800
