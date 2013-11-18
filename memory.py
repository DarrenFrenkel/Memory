# implementation of card game - Memory

import simpleguitk as simplegui
import random

card_deck1 = [0,1,2,3,4,5,6,7]
card_deck2 = [0,1,2,3,4,5,6,7]
card_deck = card_deck1 + card_deck2 


print (card_deck)

print (card_deck1[7])
print (card_deck2[3])



# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric