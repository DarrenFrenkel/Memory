# implementation of card game - Memory

import simpleguitk as simplegui
import random
card_deck1 =  [0,1,2,3,4,5,6,7]
card_deck2 =  [0,1,2,3,4,5,6,7]
card_deck = card_deck1 + card_deck2
random.shuffle(card_deck)
cardup_pos = [0,60]
carddown_pos = []
y = range (16)
exposed = []
 


  

# helper function to initialize globals
for x in y:
    if x < 16:
        carddown_pos.append([[x * 50 + 25, 0],[x * 50 + 25, 100]])
    if x % 2 == 0:
        exposed.append(True)
    else:
        exposed.append(False)
            

def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                         
# cards are logically 50x100 pixels in size    
def draw(canvas):
    z = 0
    cardup_pos[0] = 0
    for x in card_deck:
        canvas.draw_text(str(x),cardup_pos, 50, 'White')
        cardup_pos[0] += 50
    for x in exposed:
        if x == False:  
                canvas.draw_polygon(carddown_pos[z], 49, 'Green')
        z += 1 
 
# pass


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