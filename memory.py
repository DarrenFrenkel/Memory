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
state = 0
guess1 = 5000
guess2 = 5000
index1 = 5000
index2 = 5000
turns = 1

  

# helper function to initialize globals
for x in y:
    if x < 16:
        carddown_pos.append([[x * 50 + 25, 0],[x * 50 + 25, 100]])
   
            
           

def new_game():
    global turns
    turns = 0
    pass  


   
# define event handlers
def mouseclick(pos):
    global click, exposed, state,guess1, guess2, index1, index2, turns, hello
    click = pos[0] // 50
    if state == 0:
        for x in y:
            if click == x and exposed[x] == False:
                exposed.pop(x)
                exposed.insert(x,True)
                index1 = x                
                state = 1 
                guess1 = card_deck[click]
    elif state == 1:
        for x in y:
            if click == x and exposed[x] == False:
                exposed.pop(x)
                exposed.insert(x,True)
                index2 = x	                
                state = 2 
                guess2 = card_deck[click]    
    elif state == 2:
        if guess1 != guess2:
            exposed.pop(index1)
            exposed.insert(index1,False)
            exposed.pop(index2)
            exposed.insert(index2,False)
            turns += 1
            for x in y:
                if click == x and exposed[x] == False:
                    exposed.pop(x)
                    exposed.insert(x,True)
                    index1 = x
                    state = 1
                    guess1 = card_deck[click]   
        else:
            for x in y:
                if click == x and exposed[x] == False:
                    exposed.pop(x)
                    exposed.insert(x,True)
                    index1 = x
                    state = 1
                    guess1 = card_deck[click]
            
           

                         
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(turns))
    z = 0
    cardup_pos = -40
    for x in range(len(card_deck)):
        cardup_pos += 50
        if exposed[x] == True:
            canvas.draw_text(str(card_deck[x]), [cardup_pos,70] , 50, 'White')
        elif exposed[x] == False:  
                canvas.draw_polygon(carddown_pos[z], 49, 'Green')
        z += 1 



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric