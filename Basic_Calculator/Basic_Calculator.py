from tkinter import *

window = Tk()   # created a basic window
window.geometry( "500x500" )   # it is to set the measure of the basic window
window.title( "Basic Calculator" ) # created title
window.configure( background= "grey" )  # to determine the color

input_frame = StringVar   # this is to receive input
input_frame = Frame( window, background= "#4374ab", width= 500, height= 50 ) # frame created for input_frame
input_frame.pack()  




window.mainloop()