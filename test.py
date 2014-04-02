# coding: utf-8

from py2lua import PY2LUA



data = {'list': [{'cnname': u'\u65e0\u540d\u58eb23', 'id': 12}, 12, 'string'], 'tuple': (1, 2, [3,4], {1: 2}), 'number': 12.0, 'dict': {'a': 1}}

if __name__ == '__main__':
    py2lua = PY2LUA()
    result = py2lua.encode(data)
    print result.encode('utf-8')
