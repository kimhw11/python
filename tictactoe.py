def display_board(board):
    for i in range(3):
        print("-------------")
        print(f"| {board[3*i]} | {board[3*i+1]} | {board[3*i+2]} |")
    print("-------------")

def input_OX():
    # O나 X중에서 선택해주세요 O/X
    # print("O나 X중에 선택해주세요 :")
    # O가 입력되면 컴퓨터는 자동으로 X , X가 입력되면 컴퓨터는 O
    while True:
        player = input("O나 X중에 선택해 주세요 :")
        if player == 'O':
            return 'O' , 'X'
        elif player == 'X':
            return 'X' , 'O'
        # 사용자가 O나 X를 입력, O나 X가 아닌 다른 문자가 들어오면 다시 입력 받는다
        if player != 'O' or player != 'X':
            print("다시 입력해 주세요")
    # 입력 받은 문양의 반대되는 문양을 컴퓨터 문양으로 지정
    # 사용자 문양 , 컴퓨터 문양 순으로 return

def input_POS(board):
    # 사용자가 문양을 넣을 위치를 입력 받는다 (1 ~ 9)
    while True:
        pos = int(input("문양을 넣을 위치를 선택해 주세요 :"))
    # 입력 받은 자리가 놓아도 되는 자리인지 확인한다
        if 1 <= pos <= 9 :
            if board[pos-1] == '*':
                return pos-1
    # 만약 입력 받은 자리가 올바르지 않은 자리라면 다시 입력 받는다
            elif board[pos-1] != '*':
                print("이미 다른 문양이 들어와 있습니다. 다시 선택해 주세요")
        else:
            print('1부터 9까지의 정수를 입력해 주세요')

    # 제대로 입력 받았다면 해당 자리를 return 한다


def Victory(board , user):
    # 유저가 우승했을 경우 True , 아닌 경우 False를 리턴
    #가로 , 세로
        for i in range(3):
            if board[3*i] == board[3*i+1] == board[3*i+2] == user:
                return True
            elif board[0+i] == board[3+i] == board[6+i] == user:
                return True
        #대각선
        if board[0] == board[4] == board[8] == user or board[2] == board[4] == board[6] == user:
            return True
    # 우승 조건은 한줄 빙고로 가로 3 , 세로 3 ,대각선 2개의 경우가 있다

def random_POS(board , player):
    # 랜덤한 정수를 만들어 컴퓨터의 문양을 넣을 좌표로 본다
    import random
    while True:
        sp = random.randint(0,8)
        if board[sp] == "*" :
            return sp
    # 만약 올바른 좌표가 아니라면 다시 만든다
    # 잘 만들어 졌다면 return 한다

#비기는 경우
def draw(board):
    # for b in board:
    #     if b == "*":
    #         return False
    # return True
    return "*" not in board

if __name__ == "__main__":
    board = ['*'] * 9
    player , computer = "O","X"
    pos = input_POS(board)
    print(pos)
    display_board(board)
    print(Victory(board , computer))
    print(draw(board))
