import json
obj = {'a' : 'b', 'c' : 'd'}
fp = open('obj.json', 'w')
json.dump(obj, fp)
fp.close()s = json.dumps(obj)
x = json.load(open('obj.json', 'r'))
y = json.loads(s)


import json
obj = {u'姓名' : u'无名氏', u'国籍' : u'中国'}
s = json.dumps(obj, ensure_ascii=False, indent=4)
obj2 = json.loads(s, encoding='utf8')


import json
from datetime import date, datetime
class AdvEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return super().default(self, obj)

obj = {}
json.dumps(obj, cls=MyEncoder)


import functools
adumps = functools.partial(json.dumps, cls=AdvEncoder)
d = datetime.now()
adumps(d)
