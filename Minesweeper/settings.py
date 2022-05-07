global WIDTH
global HEIGHT
global ROWS
global COLS
global MINES
global FRAME_WIDTH
global FRAME_HEIGHT

WIDTH = 1440
HEIGHT = 720
ROWS = 10
COLS = 14
MINES = .1
FRAME_WIDTH = 340
FRAME_HEIGHT = 336
TOOLBAR_HEIGHT = 74

def apply(mines,rows,cols):
    global WIDTH
    global HEIGHT
    global ROWS
    global COLS
    global MINES
    MINES = mines/100
    ROWS = rows
    COLS = cols
    print(ROWS, COLS, MINES)

def frame_change():
    global FRAME_WIDTH
    global FRAME_HEIGHT
    global ROWS
    global COLS
    C = float(12.15)
    B = float(26.2)
    if int(COLS * 2 * C) > 340: #340 == min width for toolbar
        FRAME_WIDTH = int(COLS * 2 * C)
    else:
        FRAME_WIDTH = 340
    FRAME_HEIGHT = int(ROWS * B + TOOLBAR_HEIGHT)
