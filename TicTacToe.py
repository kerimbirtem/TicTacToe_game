"""
@author: kerim
"""
import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.moves = set()  # Moves is now a set to store unique moves
        self.score = 0  # Initialize score to zero

    def make_move(self, board_list):
        while True:
            move = input(f"{self.name}, lütfen hamlenizi yapın (1-9 arası bir sayı girin): ")
            if move.isdigit() and 1 <= int(move) <= 9:
                if int(move) not in board_list:
                    self.moves.add(int(move))  # Add move to the set
                    break
                else:
                    print("Bu hücre zaten dolu! Lütfen başka bir hücre seçin.")
            else:
                print("Geçersiz hamle! Lütfen 1-9 arası bir sayı girin.")

def print_board(players):
    board = []
    all_moves = set()
    for player in players:
        all_moves.update(player.moves)
    
    for i in range(1, 10):
        symbol = ' '
        if i in all_moves:
            for player in players:
                if i in player.moves:
                    symbol = player.symbol
                    break
        board.append(symbol)

    print(f"""
    {board[6]} | {board[7]} | {board[8]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[0]} | {board[1]} | {board[2]}
    """)

def check_win(players):
    win_conditions = [
        [7, 8, 9], [4, 5, 6], [1, 2, 3],
        [7, 5, 3], [9, 5, 1], [7, 4, 1],
        [8, 5, 2], [9, 6, 3]
    ]
    
    for player in players:
        for condition in win_conditions:
            if all(elem in player.moves for elem in condition):
                return player

    # Check if all cells are filled
    all_moves = {move for player in players for move in player.moves}
    if len(all_moves) == 9:  # All cells filled
        return 'Draw'
    
    return None

def main():
    print("Tic Tac Toe oyununa hoş geldiniz!")
    player1_name = ""
    player2_name = ""

    while not player1_name:
        player1_name = input("Oyuncu 1 adını giriniz: ")
    while not player2_name:
        player2_name = input("Oyuncu 2 adını giriniz: ")

    players = [
        Player(player1_name, 'X'),
        Player(player2_name, 'O')
    ]
    
    while True:
        current_player = random.choice(players)
        print(f"{current_player.name} oyunu başlatıyor. İlk oyuncu {current_player.symbol} olacak.")
        
        while True:
            print_board(players)
            current_player.make_move({move for player in players for move in player.moves})
            
            if check_win(players) == 'Draw':
                print_board(players)
                print("Oyun berabere bitti!")
                break
            elif check_win(players):
                winner = check_win(players)
                print_board(players)
                print(f"Oyunu {winner.name} kazandı!")
                winner.score += 1
                break
            
            current_player = players[(players.index(current_player) + 1) % 2]
        
        # Print current scores
        print(f"{players[0].name} skoru: {players[0].score}")
        print(f"{players[1].name} skoru: {players[1].score}")
        
        # Ask for replay or quit
        while True:
            choice = input("Devam etmek için '1', Oyunu bitirmek için '2', Yeniden başlamak için '0' tuşuna basın: ")
            if choice in ['1', '2', '0']:
                break
            else:
                print("Geçersiz seçenek! Lütfen '1', '2' veya '0' tuşlarından birini seçin.")
        
        if choice == '2':
            print("Oyunu bitirdiniz. Son skorlar:")
            print(f"{players[0].name} skoru: {players[0].score}")
            print(f"{players[1].name} skoru: {players[1].score}")
            break
        elif choice == '0':
            # Reset game for a new round
            for player in players:
                player.moves.clear()
                player.score = 0
            print("Yeni bir oyun başlatılıyor!")
            player1_name = ""
            player2_name = ""
            while not player1_name:
                player1_name = input("Oyuncu 1 adını giriniz: ")
            while not player2_name:
                player2_name = input("Oyuncu 2 adını giriniz: ")
            players = [
                Player(player1_name, 'X'),
                Player(player2_name, 'O')
            ]
        else:
            # choice == '1', continue with the current players
            # Only clear moves, keep scores
            for player in players:
                player.moves.clear()
            print("Yeni tur başlatılıyor!")

if __name__ == "__main__":
    main()

