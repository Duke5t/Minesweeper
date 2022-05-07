from tkinter import *
from PIL import ImageTk, Image
from cell import Cell
from window import Window
import settings
import utils


def refresh(location):
    location.destroy()
    Cell.all_cells = []
    Cell.pressed_btn_list = []
    Cell.images = []
    settings.frame_change()
    main()

def main():
    root = Tk()
    root.configure(bg='grey')
    root.geometry(f'{settings.FRAME_WIDTH}x{settings.FRAME_HEIGHT}')
    root.title("Minesweeper")
    root.resizable(True, True)

    mine_img_path = 'C:/Users/Spencer/.atom/Code/Minesweeper/images/mine.ico'
    mine_img = Image.open(mine_img_path)
    mine_img = mine_img.resize((18, 18), Image.ANTIALIAS)
    mine_img = ImageTk.PhotoImage(mine_img)

    smiley_img_path = 'C:/Users/Spencer/.atom/Code/Minesweeper/images/smiley.png'
    smiley_img = Image.open(smiley_img_path)
    smiley_img = smiley_img.resize((18, 18), Image.ANTIALIAS)
    smiley_img = ImageTk.PhotoImage(smiley_img)

    flag_img_path = 'C:/Users/Spencer/.atom/Code/Minesweeper/images/flag.png'
    flag_img = Image.open(flag_img_path)
    flag_img = flag_img.resize((18, 18), Image.ANTIALIAS)
    flag_img = ImageTk.PhotoImage(flag_img)

    top_frame = Frame(root, bg = '#f0f0f0',
                    bd = 2,
                    width = utils.width_pct(100),
                    height = utils.height_pct(10))
    top_frame.place(x = 0, y = 0)

    no_mines_scale_value = IntVar()
    no_mines_scale = Scale(top_frame, label = 'Mines %',
                    from_= 5, to_=90, variable=no_mines_scale_value,
                    orient=HORIZONTAL, length = 75)
    no_mines_scale.grid(row=0, column=1)
    no_mines_scale.set(settings.MINES*100)

    rows_scale_value = IntVar()
    rows_scale = Scale(top_frame, label = 'Rows',
                    from_= 6, to_= 20, variable=rows_scale_value,
                    orient=HORIZONTAL, length = 75)
    rows_scale.grid(row=0,column=2)
    rows_scale.set(settings.ROWS)

    cols_scale_value = IntVar()
    cols_scale = Scale(top_frame, label = 'Columns',
                    from_= 6, to_= 20, variable=cols_scale_value,
                    orient=HORIZONTAL, length = 75)
    cols_scale.grid(row=0, column=3)
    cols_scale.set(settings.COLS)

    apply_btn = Button(top_frame, text = 'Apply',
                    command = lambda: settings.apply(
                                no_mines_scale_value.get(),
                                rows_scale_value.get(),
                                cols_scale_value.get()),
                                pady = 22
                        )
    apply_btn.grid(row=0, column=4, ipadx=1)

    #change to refresh mainloop()
    new_game_btn = Button(top_frame, text = 'New \n Game ',
                    command = lambda: refresh(root), pady=15)

    new_game_btn.grid(row=0, column=0, ipadx=1)

    bottom_frame = Frame(root, bg = 'grey',
                    bd = 2,
                    width = utils.width_pct(100),
                    height = utils.height_pct(90))
    bottom_frame.place(x = utils.width_pct(0), y = utils.height_pct(10))

    Cell.get_images(mine_img, smiley_img, flag_img)

    for x in range(settings.COLS):
        for y in range(settings.ROWS):
            c = Cell(x, y)
            c.create_btn_obj(bottom_frame)
            c.cell_btn_obj.grid(column = x, row = y)

    Cell.randomize_mines()

    root.mainloop()

if __name__ == '__main__':
    main()
