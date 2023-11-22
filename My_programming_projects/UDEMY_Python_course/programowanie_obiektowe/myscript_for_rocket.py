from rocket_udemy import RocketBoard, Rocket

board = RocketBoard()


print(RocketBoard.get_distance(board[0], board[1]))

print(len(board))
print(board.get_amount_of_rockets())

# for rocket in board:
#     print(rocket.id)

board.show_id_of_rockets()
