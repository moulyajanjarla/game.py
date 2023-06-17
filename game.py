box=[['' ,'', ''],['' ,'', ''],['' ,'', '']]
def print_box(box):
    print(*box[0], sep="|")
    print("--------")
    print(*box[1],sep="|")
    print("-------")
    print(*box[2],sep="|")
    print("-------")
def get_marker():
    marker1=input("marker1 choice (X or O):").upper()
    marker2=" "
    if marker1 =='X':
        marker2="O"
        return ['X','O']
    elif marker1 =='O':
        marker2="X"
        return ['O','X']
    else:
        print("invalid")
        return get_marker()
def get_coordinates():
    x,y=list(map(int,input("enter the coordinates").split()))
    if x in [0,1,2] and y in [0,1,2]:
        return [x,y]
    else:
        print('invalid input')
        return get_coordinates
def winning_chances(box):
    for row in box:
        if row[0]==row[1] and row[1]==row[2] and row[1]!="":
            return True 
    for i in range(len(box)):
        if box[0][i]==box[1][i] and box[1][i]==box[2][i] and box[2][i]!="":
            return True
        if box[0][0]==box[1][1] and box[1][1]==box[2][2] and box[2][2]!="":
            return True
        if box[0][2]==box[1][1] and box[1][1]==box[0][2] and box[0][2]!="":
            return True
        return False
def update_box(box,chance,marker,x,y):
    if chance==True:
        box[x][y]= marker
        if winning_chances(box):
            print("player 1 wins")
            return "game over"
        return False
    else:
        box[x][y]= marker
        if winning_chances(box):
            print("player 2 wins")
            return "game over"
        return True
def play_game():
    player1=0
    player2=0
    m1,m2=get_marker()
    print(f"player1: {m1},player2:{m2}")
    chance=True
    while True:
        print_box(box)
        x,y=get_coordinates()
        if chance:
            chance=update_box(box,chance,m1,x,y)
            if chance=="game over":
                break
            else:
                chance = update_box(box, chance, m2, x, y)
            if chance=="game over":
                break
play_game()
    
    
    
        
         
    
    

