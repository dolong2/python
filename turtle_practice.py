import random
import turtle

turtleList = []
swidth, sheight = 500, 500

turtle.title('거북 리스트 활용')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)


shape = turtle.getshapes()[6]
# 거북이 생성
for _ in range(0, 5):
  # 거북이 형태를 가져옴
  myTurtle = turtle.Turtle(shape)
  
  # 거북이가 위치할 좌표 설정
  tX = random.randrange(int(-swidth / 2), int(swidth / 2))
  tY = random.randrange(int(-sheight / 2), int(sheight / 2))
  
  # 거북이의 RGB를 랜덤으로 설정
  r = random.random(); g = random.random(); b = random.random()
  
  # 거북이 크기 설정
  tSize = random.randrange(1, 100) / 10
  
  # 거북이의 기울기 설정
  tAngle = random.randrange(0, 360)
  
  # 설정된 거북이 값들을 turtleList에 추가
  turtleList.append([myTurtle, tX, tY, tSize, tAngle, r, g, b])

# 생성된 거북이를 크기(tSize) 별로 정렬
turtleList.sort(key=lambda x: x[3])

# 선만 긋기 위해서 만든 커서
liner = turtle.Turtle(shape = turtle.getshapes()[1])

# turtleList를 순회하면서 정보에 맞게끔 거북이 세팅
for index, turttleInfo in enumerate(turtleList):
  # 거북이 shape
  myTurtle = turttleInfo[0]
  
  # 거북이 RGB 세팅
  myTurtle.color((turttleInfo[5], turttleInfo[6], turttleInfo[7]))
  myTurtle.pencolor((turttleInfo[5], turttleInfo[6], turttleInfo[7]))
  
  # 거북이 크기 설정
  myTurtle.turtlesize(turttleInfo[3])
  
  # 설정된 기울기만큼 왼쪽으로 회전
  myTurtle.left(turttleInfo[4])
  
  # 거북이가 위치할 좌표 세팅
  myTurtle.goto(turttleInfo[1], turttleInfo[2])
  
  # 좌표가 세팅되면서 생겼던 선 제거
  myTurtle.clear()
  
  # 처음일때는 현재 거북이 좌표로 커서를 옮기고 생겼던 선 제거
  if(index == 0):
    liner.goto(turttleInfo[1], turttleInfo[2])
    liner.clear()
  # 마지막 거북가 아닐때 다음 거북이로 커서 이동 
  if(index < len(turtleList) - 1):
    nextTurtle = turtleList[index + 1]
    liner.pencolor((turttleInfo[5], turttleInfo[6], turttleInfo[7]))
    liner.goto(nextTurtle[1], nextTurtle[2])
  
turtle.done()