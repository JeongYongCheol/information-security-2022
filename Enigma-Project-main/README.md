# Enigma-Project
1차 Mini Term Project: ENIGMA 구현하기

## 201702072 정용철

# Wheels
def pass_wheels(input, reverse = False):

reverse가 참일 경우, 반사판에서 돌아오는 신호이므로 로터 순서를 뒤->앞으로 통과한다.

# Wheel Rotation
def rotate_wheels():

    # Implement Wheel Rotation Logics
    
    # 알파벳의 갯수는 26개 이므로, 26회 회전하면 원위치로 되돌아온다.
    
    # 따라서 회전수가 26회 이상일 경우, 다음 로터를 1회전하고 현 로터의 회전수를 0으로 설정해준다.
    
    # 회전수를 증가시킬 때, 해당하는 로터의 알파벳 위치를 1칸 씩 옮긴다. -> wire_rotate()
    
# wire rotate (새로 정의한 함수)
def wire_rotate(index):
    # 맨 앞 글자를 뒤로 옮기고 한칸씩 땡긴다.
