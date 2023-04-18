from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count_label = None
    cell_count = settings.CELL_COUNT
    def __init__(self,x,y, is_mine = False, is_open = False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        self.is_open = is_open

        #append the object to the Cell.all list
        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object=btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text = f"Cells left: {Cell.cell_count}",
            width=12,
            height=4,
            bg = 'black',
            fg = 'white',
            font=('arial', 30)
            )
        Cell.cell_count_label = lbl

    def left_click_action(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length==0:
                for cell_obj in self.surrouned_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If mines count is equal to the cells left count, player won !
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations ! You won the game :)', 'Game Over',0)
        
        # Cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def show_mine(self):
        self.cell_btn_object.configure(bg = 'yellow')
        # A logic to interrupt the game and display a message that player is lost!
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over',0)
        sys.exit()


    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property     
    def surrouned_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1,self.y-1),
            self.get_cell_by_axis(self.x -1,self.y),
            self.get_cell_by_axis(self.x -1,self.y+1),
            self.get_cell_by_axis(self.x ,self.y-1),
            self.get_cell_by_axis(self.x +1,self.y-1),
            self.get_cell_by_axis(self.x +1,self.y),
            self.get_cell_by_axis(self.x +1,self.y+1),
            self.get_cell_by_axis(self.x ,self.y+1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrouned_cells:
            if cell.is_mine:
                counter += 1

        return  counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mine_length)
            # Replace the text with cell count label wih newer count
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(
                    text = f"Cells left: {Cell.cell_count}"
                )
            self.cell_btn_object.configure(bg = 'SystemButtonFace')

        #Mark the cell as opened
        self.is_open = True

        


    def right_click_action(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg = 'orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg = 'SystemButtonFace')
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    
