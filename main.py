__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'



class Descriptor(object):

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return '__get__'
        #return instance.config.get(self.name)


class ServiceMeta(type):

    def __new__(mcs, name, bases, attrs):
        # for k,v in attrs.iteritems():
        #     if isinstance(v, Descriptor):
        #         print '{0}: {1}'.format(k,v.__get__(mcs))

        return super(ServiceMeta, mcs).__new__(mcs, name, bases, attrs)


class Service(object):

    __metaclass__ = ServiceMeta

    x = Descriptor('x')

    y = Descriptor('y')

    def __init__(self):
        self.config = {}

    def func(self):
        import inspect
        print 'fuck'
        print inspect.ismethoddescriptor(self.__class__.x)
        for a in dir(self):
            v = getattr(self, a)
            print '{0} -- {1} -- {2}'.format(str(a), str(v), type(a))

        print type(self.x)
        print type(self.y)

    @classmethod
    def cfunc(cls):
        import inspect

        #for name, value in ((name, getattr(cls, name, None)) for name in dir(cls) if not name.startswith('_')):
        #    print ''


        print inspect.ismethoddescriptor(cls.x)
        for a in dir(cls):
            v = getattr(cls, a)
            print '{0} -- {1} -- {2}'.format(str(a), str(v), type(v))



def main():
    s = Service()
    s.func()
    #Service.cfunc()

if __name__ == '__main__':
    main()