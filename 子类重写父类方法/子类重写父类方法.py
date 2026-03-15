# 定义父类
class Vehicle:
    """车辆类"""
    def __init__(self,maker,model):
        self.maker = maker # 品牌
        self.model = model # 型号

    def describe(self):
        # 描述车辆的基本信息
        return f"这是一辆普通的车，品牌：{self.maker},型号：{self.model}"

# 定义子类，继承自 Vehicle 类
class Car(Vehicle):
    """汽车类，继承自车辆类"""
    def __init__(self,maker,model,year):
        super().__init__(maker,model)  # 调用父类的构造函数来初始化品牌和型号
        self.year = year    # 年份

    # 重写父类的 describe 方法
    def describe(self):
        return f"这是一辆汽车。品牌：{self.maker},型号：{self.model},年份：{self.year}"

# 实例化子类对象
car = Car("Toyota","Camry",2025)
# 描述汽车基本信息
print(car.describe())
