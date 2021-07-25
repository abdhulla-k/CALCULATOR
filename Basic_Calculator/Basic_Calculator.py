from tkinter import *


# Now let's create methods

expression = ""

def clear():       # it is the method of 'clear' button.
    global expression
    expression = ""
    input_text.set( "" )


def equal():
	try:

		global expression# eval function parses the expression argument and evaluates it as a 
        # python expression. In simple words, the eval function evaluates the “String” like a python expression and returns
        #  the result as an integer.

		result = str(eval(expression))

		input_text.set(result)

		expression = ""

	except:

		input_text.set(" error ")
		expression = ""


def scan( self ):    # int is the selection metnod.this function continuously updates the input whenever enters a number
    global expression
    expression = expression + str( self )
    input_text.set( expression )


window = Tk()   # created a basic window
window.geometry( "350x159" )   # it is to set the measure of the basic window
window.title( "Basic Calculator" ) # created title
window.configure( background= "grey" )  # to determine the color


input_text = StringVar()   # this is to receive input
# now let's create an input field
input_field = Entry( window, width= 16, font= ('arial', 18, 'bold'), textvariable= input_text,
 bd= 0, bg= "white" )
input_field.grid( ipadx= 70, columnspan= 4 )    # ipady is internal padding to increase the height of input field


# create buttons


One = Button( window, text= "1", fg= 'black', bg= 'red', command= lambda: scan(1), height= 1, width= 7 )
One.grid( row= 2, column= 0 )

Two = Button( window, text= "2", fg= 'black', bg= 'red', command= lambda: scan(2), height= 1, width= 7 )
Two.grid( row= 2, column= 1 )

Three = Button( window, text= "3", fg= 'black', bg= 'red', command= lambda: scan(3), height= 1, width= 7 )
Three.grid( row= 2, column= 2 )

For = Button( window, text= "4", fg= 'black', bg= 'red', command= lambda: scan(4), height= 1, width= 7 )
For.grid( row= 3, column= 0 )

Five = Button( window, text= "5", fg= 'black', bg= 'red', command= lambda: scan(5), height= 1, width= 7 )
Five.grid( row= 3, column= 1 )

Six = Button( window, text= "6", fg= 'black', bg= 'red', command= lambda: scan(6), height= 1, width= 7 )
Six.grid( row= 3, column= 2 )

Seven = Button( window, text= "7", fg= 'black', bg= 'red', command= lambda: scan(7), height= 1, width= 7 )
Seven.grid( row= 4, column= 0 )

Eight = Button( window, text= "8", fg= 'black', bg= 'red', command= lambda: scan(8), height= 1, width= 7 )
Eight.grid( row= 4, column= 1 )

Nine = Button( window, text= "9", fg= 'black', bg= 'red', command= lambda: scan(9), height= 1, width= 7 )
Nine.grid( row= 4, column= 2 )

Zero = Button( window, text= "0", fg= 'black', bg= 'red', command= lambda: scan(0), height= 1, width= 7 )
Zero.grid( row= 5, column= 0 )

Decimal = Button( window, text= ".", fg= 'black', bg= 'red', command= lambda: scan('.'), height= 1, width= 7 )
Decimal.grid( row= 5, column= 1 )

Clear = Button( window, text= "C", fg= 'black', bg= 'red', command= clear, height= 1, width= 7 )
Clear.grid( row= 5, column= 2 )

Pluss = Button( window, text= "+", fg= 'black', bg= 'red', command= lambda: scan("+"), height= 1, width= 7 )
Pluss.grid( row= 2, column= 3 )

Miness = Button( window, text= "-", fg= 'black', bg= 'red', command= lambda: scan("-"), height= 1, width= 7 )
Miness.grid( row= 2, column= 3)

Multiple = Button( window, text= "*", fg= 'black', bg= 'red', command= lambda: scan("*"), height= 1, width= 7 )
Miness.grid( row= 3, column= 3 )

Devide = Button( window, text= "/", fg= 'black', bg= 'red', command= lambda: scan("/"), height= 1, width= 7 )
Devide.grid( row= 4, column= 3)

Equalto = Button( window, text= "=", fg= 'black', bg= 'red', command= equal, height= 1, width= 7 )
Equalto.grid( row= 5, column= 3 )



window.mainloop()