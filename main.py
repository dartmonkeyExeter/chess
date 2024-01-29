# chess pygame.py

import pygame
import chess
import stockfish as sf
import cv2 as cv

# INTIIALIZATION
pygame.init()
clock = pygame.time.Clock()
fps = 60
width = 1200
height = 800
window = pygame.display.set_mode((width, height))
board = chess.Board()

running = True

to_file_dict = {'P': 'BlackPawn.png', 'R': 'BlackRook.png', 'N': 'BlackKnight.png', 'B': 'BlackBishop.png', 'Q': 'BlackQueen.png', 'K': 'BlackKing.png', 'p': 'WhitePawn.png', 'r': 'WhiteRook.png', 'n': 'WhiteKnight.png', 'b': 'WhiteBishop.png', 'q': 'WhiteQueen.png', 'k': 'WhiteKing.png'}

def draw_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(window, (150, 77, 34), (i * 60, j * 60, 60, 60))
            else:
                pygame.draw.rect(window, (238, 220, 151), (i * 60, j * 60, 60, 60))
                

def draw_pieces():
    for i in range(8):
        for j in range(8):
            if board.piece_at(i * 8 + j) != None:
                piece = board.piece_at(i * 8 + j).symbol()
                piece = to_file_dict[piece]
                img = pygame.image.load(f'C:/Users/aaronhampson/Downloads/chess pygame/pieces/{piece}')
                window.blit(img, (j * 60, i * 60))

def piece_select(x, y):
    x = x // 60
    y = y // 60

    return chr(97 + x) + str(8 - y)

def draw_legal_moves(piece):
    legal = board.legal_moves
    cur_legal_moves = []
    legal = list(legal)
    for i in range(len(legal)):
        if str(legal[i])[0:2] == str(piece):
            pygame.draw.circle(window, (190, 190, 200), ((ord(str(legal[i])[2]) - 97) * 60 + 30, 420 - (int(str(legal[i])[3]) - 1) * 60 + 30), 10)
            cur_legal_moves.append(str(legal[i]))

# main loop!!!

piece = None

while running:
    print(piece)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            piece = piece_select(x, y)

    draw_board()
    draw_pieces()
    if piece:
        draw_legal_moves(piece)
    pygame.display.update()

pygame.quit()
