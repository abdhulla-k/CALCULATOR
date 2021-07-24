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


# Now let's create methods

expression = ""

def clear():       # it is the method of 'clear' button.
    global expression
    expression = ""
    input_text.set( "" )

def equal():      # it is for '=' button
    global expression
    expression = ""
    result = expression + str( eval( expression )) # eval function parses the expression argument and evaluates it as a 
    # python expression. In simple words, the eval function evaluates the “String” like a python expression and returns
    #  the result as an integer.
    input_text.set( result )

def scan( self ):    # int is the selection metnod.this function continuously updates the input whenever enters a number
    global expression
    expression = expression + str( self )
    input_text.set( expression )








window.mainloop()