# implementation of card game - Memory

import simpleguitk as simplegui
import random
card_deck1 =  [0,1,2,3,4,5,6,7]
card_deck2 =  [0,1,2,3,4,5,6,7]
card_deck = card_deck1 + card_deck2
random.shuffle(card_deck)
cardup_pos = 0
carddown_pos = []
y = range (16)
exposed = 16*[False]



  

# helper function to initialize globals
for x in y:
    if x < 16:
        carddown_pos.append([[x * 50 + 25, 0],[x * 50 + 25, 100]])
   
                       

def new_game():
    pass  

   
# define event handlers
def mouseclick(pos):
    global click, exposed
    # add game state logic here
    click = pos[0] // 50
    for x in y:
        if click == x:
            exposed.pop(x)
            exposed.insert(x,True)
          

                         
# cards are logically 50x100 pixels in size    
def draw(canvas):
    z = 0
    cardup_pos = -40
    for x in range(len(card_deck)):
        cardup_pos += 50
        if exposed[x] == True:
            canvas.draw_text(str(card_deck[x]), [cardup_pos,70] , 50, 'White')
        elif exposed[x] == False:  
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