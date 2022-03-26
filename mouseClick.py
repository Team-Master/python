# mouseClick.py
import mouse  
import time

clickLeftCnt  = 0    # 몇 번째 클릭인지저장할 변수  

while True:
  if mouse.is_pressed("left"):              # 마우스 왼쪽 클릭이면
    clickLeftCnt += 1                              # 클릭 숫자 증가
    print('Left-Clicked: ' + str(clickLeftCnt))    # 메시지 출력
    pos = mouse.get_position()              # 현재 마우스 포인터 좌표
    print(pos)                                  
    # mouse.move(pos[0], pos[1]+20)           # 마우스 포인터 좌표를 아래로 이동
  time.sleep(0.1)                          # 0.05초 대기 (중복 체크 예방)
