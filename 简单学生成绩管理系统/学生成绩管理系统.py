# 定义学生类
class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []
    def add_grade(self,grade):
        self.grades.append(grade)
    def average_grade(self):
        # 判断是否有成绩
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)


# 定义学生成绩管理类
class StudentGradeManager:
    def __init__(self):
        self.student = {} # 学生列表
    def add_student(self,name):
        # 判断学生是否存在
        if name not in self.student:
            self.student[name] = Student(name)
        else:
            print(f"学生{name}已存在")
    def get_student(self,name):
        return self.student.get(name)
    def add_grade_to_student(self,name,grade):
        student = self.get_student(name)
        if student:
            # 给学生添加成绩
            student.add_grade(grade)
        else:
            print(f"学生{name}不存在")
    def show_average_grades(self):
        # 查看所有学生的平均成绩
        for name,student_grade in self.student.items():
            print(f"{name}的平均成绩为{student_grade.average_grade():.2f}")

# 实例化对象
manager = StudentGradeManager()
#添加学生
manager.add_student("冰冰")
manager.add_student("苏苏")
manager.add_student("子怡")

# 添加成绩
manager.add_grade_to_student("冰冰",90)
manager.add_grade_to_student("冰冰",80)
manager.add_grade_to_student("冰冰",86)

manager.add_grade_to_student("苏苏",79)
manager.add_grade_to_student("苏苏",99)
manager.add_grade_to_student("苏苏",84)

manager.add_grade_to_student("子怡",86)
manager.add_grade_to_student("子怡",100)
manager.add_grade_to_student("子怡",77)

# 查看平均成绩
manager.show_average_grades()