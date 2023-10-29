from tictactoe import *

# 1. 보드판 준비 ---------------------------------------
board = ['*'] * 9

# 2. ox중 선택(컴퓨터는 반대) > inputOX()
player , computer = input_OX()  # O,X or X,O

# 3. 보드판 출력 ---------------------------------------
display_board(board)

# 4 ~ 10번까지 반복 > 보드판에 남은 공간이 없을 때 까지
while True:
    # 4. 사용자 자리 입력(올바른 자리 확인) > inputPOS()
    pos = input_POS(board)
    board[pos] = player
    # 5. 보드판 출력 ---------------------------------------
    display_board(board)

    # 6. 우승 조건 확인 - 우승 조건 성립 > 플레이어 승 출력 후 게임 종료 > victory()
    if Victory():
        print("Player win")
        exit()

    # 7. 컴퓨터 입력(랜덤한 정수 만들어 해당 자리에 문양 삽입) > randomPOS()
    pos = input_POS(board)
    board[pos] = computer

    # 8. 보드판 출력 ---------------------------------------
    display_board(board)

    # 9. 컴퓨터 우승 인지 확인 > victory()
    # 10. 컴퓨터가 우승 조건 성립시 컴퓨터 승 출력 후 게임 종료
    if Victory():
        print('Computer win')
        exit()






