import selenium
import time



# 单例模式装饰器写法
def singleton(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper

# 单例模式new写法
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


@singleton
class test():

    def __init__(self):
        pass

class Browser():

    def __init__(self, token):

        self.token = token

    def genZan(self):

        pass

    def getLatestPageList(self):

        pass



if __name__ == '__main__':
    print("take notes")
    print(time.time())


