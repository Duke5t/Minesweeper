from tkinter import Button
import settings
import utils
import random

class Cell:
    all_cells = []
    pressed_btn_list = []
    images = []
    colour = {1 : "blue", 2 : "green",
            3 : "brown", 4 : "purple",
            5 : "red", 6 : "pink"}

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y
        Cell.all_cells.append(self)

    def create_btn_obj(self, location):
            btn = Button(
                location,
                bg= '#f0f0f0',
                width = 2,
                height = 1,
            )
            btn.bind('<Button-1>', self.left_click_actions)
            btn.bind('<Button-3>', self.right_click_actions)
            self.cell_btn_obj = btn

    def left_click_actions(self, event):
        if self.cell_btn_obj['state'] == 'disabled':
            return
        if self.is_mine:
            self.show_mine()
            #Add Function To End Game
        else:
            self.show_number()
        #If all_cells squares without mines are pressed
        if ((settings.ROWS * settings.COLS)-int(len(Cell.all_cells)*settings.MINES)) == len(list(set(Cell.pressed_btn_list))):
            #trigger end game
            self.end_game()

    def right_click_actions(self, event):
        self.create_flag()

    def create_flag(self):
        if self not in Cell.pressed_btn_list:
            if self.cell_btn_obj['state'] == 'normal':
                #SET FLAG IMG
                self.cell_btn_obj.config(image = Cell.images[2],
                                    width = 18, height = 18,
                                    state='disabled')
            elif self.cell_btn_obj['state'] == 'disabled':
                self.cell_btn_obj.config(image = '',
                                        width = 2, height = 1,
                                        bg= '#f0f0f0',
                                        state='normal')
        else:
            pass
    def show_mine(self):
        for x in Cell.all_cells:
            if x.is_mine == True:
                x.cell_btn_obj.config(image=Cell.images[0],
                                    width = 18, height = 18,
                                    bg = 'red')
            x.cell_btn_obj.config(state = 'disabled')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell

    @property #read-only method
    def surrounding_cells(self):
        cells = []
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                if 0 <= x < settings.COLS and 0 <= y < settings.ROWS:
                    cells.append(self.get_cell_by_axis(x,y))
        return cells

    @property #read-only method
    def count_surrounding_mines(self):
        count = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                count += 1
        return count

    def show_number(self):
        if self.count_surrounding_mines == 0:
            self.cascade()
        else:
            self.cell_btn_obj.config(
                        text=self.count_surrounding_mines,
                        fg = Cell.colour.get(self.count_surrounding_mines),
                        )
            Cell.pressed_btn_list.append(self)

    def cascade(self):
        if self not in Cell.pressed_btn_list:
            Cell.pressed_btn_list.append(self)
            self.cell_btn_obj.config(
                        text=self.count_surrounding_mines,
                        fg = Cell.colour.get(self.count_surrounding_mines),
                        )
            for cell in self.surrounding_cells:
                cell.show_number()

    def __repr__(self):
        return f"Cell({self.x},{self.y})"

    def get_images(a, b, c):
        Cell.images.append(a)
        Cell.images.append(b)
        Cell.images.append(c)

    
    @staticmethod #non class-specific method
    def randomize_mines():
        cells_add_mines = random.sample(
                Cell.all_cells, int(len(Cell.all_cells)*settings.MINES)
                )
        for x in cells_add_mines:
            x.is_mine = True

    def end_game(self):
        for x in Cell.all_cells:
            if x.is_mine == True:
                x.cell_btn_obj.config(image = Cell.images[1],
                                    width = 18, height = 18)
            x.cell_btn_obj.config(state = 'disabled')
