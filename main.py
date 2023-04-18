from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
# Override the settings of the window

root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False,False)
root.title('Minesweeper Game')

top_frame = Frame(
    root,
    bg = 'black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)

top_frame.place(x = 0, y = 0)

game_title = Label(
    top_frame,
    bg = 'black',
    fg = 'white',
    text='Minesweeper Game',
    font=('arial', 48)
)

game_title.place(x = utils.width_prct(25), y =0)

left_frame = Frame(
    root,
    bg = 'black',
    height=utils.height_prct(75),
    width=utils.width_prct(25)
)

left_frame.place(x = 0, y= utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(x = utils.width_prct(25), y = utils.height_prct(25))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,row=y
        )

#Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(
    x=0,
    y=0
)

Cell.randomize_mines()
#Run the window
root.mainloop()