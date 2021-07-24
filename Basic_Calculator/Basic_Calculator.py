from tkinter import *

window = Tk()   # created a basic window
window.geometry( "500x500" )   # it is to set the measure of the basic window
window.title( "Basic Calculator" ) # created title
window.configure( background= "grey" )  # to determine the color

input_text = StringVar   # this is to receive input
input_frame = Frame( window, background= "#4374ab", width= 500, height= 50 ) # frame created for input_frame
input_frame.pack( side= TOP )

# now let's create an input field
input_field = Entry( input_frame, width= 500, font= ('arial', 18, 'bold'), textvariable= input_text, justify= RIGHT,
 bd= 0, bg= "black" )
input_field.pack( ipady= 10 )    # ipady is internal padding to increase the height of input field





window.mainloop()