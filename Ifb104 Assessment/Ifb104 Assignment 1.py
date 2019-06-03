
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 4"Student Code of Conduct".
#
#    Student no: N10132767
#    Student name: JOHN NGUYEN
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack



# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]


# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = False):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 1, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit C', 2, 1]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.

# Draw the card stacks as per the provided game specification

# Introduce a global variable here to write each suit of
# cards a face value on the top left corner every time a card is called.
suit_value = iter(['A','2','3','4','5','6', \
                    '7','8','9','10','J', 'Q', 'K'] * 6)
# Introduce a second global variable to place a suit value on the bottom right
# corner of the card suit. To make the value the same as the top left corner,
# the iteration of the list will need to be reset back to the first element.
# So lets assign and duplicate the variable again with the same elements.
suit_value2 = iter(['A','2','3','4','5','6', \
            '7','8','9','10','J', 'Q', 'K'] * 6)

# Note: iter method is used to iterate the list to a new value each time
# another card is drawn. The list is multiplied by 6, such that the iteration
# can keep iterating enough to fill a fullly stacked game of patience
# (this has been verified).

def deal_cards(any_game):
    # Define a variable to keep every card that is drawn aligned to the grid.
    # This variable will reset the heading after each card is drawn. This is
    # to prepare drawing the next card at any location.
    reset_heading = 180
    # Define a function that will store and define the suit dimensions,
    # and draw a blank suit canvas. This will be called in each suit
    # to avoid redundancy of code.
    # The three arguments in suit_canvas allows for customization
    # of cards with respect to their appearance, namely, colour and width.
    def suit_canvas(fill_colour, border_colour, suit_width = 5):
        # Define constant variables for suit dimensions.
        suit_length = 120
        suit_height = 180
        curve_radius = 10
        curve_extent = 90
        # Draw blank card canvas
        fillcolor(fill_colour)
        # Set heading backwards to rotate the pen to keep the stacks of
        # cards centered, and proportioned. This is because the stack location
        # global variable will be used assign card suits to a specific stack.
        # However, the downside to this is that it doesn't go to the start,
        # rather it goes to the center of it . So, in order to keep a card
        # vertically aligned to a stack, each time a card is drawn,
        # turtle will move forward from the center (from left to right)
        # and the heading will reset before drawing the suit of cards.
        setheading(reset_heading) 
        begin_fill()
        # Start drawing the canvas from right to left, as the heading
        # is reset to 180.
        for blank_canvas in range(2): 
            pendown()
            pencolor(border_colour)
            width(suit_width)
            forward(suit_length)
            circle(curve_radius, extent = curve_extent)
            forward(suit_height)
            circle(curve_radius, extent = curve_extent)
        end_fill()
        
    # Define a curve to draw when encountering curves.
    # This curve is defined for large ranged curves.
    def draw_curve(heading, radius, scope = 50): 
        pd() # Put the pen down
        seth(heading) # Set a certain angle
        circle(radius, extent = scope) # insert a radius and the extent
    # This curve is defined for smaller ranged curves.
    def curve2(heading, length, scope = 0.5, extent = 20, x = True):
        if x == True:
            pd()
        else: # If x is not true, then pen will lift up.
            pu()
        seth(heading)
        how_long = range(extent)
        for curve in how_long:
            fd(length)
            rt(scope)

    # This curve is defined for smaller ranged curves in the opposing
    # direction.
    def curve3(heading, length, scope = 0.5, extent = 10, x = True):
        if x == True: 
            pd()
        else: # If x is not true, then pen will lift up.
            pu()
        seth(heading)
        how_long = range(extent)
        for curve in how_long:
            fd(length)
            lt(scope)
            
    # Define a function to move in any direction and change heading for
    # efficiency, and shortening of code segments. 
    def move(heading, length = 0): 
        pd() # Put the pen down to begin drawing
        seth(heading) # Set the heading to a certain angle.
        fd(length) # Move forward a certain length.
        
    # Define 'repos' (short for repositition) for efficient navigating through
    # drawing each component. Moreover, this repos function will be used
    # later on in the logic segment, where the angle and length is positioned
    # to move down the stack, allowing the suit of cards to be cascaded.
    
    def repos(heading, length = 0):
        # lift penup so it doesnt leave a trail.
        pu()
        seth(heading)
        forward(length)
        
    # Define the drawings of 4 unique suits.
    
    def Suit_A(): # This suit will contain batman!
        # Invoke the blank suit card to draw up the suit with unique
        # border colours and card colours.
        suit_canvas('light grey', 'grey')
        # Assign variable to divide drawings to scale (adjustable). The
        # higher the scale, the smaller the drawing, vice-versa.
        scale = 2.45 # Here, 2.45 is the perfect size to fit within the suit.
        # Assign width variable to adjust the width for the drawing
        width1 = 2

        # Draw batman
        # Make the pencolor 'black' to draw bat man's edges in black.
        pencolor('black')    

        def bat_cape():
            # Set width to default value
            width(width1)
            # Reposition to draw cape
            repos(148, 113/scale)
            # Draw bat cape
            fillcolor('slate gray')
            begin_fill()
            curve2(255, 11/scale, -1)
            how_many = range(5)
            for curves in how_many:
                curve2(95, 3.5/scale, 10)
            curve2(87, 11/scale, -1)
            move(180, 150/scale)
            end_fill()
            
        def bat_body_legs():  
            fillcolor('grey')
            begin_fill()
            # Navigate to legs
            repos(280, 10)
            # Start drawing legs
            curve3(270, 16.129/scale, 1.6) 
            # Set the width to be small to minimize the width overlap that
            # the edge of the legs create on the left foot (this is a simple
            # fix, since the width of the boots sleeves and bottom leg
            # doubles the pen size).
            small = 0.5
            width(small)
            move(0, 28.22/scale)
            # Reset the width back to the default as its not on the edge of
            # the left foot.
            width(width1)
            curve3(50, 4.838/scale, 3) 
            move(0, 8.06/scale)
            curve3(278, 4.838/scale, 3)
            # Make the width smaller, as its on the right foot. This will
            # prevent the width overlap, as mentioned above.
            width(small)
            move(0, 28.22/scale)
            # Set the width back to the default value as it is no longer
            # on the right foot.
            width(width1)
            curve3(76, 16.129/scale, 1.6)
            end_fill()

            
        def bat_top():
            # Draw top
            fillcolor('grey')
            begin_fill()
            curve2(90, 2.90/scale, -0.5)
            move(220, 38.7/scale)
            move(180, 77.419/scale)
            move(140, 38.7/scale)
            curve2(264, 2.90/scale, -0.5)
            end_fill()

        def bat_foot():
            # Draw left foot
            # Navigate to the left foot
            repos(277, 159.67/scale)
            # Do upper boot sleeves
            width(width1)
            move(270) 
            fillcolor('slate gray')
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(6.45/scale)
                lt(90)
                fd(30.645/scale)
                lt(90)
            end_fill()
            repos(275, 6.45/scale)
            # Draw boots
            begin_fill()
            curve3(300, 0.8/scale, 1)
            move(180)
            circle(8.06/scale, extent = 180)
            fd(16.13/scale)
            circle(8.06/scale, extent = 90)
            fd(14.516/scale)
            end_fill()
            # Draw right foot
            # Navigate to right foot
            repos(5, 76.61/scale)
            # Do upper boot sleeves
            width(width1)
            move(270)
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(6.45/scale)
                rt(90)
                fd(30.64/scale)
                rt(90)
            end_fill()
            repos(260, 6.45/scale)
            # Draw boots
            begin_fill()
            curve3(240, 0.8/scale, -1)
            move(0)
            circle(-8.06/scale, extent = 180)
            fd(16.13/scale)
            circle(-8.06/scale, extent = 90)
            fd(14.516/scale)
            end_fill()
            
        def bat_head():
            # Reposition turtle to go above the body to draw the head
            repos(113, 240/scale)
            # Begin drawing head
            fillcolor('slate gray')
            begin_fill()
            curve2(117, 7/scale, 2)
            curve2(25, 8.5/scale, 2.5)
            curve2(290, 7/scale, 2.5)
            move(222, 43/scale)
            curve2(195, 4/scale, 1.8)
            move(142, 35/scale)
            end_fill()
            # Reposition to the cheek
            repos(23.5, 172/scale)
            # Draw curve to the top spike
            begin_fill()
            curve2(76, 7.8/scale, -1.5)
            curve2(230, 4.2/scale, -1.5)
            end_fill()
            # Reposition to the other cheek side
            repos(209, 161/scale)
            # Repeat as above
            begin_fill()
            curve2(105, 7.8/scale, 1.5)
            curve2(310, 4.2/scale, 1.5)
            end_fill()
            # Reposition to the left eye
            repos(260, 40/scale)
            # Draw the left eye
            fillcolor('white')
            begin_fill()
            move(340, 40/scale)
            curve2(270, 1/scale, 2.5)
            curve2(190, 1.5/scale, 1.5)
            curve2(100, 1.4/scale, 0.8)
            end_fill()
            # Reposition to the right eye
            repos(0.5, 130/scale)
            # Draw the right eye
            begin_fill()
            move(200, 40/scale)
            curve2(270, 1/scale, -2.5)
            curve2(350, 1.5/scale, -1.5)
            curve2(80, 1.4/scale, -0.8)
            end_fill()

        def face_mouth():
            # Reposition turtle to draw the face
            repos(210, 170/scale)
            # Begin drawing
            fillcolor('bisque')
            begin_fill()
            curve2(60, 1.2/scale, 2)
            move(340, 60/scale)
            curve2(330, 0.5/scale, -3)
            move(20, 60/scale)
            curve2(330, 1.2/scale, 2)
            move(245, 18/scale)
            move(222, 43/scale)
            curve2(195, 4/scale, 1.8)
            move(142, 35/scale)
            move(115, 25/scale)
            end_fill()
            # Reposition to mouth to draw the mouth
            repos(335, 60/scale)
            curve2(350.5, 2.5/scale, -1)

        def bat_arms():
            # Draw left arm
            repos(166, 110/scale)
            fillcolor('grey')
            begin_fill()
            curve2(240, 7.75/scale, -2)
            curve2(320, 1.3/scale, -2)
            curve2(50, 0.8/scale, -2)
            curve2(100, 3.7/scale, 2)
            curve2(90, 2.2/scale, 0.5)
            end_fill()
            # Navigate to right arm
            repos(9, 149/scale)
            # Draw right arm
            begin_fill()
            curve2(300, 7.75/scale, 2)
            curve2(220, 1.3/scale, 2)
            curve2(130, 1/scale, 2)
            curve2(80, 3/scale, -1.5)
            curve2(85, 2.9/scale, -1.4)
            end_fill()

        def bat_belt():
            # Draw belt with alternating colors 'gold' and 'goldenrod'
            # Navigate to waistline for the belt
            repos(345, 14/scale)
            curve3(270, 10/scale, -0.8, 10, False)
            width(width1)
            move(180)
            # Define colour 1 and 2, to be iterated in the loop
            col1 = 'gold'
            col2 = 'goldenrod'
            # Iterate these 7 times as there are 7 blocks in the belt
            alternating_colors = iter([col1, col2, col1, col2, col1 , col2])
            how_many = range(6)
            # Draw the belts in alternating colours as mentioned above
            for belt in how_many:
                fillcolor(next(alternating_colors))
                begin_fill()
                how_many = range(5)
                for blocks in how_many:
                    fd(23.5/scale)
                    rt(90)
                # Set the heading to 180 such that the next block in the belt
                # can be aligned and drawn from left to right.
                seth(180)
                end_fill()

        def bat_pants_gloves(): # Draw batman's pants and gloves
            # Reposition turtle to draw pants
            repos(278, 2/scale)
            # Draw pants
            fillcolor('slate gray')
            begin_fill()
            move(278, 40/scale)
            move(342, 69/scale)
            move(18, 69/scale)
            move(84, 40/scale)
            end_fill()
            # Reposition turtle to right glove location
            repos(290, 15/scale)
            # Begin drawing gloves
            begin_fill()
            move(23, 35/scale)
            move(265, 22/scale)
            curve2(210, 1.2/scale, 1)
            curve2(130, 1/scale, 2.2)
            end_fill()
            # Reposition turtle to left glove location
            repos(179, 163/scale)
            begin_fill()
            move(150, 35/scale)
            move(275, 25/scale)
            curve2(330, 1.2/scale, -1)
            curve2(50, 1/scale, -2.2)
            end_fill()

        def bat_torso():
            # Navigate to the center of the torso
            repos(57, 88/scale)
            # Draw the bat
            fillcolor('black')
            begin_fill()
            curve2(340, 1.4/scale, -2.5)
            curve2(335, 1/scale, -3.3)
            curve2(335, 1.4/scale, -2.5)
            curve2(300, 1.3/scale, 2.5)
            curve2(159, 0.9/scale, -3)
            curve2(180, 1.3/scale, -3)
            curve2(126, 1.3/scale, -3)
            curve2(139, 0.9/scale, -3)
            curve2(115, 1.2/scale, 2.5)
            end_fill()
            # Repositition turtle to draw the top bat ears
            repos(0, 30/scale)
            move(75, 5/scale)
            move(285, 5/scale)
            repos(0, 10/scale)
            move(75, 6/scale)
            move(285, 6/scale)

        def batman(): # Piece all components into one, and this will be batman!
            bat_cape()
            bat_body_legs()
            bat_top()
            bat_foot()
            bat_head()
            face_mouth()
            bat_arms()
            bat_belt()
            bat_pants_gloves()
            bat_torso()
            
        repos(248, 144) # Reposition batman to the center of the card.
        batman() # Call batman here!
        repos(62.54259, 128.15) # Reposition turtle back to the start of canvas.
        setheading(reset_heading) # Reset heading back for drawing face values.
        
##########-------------------End of Batman Suit--------------------------------#           

    def Suit_B(): # This suit will contain dead pool!
        # Invoke the blank suit card to draw up the suit with unique
        # border colours and card colours.
        suit_canvas('salmon', 'black')

        # Assign variable to divide drawings to scale (adjustable). The
        # higher the scale, the smaller the drawing, vice-versa.
        scale = 2.1 # Here, 2.1 is the perfect size to fit within the suit.
        # Assign width variable to adjust the width for the drawing
        width1 = 2
        
        # Draw dead pool
        # Make the pencolor 'black' to draw dead pool's edges in black.
        pencolor('black')
        
        def pool_body_legs():
            # set width to default value
            width(width1)
            fillcolor('firebrick')
            begin_fill()
            move(270)
            # Start drawing legs
            curve3(270, 16.129/scale, 1.6) 
            # Set the width to be small to minimize the width overlap that
            # the edge of the legs create on the left foot (this is a simple
            # fix, since the width of the boots sleeves and bottom leg
            # doubles the pen size).
            small = 0.5
            width(small)
            move(0, 28.22/scale)
            # Reset the width back to the default as its not on the edge of
            # the left foot.
            width(width1)
            curve3(50, 4.838/scale, 3) 
            move(0, 8.06/scale)
            curve3(278, 4.838/scale, 3)
            # Make the width smaller, as its on the right foot. This will
            # prevent the width overlap, as mentioned above.
            width(small)
            move(0, 28.22/scale)
            # Set the width back to the default value as it is no longer
            # on the right foot.
            width(width1)
            curve3(76, 16.129/scale, 1.6)
            end_fill()
            
        def pool_top():
            # Draw top
            fillcolor('firebrick')
            begin_fill()
            curve2(90, 2.90/scale, -0.5)
            move(220, 38.7/scale)
            move(180, 77.419/scale)
            move(140, 38.7/scale)
            curve2(264, 2.90/scale, -0.5)
            end_fill()

        def pool_foot():
            # Draw left foot
            # Navigate to the left foot
            repos(277, 159.67/scale)
            # Do upper boot sleeves
            move(270) 
            fillcolor('sienna')
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(6.45/scale)
                lt(90)
                fd(30.645/scale)
                lt(90)
            end_fill()
            repos(275, 6.45/scale)
            # Draw boots
            width(width1)
            begin_fill()
            curve3(300, 0.8/scale, 1)
            move(180)
            circle(8.06/scale, extent = 180)
            fd(16.13/scale)
            circle(8.06/scale, extent = 90)
            fd(14.516/scale)
            end_fill()
            # Draw right foot
            # Navigate to right foot
            width(width1)
            repos(5, 76.61/scale)
            # Do upper boot sleeves
            move(270)
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(6.45/scale)
                rt(90)
                fd(30.64/scale)
                rt(90)
            end_fill()
            repos(260, 6.45/scale)
            # Draw boots
            begin_fill()
            curve3(240, 0.8/scale, -1)
            move(0)
            circle(-8.06/scale, extent = 180)
            fd(16.13/scale)
            circle(-8.06/scale, extent = 90)
            fd(14.516/scale)
            end_fill()
            
        def pool_head():
            # Navigate to dead pool's head
            repos(115, 260/scale)
            fillcolor('firebrick')
            # begin drawing dead pool's head
            begin_fill()
            curve2(85, 7/scale, 1.5)
            draw_curve(40, -100/scale, 100)
            curve2(275, 7/scale, 1.5)
            draw_curve(214, -125/scale, 90)
            end_fill()
            # Navigate to left eye
            repos(55, 115/scale)
            # Begin drawing dead pools left eye
            fillcolor('black')
            begin_fill()
            curve2(300, 3.5/scale, 1.5)
            move(230, 40/scale)
            draw_curve(165, -50/scale, 90)
            curve2(75, 3/scale, 1.5)
            curve2(319, 1.5/scale, 1.5)
            end_fill()
            # Reposition to inner eye
            repos(270, 60/scale)
            # Make the width of the pen smaller when drawing the eyes.
            pensize(2)
            # Draw inner eye
            fillcolor('pale turquoise')
            begin_fill()
            curve2(75, 2/scale, -5)
            curve2(255, 2/scale, -5)
            end_fill()
            # Navigate to right eye
            repos(25, 110/scale)
            # begin drawing dead pools right eye
            fillcolor('black')
            begin_fill()
            curve2(205, 3.9/scale, -1.5)
            move(285, 40/scale)
            draw_curve(0, 55/scale, 85)
            curve2(80, 1.9/scale, -1.5)
            curve2(190, 0.1/scale, -1.5)
            end_fill()
            # Draw inner eye
            fillcolor('pale turquoise')
            begin_fill()
            repos(228, 75/scale)
            curve2(75, 2/scale, 5)
            curve2(255, 2/scale, 5)
            end_fill()
            # Reset the pen width to the default value for next drawings.
            pensize(width1)

        def pool_arms():
            # Draw left arm
            repos(191, 118/scale)
            fillcolor('firebrick')
            begin_fill()
            curve2(240, 7.75/scale, -2)
            curve2(320, 1.3/scale, -2)
            curve2(50, 0.8/scale, -2)
            curve2(100, 3.7/scale, 2)
            curve2(90, 2.7/scale, 0.5)
            end_fill()
            # Navigate to right arm
            repos(355.5, 149/scale)
            # Draw right arm
            begin_fill()
            curve2(300, 7/scale, 2)
            curve2(220, 1.3/scale, 2)
            curve2(130, 1/scale, 2)
            curve2(80, 3/scale, -2)
            curve2(85, 2.9/scale, -0.5)
            end_fill()


        def pool_belt():
            # Navigate to the top section of the belt
            repos(270, 40/scale)
            # Draw top section of the belt
            fillcolor('sienna')
            begin_fill()
            move(180, 43/scale)
            move(215, 10/scale)
            move(180, 37/scale)
            move(145, 10/scale)
            move(180, 43/scale)
            # Draw the side of the belt at the waist
            # Make width smaller to avoid line overlap
            width(1)
            curve2(265, 2/scale, -0.5)
            # Reset the width back to the default
            width(width1)
            # Draw the bot section of the belt
            move(0, 41/scale)
            move(35, 10/scale)
            move(0, 37/scale)
            move(325, 10/scale)
            move(0, 45/scale)
            end_fill()
            # Navigate to the center of the belt
            repos(164, 75/scale)
            # Draw an orb in the belt
            pencolor('black')
            dot(45/scale)
            # Repostion to draw red line
            repos(270, 22.5/scale)
            # Draw a red line through it
            pencolor('firebrick')
            # Make the pen width a little thick
            pensize(3)
            # intersect belt
            move(90, 45/scale)
            # Reset the width to the default value
            width(width1)
            # Set the pen color to the default color.
            pencolor('black')
            # Resposition to the left half
            repos(260, 30/scale)
            # Make the width of the drawing smaller for the eyes
            width(2)
            # Draw left eye
            fillcolor('pale turquoise')
            begin_fill()
            curve2(85, 1/scale, -5)
            curve2(255, 1/scale, -5)
            end_fill()
            # Reposition to right eye
            repos(15, 13/scale)
            # Begin drawing right eye
            fillcolor('pale turquoise')
            begin_fill()
            curve2(85, 1/scale, 5)
            curve2(275, 1/scale, 5)
            end_fill()
            # Reposition to the start circumfererance of the belt
            repos(21.5, 17/scale)
            # Set the pen color to red
            pencolor('maroon')
            # Set the width a little larger
            pensize(5/scale)
            # reset the heading to 0 to center the circle to the orb
            move(90)
            # Draw red glow on the circumference of the belt
            circle(22.5/scale)
            # Reset the pensize to the default value
            pensize(width1)
            # Reset the pen color to the default color
            pencolor('black')

        # Draw pool clothing
        def pool_clothing():
            # Navigate to the top chest
            repos(139, 114/scale)
            # Draw the chest clothing
            # left hand side
            fillcolor('black')
            begin_fill()
            move(315, 30/scale)
            move(270, 31/scale)
            move(180, 28/scale)
            end_fill()
            # right hand side
            repos(12, 145/scale)
            begin_fill()
            move(195, 25/scale)
            move(270, 25/scale)
            move(0, 25/scale)
            end_fill()
            # Reposition to the right legs
            repos(267, 70/scale)
            # Draw leg clothing
            # begin drawing right leg side
            begin_fill()
            move(180, 25/scale)
            move(220, 20/scale)
            move(285, 30/scale)
            move(310, 15/scale)
            move(340, 14/scale)
            end_fill()
            # Reposition to the left leg side
            repos(155, 136/scale)
            # begin drawing left leg side
            begin_fill()
            move(0, 25/scale)
            move(320, 20/scale)
            move(255, 30/scale)
            move(240, 15/scale)
            move(200, 14/scale)
            end_fill()
            # Reposition to draw clothing on the arms
            # Left hand side
            repos(120, 118/scale)
            # Begin drawing on the lower arm
            begin_fill()
            move(83, 25/scale)
            move(330, 35/scale)
            move(265, 27/scale)
            move(150, 35/scale)
            end_fill()
            # To the upper
            repos(78, 80/scale)
            # Begin drawing
            begin_fill()
            move(330, 35/scale)
            move(85, 15/scale)
            move(130, 33/scale)
            end_fill()
            # Reposition to the right arm
            repos(335, 215/scale)
            # Begin drawing on the lower arm
            begin_fill()
            move(200, 33/scale)
            move(280, 30/scale)
            move(20, 30/scale)
            end_fill()
            # To the upper
            repos(105, 95/scale)
            # Begin drawing
            begin_fill()
            move(220, 30/scale)
            move(268, 20/scale)
            move(30, 40/scale)
            end_fill()
            # Reposition to right hand to draw gloves
            repos(278, 94/scale)
            # Draw gloves
            fillcolor('black')
            begin_fill()
            move(200, 32/scale)
            move(299, 15/scale)
            move(20, 22/scale)
            end_fill()
            # Reposition to the left hand to draw gloves
            repos(172, 223/scale)
            # Draw gloves
            begin_fill()
            move(340, 32/scale)
            move(255, 12/scale)
            move(230, 5/scale)
            move(155, 23/scale)
            end_fill()

        # Draw sword sheath
        def sword_shealth():
            # Reposition to the left hand side
            repos(82, 180/scale)
            # Begin drawing
            fillcolor('sienna')
            begin_fill()
            move(120, 60/scale)
            move(60, 8/scale)
            move(220, 25/scale)
            move(0, 8/scale)
            move(302, 67/scale)
            end_fill()
            # Reposition to the hilt
            repos(302, -73/scale)
            # Draw the hilt
            fillcolor('black')
            begin_fill()
            move(302, -10/scale)
            move(220, -10/scale)
            move(302, 10/scale)
            end_fill()
            
        def dead_pool(): # Piece all of dead pool modules into 1 function
            pool_body_legs()
            pool_top()
            pool_foot()
            pool_head()
            pool_arms()
            pool_belt()
            pool_clothing()
            sword_shealth()
            
        repos(229, 145) # Reposition dead pool to the center of the card suit.
        dead_pool() # Reposition turtle back to the start of the suit canvas.
        repos(19.321, 123.751)
        setheading(reset_heading) # Reset heading back for drawing face values.
        
##########-------------------End of Dead Pool Suit-----------------------------#

    def Suit_C():# This suit will contain iron man!
        # Invoke the blank suit card to draw up the suit with unique
        # border colours and card colours.
        suit_canvas('moccasin', 'goldenrod') 
        
        # Assign variable to divide drawings to scale (adjustable). The
        # higher the scale, the smaller the drawing, vice-versa.
        scale = 3.6 # Here, 3.6 is the perfect size to fit within the suit.
        # Assign width variable to adjust the width for the drawing
        width1 = 2
        
        # Draw Iron man
        # Make the pencolor 'black' to draw iron man's edges in black.
        pencolor('black')         

        def iron_head():
            width(width1)
            # Begin drawing head
            fillcolor('dark red')
            begin_fill()
            draw_curve(25, -300/scale, 52)
            curve2(278, 5/scale)
            draw_curve(325, -62/scale, 120)
            move(270, 30/scale)
            move(220, 100/scale)
            move(180, 120/scale)
            move(140, 100/scale)
            move(90, 30/scale)
            draw_curve(150, -62/scale, 120)
            curve2(270, -5/scale)
            draw_curve(70, -8/scale, 80)
            end_fill()
            # Create the ears
            # Reposition to left
            repos(261, 105/scale)
            # Draw line
            move(270, 112/scale)
            # Reposition to right
            repos(22, 303/scale)
            # Draw line
            move(266, 112/scale)
            # Reposition to draw yellow mask
            repos(170, 25/scale)
            # Begin drawing mask
            fillcolor('goldenrod')
            begin_fill()
            curve2(85, 8/scale, -0.5)
            move(150, 50/scale)
            move(220, 50/scale)
            move(180, 60/scale)
            move(140, 50/scale)
            move(210, 50/scale)
            curve2(85, -8/scale, -0.5)
            move(330, 15/scale)
            move(300, 15/scale)
            move(320, 60/scale)
            move(30, 8/scale)
            move(0, 75/scale)
            move(330, 8/scale)
            move(40, 60/scale)
            move(60, 15/scale)
            move(30, 15/scale)
            end_fill()
            # Navigate to right cheek line
            repos(80, 20/scale)
            # Draw right cheek line
            curve2(210, 5.4/scale, -2)
            # Reposition to mouth line
            repos(65, 20/scale)
            # Draw mouth line
            move(140, 20/scale)
            curve2(170, 3.7/scale, -1)
            move(220, 20/scale)
            # Reposition to the left cheek line
            repos(135, 82/scale)
            # Draw left cheek line
            curve2(330, 5.1/scale, 2.2)

        def iron_eyes():
            width(width1)
            # Reposition to iron man eye brows
            repos(105, 170/scale)
            # Draw eye brows
            move(340, 95/scale)
            move(20, 95/scale)
            # Reposition to the right eye
            repos(-340, -15/scale)
            repos(270, 2/scale)
            # Draw right eye
            fillcolor('pale turquoise')
            begin_fill()
            curve2(270, 1.3/scale, 0.5)
            curve2(210, 1.6/scale, 0.5)
            curve2(150, 1.65/scale, 0.5)
            end_fill()
            # Reposition to the left eye
            repos(167, 97/scale)
            # Draw right eye
            begin_fill()
            curve2(270, 1.3/scale, -0.5)
            curve2(330, 1.6/scale, -0.5)
            curve2(25, 1.75/scale, -0.5)
            end_fill()

        def iron_body_legs():
            # Navigate to legs
            repos(248, 237.5/scale)
            fillcolor('dark red')
            begin_fill()
            # Start drawing legs
            curve3(270, 25/scale, 1.6)
            # Set the width to be small to minimize the width overlap that
            # the edge of the legs create on the left foot (this is a simple
            # fix, since the width of the boots sleeves and bottom leg
            # doubles the pen size).
            small = 0.5
            width(small)
            move(0, 43.75/scale)
            # Reset back to the standard width as the pen is not on the edge
            # of the left leg
            width(width1)
            curve3(50, 7.5/scale, 3)
            move(0, 12.5/scale)
            curve3(278, 7.5/scale, 3)
            # Make the width small again as it draws the edge of the right foot.
            width(small) 
            move(0, 43.75/scale)
            # Set the width back to the default value as it is no longer
            # on the right foot.
            width(width1)
            curve3(76, 25/scale, 1.6)
            end_fill()

        def iron_top():
            # Draw top
            fillcolor('dark red')
            begin_fill()
            curve2(90, 4.5/scale, -0.5)
            move(220, 60/scale)
            move(180, 120/scale)
            move(140, 60/scale)
            curve2(264, 4.5/scale, -0.5)
            end_fill()

        def iron_foot(): # Draw left foot
            # Navigate to the left foot
            repos(277, 247.5/scale)
            # Do upper boot sleeves
            move(270) 
            fillcolor('goldenrod')
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(10/scale)
                lt(90)
                fd(47.5/scale)
                lt(90)
            end_fill()
            repos(275, 10/scale)
            # Draw boots
            width(width1)
            begin_fill()
            curve3(300, 1.25/scale, 1)
            move(180)
            circle(12.5/scale, extent = 180)
            fd(25/scale)
            circle(12.5/scale, extent = 90)
            fd(22.5/scale)
            end_fill()
            # Draw right foot
            # Navigate to right foot
            width(width1)
            repos(5, 118.75/scale)
            # Do upper boot sleeves
            move(270)
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(10/scale)
                rt(90)
                fd(47.5/scale)
                rt(90)
            end_fill()
            repos(260, 10/scale)
            # Draw boots
            begin_fill()
            curve3(240, 1.25/scale, -1)
            move(0)
            circle(-12.5/scale, extent = 180)
            fd(25/scale)
            circle(-12.5/scale, extent = 90)
            fd(22.5/scale)
            end_fill()

        def iron_body():# Draw lines and orb in iron man's torso
            # Reposition turtle to the top 
            repos(106, 315/scale)
            # Begin drawing lines
            move(270, 25/scale)
            curve2(0, 1.5/scale, 3)
            # Navigate to orb
            repos(290, 65/scale)
            # Draw orb
            fillcolor('light cyan')
            begin_fill()
            draw_curve(0, 35/scale, 360)
            end_fill()
            # Reposition to line curve
            repos(70, 67/scale)
            # draw line curve
            curve2(58, 1.5/scale, 3)
            move(90, 25/scale)
            # Reposition to next line
            repos(330, 75/scale)
            # Begin drawing next line
            move(230, 55/scale)
            move(180, 42/scale)
            repos(180, 67/scale)
            move(180, 42/scale)
            move(130, 55/scale)
            repos(130, -55/scale)
            move(250, 20/scale)
            move(150, 30/scale)
            # Draw gold plate on left side
            fillcolor('goldenrod')
            begin_fill()
            move(150, -30/scale)
            move(300, 30/scale)
            move(230, 20/scale)
            move(160, 25/scale)
            end_fill()
            # Reposition to the other side, segment above
            repos(16, 189/scale)
            # Begin drawing
            move(290, 20/scale)
            move(30, 30/scale)
            # Draw gold plate on the right side
            begin_fill()
            move(30, -30/scale)
            move(240, 30/scale)
            move(310, 20/scale)
            move(20, 25/scale)
            end_fill()
            # Reposition to next line
            repos(170, 40/scale)
            # Begin drawing
            move(180, 46/scale)
            move(230, 7/scale)
            move(180, 30/scale)
            move(130, 7/scale)
            move(180, 46/scale)
            # Reposition to next line
            repos(225, 55/scale)
            # Begin drawing next line
            move(350, 30/scale)
            move(26, 82/scale)
            move(333, 82/scale)
            move(10, 30/scale)
            move(10, -30/scale)
            move(206, 82/scale)
            move(153, 82/scale)
            # Draw golden lower piece
            fillcolor('goldenrod')
            begin_fill()
            move(26, 41/scale)
            move(0, 20/scale)
            move(290, 7/scale)
            move(0, 25/scale)
            move(70, 7/scale)
            move(0, 20/scale)
            move(290, 35/scale)
            move(180, 22/scale)
            move(250, 7/scale)
            move(180, 40/scale)
            move(110, 7/scale)
            move(180, 22/scale)
            move(75, 35/scale)
            end_fill()
            # Navigate to lines for left plate legs
            repos(205, 47/scale)
            # Draw line left legs plate 
            begin_fill()
            move(270, 50/scale)
            move(310, 20/scale)
            move(0, 40/scale)
            move(270, 5/scale)
            move(0, 15/scale)
            curve2(60, 1.65/scale, -2)
            end_fill()
            # Reposition to line in gold leg plate
            repos(150, 55/scale)
            # Begin drawing line in gold leg plate
            move(270, 24/scale)
            move(320, 10/scale)
            move(285, 24/scale)
            # Reposition to the right side for right leg plates
            repos(29, 130/scale)
            # Draw line right legs plate
            begin_fill()
            move(270, 48/scale)
            move(230, 20/scale)
            move(180, 39/scale)
            move(270, 4/scale)
            move(180, 14/scale)
            curve2(120, 1.70/scale, 2)
            end_fill()
            # Reposition to line in gold leg plate
            repos(27, 55/scale)
            # begin drawing line in gold leg plate
            move(270, 24/scale)
            move(220, 10/scale)
            move(255, 24/scale)
            # Reposition to lower right leg
            repos(0, 25/scale)
            # Draw lines on lower right leg
            move(320, 35/scale)
            move(220, 20/scale)
            fillcolor('goldenrod')
            # Give the knee pads a gold color
            begin_fill()
            move(110, 20/scale)
            move(182, 25/scale)
            move(265, 20/scale)
            move(290, 10/scale)
            move(3, 25/scale)
            move(70, 10/scale)
            end_fill()
            move(70, -10/scale)
            move(275, 15/scale)
            repos(180, 30/scale)
            move(80, 15/scale)
            repos(110, 10/scale)
            move(140, 30/scale)
            repos(0, 25/scale)
            move(100, 20/scale)
            # Reposition to the lower left leg
            repos(182, 100/scale)
            # Draw lines on lower right leg
            move(220, 35/scale)
            move(320, 20/scale)
            # Give the knee pads a gold color
            begin_fill()
            move(70, 20/scale)
            move(2, 25/scale)
            move(275, 19/scale)
            move(250, 9/scale)
            move(183, 25/scale)
            move(110, 10/scale)
            end_fill()
            move(110, -10/scale)
            move(265, 14/scale)
            repos(0, 30/scale)
            move(100, 15/scale)
            move(70, 10/scale)
            move(40, 34/scale)
            repos(185, 30/scale)
            move(80, 15/scale)
        
        def iron_arms(): # draw two arms including the lines and plates
            # Reposition to left arm
            repos(107, 300/scale)
            # Draw left arm
            fillcolor('dark red')
            begin_fill()
            curve2(220, 12/scale, -2)
            curve2(320, 3.5/scale, -2)
            curve2(50, 1/scale, -2)
            curve2(85, 8/scale, 2)
            curve2(90, 2.3/scale, 0.5)
            end_fill()
            # Reposition to draw line on left arm
            repos(265, 20/scale)
            # Draw lines on the arm
            curve2(180, 2.3/scale, 1.5)
            # To next line and draw the gold plate
            repos(230, 40/scale)
            # Begin drawing
            fillcolor('goldenrod')
            begin_fill()
            move(345, 40/scale)
            move(10, 30/scale)
            # Make pen width smaller so it doesnt overlap the other line
            width(1)
            curve2(37.5, -4/scale, -2)
            # Reset pendwidth to default value
            width(width1)
            move(165, 40/scale)
            move(140, 20/scale)
            end_fill()
            # Reposition to draw line in gold plate
            repos(140, -15/scale)
            # Begin drawing line in gold plate
            move(65, 27/scale)
            move(15, 20/scale)
            move(60, 20/scale)
            repos(345, 10/scale)
            move(240, 20/scale)
            move(295, 20/scale)
            move(230, 25/scale)
            # Reposition to next gold plate
            repos(185, 60/scale)
            # Begin drawing next gold plate
            begin_fill()
            move(310, 40/scale)
            move(330, 30/scale)
            repos(265, 15/scale)
            move(170, 40/scale)
            move(120, 15/scale)
            move(140, 15/scale)
            end_fill()
            # Reposition to draw line in plate
            repos(327, 50/scale)
            # begin drawing
            move(75, 20/scale)
            # Reposition to prepare and draw a curve in the hands
            repos(280, 40/scale)
            # Draw a curve in the hands
            draw_curve(185, -80/scale, 50)
            
            # Reposition to the right arm before drawing 
            repos(27.5, 411/scale)
            # Begin drawing right arm
            fillcolor('dark red')
            begin_fill()
            curve2(320, 12/scale, 2)
            curve2(220, 3.5/scale, 2)
            curve2(130, 1/scale, 2)
            curve2(95, 8/scale, -2)
            curve2(90, 2.4/scale, -0.5)
            end_fill()
            # Reposition to draw line of right arm
            repos(276, 20/scale)
            # Draw line on the arm
            curve2(0, 2.3/scale, -1.5)
            # To the next line and draw the gold plate
            repos(310.5, 40/scale)
            # begin drawing
            fillcolor('goldenrod')
            begin_fill()
            move(195, 40/scale)
            move(175, 30/scale)
            # Make pen width smaller so it doesnt overlap the other line
            width(1)
            curve2(142.5, -4/scale, 2)
            # Reset pendwidth to default value
            width(width1)
            move(15, 40/scale)
            move(40, 22/scale)
            end_fill()
            # Reposition to draw line in gold plate
            repos(40, -18/scale)
            # Begin drawing line in gold plate
            move(115, 27/scale)
            move(165, 21/scale)
            move(110, 21/scale)
            repos(170, 10/scale)
            move(285, 25/scale)
            move(235, 20/scale)
            move(315, 26/scale)
            repos(355, 60/scale)
            # Begin drawing next gold plate
            begin_fill()
            move(230, 40/scale)
            move(210, 28/scale)
            repos(278, 15/scale)
            move(10, 40/scale)
            move(60, 16/scale)
            move(40, 16/scale)
            end_fill()
            # Reposition to draw line in plate
            repos(213, 50/scale)
            # begin drawing
            move(105, 20/scale)
            # Reposition to prepare and draw a curve in the hands
            repos(260, 45/scale)
            # Draw a curve in the hands
            draw_curve(0, 80/scale, 50)
            
        def iron_man(): # Piece all components of iron man into one function  
            iron_head()
            iron_eyes()
            iron_body_legs()
            iron_top()
            iron_foot()
            iron_body()
            iron_arms()  
                
        # Insert iron man in the center of Suit C, and enable him
        # to be playable in the game: patience.
        repos(190, 98)
        iron_man()
        # Return back to the start position when drawing the suit face value.
        repos(91.87, 136.9841) 
        # Reset turtle back to the heading to facilitate drawing
        # of the next card suit.
        setheading(reset_heading)

##########-------------------End of Iron Man Suit------------------------------#

    def Suit_D():
        # Invoke the blank suit card to draw up the suit with unique
        # border colours and card colours.
        suit_canvas('white', 'turquoise')
        
        # This suit will contain captain america!
        # Define two variables which can control the scale and width
        # of all components
        scale = 2.7 # Here, 2.7 is the perfect size to fit within the suit.
        width1 = 2 # pen width of components
        
        # Components of captain america:
        # This is the drawing of the blank suit, in which captain america
        # will be placed in later.
        # Make the pencolor 'black' to draw captain america's edges in black.
        pencolor('black')
    
        def top_head(): # Draw 3/4 upper head
            width(width1)
            pencolor('black')
            fillcolor('light sky blue')
            # Begin drawing
            begin_fill()
            move(270, 150/scale)
            move(0, 240/scale)
            move(90, 150/scale)
            move(90)
            circle(40/scale, extent = 100)
            move(180) 
            curve3(180, 4.8/scale, 0.32, 16)
            curve3(180, 4.8/scale, -0.32, 16)
            move(180) 
            circle(40/scale, extent = 100)
            end_fill()

        def lower_head(): # Draw lower head
            # Navigate to lower head
            repos(270, 145/scale)
            # Draw lower head
            fillcolor('peach puff')
            begin_fill()
            move(270, 35/scale)
            circle(10/scale, extent = 90)
            fd(219/scale)
            circle(11/scale, extent = 90)
            fd(35/scale)
            end_fill()
            # Navigate to mouth
            repos(195, 100/scale)
            # Draw mouth
            width(width1)
            curve3(198, 4/scale, -2.4, 15)
            
        def legs(): # Draw legs
            # Navigate to legs
            repos(200, 60/scale)
            fillcolor('light sky blue')
            # Start drawing legs
            begin_fill()
            curve3(270, 20/scale, 1.6) 
            # Set the width to be small to minimize the width overlap that
            # the edge of the legs create on the left foot (this is a simple
            # fix, since the width of the boots sleeves and bottom leg
            # doubles the pen size).
            small = 0.5
            width(small)
            move(0, 35/scale)
            # Reset the width back to the default as its not on the edge of
            # the left foot.
            width(width1)
            curve3(50, 6/scale, 3) 
            move(0, 10/scale)
            curve3(278, 6/scale, 3)
            # Make the width smaller, as its on the right foot. This will
            # prevent the width overlap, as mentioned above.
            width(small)
            move(0, 35/scale)
            # Set the width back to the default value as it is no longer
            # on the right foot.
            width(width1)
            curve3(76, 20.1/scale, 1.6)
            end_fill()
               

        def belt(): # Draw belt with alternating colors 'red', 'white'
            # Navigate to waistline for the belt
            curve3(272.5, 10/scale, -0.8)
            width(width1)
            move(180)
            # Define colour 1 and 2, to be iterated in the loop
            col1 = 'red'
            col2 = 'white'
            # Iterate these 7 times as there are 7 blocks in the belt
            alternating_colors = iter([col1, col2, col1,
                                       col2, col1 , col2,
                                       col1])
            how_many = range(7)
            # Draw the belts in alternating colours as mentioned above
            for belt in how_many:
                fillcolor(next(alternating_colors))
                begin_fill()
                how_many = range(5)
                for blocks in how_many:
                    fd(24/scale)
                    rt(90)
                # Set the heading to 180 such that the next block in the belt
                # can be aligned and drawn from left to right.
                seth(180) 
                end_fill()

        def left_foot(): # Draw left foot
            # Navigate to the left foot
            repos(280, 100/scale)
            # Do upper boot sleeves
            move(270) 
            fillcolor('red')
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(8/scale)
                lt(90)
                fd(38/scale)
                lt(90)
            end_fill()
            # Reposition turtle to the boots
            repos(275, 8/scale)
            # Draw boots
            width(width1)
            begin_fill()
            curve3(300, 1/scale, 1)
            move(180)
            circle(10/scale, extent = 180)
            fd(20/scale)
            circle(10/scale, extent = 90)
            fd(18/scale)
            end_fill()

        def right_foot(): # Draw right foot
            # Navigate to right foot
            repos(5, 95/scale)
            # Do upper boot sleeves
            width(width1)
            move(270)
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(8/scale)
                rt(90)
                fd(38/scale)
                rt(90)
            end_fill()
            # Navigate turtle to the boots
            repos(260, 8/scale)
            # Draw boots
            begin_fill()
            curve3(240, 1/scale, -1)
            move(0)
            circle(-10/scale, extent = 180)
            fd(20/scale)
            circle(-10/scale, extent = 90)
            fd(18/scale)
            end_fill()
            
        # Define star to draw star on captain america's torso.
        # This is referenced from flag_elements in week 3 exercise.
        # This will also be used to draw on captain amercia's shield.
        def star(height, colour):
            width(width1) # width of the drawings is 5 by default
            pencolor('black') # pencolor is black
            lt_angle = 72 # degrees, going left
            rt_angle = 144  # degrees, going right
            line_size = height * 0.409 # the length of each of the ten lines

            # Draw a five-pointed, filled star as five concave segments
            seth(-lt_angle) # pointing down from top point
            fillcolor(colour) # use the fillcolor as stated in the argument
            pd()
            begin_fill()
            section_numbers = range(5)
            for sec_no in section_numbers: # draw each of the star sections
              fd(line_size)
              lt(lt_angle)
              fd(line_size)
              rt(rt_angle)
            end_fill()
            pu()

        def torso_star(): # Define torso star
            # Navigate to the center of the torso to draw star
            repos(100, 195/scale)
            # Draw the star at the torso
            move(0)
            width(width1)
            star(50/scale, 'white')
            
        def red_glove_1(): # Define red glove 1
            # Navigate to the left hands
            repos(215, 120/scale)
            # Begin drawing
            width(width1)
            fillcolor('red')
            begin_fill()
            curve3(30, 8/scale, 17)
            curve3(220, 8/scale, 17, 9)
            end_fill()

        def red_glove_2():  # Define red glove 2
            # Navigate to the second glove
            repos(30, 25/scale)
            # Begin drawing
            move(35)
            fillcolor('red')
            begin_fill()
            curve3(35, 8/scale, 17)
            curve3(220, 8/scale, 17, 9)
            end_fill()

        def shield(): # Define shield
            # Navigate to the shield location
            repos(2, 210/scale)
            # Draw the shield through the concentric circle method
            # Firstly, define the radius for each circle in the shield.
            radii = [70/scale, 55/scale, 40/scale, 25/scale]
            # Make shield colors iterable, such that when used in the loop,
            # the colors listed will fill to the according radius listed in
            # radii, respectively.
            shield_color = iter(['red', 'white', 'red', 'light sky blue'])
            for circles in radii:
                pu()
                seth(0)
                fd(circles)
                setheading(90)
                fillcolor(next(shield_color)) # This will iterate shield colors.
                begin_fill()
                pd()
                circle(circles)
                # Go back to center position to draw the second circle
                setheading(180)
                pu()
                fd(circles)
                end_fill()
            # Navigate turtle to position where star can be drawn to the center
            repos(90, 22/scale)
            # Draw the star within the center of the shield and make the
            # width smaller
            width(1)
            star(40/scale, 'white')
            # Reset the width back to the default value
            width(width1)

        def left_horn(): # Define left horn
            # Navigate to the left horn
            repos(133, 368/scale)
            fillcolor('white')
            # Begin drawing
            width(width1)
            move(330)
            how_many = range(2)
            begin_fill()
            for horn in how_many:
                fd(30/scale)
                circle(-11/scale, extent = 180)
            end_fill()

        def right_horn(): # Define right horn
            # Navigate to the right horn
            repos(357, 237/scale)
            # Begin drawing
            move(26)
            begin_fill()
            how_many = range(2)
            for horn in how_many:
                forward(30/scale)
                circle(-11/scale, extent = 180)
            end_fill()

        def two_eyes(): # Define right eye and left eye
            # Navigate to the left eye
            repos(212, 230/scale)
            # Draw first eye
            width(width1)
            fillcolor('white')
            begin_fill()
            move(333, 35/scale)
            curve3(243, 0.6/scale, -1.2, 66)
            how_many = range(66)
            for curve in how_many:
                fd(0.6/scale)
                rt(1.6)
            fd(5.5/scale)
            move(333, 15/scale)
            end_fill()
            # Draw left eye pupil
            fillcolor('black')
            begin_fill()
            move(153, 2.1/scale)
            move(243)
            circle(11/scale, extent = 180)
            end_fill()
            # Navigate to the right eye
            repos(3, 150/scale)
            # Draw right eye
            fillcolor('white')
            begin_fill()
            move(203, 35/scale)
            curve3(293, 0.6/scale, 1.2, 66)
            for curve in how_many:
                fd(0.6/scale)
                lt(1.6)
            fd(5.5/scale)
            move(203, 15/scale)
            end_fill()
            # Draw right eye pupil
            fillcolor('black')
            begin_fill()
            move(27, 2.1/scale)
            move(297)
            circle(-11/scale, extent = 190)
            end_fill()
            
        def letter_A(): # Define letter A on forehead
            # Reposition turtle to the start of letter A
            repos(78, 40/scale)
            # Draw letter outer A on for head
            width(width1)
            fillcolor('white')
            begin_fill()
            move(112, 95/scale)
            move(182, 80/scale)
            move(248, 95/scale)
            move(335, 40/scale)
            lt(95)
            fd(35/scale)
            move(2, 50/scale)
            move(290, 30/scale)
            move(15, 44/scale)
            end_fill()
            # Reposition turtle to inner A
            repos(144, 71/scale)
            # Draw inner A
            fillcolor('light sky blue')
            begin_fill()
            move(110, 30/scale)
            move(182, 25/scale)
            move(260, 35/scale)
            move(3, 44/scale)
            move(110, 5/scale)
            end_fill()
            penup()

        def captain_america(): # Complete captain america for Suit D
            top_head()
            lower_head()
            legs()
            belt()
            left_foot()
            right_foot()
            torso_star()
            red_glove_1()
            red_glove_2()
            shield()
            left_horn()
            right_horn()
            two_eyes()
            letter_A()

        # Finally, insert captain america in the center of Suit D,
        # and enable him to be played in the game: patience.
        repos(200, 112) # Reposition captain america to the center of the card.
        captain_america()
        # Reposition turtle back to the start of the suit canvas
        repos(43.1236, 75.8665) 
        # Reset turtle back to the heading to facilitate drawing
        # of the next card suit.
        setheading(reset_heading) 
        
##########-------------------End of Captain America----------------------------#    

    def Joker(): # This suit will contain the Joker!!
        # Invoke the blank suit card to draw up the suit with unique
        # border colours and card colours.
        suit_canvas('medium slate blue', 'purple')
        # Assign variable to divide drawings to scale (adjustable). The
        # higher the scale, the smaller the drawing, vice-versa.
        scale = 4.55 # Here, 4.55 is the perfect size to fit within the suit.
        # Assign width variable to adjust the width for the drawing
        width1 = 3

        # Draw Joker
        # Make the pencolor 'black' to draw Joker's edges in black.
        pencolor('black')

        def Joker_whole_head():
            repos(50, 430/scale)
            width(width1)
            # Draw the head
            fillcolor('white')
            begin_fill()
            curve2(170, 15/scale, -1.1)
            curve2(240, 2.45/scale, -1.5)
            # Draw left ear
            curve2(110, 3/scale, -10)
            curve2(290, 2/scale, -2)
            # Continue drawing the head
            curve2(270, 3/scale, -1.2)
            curve2(290, 2/scale, -1)
            curve2(310, 5.3/scale, -2)
            curve2(310, 1.5/scale, 2)
            move(0, 65/scale)
            curve2(90, 1.5/scale, 2)
            curve2(355, 12.5/scale, -4.5)
            # Draw the Right ear
            curve2(30, 2/scale, -2)
            curve2(60, 3/scale, -10)
            curve2(76, 2.2/scale, -1)
            end_fill()
            # Make the width smaller since scaling joker will cause width
            # problems.
            small = 2.45
            width(small)
            # Navigate to the left eye
            repos(195, 325/scale)
            # Draw first eye
            fillcolor('sea green')
            begin_fill()
            move(333, 35/scale)
            curve3(243, 0.6/scale, -1.2, 66)
            how_many = range(66)
            for curve in how_many:
                fd(0.6/scale)
                rt(1.6)
            fd(5.8/scale)
            move(331, 15/scale)
            end_fill()
             # Draw left eye pupil
            move(153, 2.1/scale)
            fillcolor('black')
            begin_fill()
            move(243, 0/scale)
            circle(11/scale, extent = 180)
            end_fill()
            # Navigate to the right eye
            repos(2, 170/scale)
            # Draw right eye
            fillcolor('sea green')
            begin_fill()
            move(203, 35/scale)
            curve3(293, 0.6/scale, 1.2, 66)
            for curve in how_many:
                fd(0.6/scale)
                lt(1.6)
            fd(5.5/scale)
            move(203, 15/scale)
            end_fill()
            # Draw right eye pupil
            fillcolor('black')
            begin_fill()
            move(27, 2.1/scale)
            move(297)
            circle(-11/scale, extent = 190)
            end_fill()
            # Reset the width back to the default value
            width(width1)
     
        def Joker_hair():
            repos(160, 245/scale)
            width(width1)
            # begin drawing hair
            fillcolor('medium sea green')
            begin_fill()
            curve2(80, 2/scale)
            curve2(100, 6/scale, 2)
            curve2(60, 4/scale, 3.5)
            curve2(30, 12/scale, 3.5)
            draw_curve(355, -100/scale, 50)
            curve2(295, 4.5/scale, 2.5)
            curve2(250, 5/scale, 3)
            curve2(180, 6.5/scale, 0.8)
            curve2(160, 0.5/scale, -3)
            move(215, 60/scale)
            move(60, 30/scale)
            curve2(60, 0.5/scale, -3)
            curve2(124, 3/scale, -3)
            curve2(230, 0.5/scale, -3)
            curve2(280, 1/scale, 1)
            curve2(250, 3/scale, 2)
            curve2(200, 2/scale, 6)
            curve2(300, 1.5/scale, -7)
            curve2(90, 1.5/scale)
            curve2(220, 2.5/scale, 5)
            curve2(245, 1.1/scale, 4)
            end_fill()
            # Draw lines in the hair
            repos(30, 20/scale)
            curve2(108, 1.4/scale)
            repos(328, 60/scale)
            curve2(85, 3.5/scale, 1)
            curve2(50, 0.5/scale, 1)
            curve2(352, 6/scale, 4.5)
            repos(40, 75/scale)
            fillcolor('black')
            begin_fill()
            curve2(110, 7/scale, -3)
            curve2(338, 6.8/scale, 2)
            end_fill()
            repos(335, 50/scale)
            begin_fill()
            curve2(85, 9/scale, -4.5)
            curve2(344, 8.5/scale, 3.7)
            end_fill()
            repos(345, 30/scale)
            begin_fill()
            curve2(40, 7/scale, -6.5)
            curve2(335, 6.5/scale, 5.5)
            end_fill()
            # Draw right side burns
            repos(353, 89/scale)
            fillcolor('medium sea green')
            begin_fill()
            curve2(275, 3/scale, 1.5)
            curve2(95, 2.1/scale, -1.5)
            end_fill()
            
        def Joker_body_legs():
            width(width1)
            repos(235, 450/scale)
            fillcolor('blue violet')
            begin_fill()
            # Start drawing legs
            curve3(270, 16.129*2/scale, 1.6) 
            # Set the width to be small to minimize the width overlap that
            # the edge of the legs create on the left foot (this is a simple
            # fix, since the width of the boots sleeves and bottom leg
            # doubles the pen size).
            small = 0.5
            width(small)
            move(0, 28.22*2/scale)
            # Reset the width back to the default as its not on the edge of
            # the left foot.
            width(width1)
            curve3(50, 4.838*2/scale, 3) 
            move(0, 8.06/scale)
            curve3(278, 4.838*2/scale, 3)
            # Make the width smaller, as its on the right foot. This will
            # prevent the width overlap, as mentioned above.
            width(small)
            move(0, 28.22*2/scale)
            # Set the width back to the default value as it is no longer
            # on the right foot.
            width(width1)
            curve3(76, 16.129*2/scale, 1.6)
            end_fill()

        def Joker_top():
            # Draw top
            fillcolor('blue violet')
            begin_fill()
            curve2(90, 2.90*2/scale, -1)
            move(180, 120*2/scale)
            curve2(251.5, 2.90*2/scale, -1)
            end_fill()
            
        def Joker_foot(): # Draw left foot
            # Make the width smaller since scaling joker will cause width
            # problems.
            small = 2.49
            width(small)
            # Navigate to the left foot
            repos(245.5, 670/scale)
            # Do upper boot sleeves
            move(270) 
            fillcolor('white')
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(10*1.2/scale)
                lt(90)
                fd(47.5*1.2/scale)
                lt(90)
            end_fill()
            repos(275, 10*1.2/scale)
            # Draw boots
            width(small)
            begin_fill()
            curve3(300, 1.25*1.2/scale, 1)
            move(180)
            circle(12.5*1.2/scale, extent = 180)
            fd(25*1.2/scale)
            circle(12.5*1.2/scale, extent = 90)
            fd(22.5*1.2/scale)
            end_fill()
            # Draw right foot
            # Navigate to right foot
            repos(5, 118.75*1.2/scale)
            # Do upper boot sleeves
            move(270)
            how_many = range(2)
            begin_fill()
            for sleeves in how_many:
                fd(10*1.2/scale)
                rt(90)
                fd(47.5*1.2/scale)
                rt(90)
            end_fill()
            repos(260, 10*1.2/scale)
            # Draw boots
            begin_fill()
            curve3(240, 1.25*1.2/scale, -1)
            move(0)
            circle(-12.5*1.2/scale, extent = 180)
            fd(25*1.2/scale)
            circle(-12.5*1.2/scale, extent = 90)
            fd(22.5*1.2/scale)
            end_fill()
            # Reset the width back to the default value
            width(width1)

        def Joker_bow_tie():
            fillcolor('sea green')
            repos(96,395/scale)
            begin_fill()
            curve2(300, 2/scale, -3)
            curve2(0, 0.2/scale, -1)
            curve2(80, 2.5/scale, -1)
            curve2(170, 2/scale, -3)
            curve2(110, 0.5/scale, -3)
            curve2(170, 2/scale, -1.5)
            curve2(135, 2/scale, -3)
            curve2(260, 2.5/scale, -1)
            curve2(0, 2/scale, -3)
            curve2(290, 0.5/scale, -3)
            curve2(350, 2.2/scale, -1.5)
            end_fill()
            curve2(59.5, 1.1/scale, -3)
            repos(178, 48/scale)
            curve2(235, 1.1/scale, -3)

        def Joker_clothing():
            # Draw gold vest
            fillcolor('dark goldenrod')
            begin_fill()
            curve2(260, 9/scale, -1.2)
            curve2(10, 3/scale, 1)
            curve2(83, 8.9/scale, -1.2)
            curve2(200, 2.5/scale, 2)
            end_fill()
            # Write two J's on the torso
            repos(240, 150/scale)
            write('J', font=('Helvetica', int(100//scale), 'normal'))
            repos(0, 175/scale)
            write('J', font=('Helvetica', int(100//scale), 'normal'))
            # Draw next clothing
            repos(209.5, 210/scale)
            curve2(49, 14.6/scale, 5.2)
            repos(135, 33/scale)
            fillcolor('goldenrod')
            begin_fill()
            move(180, 207/scale)
            curve2(38.5, 11.1/scale, 4)
            end_fill()

        def Joker_mouth_ear_curve():
            # Navigate to Joker's Mouth
            repos(122, 327/scale)
            # Draw Joker Mouth
            curve2(338, 5.5/scale, -2.2)
            # Navigate to the right ear to draw crease
            repos(30.5, 195/scale)
            # Draw crease on right ear
            curve2(90, 0.5/scale)
            # Navigate to the left ear to draw crease
            repos(180, 384/scale)
            # Draw crease on left ear
            curve2(90, 0.5/scale, 0.5)
            
        def Joker_arms():
            # Draw left arm
            repos(289, 120/scale)
            fillcolor('blue violet')
            begin_fill()
            curve2(240, 7.75*1.8/scale, -2)
            curve2(320, 1.3*1.8/scale, -2)
            curve2(50, 0.8*1.8/scale, -2)
            curve2(109, 3.7*1.8/scale, 2)
            curve2(89, 3.1*1.8/scale, 0.9)
            end_fill()
            # Navigate to right arm
            repos(2, 149*1.8/scale)
            # Draw right arm
            begin_fill()
            curve2(300, 7*1.8/scale, 2)
            curve2(220, 1.3*1.8/scale, 2)
            curve2(130, 1*1.8/scale, 2)
            curve2(71, 3*1.8/scale, -2)
            curve2(94, 2.85*1.8/scale, -0.6)
            end_fill()
            # Reposition to the left hand
            repos(223, 348/scale)
            # Draw Joker card on hand
            seth(140)
            fillcolor('white')
            begin_fill()
            for joker_card in range(2):
                pd()
                fd(75/scale)
                lt(90)
                fd(50/scale)
                lt(90)
            end_fill()
            # Make the width smaller since scaling joker will cause width
            # problems.
            small = 2
            width(small)
            # Navigate to the card to draw the 'J'
            repos(174, 68/scale)
            move(50, 30/scale)
            move(50, -15/scale)
            move(320, 40/scale)
            curve2(240, 1/scale, 2)
            # Reset the width back to default
            width(width1)
            # Reposition to the right hand
            repos(7, 310/scale)
            # Draw Joker card on hand
            seth(40)
            fillcolor('white')
            begin_fill()
            for joker_card in range(2):
                pd()
                fd(75/scale)
                rt(90)
                fd(50/scale)
                rt(90)
            end_fill()
            # Make the width smaller since scaling joker will cause width
            # problems.
            small = 2
            width(small)
            # Navigate to the card to draw the 'J'
            repos(6, 68/scale)
            move(130, 30/scale)
            move(130, -15/scale)
            move(220, 40/scale)
            curve2(140, 0.8/scale, 2)
            # Make the width smaller since scaling joker will cause
            # width problems.
            small = 1
            width(small)
            # This is not related to the module, although joker's ears needs
            # some polishing.
            # Navigate to Joker's right ear to further put creases on there
            repos(81.5, 380/scale)
            # Draw crease
            curve2(10, 0.9/scale, 5)
            curve2(250, 1.2/scale, 3)
            # Reposition to the left ear
            repos(174, 395/scale)
            curve2(190, 0.7/scale, -5)
            curve2(300, 1/scale, -1.5)
        
        def Complete_Joker(): # Assimilate all of Joker's parts to one module.
            Joker_body_legs()
            Joker_top()
            Joker_whole_head()
            Joker_hair()
            Joker_foot()
            Joker_bow_tie()
            Joker_clothing()
            Joker_mouth_ear_curve()
            Joker_arms()

        # Finally, insert Joker in the center of the Joker Card,
        # and enable him to be played in the game: patience.
        repos(225, 50)
        Complete_Joker() # Invoke the Joker, providing the module is called!
        # Reposition turtle back to the start of the suit canvas
        repos(30.595338, 117.99309)
        # Reset turtle back to the heading to facilitate drawing
        # of the next card suit.
        setheading(reset_heading) 
    
##########--------END OF DRAWINGS. NEXT, ONTO LOGIC AND DECISIONS -------------#  

    # Access the stack_location global variable.
    # This particular global variable will determine where to place our
    # suit of cards
    global stack_locations
    # Using the global variable, define all 6 stack locations
    Stack_1 = stack_locations[0][1] # precise x & y coordinate of stack 1
    Stack_2 = stack_locations[1][1] # precise x & y coordinate of stack 2
    Stack_3 = stack_locations[2][1] # precise x & y coordinate of stack 3
    Stack_4 = stack_locations[3][1] # precise x & y coordinate of stack 4
    Stack_5 = stack_locations[4][1] # precise x & y coordinate of stack 5
    Stack_6 = stack_locations[5][1] # precise x & y coordinate of stack 6
    
    # Define constant variables for setheading() and moving forward():
    # If more than one card is specified in instruction[2], turtle needs to
    # rotate down to draw subsequent card.
    rotate_down = 270
    # If more than one card is specified in instruction[2], turtle needs to
    # move down to draw subsequent card.
    move_down = 47
    
    # Introduce another constant variable which will control the turtle heading
    # and facilitate the suits to be vertically aligned to any stack.
    # Since the stack locations start from a precise x coordinate of any
    # stack - intially, the cards which will be drawn will be off center
    # from any stack. Thus, to resolve this the heading will be brought back
    # to start (0), the turtle is moved forward half the suit length and rotate
    # 180 degrees to ensure the card drawing is centered to the stack.
    start_heading = 0
    
    # This variable will be used when the turtle goes to a new stack coordinate,
    # and will move 60 pixels at 0 degrees forward to facilitate the
    # centering of a card to a stack.
    center = 60
    # (Note: after 60 pixels have been moved, reset heading (180) will be acted,
    # each time a new card is about to be drawn, such that it will begin
    # drawing from left to right.)

    # These variables will be used to navigate up or down from drawing the
    # card suit face values in each stack.
    rotate_up, rotate_down = 90, 270 # rotate turtle up or down, respectively
    move_up1, move_down1 = 25, 25 # move turle up or down, respectively
    # Define dimensions of the card suits
    suit_length = 120
    suit_height = 180

    # Define one function to write Suit_A - D face values on each card.
    
    def Suit_face_value():
        # Lift the penup so we dont leave a trail when drawing face value
        penup()
        # Access the global variables to write a suit value on the top left
        # and bottom right corners of a card, each time a card is called.
        global suit_value
        global suit_value2
        # Define a gap variable since bat man's head is quite large!
        # This is so turtle doesnt right the face values on top.
        gap = 5
        # Head towards the far left corner of the suit
        forward(suit_length + gap)
        # Go downwards so that the face value isn't at the top edge
        setheading(rotate_down)
        forward(move_down1)
        # Define the r, g, b values, making them random using floating point
        # values with the uniform method
        r = uniform(0.0, 0.7) # The values are between 0.0 and 0.7 to avoid
        g = uniform(0.0, 0.7) # making the pen color too light.
        b = uniform(0.0, 0.7)
        # Set the pen color to a random r,g,b floating point color
        pencolor(r, g, b)
        # Write the face value using the next() method to iterate the list
        # to a new value each time a new card is drawn.
        write(next(suit_value), font=('Helvetica', 18, 'normal'))
        # Rotate the turtle back up to the start position
        setheading(rotate_up)
        forward(move_up1)
        setheading(start_heading)
        forward(suit_length + gap)
        # Draw the second face value on the bottom right corner.
        # Head towards the bottom right corner of the suit.
        setheading(rotate_down) 
        forward(suit_height + gap) # Move down to a good area to write.
        # Here we'll use the predefined function in the preamble
        # to write our face values on the bottom right corner upside down.
        write_upside_down(next(suit_value2), font=('Helvetica', 18, 'normal'))
        # Rotate the turtle back up to the start position.
        setheading(rotate_up)
        forward(suit_height + gap)
        
    # Define four functions Suit A - D to store their Card and Suit Value.
    # After drawing, the card will reposition down the stack with the pen
    # lifted up.
    def Card_Suit_A():
        # Call Suit A
        Suit_A()
        # Write a unique face value on Suit A.
        Suit_face_value()
        # Move down to the next position to begin drawing the next card
        repos(rotate_down, move_down)
        
    def Card_Suit_B():
        # Call Suit B
        Suit_B()
        # Write a unique face value on Suit B.
        Suit_face_value()
        # Move down to the next position to begin drawing the next card
        repos(rotate_down, move_down)

    def Card_Suit_C():
        # Call Suit C
        Suit_C()
        # Write a unique face value on Suit C.
        Suit_face_value()
        # Move down to the next position to begin drawing the next card
        repos(rotate_down, move_down)

    def Card_Suit_D():
        # Call Suit D
        Suit_D()
        # Write a unique face value on Suit D.
        Suit_face_value()
        # Move down to the next position to begin drawing the next card
        repos(rotate_down, move_down)
    
    # The purpose of defining this function is so that when the Joker card
    # is specified, it will draw joker without a face value.
    def call_joker():
        # Call Joker here and move to the next position
        how_many = range(1)
        for card in how_many:
            Joker()
            # Move down to the next position to begin drawing the next card
            repos(rotate_down, move_down)

    # Define a function to Bring the turtle back to start position after
    # drawing any card(s).
    def to_start_pos():
        setheading(start_heading)
        forward(center)

    # Define one function that instructs the turtle to move to the specfic stack
    # according to the instructions given by the random_game function
    def goto_stack(stack_num):
        # Lift the pen up since the turtle will be navigating to stack 1.
        penup()
        # go to the precise location of stack 1, using the stack locations.
        goto(stack_num)
        # Bring the turtle back to start position to begin drawing card(s).
        to_start_pos()
        
    # Define one function that instructs how many cards of a certain
    # suit type and the position of joker to draw out. This function will be
    # placed in the loop later where it will be called in each Stack
    # from 1 to 6, with it's suit name and suit type as parameters for the
    # execution of patience.
    def Cards_Amount(suit_name, suit_type):
        # Define all variables for the range of cards to draw:
        card_1, card_2, card_3 = range(1, 2), range(1, 3), range(1, 4)
        card_4, card_5, card_6 = range(1, 5), range(1, 6), range(1, 7)
        card_7, card_8, card_9 = range(1, 8), range(1, 9), range(1, 10)
        card_10, card_11, card_12 = range(1, 11), range(1, 12), range(1, 13)
        card_13 = range(1, 14)
            
        # Function to draw cards if there is a joker
        def cards_with_joker(card_amount, joker_position):
            for index in card_amount:
                # Invoke joker at a specific index position
                if index == joker_position:
                    call_joker()
                # Continue drawing the cards after invoking joker
                else:
                    suit_type()
        # Function to draw cards if there is no joker
        def card_no_joker(card_amount):
            for card in card_amount:
                suit_type()

        # Regarding to the Instruction[x] variable below, it is only relative
        # to when this function is placed in the loop later. The elements of
        # instruction[x] are the list values in any_game where the first,
        # second, third and fourth elements are 'Stack x', 'Suit x',
        # num of cards x and joker position x, respectively.
        # Here we will not use the first element of the instruction[0]
        # variable as we do not want too many nested if statements.
        # Instruction[0] variable will be defined later in the loop below this
        # function.
        # Note that we do not draw any cards if the number specified is 0.
        # If both conditions are true, move to the next condition
        if instruction[1] == suit_name and instruction[2] > 0:
            # If one card is specified, lets draw one in the stack.
            if instruction[2] == 1:
                # This means a joker exists, so draw cards with joker
                if instruction[3] == 1:
                    cards_with_joker(card_1, 1)
                # This means a joker doesn't exist, so draw cards without joker
                else:
                    card_no_joker(card_1)
            # If two cards are specified, lets draw two in the stack.
            elif instruction[2] == 2:
                if instruction[3] == 1:
                    cards_with_joker(card_2, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_2, 2)
                else:
                    card_no_joker(card_2)
            # If three cards are specified, lets draw three in the stack.
            elif instruction[2] == 3:
                if instruction[3] == 1:
                    cards_with_joker(card_3, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_3, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_3, 3)
                else:
                    card_no_joker(card_3)
            # If four cards are specified, lets draw four in the stack.
            elif instruction[2] == 4:
                if instruction[3] == 1:
                    cards_with_joker(card_4, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_4, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_4, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_4, 4)
                else:
                    card_no_joker(card_4)
            # If five cards are specified, lets draw five in the stack.
            elif instruction[2] == 5:
                if instruction[3] == 1:
                    cards_with_joker(card_5, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_5, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_5, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_5, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_5, 5)
                else:
                    card_no_joker(card_5)
            # If six cards are specified, lets draw six in the stack.
            elif instruction[2] == 6:
                if instruction[3] == 1:
                    cards_with_joker(card_6, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_6, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_6, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_6, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_6, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_6, 6)
                else:
                    card_no_joker(card_6)
            # If seven cards are specified, lets draw seven in the stack.
            elif instruction[2] == 7:
                if instruction[3] == 1:
                    cards_with_joker(card_7, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_7, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_7, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_7, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_7, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_7, 6)
                elif instruction[3] == 7:
                    cards_with_joker(card_7, 7)
                else:
                    card_no_joker(card_7)
            # If eight cards are specified, lets draw eight in the stack.
            elif instruction[2] == 8:
                if instruction[3] == 1:
                    cards_with_joker(card_8, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_8, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_8, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_8, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_8, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_8, 6)
                elif instruction[3] == 7:
                    cards_with_joker(card_8, 7)
                elif instruction[3] == 8:
                    cards_with_joker(card_8, 8)
                else:
                    card_no_joker(card_8)
            # If nine cards are specified, lets draw nine in the stack.
            elif instruction[2] == 9:
                if instruction[3] == 1:
                    cards_with_joker(card_9, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_9, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_9, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_9, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_9, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_9, 6)
                elif instruction[3] == 7:
                    cards_with_joker(card_9, 7)
                elif instruction[3] == 8:
                    cards_with_joker(card_9, 8)
                elif instruction[3] == 9:
                    cards_with_joker(card_9, 9)
                else:
                    card_no_joker(card_9)
            # If ten cards are specified, lets draw ten in the stack.
            elif instruction[2] == 10:
                if instruction[3] == 1:
                    cards_with_joker(card_10, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_10, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_10, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_10, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_10, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_10, 6)
                elif instruction[3] == 7:
                    cards_with_joker(card_10, 7)
                elif instruction[3] == 8:
                    cards_with_joker(card_10, 8)
                elif instruction[3] == 9:
                    cards_with_joker(card_10, 9)
                elif instruction[3] == 10:
                    cards_with_joker(card_10, 10)
                else:
                    card_no_joker(card_10)
            # If eleven cards are specified, lets draw eleven in the stack.
            elif instruction[2] == 11:
                if instruction[3] == 1:
                    cards_with_joker(card_11, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_11, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_11, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_11, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_11, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_11, 6)
                elif instruction[3] == 7:
                    cards_with_joker(card_11, 7)
                elif instruction[3] == 8:
                    cards_with_joker(card_11, 8)
                elif instruction[3] == 9:
                    cards_with_joker(card_11, 9)
                elif instruction[3] == 10:
                    cards_with_joker(card_11, 10)
                elif instruction[3] == 10:
                    cards_with_joker(card_11, 11)
                else:
                    card_no_joker(card_11)
            # If twelve cards are specified, lets draw twelve in the stack.
            elif instruction[2] == 12:
                if instruction[3] == 1:
                    cards_with_joker(card_12, 1)
                elif instruction[3] == 2:
                    cards_with_joker(card_12, 2)
                elif instruction[3] == 3:
                    cards_with_joker(card_12, 3)
                elif instruction[3] == 4:
                    cards_with_joker(card_12, 4)
                elif instruction[3] == 5:
                    cards_with_joker(card_12, 5)
                elif instruction[3] == 6:
                    cards_with_joker(card_12, 6)
                elif instruction[3] == 7:
                    cards_with_joker(card_12, 7)
                elif instruction[3] == 8:
                    cards_with_joker(card_12, 8)
                elif instruction[3] == 9:
                    cards_with_joker(card_12, 9)
                elif instruction[3] == 10:
                    cards_with_joker(card_12, 10)
                elif instruction[3] == 10:
                    cards_with_joker(card_12, 11)
                elif instruction[3] == 10:
                    cards_with_joker(card_12, 12)
                else:
                    card_no_joker(card_12)
            # If thirteen cards are specified, lets draw thirteen in the stack.
            else:
                if instruction[2] == 13:
                    if instruction[3] == 1:
                        cards_with_joker(card_13, 1)
                    elif instruction[3] == 2:
                        cards_with_joker(card_13, 2)
                    elif instruction[3] == 3:
                        cards_with_joker(card_13, 3)
                    elif instruction[3] == 4:
                        cards_with_joker(card_13, 4)
                    elif instruction[3] == 5:
                        cards_with_joker(card_13, 5)
                    elif instruction[3] == 6:
                        cards_with_joker(card_13, 6)
                    elif instruction[3] == 7:
                        cards_with_joker(card_13, 7)
                    elif instruction[3] == 8:
                        cards_with_joker(card_13, 8)
                    elif instruction[3] == 9:
                        cards_with_joker(card_13, 9)
                    elif instruction[3] == 10:
                        cards_with_joker(card_13, 10)
                    elif instruction[3] == 10:
                        cards_with_joker(card_13, 11)
                    elif instruction[3] == 10:
                        cards_with_joker(card_13, 12)
                    elif instruction[3] == 10:
                        cards_with_joker(card_13, 13)
                    else:
                        card_no_joker(card_13)

    # Perform a for loop on the argument any game, where the elements
    # in the list are iterated. The output of the iterated elements can
    # be controlled by instructions using conditional statements.
    # These instructions will ultimately allow for all fixed games
    # and random game() to be run through this function successfully.
    # The result will play a game of patience.
    
    for instruction in any_game:
        # If the first Instruction list value is equal to 'Stack 1', lets
        # redirect turtle to the x - y coordinate of Stack 1
        if instruction[0] == 'Stack 1':
            goto_stack(Stack_1)
            # Call a the cards suits A - D with Joker. The function
            # Card_Amount determines the number cards to draw based on a
            # game that is substituted on argument 'any_game' in deal cards.
            Cards_Amount('Suit A', Card_Suit_A)
            # If the suit is 'Suit B', lets Draw out Suit B, the amount of
            # cards required, and place Joker at a position if he exists
            Cards_Amount('Suit B', Card_Suit_B)
            # If the suit is 'Suit C', lets Draw out Suit C, the amount of
            # cards required, and place Joker at a position if he exists.
            Cards_Amount('Suit C', Card_Suit_C)
            # If the suit is 'Suit D', lets Draw out Suit D, the amount of
            # cards required, and place Joker at a position if he exists.
            Cards_Amount('Suit D', Card_Suit_D)
        # If stack 2, repeat process
        if instruction[0] == 'Stack 2':
            goto_stack(Stack_2)
            Cards_Amount('Suit A', Card_Suit_A)
            Cards_Amount('Suit B', Card_Suit_B)
            Cards_Amount('Suit C', Card_Suit_C)
            Cards_Amount('Suit D', Card_Suit_D)
        # If stack 3, repeat process
        if instruction[0] == 'Stack 3':
            goto_stack(Stack_3)
            Cards_Amount('Suit A', Card_Suit_A)
            Cards_Amount('Suit B', Card_Suit_B)
            Cards_Amount('Suit C', Card_Suit_C)
            Cards_Amount('Suit D', Card_Suit_D)
        # If stack 4, repeat process
        if instruction[0] == 'Stack 4':
            goto_stack(Stack_4)
            Cards_Amount('Suit A', Card_Suit_A)
            Cards_Amount('Suit B', Card_Suit_B)
            Cards_Amount('Suit C', Card_Suit_C)
            Cards_Amount('Suit D', Card_Suit_D)
        # If stack 5, repeat process
        if instruction[0] == 'Stack 5':
            goto_stack(Stack_5)
            Cards_Amount('Suit A', Card_Suit_A)
            Cards_Amount('Suit B', Card_Suit_B)
            Cards_Amount('Suit C', Card_Suit_C)
            Cards_Amount('Suit D', Card_Suit_D)
        # This must be 'stack 6'. # If stack 6, repeat process
        if instruction[0] == 'Stack 6':
            goto_stack(Stack_6)
            Cards_Amount('Suit A', Card_Suit_A)
            Cards_Amount('Suit B', Card_Suit_B)
            Cards_Amount('Suit C', Card_Suit_C)
            Cards_Amount('Suit D', Card_Suit_D)
            
##########------------------END OF LOGIC AND DECISIONS ------------------------#       

#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas(False)

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('slowest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("Marvel & DC Comics")

### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(fixed_game_0) # <-- used for code development only, not marking)
#deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas(True)

#--------------------------------------------------------------------#
