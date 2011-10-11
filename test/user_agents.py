IE = {'type': 'desktop', 'engine': 'trident'}
FF = {'type': 'desktop', 'engine': 'gecko'}
SA = {'type': 'desktop', 'engine': 'webkit', 'app': 'safari'}
CH = {'type': 'desktop', 'engine': 'webkit', 'app': 'chrome'}
OP = {'type': 'desktop', 'engine': 'presto'}
KQ = {'type': 'desktop', 'engine': 'khtml'}
GWK = {'type': 'desktop', 'engine': 'webkit'} # Generic WebKit
GGK = {'type': 'desktop', 'engine': 'gecko'} # Generic Gecko
OLD = {'type': 'desktop', 'engine': 'unknown'}

user_agents = (
    ("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; "
    ".NET CLR 1.1.4322)", IE),
    ("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.2) Gecko/20100115 "
    "Firefox/3.6", FF),
    ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) "
    "AppleWebKit/531.22.7 (KHTML, like Gecko) Version/4.0.5 Safari/531.22.7",
     SA),
    ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.2) "
    "Gecko/20100316 Firefox/3.6.2", FF),
    ("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.1) "
    "Gecko/20090715 Firefox/3.5.1", FF),
    ("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322)",
     IE),
    ("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; "
     ".NET CLR 2.0.50727", IE),
    ("Mozilla/4.0 (compatible; MSIE 6.01; Windows NT 6.0)", IE),
    ("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98; Win 9x 4.90)", IE),
    ("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.2 (KHTML, like "
    "Gecko) Chrome/5.0.342.7 Safari/533.2", CH),
    ("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3pre) Gecko/20100328 "
    "Ubuntu/9.10 (karmic) Namoroka/3.6.3pre", FF),
    ("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 "
    "(KHTML, like Gecko) Version/3.1 Safari/525.13", SA),
    ("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.1) Gecko/20090703 "
    "Firefox/3.5", FF),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 "
    "(KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1", CH),
    ("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 "
    "(KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9", CH),
    ("Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 "
    "(like Gecko)", KQ),
    ("Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 "
    "(like Gecko)", KQ),
    ("Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.9.1.6) Gecko/20091201 "
    "Firefox/3.5.6 Opera 10.53", OP),
    ("Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
     OP),
    ("Opera/5.0 (SunOS 5.8 sun4u; U) [en]", OP),
    ("Mozilla/5.0 (X11; U; Linux i686; fr-fr) AppleWebKit/525.1+ "
    "(KHTML, like Gecko, Safari/525.1+) midori/1.19", GWK),
    ("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051007 "
    "Galeon/2.0.0 (Debian package 2.0.0-1)", GGK),
    ("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.14) "
    "Gecko/20101020 Conkeror/0.9.2 (Debian-0.9.2+git100804-1)", GGK),
    ("Mozilla/4.5 (compatible; OmniWeb/4.2.1-v435.9; Mac_PowerPC)", OLD),
)

mobile_agents = (
    "Mozilla/5.0 (Linux; U; Android 2.1-update1; en-gb; Nexus One Build/ERE27) "
    "AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0_1 like Mac OS X; en-us) "
    "AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5B108 "
    "Safari/525.20",
    "Mozilla/5.0 (iPhone Simulator; U; CPU iPhone OS 3_1_3 like Mac OS X; "
    "en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 "
    "Safari/528.16",
    "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) "
    "AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 "
    "Safari/531.21.10",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) "
    "AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 "
    "Safari/528.16",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.10pre) Gecko/20100325 "
    "Fennec/1.0a2",
)
