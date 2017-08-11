# iterate through args
def func1(*args,**kwargs):
  for arg in args:
    print arg
  for key, value in kwargs.iteritems():
    print key, value
   
func1(1,2,3,4,a=1,b=2,c=3,d=4)
