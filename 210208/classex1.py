# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:33:38 2021

@author: user

classex1.py : 클래스 예제
"""
#기본 생성자 : __init(self):
#               pass
# self : 자바의 this
class Car :
    color = "" #변수
    speed = 0 # 변수
    def upSpeed(self,value): #메서드
        self.speed += value
    def downSpeed(self,value): #메서드
        self.speed -= value
myCar1 = Car() #객체화
myCar1.color = "빨강"
myCar1.speed = 0
myCar2 = Car() #객체화
myCar2.color = "노랑"
myCar2.speed = 0
myCar3 = Car() #객체화
myCar3.color = "파랑"
myCar3.speed = 0
myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재속도는 %dkm입니다."
      % (myCar1.color, myCar1.speed))
myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재속도는 %dkm입니다."
      % (myCar2.color, myCar2.speed))
myCar3.upSpeed(10)
print("자동차3의 색상은 %s 이며, 현재속도는 %dkm입니다."
      % (myCar3.color, myCar3.speed))