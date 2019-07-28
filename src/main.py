from Action import Action
from Board import Board
from Game import Game
from Piece import Piece
from Player import Player
from Position import Position


def main():
    type = input("输入chess或go：")
    players_name = input("输入两个用户的名字（用空格分开）：")
    player1 = Player(players_name.split(" ")[0])
    player2 = Player(players_name.split(" ")[1])
    board = Board(type)
    game = Game(player1, player2, board)

    player = player1
    while True:
        action = input("{} 请输入操作\n".format(player.name) +
                       "1: 将尚未在棋盘上的一颗棋子放在棋盘上的指定位置\n" +
                       "2: 移动棋盘上某个位置的棋子至新位置\n" +
                       "3: {}".format("提子\n" if type == "go" else "吃子\n") +
                       "4: 查询某个位置的占用情况(空闲，或者被哪一方的什么棋子所占用)\n" +
                       "5: 计算两个玩家分别在棋盘上的棋子总数\n")

        if player == player1:
            while action == "1":
                line = input("请输入坐标:")
                x, y = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                if game.board.see(x, y) is not None:
                    print("该位置已经有子")
                    continue
                piece = input("请输入棋子名称:")

                piece = Piece(piece)
                position = Position(piece, player)
                game.board.put(x, y, position)
                game.player1.record(Action.put(x, y, position))
                break

            while action == "2":
                line = input("请输入原始坐标:")
                x1, y1 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                if game.board.see(x1, y1) is None:
                    print("该位置没有棋子")
                    continue

                line = input("请输入移动坐标:")
                x2, y2 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                if game.board.see(x2, y2) is not None:
                    print("该位置已经有子")
                    continue

                game.board.move(x1, y1, x2, y2)
                game.player1.record(Action.move(x1, x2, x2, y2))
                break

            while action == "3":
                if type == "go":
                    line = input("请输入坐标:")
                    x, y = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                    if game.board.see(x, y) is None:
                        print("该位置没有棋子")
                        continue
                    game.board.eat(x, y)
                    game.player1.record(Action.eat(x, y))
                if type == "chess":
                    line = input("请输入原始坐标:")
                    x1, y1 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                    if game.board.see(x1, y1) is None:
                        print("该位置没有棋子")
                        continue

                    line = input("请输入吃棋子坐标:")
                    x2, y2 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                    if game.board.see(x2, y2) is None:
                        print("该位置没有棋子")
                        continue

                    game.board.eat(x2, y2)
                    game.player1.record(Action.eat(x2, y2))

                    game.board.move(x1, y1, x2, y2)
                    game.player1.record(Action.move(x1, y1, x2, y2))
                    break

            while action == "4":
                line = input("请输入坐标:")
                x, y = list(map(lambda x: int(x.strip(" ")), line.split(",")))

                print("player: {}, 棋子:{}".format(game.board.see(x, y).player.name, game.board.see(x, y).piece.name))
                game.player1.record(Action.see(x, y))
                break


            while action == "5":
                print(game.board.nums())
                game.player1.record(Action.nums())
                break

        if player == player2:
            while action == "1":
                line = input("请输入坐标:")
                x, y = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                if game.board.see(x, y) is not None:
                    print("该位置已经有子")
                    continue
                piece = input("请输入棋子名称:")

                piece = Piece(piece)
                position = Position(piece, player)
                game.board.put(x, y, position)
                game.player2.record(Action.put(x, y, position))
                break

            while action == "2":
                line = input("请输入原始坐标:")
                x1, y1 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                if game.board.see(x1, y1) is None:
                    print("该位置没有棋子")
                    continue

                line = input("请输入移动坐标:")
                x2, y2 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                if game.board.see(x2, y2) is not None:
                    print("该位置已经有子")
                    continue

                game.board.move(x1, y1, x2, y2)
                game.player2.record(Action.move(x1, x2, x2, y2))
                break

            while action == "3":
                if type == "go":
                    line = input("请输入坐标:")
                    x, y = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                    if game.board.see(x, y) is None:
                        print("该位置没有棋子")
                        continue
                    game.board.eat(x, y)
                    game.player2.record(Action.eat(x, y))
                if type == "chess":
                    line = input("请输入原始坐标:")
                    x1, y1 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                    if game.board.see(x1, y1) is None:
                        print("该位置没有棋子")
                        continue

                    line = input("请输入吃棋子坐标:")
                    x2, y2 = list(map(lambda x: int(x.strip(" ")), line.split(",")))
                    if game.board.see(x2, y2) is None:
                        print("该位置没有棋子")
                        continue

                    game.board.eat(x2, y2)
                    game.player2.record(Action.eat(x2, y2))

                    game.board.move(x1, y1, x2, y2)
                    game.player2.record(Action.move(x1, y1, x2, y2))
                break

            while action == "4":
                line = input("请输入坐标:")
                x, y = list(map(lambda x: int(x.strip(" ")), line.split(",")))

                print("player: {}, 棋子:{}".format(game.board.see(x, y).player.name, game.board.see(x, y).piece.name))
                game.player2.record(Action.see(x, y))
                break

            while action == "5":
                print(game.board.nums())
                game.player2.record(Action.nums())
                break

        end = input("如果想结束，请输入 end，否则输入任何其他字符按回车继续\n")

        if end == "end":
            break
        player = player1 if player == player2 else player2

    game.print_history()

if __name__ == '__main__':
    main()
