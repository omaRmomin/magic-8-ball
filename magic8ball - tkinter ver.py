#time taken to finish : 25/11/2020 - 27/11/2020
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('MAGIC 8 BALL')
root.iconbitmap('8ball.ico')

bgcolor = '#101010'
root['bg'] = bgcolor

img = ImageTk.PhotoImage( Image.open('8ball.ico') )
imglabel = Label( image = img, bg = '#202020' ).pack()

title = Label( text = 'MAGIC 8 BALL', font = ( 'fixedsys', 35, 'bold' ),
      fg = 'royalblue', bg = bgcolor ).pack( pady = ( 10, 40 ) )

answers = ['It is certain','It is decidedly so','without a doubt','yes,definitely','you may rely on it','as I see it, yes','most likely','outlook good','yes',
           'better not tell you now','cannot predict now','contentrate and ask again','dont count on it','my sources say no','outlook not so good','very doubtful',
           'sign points to yes','reply hazy, try again','ask again later','my reply is no']

def answer():
    random_answer = answers[ random.randint( 0, len(answers) - 1 ) ]
    response = question.get() + '\n :' + random_answer
    displayed_response.configure( text = response )
    
    question.delete( 0, END )
    
display = Label( root, text = 'Ask the Magic 8 Ball a question:', font = ( 'crystal', 12 ),
                fg = 'aqua', bg = bgcolor ).pack( padx = '30' )

question = Entry( root, fg = 'white', bg = '#303030' )
question.pack( fill = 'x', expand = 'True' )

enter = Button( root, text = 'Enter',fg = 'aqua', bg = bgcolor,
               font = ( 'crystal', 10 ), command = answer ).pack()

displayed_response = Label( root, text = ' ', fg = 'deepskyblue', bg = bgcolor, font = ( 'crystal', 10 ) )
displayed_response.pack( pady = ( 10, 0 ) )

root.mainloop()
