from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
root = Tk()
root.resizable(False, False)
root.geometry('310x450')
root.configure(bg='white')
MainBoard = [["" for i in range(9)]for j in range(9)]
for row in range(9):
    for col in range(9):
        MainBoard[row][col] = StringVar(root)

class SudokuGenerator:
# This is the place where the main thing happens!!!

  def __init__(self , diffLevel):
    self.numberList=[1,2,3,4,5,6,7,8,9]

    #we use genBoard to do the generation calculations 
    #genBoard and MainBoard are related in convertBoardsGenToMain()
    self.genBoard = [[0 for i in range(9)]for j in range(9)]
    
    self.generateBoard()

    #after generating a full Sudoku now we erase some of them to match our desired difficulty level
    self.boardDiff(diffLevel)
    
    #convert genBoard to MainBoard
    self.convertBoardsGenToMain()
 
  def generateBoard(self):
    # We use this func to create our sudoku with backtracking algorithm
    for i in range(0,81):
      row=i//9
      col=i%9
      if self.genBoard[row][col]==0:
        random.shuffle(self.numberList)      
        for value in self.numberList:
          if self.isValid(row,col,value):
            self.genBoard[row][col]=value
            if self.checkBoard():
              return True
            else:
              if self.generateBoard():
                return True
        break
    self.genBoard[row][col]=0    
 
  def checkBoard(self):
    #We use this to see if we found a valid sudoku or not
    for row in range(0,9):
        for col in range(0,9):
          if self.genBoard[row][col]==0:
            return False # we haven't found one :(

    return True #we found on!!! :)
   
  def isValid(self, row, col, value):
      # we use this func to see if a chosen position is isValid or not
      if not (value in self.genBoard[row]): #check for row repetion
         tempBoard = list(zip(*self.genBoard))
         if not value in tempBoard[col]: #check for col repetion
              box = self.findBox(row,col)
              if not value in (box[0] + box[1] + box[2]): #check for box repetion
                return True
      return False
  
  def findBox(self, row, col):
    #We use this func to find out that which box  is our chosen position in?
    box=[]
    if row<3:
      if col<3:
        #top-left
        box=[self.genBoard[i][0:3] for i in range(0,3)]
      elif col<6:
        #top-mid
        box=[self.genBoard[i][3:6] for i in range(0,3)]
      else:  
        #top_right
        box=[self.genBoard[i][6:9] for i in range(0,3)]
    elif 2<row<6:
      if col<3:
        #mid-left
        box=[self.genBoard[i][0:3] for i in range(3,6)]
      elif col<6:
        #mid-mid
        box=[self.genBoard[i][3:6] for i in range(3,6)]
      else:  
        #mid-right
        box=[self.genBoard[i][6:9] for i in range(3,6)]
    else:
      if col<3:
        #buttom-left
        box=[self.genBoard[i][0:3] for i in range(6,9)]
      elif col<6:
        #buttom-mid
        box=[self.genBoard[i][3:6] for i in range(6,9)]
      else:  
        #buttom-right
        box=[self.genBoard[i][6:9] for i in range(6,9)]
    return box
 
  def boardDiff(self,i):
     #we use this func to set our desired difficulty with deleting cells from genBoard
     j=0
     while j < i.get():
        row = random.randint(0,8)
        col = random.randint(0,8)
        if self.genBoard[row][col] != 0:
           self.genBoard[row][col] = 0
           j += 1
              
  def convertBoardsGenToMain(self):
    #we convert genBoard to MainBoard to show on GUI
    for row in range(9):
       for col in range(9):
          MainBoard[row][col].set(str(self.genBoard[row][col]))
          if self.genBoard[row][col] ==0:
             MainBoard[row][col].set('')

class sudokuSolver:

  def __init__(self):
     self.numberList=[1,2,3,4,5,6,7,8,9]
     # we use solBoard to do the solving caluculations
     self.solBoard = [[0 for i in range(9)]for j in range(9)]
     
     self.convertBoardsMainToSol()

     self.Solver()

     self.convertBoardsGenToMain()
  
  def convertBoardsMainToSol(self):
    #we use this func to convert MainBoard to SolBoard
    for i in range(9):
      for j in range(9):
        if MainBoard[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
             MainBoard[i][j].set(0)
        self.solBoard[i][j] = int(MainBoard[i][j].get())
 
  def Solver(self):
    # main solving function using backtracking
    for i in range(0,81):
      row=i//9
      col=i%9
      if self.solBoard[row][col]==0:
        random.shuffle(self.numberList)      
        for value in self.numberList:
          if self.isValid(row,col,value):
            self.solBoard[row][col]=value
            if self.checkBoard():
              return True
            else:
              if self.Solver():
                return True
        break
    self.solBoard[row][col]=0  

  def convertBoardsGenToMain(self):
    for row in range(9):
       for col in range(9):
          MainBoard[row][col].set(str(self.solBoard[row][col]))
 
  def findBox(self, row, col):
    #We use this func to find out that which box  is our chosen position in?
    box=[]
    if row<3:
      if col<3:
        #top-left
        box=[self.solBoard[i][0:3] for i in range(0,3)]
      elif col<6:
        #top-mid
        box=[self.solBoard[i][3:6] for i in range(0,3)]
      else:  
        #top_right
        box=[self.solBoard[i][6:9] for i in range(0,3)]
    elif 2<row<6:
      if col<3:
        #mid-left
        box=[self.solBoard[i][0:3] for i in range(3,6)]
      elif col<6:
        #mid-mid
        box=[self.solBoard[i][3:6] for i in range(3,6)]
      else:  
        #mid-right
        box=[self.solBoard[i][6:9] for i in range(3,6)]
    else:
      if col<3:
        #buttom-left
        box=[self.solBoard[i][0:3] for i in range(6,9)]
      elif col<6:
        #buttom-mid
        box=[self.solBoard[i][3:6] for i in range(6,9)]
      else:  
        #buttom-right
        box=[self.solBoard[i][6:9] for i in range(6,9)]
    return box
 
  def isValid(self,row,col,value):
      # we use this func to see if a chosen position is isValid or not
      if not (value in self.solBoard[row]):
         tempBoard = list(zip(*self.solBoard))
         if not value in tempBoard[col]:
              box = self.findBox(row,col)
              if not value in (box[0] + box[1] + box[2]):
                return True
      return False
  
  def checkBoard(self):
    #We use this to see if we found a valid sudoku or not
    for row in range(0,9):
        for col in range(0,9):
          if self.solBoard[row][col]==0:
            return False
    return True 

class GUI:
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Game")
        self.newBoard()

        #------------------------
        #difficulty levels
        self.selected_option = IntVar()
        self.selected_option.set(-1)
        self.easyR = Radiobutton(root, text="Easy", value=30, font=('futura', 8), variable=self.selected_option)
        self.easyR.grid(column=0, row=19,columnspan=3)
        self.mediumR = Radiobutton(root, text="Medium", value=40, font=('futura', 8), variable=self.selected_option)
        self.mediumR.grid(column=3, row=19,columnspan=3)
        self.hardR = Radiobutton(root, text="Hard", value=50, font=('futura', 8), variable=self.selected_option)
        self.hardR.grid(column=6, row=19,columnspan=3)
        #-------------------------
        self.create = Button(root, width=27,height=3,text='Generate', font=('futura', 8), command=self.generate)
        self.create.grid(column=0,columnspan=5, row=20,rowspan=2)
        
        self.check = Button(root, width=21,height=3, text='Check', font=('futura', 8), command=self.Check)
        self.check.grid(column=5,columnspan=4, row=20,rowspan=2)
        
        self.solve = Button(root, width=21,height=3,text='Solve', font=('futura', 8), command=self.Solve)
        self.solve.grid(column=0,columnspan=4, row=22,rowspan=2)

        self.load = Button(root, width=27,height=3, text='Load', font=('futura', 8), command=self.Load)
        self.load.grid(column=4, columnspan=5,row=22,rowspan=2)
    
    
    # Board misaze to GUI
    def newBoard(self):
        self.board = [["" for i in range(9)]for j in range(9)]
        for row in range(9):
            for col in range(9):
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'grey'
                elif (row >= 3 and row < 6) and (col >= 3 and col < 6):
                    color = 'grey'
                else:
                    color = '#46cabb'

                self.board[row][col] = Entry(root, width=2, font=('Arial', 20), bg=color, borderwidth=0.5, fg='black',justify='center',
                                             textvariable=MainBoard[row][col])
                self.board[row][col].bind('<FocusIn>', self.gridChecker)
                self.board[row][col].grid(row=row, column=col)

    def generate(self):
        SudokuGenerator(self.selected_option)

    def Check(self):
        for row in range(9):
            for column in range(9):
                if MainBoard[row][column].get() == '':
                    return messagebox.showwarning("Error", "Each row and column \n needs to be filled out!")
                elif (int(MainBoard[row][column].get()) > 9) or (int(MainBoard[row][column].get()) < 0):
                    return messagebox.showwarning("Error", "Numbers must be in the range 1 to 9")

        for column in range(9):
            values = [MainBoard[row][column].get() for row in range(9) if MainBoard[row][column].get()]

            if len(set(values)) != len(values):
                return messagebox.showerror('loser', 'Nah, try again!')

        messagebox.showinfo("winner", "You won!")
        return
    

    def Solve(self):
        for row in range(9):
            for col in range(9):
                num = MainBoard[row][col].get()
                if num != '':
                    if self.check_duplicate(row, col, int(num)):
                        return messagebox.showerror("Error", "ROW and COLUMNS and GRIDS can't contain more than \n"
                                                             "one of the same numbers from one to nine!")
                    elif int(num) > 9 or int(num) < 0:
                        return messagebox.showerror("Error", "Numbers must be in the range 1 to 9!")
        i = True
        while i:
           sudokuSolver()
           for row in range(9):
              for col in range(9):
                if MainBoard[row][col].get() =="0":
                   MainBoard[row][col].set('')
                   i =False
        return messagebox.showinfo("attention","if it didn't work press solve another time")


    def Load(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                content = f.read()
                for row, line in enumerate(content.split("\n")):
                    for col, num in enumerate(line.split(",")):
                        MainBoard[row][col].set(num.strip())
            for row in range(9):
                for col in range(9):
                    num = MainBoard[row][col].get()
                    if num != '':
                        self.board[row][col].config(fg='black')
                        self.board[row][col].delete(0, END)
                        self.board[row][col].insert(0, num)
                    else:
                        self.board[row][col].config(fg='black')


    def check_duplicate(self, row, col, num):
        for i in range(9):
            if MainBoard[row][i].get() == str(num) and i != col:
                return True

        for i in range(9):
            if MainBoard[i][col].get() == str(num) and i != row:
                return True

        block_row = row // 3
        block_col = col // 3
        for i in range(block_row * 3, block_row * 3 + 3):
            for j in range(block_col * 3, block_col * 3 + 3):
                if MainBoard[i][j].get() == str(num) and (i != row or j != col):
                    return True

        return False

    def gridChecker(self,event):
      for row in range(9):
          for col in range(9):
              if MainBoard[row][col].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                  MainBoard[row][col].set('')

GUI(root)
root.mainloop()
