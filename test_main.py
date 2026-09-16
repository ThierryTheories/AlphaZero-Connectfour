import pytest

from main import create_board, apply_move, legal_moves, is_win, is_draw


def test_create_board():
    board = create_board()

    assert len(board) == 6
    assert len(board[0]) == 7

    for row in board:
        for cell in row:
            assert cell == " "


def test_apply_move():
    board = create_board()

    row = apply_move(board, 3, "X")

    assert row == 5
    assert board[5][3] == "X"


def test_apply_move_stacking():
    board = create_board()

    row1 = apply_move(board, 3, "X")
    row2 = apply_move(board, 3, "O")
    row3 = apply_move(board, 3, "X")

    assert row1 == 5
    assert row2 == 4
    assert row3 == 3

    assert board[5][3] == "X"
    assert board[4][3] == "O"
    assert board[3][3] == "X"


def test_legal_moves():
    board = create_board()

    assert legal_moves(board) == [0, 1, 2, 3, 4, 5, 6]


def test_full_column_not_legal():
    board = create_board()

    for _ in range(6):
        apply_move(board, 3, "X")

    assert 3 not in legal_moves(board)


def test_apply_move_full_column_raises():
    board = create_board()

    for _ in range(6):
        apply_move(board, 3, "X")

    with pytest.raises(ValueError):
        apply_move(board, 3, "O")


def test_horizontal_win():
    board = create_board()

    row = None

    for column in range(4):
        row = apply_move(board, column, "X")

    assert is_win(board, row, 3)


def test_vertical_win():
    board = create_board()

    row = None

    for _ in range(4):
        row = apply_move(board, 3, "X")

    assert is_win(board, row, 3)


def test_diagonal_down_right_win():
    board = create_board()

    apply_move(board, 0, "X")

    apply_move(board, 1, "O")
    row = apply_move(board, 1, "X")

    apply_move(board, 2, "O")
    apply_move(board, 2, "O")
    row = apply_move(board, 2, "X")

    apply_move(board, 3, "O")
    apply_move(board, 3, "O")
    apply_move(board, 3, "O")
    row = apply_move(board, 3, "X")

    assert is_win(board, row, 3)


def test_diagonal_up_right_win():
    board = create_board()

    apply_move(board, 3, "X")

    apply_move(board, 2, "O")
    row = apply_move(board, 2, "X")

    apply_move(board, 1, "O")
    apply_move(board, 1, "O")
    row = apply_move(board, 1, "X")

    apply_move(board, 0, "O")
    apply_move(board, 0, "O")
    apply_move(board, 0, "O")
    row = apply_move(board, 0, "X")

    assert is_win(board, row, 0)


def test_three_in_a_row_is_not_win():
    board = create_board()

    row = None

    for column in range(3):
        row = apply_move(board, column, "X")

    assert not is_win(board, row, 2)


def test_mixed_pieces_are_not_win():
    board = create_board()

    apply_move(board, 0, "X")
    apply_move(board, 1, "X")
    apply_move(board, 2, "O")
    row = apply_move(board, 3, "X")

    assert not is_win(board, row, 3)


def test_last_piece_in_middle_of_line():
    board = create_board()

    apply_move(board, 0, "X")
    apply_move(board, 2, "X")
    apply_move(board, 3, "X")

    row = apply_move(board, 1, "X")

    assert is_win(board, row, 1)

def test_not_draw():
    board = create_board()
    assert not is_draw(board)

def test_draw():
    board = [
        ["O", "X", "X", "O", "O", "X", "O"],
        ["X", "O", "X", "X", "O", "X", "X"],
        ["X", "O", "O", "O", "X", "X", "X"],
        ["O", "O", "X", "X", "O", "O", "X"],
        ["O", "X", "O", "O", "X", "X", "O"],
        ["X", "O", "O", "O", "X", "O", "X"],
    ]

    assert is_draw(board)