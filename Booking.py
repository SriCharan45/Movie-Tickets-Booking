import tkinter as tk
import tkinter.ttk

Screens = ["Screen 1" , "Screen 2" , "Screen 3" , "Screen 4" , "Screen 5" , "Screen 6"]

Movies = {"Action" : ["RRR" , "Bharath Ane Nenu" , "Aravinda Sametha Veera Raghava" , "Vakeel Saab" , "Ala Vaikuntapuramulo"],
          "Horror" : ["Chandramukhi" , "Muni" , "Kanchana" , "Ganga" , "Nagavalli" , "Masooda"],
          "Comedy"  : ["RRR" , "Bharath Ane Nenu" , "Aravinda Sametha Veera Raghava" , "Vakeel Saab" , "Ala Vaikuntapuramulo"],
          "Romance" : ["RRR" , "Bharath Ane Nenu" , "Aravinda Sametha Veera Raghava" , "Vakeel Saab" , "Ala Vaikuntapuramulo"],
          "Sci-Fi" : ["RRR" , "Bharath Ane Nenu" , "Aravinda Sametha Veera Raghava" , "Vakeel Saab" , "Ala Vaikuntapuramulo"]
        }

times = ["10:00" , "10:30" , "11:00" , "11:30" , "12:00" , "12:30" , "1:00" , "1:30" , "2:00" , "2:30" , "3:00" , "3:30" , "4:00" , "4:30"]

Seats = []
Selected_Seats = []

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Movie Booking")
        self.creatWidgets()

    def updateMovies(self , event = None):
        self.movieCombo['values'] = Movies[self.generCombo.get()]

    def creatWidgets(self):
        headingLabel = tk.Label(self , text = "Cinema Seats Booking" , font = "Aries 12 bold")
        headingLabel.grid(row = 0 , column = 0 , columnspan = 5 , padx = 10 , pady = 10 , sticky = "w")
        tkinter.ttk.Separator(self , orient = "horizontal").grid(row = 1 , column = 0 , columnspan = 5 , sticky = 'ew')

        day = tk.Frame(self)
        tk.Label(day , text = "_________").pack()
        tk.Label(day , text = "Today" , font = "Aries 10 underline").pack()
        tk.Label(day , text = "").pack()
        day.grid(row = 2 , column = 0 , padx = 10)
        tk.Label(self , text = "Genre :").grid(row = 2 , column = 1 , padx = (10,0))
        self.generCombo = tkinter.ttk.Combobox(self , width = 15 , values = list(Movies.keys()) , state = "readonly")
        self.generCombo.set("Select Genre")
        self.generCombo.bind('<<ComboboxSelected>>' , self.updateMovies)
        self.generCombo.grid(row = 2 , column = 2)

        tk.Label(self , text = "Movie :").grid(row = 2 , column = 3 , padx = (10,0))
        self.movieCombo = tkinter.ttk.Combobox(width = 15 , state = "readonly")
        self.movieCombo.bind('<<ComboboxSelected>>' , self.createTimeButtons)
        self.movieCombo.set("Select Movie")
        self.movieCombo.grid(row = 2 , column = 4 , padx = (10,0))
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky="ew")

    def createTimeButtons(self , event = None):
        tk.Label(self , text = "Select Time Slot" , font = "Aries 11 bold underline").grid(row = 4 , column = 2 , columnspan = 2 , pady = 5)
        Time = tk.Frame(self)
        Time.grid(row=5 , column=0 , columnspan=5)
        for i in range(14):
            tk.Button(Time , text = times[i] , command = self.seatSelection).grid(row = 4+i//7 , column = i%7)

    def seatSelection(self):
        window = tk.Toplevel()
        window.title("Select Your Seat(s)")
        checkoutHeading = tk.Label(window , text = "Seat(s) Selection" , font =  "Aries 12")
        checkoutHeading.grid(row = 0 , column = 0 , columnspan = 5 , padx = 10 , pady = (10,0) , sticky = "w")

        infer = tk.Frame(window)
        infer.grid(row = 1 , column = 0)
        tk.Label(infer , text = "BLUE = SELECTED" , fg = 'blue').grid(row = 0 , column = 0 , padx = 10)
        tk.Label(infer , text = "RED = BOOKED" , fg = 'brown').grid(row = 0 , column = 1 , padx = 10)
        tk.Label(infer , text = "GREEN = AVAILABLE" , fg = 'green').grid(row = 0 , column = 2 , padx = 10)
        tkinter.ttk.Separator(window, orient="horizontal").grid(row=2, column=0, pady=(0,5), sticky="ew")

        w = tk.Canvas(window , width = 500 , height = 15)
        w.create_rectangle(10 , 0 , 490 , 10 , fil = 'black')
        w.grid(row = 3 , column = 0)
        tk.Label(window , text = "SCREEN").grid(row = 4 , column = 0 , pady = (0,10))
        seats = tk.Frame(window)
        seats.grid(row = 5 , column = 0)
        Seats.clear()
        Selected_Seats.clear()
        for i in range(4):
            temp = []
            for j in range(15):
                but = tk.Button(seats , bd = 2 , bg = 'Green' , activebackground = 'forestGreen' , command=lambda x = i , y = j: self.selected(x ,y))
                temp.append(but)
                but.grid(row = i , column = j , padx = 5 , pady = 5)
            Seats.append(temp)
        tk.Button(window , text = "Book Seats" , bg = 'black' , fg = 'white' , command = self.bookseat).grid(row = 6 , column = 0 , pady = 10)

    def selected(self , i ,j):
        if Seats[i][j]['bg'] == "blue":
            Seats[i][j]['bg'] == "green"
            Seats[i][j]['activebackground'] = "forestGreen"
            Seats.remove((i,j))
            return 
        Seats[i][j]['bg'] = 'blue'
        Seats[i][j]['activebackground'] = 'blue'
        Selected_Seats.append((i,j))

    def bookseat(self):
        for i in Selected_Seats:
            Seats[i[0]][i[1]]['bg'] = 'brown'
            Seats[i[0]][i[1]]['activebackground'] = 'brown'
            Seats[i[0]][i[1]]['relief'] = 'sunken'
app = Application()
app.mainloop()