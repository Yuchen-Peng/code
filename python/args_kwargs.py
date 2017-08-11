# iterate through args
def func1(*args,**kwargs):
  for arg in args:
    print arg
  for key, value in kwargs.iteritems():
    print key, value
   
