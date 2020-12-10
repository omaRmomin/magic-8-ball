# Started   - 25/11/2020
# Completed - 27/11/2020
# @author   - OMAR REHAN MOMIN

from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('MAGIC 8 BALL')
root.iconbitmap('8ball.ico')

bgcolor = '#101010'
root['bg'] = bg_color

img = ImageTk.PhotoImage( Image.open('8ball.ico') )
imglabel = Label( image = img, bg = '#202020' ).pack()

title = Label( text = 'MAGIC 8 BALL', font = ( 'fixedsys', 35, 'bold' ), fg = 'royalblue', bg = bg_color ).pack( pady = ( 10, 40 ) )

answers = ['It is certain','It is decidedly so','without a doubt','yes,definitely','you may rely on it','as I see it, yes','most likely','outlook good','yes',
           'better not tell you now','cannot predict now','contentrate and ask again','dont count on it','my sources say no','outlook not so good','very doubtful',
           'sign points to yes','reply hazy, try again','ask again later','my reply is no']

def answer():
    response = question.get() + '\n :' + answers[ random.randint( 0, len( answers ) - 1 )]
    displayed_response.configure( text = response )
    question.delete( 0, END )
    
ask_label = Label( root, text = 'Ask the Magic 8 Ball a question:', font = ( 'crystal', 12 ), fg = 'aqua', bg = bg_color ).pack( padx = '30' )

question = Entry( root, fg = 'white', bg = '#303030' )
question.pack( fill = 'x', expand = 'True' )

enter_button = Button( root, text = 'Enter',fg = 'aqua', bg = bg_color, font = ( 'crystal', 10 ), command = answer ).pack()

displayed_response = Label( root, text = ' ', fg = 'deepskyblue', bg = bg_color, font = ( 'crystal', 11 ) )
displayed_response.pack( pady = ( 10, 0 ) )

root.mainloop()
