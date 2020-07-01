

### 单例模式

## 函数装饰器
def singleton(cls):
    instance = {}
    def inner():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return inner

@singleton

### 类装饰器实现

class singleton(object):
    def __init__(self, cls):
        self.cls = cls
        self.instance = {}
    def __call__(self):
        if self.cls not in self.instance:
            self.instance[self.cls] = self.cls()
        return self.instance[self.cls]
