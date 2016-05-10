
>>> _
Traceback (most recent call last):
  File "", line 1, in 
NameError: name '_' is not defined
>>> 42
>>> _
42
>>> 'alright!' if _ else ':('
'alright!'
>>> _
'alright!'


n = 42
for _ in range(n):
    do_something()


from django.utils.translation import ugettext as _
from django.http import HttpResponse

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)



>>> class A(object):
...     def _internal_use(self):
...         pass
...     def __method_name(self):
...         pass
... 
>>> dir(A())
['_A__method_name', ..., '_internal_use']


>>> class B(A):
...     def __method_name(self):
...         pass
... 
>>> dir(B())
['_A__method_name', '_B__method_name', ..., '_internal_use']


>>> class C(object):
...     def __mine__(self):
...         pass
...
>>> dir(C)
... [..., '__mine__', ...]


