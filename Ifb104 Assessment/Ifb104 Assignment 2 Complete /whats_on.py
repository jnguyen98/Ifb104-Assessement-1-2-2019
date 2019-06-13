
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10132767
#    Student name: JOHN NGUYEN
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  What's On?: Online Entertainment Planning Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for planning an entertainment schedule.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

# Import os module so that the webbrowser can open a html file from a local path
import os

# Import the Webbrowser module to open a html file from the tkinter gui
import webbrowser

# Import choice module to change colors & text of the progress_tracker
from random import choice

# Import reduce from the functools library which is used for the convenience
# of replacing multiple words contained within a string 
from functools import reduce

# Import itertools module to perform complex iteration on multiple lists
import itertools

#--------------------------------------------------------------------#

#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.

# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'

# Define the file path of the three pre-downloaded html webpages
Art_Path = 'Archive/Bne Art.html'
Zoo_Path = 'Archive/The Zoo.html'
Cinema_Path = 'Archive/Movies Coming Soon.html'

# Define the Urls of the three webpages pertaining to the event categories 
Art_Url = 'http://bneart.com/'
Zoo_Url = 'http://thezoo.com.au/'
Cinema_Url = 'https://www.fivestarcinemas.com.au/new-farm/coming-soon'

##----------FUNCTION AND METHOD TO SOURCE EVENT INFO FROM WEBPAGES------------##
# Define An Empty List variable to store titles, datetimes and images of events.
event_info = []

# Define a function to open and extract a particular catgegory page. 
def page_extract(stat_page, live_page, regex_title, regex_datetime, regex_img):
    # Access the event_info list to re-assign it as a flattened list later.
    global event_info
    # If offline mode is selected, open a specific archived file from a path
    if work_offline_selection.get() == True: 
        # If the offline checkbutton evaluates to true, open a static webpage.
        web_page_type = open(stat_page, encoding = 'UTF-8')
        # Read the archived file - allowing it to be extracted.
        html = web_page_type.read()
    else: # If the offline checkbutton evaluates to false, open a live webpage.
        web_page_type = urlopen(live_page)
        # Read and decode the live webpage - allowing it to be extracted.
        html = web_page_type.read().decode('UTF-8')
        
    # Find the event titles from html code using findall from the re module
    event_titles = findall(regex_title, html)
    # Create a list of 10 event titles. Not all unicodes are translated when
    # converted, the codes are replaced with their appropriate character.
    unicodes = ('&#038;', '&'), ('&#8230;', '...'), ('&#8211;', '–'), \
              ('&#8216;', '‘'), ('&#8217;', '’'), ('&#x27;', '’')
    title_list = [reduce(lambda uni_code, uni_char: uni_code.replace(*uni_char),
                       unicodes, title.strip()) for title in event_titles[0:10]]
    # Find the event datetime from html code using findall from the re module
    event_dates_times = findall(regex_datetime, html)
    # Create a list of 10 event date-times. Also, Strip and remove line breaks.
    datetime_list  = [datetime.replace('\n', '').strip() for datetime in\
                      event_dates_times[0:10]]
    # Find the event images from html code using findall from the re module
    event_images = findall(regex_img, html)
    # Extract the 10 image sources to the event image list
    image_list  = [image for image in event_images[0:10]]

    # The next step involves the concatenation of "each element" in the 3 lists
    # to produce a new list at alternating positions: e.g, ['title_1', 'date_1',
    # 'image_1', 'title_2'] etc. The itertools and zip method is used.
    merged_list = list(itertools.chain.from_iterable\
                       (zip(title_list, datetime_list, image_list)))
    # Append the merged list to the event_info list
    event_info.append(merged_list)
    # Flatten out the event_info list 
    event_info = [flatten for sublst in event_info for flatten in sublst]
    
##-----------------------EXTRACT FROM WEBPAGES 1, 2 & 3-----------------------## 
# Define webpage_1 where static and live event info can be sourced from here
def webpage_1():
    # Define a regular expression to find the the title of events from Bne Art
    Art_title = 'rel="bookmark">(.+)</a></h2>'
    # This regular expression will find the datetime of events from Bne Art
    Art_datetime = '<h5><span class="caps">WHEN</span> : (.+)</h5>'
    # Define a regular expression to find the images of events from Bne Art.
    Art_img = '<img width="[\d]+" height="[\d]+" src=(.+)class'
    # Call the function to extract either live or static webpage event details
    page_extract(Art_Path, Art_Url, Art_title, Art_datetime, Art_img)
        
# Define webpage_2 where static and live event info can be sourced from here
def webpage_2():
    # Define a regular expression to find the the title of events from The Zoo
    Zoo_title = '/">(.+)</a></h2>'
    # This regular expression will find the datetime of events from The Zoo
    Zoo_datetime = '<span class="like-nav custom-meta">([\w\s\d,:]+)</span>'
    # Define a regular expression to find the images of events from The Zoo.
    Zoo_img = '<img width=.+src=(".+")\sclass'
    # Call the function to extract either live or static webpage event details
    page_extract(Zoo_Path, Zoo_Url, Zoo_title, Zoo_datetime, Zoo_img)
    
# Define webpage_3 where static and live event info can be sourced from here    
def webpage_3():
    # Define a regular expression to find the title of events from the Cinema.
    Cinema_title = '<h2>(.+)</h2></a>'
    # This regular expression will find the datetime of events from the Cinema
    Cinema_datetime ='<p class="release-date">([\w\s\d]+)</p>'
    # Define a regular expression to find the images of events from the Cinema.
    Cinema_img = '<img src=(".+")\sclass="poster-portrait.+</a>'
    # Call the function to extract either live or static webpage event details
    page_extract(Cinema_Path,Cinema_Url,Cinema_title,Cinema_datetime,Cinema_img)

##----------METHODS TO RETURN EVENT INFO AND LIST OF EVENT CONTENTS-----------##

# Define a function to get the text and details of an event and number label.
def event(event_x, number_label = ''): # default number label equals nothing.
    # These variables from 1 - 10 entail 1 element: the title of the event
    title_1, title_2, title_3 = event_info[0], event_info[3], event_info[6]
    title_4, title_5, title_6 = event_info[9], event_info[12], event_info[15]
    title_7, title_8, title_9 = event_info[18], event_info[21], event_info[24]
    title_10 = event_info[27]
    # These variables 1 - 10 entail 1 element: the datetime of the event
    date_1, date_2, date_3 = event_info[1], event_info[4], event_info[7]
    date_4, date_5, date_6 = event_info[10], event_info[13], event_info[16]
    date_7, date_8, date_9 = event_info[19], event_info[22], event_info[25]
    date_10 = event_info[28]
    # These variables 1 - 10 entail 1 element: the image of the event
    image_1, image_2, image_3 = event_info[2], event_info[5], event_info[8]
    image_4, image_5, image_6 = event_info[11], event_info[14], event_info[17]
    image_7, image_8, image_9 = event_info[20], event_info[23], event_info[26]
    image_10 = event_info[29]
    # This variable adds a space between the concatenation of title and datetime
    pad = ' '
    # These two variables are used to bracket the datetime in the tkinter GUI.
    startb, endb = '(', ')'
    # If this condition is true, lets return the title and datetime of event 1
    if event_x == '1': # String argument '1' will name the first checkbutton
        # Concatenate number_label, title_1, a space and brackets around date_1.
        return number_label + title_1 + pad + startb + date_1 + endb
    # If this condition is true, lets return the title and datetime of event 2
    elif event_x == '2': 
        return number_label + title_2  + pad + startb + date_2 + endb
    elif event_x == '3': 
        return number_label + title_3  + pad + startb + date_3 + endb
    elif event_x == '4': 
        return number_label + title_4  + pad + startb + date_4 + endb
    elif event_x == '5': 
        return number_label + title_5  + pad + startb + date_5 + endb
    elif event_x == '6': 
        return number_label + title_6  + pad + startb + date_6 + endb
    elif event_x == '7': 
        return number_label + title_7  + pad + startb + date_7 + endb
    elif event_x == '8': 
        return number_label + title_8  + pad + startb + date_8 + endb
    elif event_x == '9':
        return number_label + title_9  + pad + startb + date_9 + endb
    elif event_x == '10':
        return number_label + title_10  + pad + startb + date_10 + endb
    # The next series will contain all 3 elements where arguments are bracketed.
    elif event_x == '(1)': # String argument '(1)' returns event 1 if selected.
        return title_1, image_1, date_1 
    elif event_x == '(2)':
        return title_2, image_2, date_2 
    elif event_x == '(3)': 
        return title_3, image_3, date_3
    elif event_x == '(4)': 
        return title_4, image_4, date_4
    elif event_x == '(5)': 
        return title_5, image_5, date_5
    elif event_x == '(6)': 
        return title_6, image_6, date_6
    elif event_x == '(7)':
        return title_7, image_7, date_7
    elif event_x == '(8)':
        return title_8, image_8, date_8
    elif event_x == '(9)':
        return title_9, image_9, date_9
    else:
        if event_x == '(10)':
            return title_10, image_10, date_10
    
# Define a function to return a list of events either for the planner or tk gui.
def list_events(string_value):
    # The list contains 10 events displaying text on the tkinter gui for later.
    tkinter_events = [event('1', '1: '), event('2', '2: '), event('3', '3: '),
                      event('4', '4: '), event('5', '5: '), event('6', '6: '),
                      event('7', '7: '), event('8', '8: '), event('9', '9: '),
                      event('10', '10: ')]
    # The list contains details of 10 events for adding to the planner later
    planner_events = [event('(1)'), event('(2)'), event('(3)'), event('(4)'),
                      event('(5)'), event('(6)'), event('(7)'), event('(8)'),
                      event('(9)'), event('(10)')]
    # If statements to return what value when the function is called:
    if string_value == 'tkinter': # If arg is 'tkinter' return tkinter events
        return tkinter_events
    if string_value == 'planner': # If arg is 'planner' return planner events
        return planner_events
        
##----------------------EXECUTION & TKINTER POP-UP WINDOW---------------------## 
# The lists below stores StringVar() variables to their respective event
# checkbuttons (where each event checkbutton state can be checked).
cba_value = [] 
cbm_value = [] 
cbc_value = []

# Define a function to set all the main widgets state, either disable or normal.
def widgets_state(state):
    # Create an empty list to append all the main widgets
    widgets = []
    # Append the widgets
    widgets.append([Art_button] + [Cinema_button] + [Music_button] + \
                   [Print_button] + [Offline_button])
    # Flatten out the list so that it can be iterated without nested looping.
    widgets = [flatten for sublist in widgets for flatten in sublist]
    # Turn on all the widgets if the argument string value is 'turn on'
    if state == 'turn on':
        for set_to in widgets:
            set_to['state'] = 'normal'
    else: # Turn off all the widgets if the arugment value is 'turn off'
        if state == 'turn off':                
            for set_to in widgets:
                set_to['state'] = 'disable'

# Function to change the label colors of a label type using the choice
# method. Choice method is used on a list of colors within its argument.
def update_color(label_type):
    label_type['fg'] = choice(['salmon', 'limegreen', 'mediumslateblue', 'blue',
                                  'darkmagenta', 'dark goldenrod', 'goldenrod',
                                  'midnight blue', 'dark red', 'dark green',
                                  'seagreen', 'darkviolet', 'mediumvioletred',
                                  'darkslateblue', 'olive', 'orangered',
                                   'maroon', 'peru', 'indigo', 'thistle',
                                   'steelblue', 'teal', 'chocolate', 'hotpink',
                                   'dodgerblue', 'plum', 'crimson', 'deeppink',
                                   'lightpink', 'lightseagreen', 'black',
                                   'lightslateblue', 'magenta4', 'maroon1',
                                   'maroon2', 'maroon3', 'maroon4', 'olivedrab',
                                   'mediumpurple1', 'mediumpurple2', 'orange4',
                                   'orchid1', 'orchid2', 'orchid3', 'orchid4'])
    
# The progress_tracker performs an update in the tkinter gui window.
def progress_tracker(update_text):
    # Call the function to provide a unique foreground color of the label
    update_color(Progress_label)
    # The process below updates the text
    Progress_label.config(text = update_text)
    main_window.update()

# Similar to above, repeat the same process for the open and save label text
def open_label(update_text):
    update_color(Open_label)
    Open_label.config(text = update_text)
    main_window.update()

# Provide a unique color for the save label text
def save_label(update_text):
    update_color(Save_label)
    Save_label.config(text = update_text)
    main_window.update()
    
# A Function to display a choice of text for the progress
# tracker when the category done buttons are pressed
def done_choice():
    # Update the progress tracker with a choice of text
    progress_tracker(choice(['Would you like to add more?', 'Done already?☹',
                             'Interesting...', 'Count your events!☑',
                             'Select more please!', 'Pick lots and lots! ☺',
                             'Are you ready to print?', 'Choose more and more!',
                             'You can\'t be done yet.. come on☹', 
                             'Oh, already done? Pick some more',
                             'Fill up your planner! Go, go, go!',
                             'I hope you made good choices! ☺',
                             'don\'t forget to print!✌❣',
                             'Are you having a good day?☀️',
                             'Pick at least 30 events ☺']))
    
# A Function to display a choice of text for the progress
# tracker when the program has printed the file.
def Printed_choice():
    progress_tracker(choice(['Printed! ❤', 'Done❣', 'Finished✅ ',
                             'Planner created!♥', 'Printed!',
                             'Planner Printed!✌']))

# Define a popup window a unique title based on online or offline mode
def popup_title(Toplevel_window, past_text, live_text):
    # This is offline mode give the title a past text, as events have occurred.
    if work_offline_selection.get() == 1: 
        Toplevel_window.title(past_text)
    else: # This must be online mode - give the title a live text
        Toplevel_window.title(live_text)

# Define a category label to display in each pop-up window in the Tkinter gui.
def c_label(Toplevel_window, text, bgcolor, fgcolor):
    # Define a margin for the event label 
    marginx , marginy = 85, 10
    event_label = Label(Toplevel_window, text = text, font = ('Helticava', 30),
                        bg = bgcolor, fg = fgcolor)\
                        .grid(row=0, padx=marginx, pady=marginy)

# Function to create and display the event checkbuttons in tkinter GUI.
def event_buttons(event_td, event_tdi, cbx_value, win, cbx, bgcolor,
                  activecolor, command_x):
    # Define the margin of x and y when padding the check buttons
    mx, my = 15, 10
    # Perform an enumerated loop and zip the two tkinter and planner event list
    # where they are assigned as event_td and event_tdi respectively.
    for num, (td, tdi) in enumerate(zip(event_td, event_tdi)):
        # Create a StringVar(), append it to the list and allocate it to the
        # check button variable so the string value states can be checked.
        # (Note: when a checkbutton is checked, the title, date and image
        # string will return an onvalue to said checkbutton).
        cbx_value.append(StringVar())
        # Define checkbuttons naming them as the first 10 events and titles.
        cbx.append(Checkbutton(win, text = td, variable = cbx_value[num],
                   bg = bgcolor, font = ('Helticava', 17), offvalue = '',
                   onvalue = tdi, activebackground = activecolor,
                   command = command_x))
        # Use the grid geometry manager to place 10 checkbuttons accordingly.
        cbx[num].grid(sticky='w', padx=mx, pady=my)
        
# Define a function to display a url text on the pop up window of a category
def url_label(win, url_text, bgcolor, fgcolor):
    # Define the margin of x and y when padding the Url label
    mx, my = 15, 10
    # Create the url label by adding attributes
    Url_label = Label(win, text = url_text,
                font = ('Helticava', 17), bg = bgcolor, fg = fgcolor)\
                .grid(row=11, sticky='w', padx = mx, pady = my)

# Create a done button for each category so users can exit the pop-up.
def done_button(win, bgcolor, fgcolor, row, margin, command_x):
    # Define the done button with some attributes
    Done = Button(win, text = ' Done ', borderwidth = 3, width = 7,
                  bg = bgcolor, fg = fgcolor, relief = 'raised',
                  state = 'normal', command = command_x)\
                  .grid(row=row, pady = margin)

# This updates the certain widgets when any event checkbox is selected 
def update_events_toggled():
    # Checking whether events from the any category have been selected    
    if cba_value[0].get() or cba_value[1].get() or cba_value[2].get() or\
       cba_value[3].get() or cba_value[4].get() or cba_value[5].get() or\
       cba_value[6].get() or cba_value[7].get() or cba_value[8].get() or\
       cba_value[9].get() or cbm_value[0].get() or cbm_value[1].get() or\
       cbm_value[2].get() or cbm_value[3].get() or cbm_value[4].get() or\
       cbm_value[5].get() or cbm_value[6].get() or cbm_value[7].get() or\
       cbm_value[8].get() or cbm_value[9].get() or cbc_value[0].get() or\
       cbc_value[1].get() or cbc_value[2].get() or cbc_value[3].get() or\
       cbc_value[4].get() or cbc_value[5].get() or cbc_value[6].get() or\
       cbc_value[7].get() or cbc_value[8].get() or cbc_value[9].get() == True:
        # Enable the categories and print button (in case user has printed)
        Print_button['state'] = 'normal'
        Art_button['state'] = 'normal'
        Music_button['state'] = 'normal'
        Cinema_button['state'] = 'normal'
        # Enable the offline button
        Offline_button['state'] = 'normal'
        # Hide the cinema ticket image label
        Ticket_label.grid_forget()
        # Unhide the save button by using the grid geometry manager
        Save_db_button.grid(row = 2, sticky = 'ne', padx = 35.5, pady=(105, 0))
        # If any event(s) are selected, update the progress tracker text
        progress_tracker('Event(s) are selected! ☺')
    else: # If no event(s) are selected, update the progress tracker text
        progress_tracker('No Event(s) selected ☹')
        # Unhide the cinema ticket image label
        Ticket_label.grid(row = 2, sticky = 'e', padx = (0, 20), pady = (50, 0))
        # Hide the save button and save label
        Save_db_button.grid_forget()
        Save_label.grid_forget()
           
# This function destroys a specific popup window when the done button is pressed
def update_done_pressed(popup_window):
    popup_window.destroy()
    # Call the function to update the progress tracker with a choice of text
    done_choice()
  
# Define a function to create a new window when the Art button is pressed
def Art_button_pressed(withdraw = False):
    # Reset the event info list when a category button is pressed
    del event_info[:]
    # Create a new 'top level' window for this cateogry
    Art_window = Toplevel()
    # If withdraw is true, this category pop up window is withdrawn.
    # (Head to the load_pages function below for explanation).
    if withdraw == True:
        Art_window.withdraw()
    # Set the background color of the window
    Art_window.configure(bg='light cyan')
    # Give the popup window a unique title based on online or offline mode
    popup_title(Art_window, 'Past Art events in Brisbane',
                'Upcoming Art events in Brisbane')
    # Create a category label for the Art category in the pop-up window
    c_label(Art_window, 'Art events in Brisbane:', 'light cyan', 'dark blue')
    # Call the webpage so that the event list below can source the information
    webpage_1()
    # Two event lists for the the tkinter gui and the planner, respectively
    Art_td, Art_tdi = list_events('tkinter'), list_events('planner')
    # Define a global list which will store the checkbuttons of this category
    global cba 
    cba = []
    # Call the function to create 10 check buttons for the art category
    event_buttons(Art_td, Art_tdi, cba_value, Art_window, cba, 'light cyan',
                  'pale turquoise', update_events_toggled)
    # Create a url label for this pop up window
    url_label(Art_window, 'http://bneart.com/', 'light cyan', 'dark blue')
    # Create a done button so users can exit the pop-up when finished.
    # (Lambda method allows parameters to be accepted in the command function.)
    done_button(Art_window, 'cyan', 'dark blue',
                11, 0, lambda:(update_done_pressed(Art_window)))

# Define a function to create a new window when the Music button is pressed
def Music_button_pressed(withdraw = False):
    # Reset the event info list when the music button is pressed
    del event_info[:]
    # Create a new 'top level' window for this cateogry
    Music_window = Toplevel()
    # If withdraw is true, the window is withdrawn
    if withdraw == True:
        Music_window.withdraw()
    # Set the background color of the window
    Music_window.configure(bg='light salmon')
    # Give the popup window a unique title based on online or offline mode
    popup_title(Music_window, 'Previous music events in Brisbane',
                'Live music events in Brisbane')
    # Create a category label for the Music category in the pop-up window
    c_label(Music_window,'Music events in Brisbane:','light salmon','dark red')
    # Call the webpage so that the event list below can source the information
    webpage_2()
    # Two event lists for the the tkinter gui and the planner, respectively
    Music_td, Music_tdi = list_events('tkinter'), list_events('planner')
    # Define a global list which will store the checkbuttons of this category
    global cbm 
    cbm = []
    # Call the function to create 10 check buttons for the music category
    event_buttons(Music_td, Music_tdi, cbm_value, Music_window, cbm,
                  'light salmon', 'light coral', update_events_toggled)
    # Create a url label for this pop up window
    url_label(Music_window, 'http://thezoo.com.au/', 'light salmon', 'dark red')
    # Create a done button so users can exit the pop-up when finished
    done_button(Music_window, 'salmon', 'dark red',
                11, 0, lambda:(update_done_pressed(Music_window)))
    
# Define a function to create a new window when the Cinema button is pressed        
def Cinema_button_pressed(withdraw = False):
    # Reset the event info list when the cinema button is pressed
    del event_info[:]
    # Create a new 'top level' window for this cateogry
    Cinema_window = Toplevel()
    # If withdraw is true, this category pop up window is withdrawn 
    if withdraw == True:
        Cinema_window.withdraw()
    # Set the background color of the window
    Cinema_window.configure(bg='light goldenrod')
    # Give the popup window a unique title based on online or offline mode
    popup_title(Cinema_window, 'Previous movies hosted in Newfarm Cinemas',
                'Upcoming movies hosting in Newfarm Cinemas')
    # Create an event label for the Cinema category in the pop-up window
    c_label(Cinema_window, 'Movies in New Farm Cinemas:', 'light goldenrod',
            'dark goldenrod')
    # Call the webpage so that the event list below can source the information
    webpage_3()
    # Two event lists for the the tkinter gui and the planner, respectively
    Cinema_td, Cinema_tdi = list_events('tkinter'), list_events('planner')
    # Define a global list which will store the checkbuttons of this category
    global cbc 
    cbc = []
    # Call the function to create 10 check buttons for the cinema category
    event_buttons(Cinema_td, Cinema_tdi, cbc_value, Cinema_window, cbc,
                  'light goldenrod', 'khaki1', update_events_toggled)
    # Creat the Url for the pop up window of this category
    url_label(Cinema_window,
              'https://www.fivestarcinemas.com.au/new-farm/coming-soon',
              'light goldenrod', 'dark goldenrod')
    # Create a done button so users can exit the pop-up when finished
    done_button(Cinema_window, 'goldenrod', 'dark goldenrod4',
                12, (0, 20), lambda:(update_done_pressed(Cinema_window)))

##---------------------------HTML CODE FOR PLANNER----------------------------##
# This html segment defines the html creation and cascading styling sheet. 
outcome_message1a = """
<!DOC TYPE HTML>
<html>
<head>
    <!-- Add a Meta Character set for unicodes -->
    <meta charset="UTF-8">
    <!-- Add a CSS style to the html document -->
    <style>
        body       {border: solid blue; border-width: thin;
                    background-color: rgb(165, 255, 255)}
        p          {text-align: center; color:rgb(0, 100, 255)}
        h1, h2     {text-align: center; color:rgb(0, 100, 255)}
        h3         {text-align: left; color:rgb(0, 100, 255)}
        td         {color: #000080}
        img        {border: 2px double #DAA520; border-radius: 2px;
                    padding: 1px}
        img.table  {max-width: 70%; max-height: auto}
        
    </style>
</head>
    <title> Your Entertainment Planner & Guide </title>
    <body>
        <h1>Your Entertainment Planner & Guide</h1>
        <p><img src='https://urlzs.com/TWNs'
        alt="Entertainment image photo" width='500' height='250'></p>
        <h2>This is an Itinerary containing your preferences</h2>
        
        <!-- The section below will include the selected events -->
        <table align='center'; style="width:500px"; border="solid";
               cellpadding='15'>
        """
# This segment will be used to store events inside.
outcome_message1b = ""

# This is the references segment of the html planner
outcome_message1c = """
        </table>
    <!-- Create a series of spacing between the tables above and below -->
        <br><br><br></br></br></br>
        <!-- Write a list of references in a table-->
        <table align="center">
            <td>
            <h3>Events Sourced from</h3>
            <ul align='left'>
               <li><a href='http://bneart.com/'</a>http://bneart.com/</li>
               <li><a href='http://thezoo.com.au/'</a>http://thezoo.com.au/</li>
               <li><a href=
               'https://www.fivestarcinemas.com.au/new-farm/coming-soon'</a>
               https://www.fivestarcinemas.com.au/new-farm/coming-soon</li>
            <td>
            </ul>
        </table>
    </body>
</html>"""

# This outcome will display no events as users have not made a selection.
outcome_message2 = """
<!DOC TYPE HTML>
<html>
<head>
    <!-- Add a Meta Character set for unicodes -->
    <meta charset="UTF-8">
    <!-- Add a CSS style to the html document -->
    <style>
        body       {border: solid blue; border-width: thin;
                    background-color: rgb(165, 255, 255)}
        p          {color:rgb(0, 100, 255)}
        h1, h2     {text-align: center; color:rgb(0, 100, 255)}
        h3         {text-align: left; color:rgb(0, 100, 255)}
        img        {border: 1px solid #DAA520; border-radius: 2px;
                    padding: 1px}
    </style>
</head>
    <title> Your Entertainment Planner & Guide </title>
    <body>
        <h1>Your Entertainment Planner & Guide</h1>
        <p align="center"><img src='https://urlzs.com/TWNs'
        alt="Entertainment image photo" width='500' height='250'></p>
        <h2>This is an Itinerary containing your preferences</h2><br>
        <h1>You have not chosen any events</h1>
        <h2>Please select some entertaining events next time</h2>
        <h2> Thank you! </h2>
    <!-- Create a series of spacing between the table below and text above -->
        <br><br><br><br></br></br></br></br>
    <!-- Write a list of references in a table-->
        <table align="center">
            <td>
            <h3>Events Sourced from</h3>
            <ul align='left'>
               <li><a href='http://bneart.com/'</a>http://bneart.com/</li>
               <li><a href='http://thezoo.com.au/'</a>http://thezoo.com.au/</li>
               <li><a href=
               'https://www.fivestarcinemas.com.au/new-farm/coming-soon'</a>
               https://www.fivestarcinemas.com.au/new-farm/coming-soon</li>
            <td>
            </ul>
        </table>
    </body>
</html>"""

##---------------------WRITING EVENTS INTO HTML AND DATABASE------------------##
# Define an empty list stores selected events from all categories in the tk gui.
s_events_list = []

# Add contents to a string. The contents are the selected events from the gui
def table_events():
    # This is the string to store the selected events from the tkinter gui
    events = ""
    # Only add contents if at least one event has been selected
    if len(s_events_list) > 0:
        # For each event element - title, image and date - add to the string.
        for add in s_events_list:
                # Add the titles, images and datetime into the string
                events = events + '<tr><td width=\'100%\'; height=\'100%\'>'\
                                + '<center><big><strong>'\
                                + add[0] + '</big></strong>'\
                                + '<br><br>'\
                                + '<img class="table" src=' \
                                + add[1] + '>'\
                                + '<strong><br><br>' + 'When: '\
                                + add[2] + '</strong></center></td></tr>'
    # The event components containing title, image and date are added
    outcome_message1b = events
    # Return the outcome message as 1b, providing the function is called.
    return outcome_message1b
    
# Function that formats the the selected events list which allows
# events to be writed into the database or added to the html planner. 
def events_to_write():
    # Make the list global so it can be accessed externally
    global s_events_list
    # This is a list of 30 checkboxes combining the three categories 
    all_checkbox =  [cba_value[0].get(), cba_value[1].get(), cba_value[2].get(), 
                     cba_value[3].get(), cba_value[4].get(), cba_value[5].get(),
                     cba_value[6].get(), cba_value[7].get(), cba_value[8].get(),
                     cba_value[9].get(), cbm_value[0].get(), cbm_value[1].get(),
                     cbm_value[2].get(), cbm_value[3].get(), cbm_value[4].get(),
                     cbm_value[5].get(), cbm_value[6].get(), cbm_value[7].get(),
                     cbm_value[8].get(), cbm_value[9].get(), cbc_value[0].get(),
                     cbc_value[1].get(), cbc_value[2].get(), cbc_value[3].get(),
                     cbc_value[4].get(), cbc_value[5].get(), cbc_value[6].get(),
                     cbc_value[7].get(), cbc_value[8].get(), cbc_value[9].get()]
    # Append the list so the string_var can return a string of an
    # event when a check button is either checked or unchecked.
    s_events_list.append(all_checkbox)
    # Flatten out the selected events list
    s_events_list = [flatten for sub in s_events_list for flatten in sub]

    # Convert the list to a string using the join method (to prepare for split)
    s_events_list = ''.join(s_events_list)
    # re.split method will be used to divide the string where there are repeat-
    # ing occurrences of brackets. The list will have the 3 elements separated.
    s_events_list = re.split('[{}]+', s_events_list)
    # After splitting the list and when an event is unchecked, the string values
    # of ('') and (' ') are present. Thus, remove the empty values from the list
    s_events_list = [char for char in s_events_list if char not in ('', ' ')]

    # The next step will prepare the list so that events can be sorted by
    # strictly date and month. Reduce method is used to replace multiple strings
    all_days = ('Monday, ', ''), ('Tuesday, ', ''), ('Wednesday, ', ''), \
              ('Thursday, ', ''), ('Friday, ', ''), ('Saturday, ', ''),\
              ('Sunday, ', '')
    # Re-assign the list where all days of the week are replaced with nil ''.
    s_events_list = [reduce(lambda day, nil: day.replace(*nil), all_days, day)\
                     for day in s_events_list]
    # For every 3 elements make the list into a list with sublists. Thus, every
    # 'single' digit index will contain 3 elements: title, datetime and image.
    s_events_list = [s_events_list[divide: divide + 3] for divide in range\
                     (0, len(s_events_list), 3)]
    # Sort the list by date & month using the sorted function.
    s_events_list = sorted(s_events_list, key = lambda event: event[2])
    
    # Return the formatted selected events list
    return s_events_list

# Function that determines which sort of outcome will display in the html doc.
def create_planner():
    # If no events are selected in all 27 event checkboxes, do the following:
    if len(s_events_list) == 0:
        # Open and create a new html file under the name 'planner'
        file = open('planner.html', 'w')
        # Write outcome_message 2, which will display no events
        file.write(outcome_message2)
        # Close the file
        file.close()
    else:# If events are selected, create a html document
         # And write the contents of the events inside. 
        if len(s_events_list) > 0:
            # Open and create a new html file under the name 'planner'
            file = open('planner.html', 'w')
            # Write the outcome messages and call the table events into the file
            file.write(outcome_message1a + table_events() + outcome_message1c)
            # Close the file
            file.close()

# Function to save selected events to the database upon printing the planner.
def save_database():    
    # Make a connection to the entertainment planner database
    link = connect(database = "entertainment_planner.db")
    
    # Get a cursor on the database
    events = link.cursor()
    
    # Query to clear the databases events table
    clear_db = "DELETE FROM events"
    
    # Query to add events into the database
    add_db = "INSERT INTO events(event_name, event_date) VALUES"
    
    # Call this function so events can be added to the database accordingly.
    events_to_write()
    
    # If arrangements to add events to db based on how many are selected
    if len(s_events_list) == 1:
        # Update the progress tracker!
        progress_tracker('Your choice is saved!')
        add_db = add_db + \
             "('" + s_events_list[0][0] + "','" + s_events_list[0][2] + "')"
    elif len(s_events_list) == 2:
        # Update the progress tracker!
        progress_tracker('A couple of your choices are saved!')
        add_db = add_db + \
          "('" + s_events_list[0][0] + "','" + s_events_list[0][2] + "'),"+\
          "('" + s_events_list[1][0] + "','" + s_events_list[1][2] + "')"
    # If the amount is greater than 2, perform a loop to add events
    elif len(s_events_list) > 2:
        # Update the progress tracker!
        progress_tracker('You saved a lot of choices! ☺ ')
        # Create two variables to insert more than two tuples simultaneously
        lots_events = s_events_list
        # This variable stores the last event in the list
        end_event = s_events_list[-1]
        # For each event excluding the last event with index [0:-1]
        for event in lots_events[0:-1]:
            add_db = add_db + "('" + event[0] + "','" + event[2] + "'),"
        # Insert the last value with a close ')' to end the dml statement.
        add_db = add_db + "('" + end_event[0] + "','" + end_event[2] + "')"
    else: # This means there are no db events selected so lets add nothing
        if len(s_events_list) == 0:
            # Update the progress tracker!
            progress_tracker('You saved an empty planner ☹')
            # Add a blank value to both columns in the table
            add_db = add_db + "('" + "','" + "')"
            
    # Execute both statements
    events.execute(clear_db)
    events.execute(add_db)
    
    # Commit the changes to the database
    link.commit()
    
    # Close the cursor and the connection
    events.close()
    link.close()
    
    # Clear the selected events list after saving events into the database 
    del s_events_list[:]
    
    # Hide the save button and clear the save label text
    Save_db_button.grid_forget()
    save_label('')
    
##---------METHODS TO LOAD PAGES, PRINT PLANNER AND OTHER FEATURES------------##

# Function to load all pages at startup, when printing and toggling offline mode
def load_pages():
    # Define a function to call the three webpages and withdraw them immediately
    def invoke_pages():
        Art_button_pressed(True) # True withdraws the window upon opening.
        Music_button_pressed(True)
        Cinema_button_pressed(True)
    # To speed up the process when booting the program it is ideal that live
    # webpages should not be loaded as it will take longer to load the program.
    # This is required when toggling the offline button and printing the planner
    if work_offline_selection.get() == False:
        Offline_button.select()
        invoke_pages()
        Offline_button.deselect()
    else:# If user decides to work offline, the selection won't be reverted.
        if work_offline_selection.get() == True:
            invoke_pages()
        
# Function that binds to the print button. It will export a html document.
def Print_planner():
    # Call the function pack the additional widgets
    additional_widgets('pack')
    # Enable the save button when the planner is printed
    Save_db_button['state'] = 'normal'
    # Call the function to load the pages so the new planner button can function
    load_pages()
    # Call the function to to make events writeable and create the planner
    events_to_write()
    create_planner()
    # When the file is printed, call the function to display a choice of text
    Printed_choice()
    # Disable all the main widgets when the planner has finished.
    widgets_state('turn off')
    # Hide all the Extra images (except movie reel & music notes) from window
    extra_images('hide')
    # Update the open label to direct users to the open button or make new
    open_label('☚☚ \n open/ \n new')
    # Update the save label to direct users for their option to save
    save_label('☛☛ \n save!')
    # Clear the selected events list for the next selection
    del s_events_list[:]

# Function to bind to the 'Open button'. Opens the local html file to a browser
def Open_planner():
    # Hide the open button when it is pressed!
    Open_button.grid_forget()
    # Use the os path method to open the html file from a local directory
    local_dir = os.path.dirname(os.path.abspath(__file__))
    # Use the webbrowser method with local_dir as the parameter
    webbrowser.open('file://' + os.path.join(local_dir, 'Planner.html'))
    # Update the progress tracker and the open label after file has been opened.
    progress_tracker('Planner Opened!')
    # Update the open label text to 'new'
    open_label('☚☚ \n new')

# Function to change the text mode of category labels when
# the new or offline buttons are pressed
def category_text(mode):
    # Change the text of the 3 categories to live text
    if mode == 'online': 
        Art_button['text'] = ' New Art/works! '
        Music_button['text'] = ' Live Music! '
        Cinema_button['text'] = ' Upcoming Movies! '
    # Change the text of the 3 categories to past text
    if mode == 'offline': 
        Art_button['text'] = '  Former Art/works!  '
        Music_button['text'] = '  Past Music!  '
        Cinema_button['text'] = '  Past Movies!  '

# Function to deselect the event check buttons and/or offline button
def deselect_cb(action):
    # Define a variable to store all the event check buttons
    all_cb = cba + cbm + cbc
    # A variable to store all the event check buttons and the offline button
    all_cb_offline = cba + cbm + cbc + [Offline_button]
    if action == 'event cb':
        for checkbutton in all_cb:
            # Deselect method unchecks the event checkbuttons
            checkbutton.deselect()
    if action == 'event cb & offline':
        for checkbutton in all_cb_offline:
            # Deselect method unchecks the event checkbuttons
            checkbutton.deselect()
        

# Function to bind to the 'New button'. Creates a new planner.
def Start_new_planner():
    # Call the function Hide the additional widgets
    additional_widgets('hide')
    # Disable the save button when the new button is pressed
    Save_db_button['state'] = 'disable'
    # Using the grid manager - repack all the hidden images to the main window
    extra_images('pack')
    # Set all main widget states to normal, so that users can make a new planner
    widgets_state('turn on')
    # Deselect all the event check buttons and the offline button
    deselect_cb('event cb & offline')
    # Thereafter, the update the progress tracker with 'new planner created'.
    progress_tracker('New Planner Created!')
    # Clear the open and save label text
    open_label('')
    save_label('')
    # Change the text of the 3 category buttons back to live text
    category_text('online')

# Function to bind to the offline button.
def update_offline():
    # Call the function to load the pages to facilitate the process below
    load_pages()
    # If statement to process outcomes based on toggling the offline button:
    if work_offline_selection.get() == True:
        # Update the display of the progress_tracker label to offline mode
        progress_tracker('you are working offline! ☜')
        # Call the function to change the text of the 3 categories to past text
        category_text('offline')
        # the event checkboxes are deselected upon toggling the offline button.
        deselect_cb('event cb')
    else:# When offline mode is deselected - revert back to the original text.
        # Update the display of the progress tracker label to online mode
        progress_tracker('you are working online! ☞')
        # Call the function to change the 3 category buttons to present text
        category_text('online')
        # the event checkboxes are deselected upon toggling the offline button.
        deselect_cb('event cb')

##--------------------MAIN_WINDOW GRAPHICAL USER INTERFACE--------------------##
# Create the main window
main_window = Tk()

# Give the main window a title
main_window.title('Your Entertainment Planner & Guide')

# Change the background color of main window to light blue
main_window.configure(bg='pale turquoise')

# Import the entertainment guide image to display in the main window
entertainment_guide_image = PhotoImage(file = 'Assignment2-WhatsOn.png')
# Add the image by defining a label.                          
Image_label = Label(main_window, image = entertainment_guide_image,
                    bg = 'pale turquoise')

# Define extra photo images by assigning file images from a local folder
Movie_img = PhotoImage(file = 'Image1.png')
Note_img = PhotoImage(file = 'Image2.png')
Hat_img = PhotoImage(file = 'Image3.png')
Mask_img = PhotoImage(file = 'Image4.png')
Ticket_img = PhotoImage(file = 'Image5.png')

# Place the extra photo images in a label
Movie_label = Label(main_window, image = Movie_img, bg = 'pale turquoise')
Note_label = Label(main_window, image = Note_img, bg = 'pale turquoise')
Hat_label = Label(main_window, image = Hat_img, bg = 'pale turquoise')
Mask_label = Label(main_window, image = Mask_img, bg = 'pale turquoise')
Ticket_label = Label(main_window, image = Ticket_img, bg = 'pale turquoise')

# Create a label with text displaying
# alternatives for either save to db or work offline.
Alternatives_label = Label(main_window, text='Alternatives:',
                     font = ('Helticava', 20), bg='pale turquoise',
                     anchor='se') # Use anchor to align text south east

# Create an Intvar variable that can check the state of the offline checkbutton. 
work_offline_selection = IntVar()

# Create an Intvar variable that can check the state of the SaveDB checkbutton.
save_to_db_selection = IntVar()

# Create a work offline button
Offline_button = Checkbutton(main_window, text = 'Work offline',
                             variable = work_offline_selection,
                             font = ('Helticava', 17), bg = 'pale turquoise',
                             state = 'normal', command = update_offline)

# Create a save to db button which will appear when an event is selected
Save_db_button = Button(main_window, text = '   Save ✍️',
                        width = 8, relief = 'raised',
                        borderwidth = 3, font = ('Helticava', 17),
                        bg = 'goldenrod2', activebackground = 'gold',
                        highlightbackground = 'goldenrod2', 
                        state = 'disable', command = save_database)

# Create a save label which will appear after printing
Save_label = Label(main_window, text = '', font = ('Helticava', 15),
                   bg='pale turquoise')

# Create an "event categories" label frame for the 3 category widgets
Event_categories = LabelFrame(main_window, relief = 'ridge',
                              font = ('Helticava', 22), borderwidth = 2,
                              text = 'Event categories', bg='pale turquoise')

# Create the three category buttons for Art, Music and Cinema.
Art_button = Button(Event_categories, text = ' New Art/works! ',
                    relief = 'raised', activebackground = 'turquoise',
                    activeforeground = 'cyan', fg = 'blue', state = 'normal', 
                    font = ('Helticava', 22), bg = 'midnight blue',
                    highlightbackground = 'deep sky blue',
                    command = Art_button_pressed)

Music_button = Button(Event_categories, text = ' Live Music! ', fg = 'red',
                      relief = 'raised', activebackground = 'light coral',
                      activeforeground = 'crimson', bg = 'dark red',
                      highlightbackground = 'crimson',
                      font = ('Helticava', 22), state = 'normal',
                      command = Music_button_pressed)

Cinema_button = Button(Event_categories, text = ' Upcoming Movies! ',
                       relief = 'raised', activebackground = 'khaki1',
                       bg = 'dark goldenrod4', fg = 'dark goldenrod2',
                       highlightbackground = 'gold',
                       font = ('Helticava', 22), activeforeground = 'gold',
                       state = 'normal', command = Cinema_button_pressed)

# Create a Print button to export a html doc. 
Print_button = Button(main_window, text = ' Print Planner ☺ ',
                      relief = 'raised', fg = 'midnight blue',
                      bg = 'deepskyblue', activeforeground = 'turquoise',
                      activebackground = 'cyan', font = ('Helticava', 20),
                      highlightbackground = 'limegreen',
                      state = 'normal', command = Print_planner)

# Create a Progress label, which is originally set to empty string ''.
# It will become updated each time the progress tracker is called.
Progress_label = Label(main_window, text= '',
                       font = ('Helticava', 20),   bg='pale turquoise')

# Create a features labelframe named as: ' Extra Widgets '.
Features = LabelFrame(main_window, text = ' Extras ',
                       relief = 'ridge', font = ('Helticava', 20),
                       bg='pale turquoise',  fg = 'black')

# Create a 'New' button for users who wish to make a new preference.
# The button will not appear until the print button is pressed
New_button = Button(Features, text = ' New ', fg = 'midnight blue',
                    font = ('Helticava', 16), state = 'normal',
                    relief = 'raised', command = Start_new_planner)

# Create an 'Open' button for users who wish to view planner after printing it.
# The button will not appear until the print button is pressed
Open_button = Button(Features, text = ' Open ', fg = 'midnight blue',
                    font = ('Helticava', 16), state = 'normal',
                    relief = 'raised', command = Open_planner)

# Open label displays an arrow to open the html file upon printing the planner
Open_label = Label(main_window, text = '', font = ('Helticava', 15),
                   bg='pale turquoise')


# Constants for padding the x and y margin for the categories label frame
lb_marginx, lb_marginy = 30, 20

# Use the grid geometry manager to put the four category buttons into
# event_categories label frame.
Art_button.grid(row = 3, column = 0, sticky='w', padx = lb_marginx,
                pady = lb_marginy)
Cinema_button.grid(row = 3, column = 1, sticky='w', padx = lb_marginx,
                   pady = lb_marginy)
Music_button.grid(row = 3, column = 2, sticky='w', padx = lb_marginx,
                  pady=lb_marginy)

# Using the geometry grid manager, assign all main widgets into the main window
# where their positions will be determined by the row, column pad specifications
Image_label.grid(row = 0, pady = 30) 
Event_categories.grid(row = 1, padx = 30)
Alternatives_label.grid(row = 2, sticky = 'ne', padx = 30, pady = (33, 0))
Offline_button.grid(row = 2, sticky = 'ne', padx = 30, pady = (68, 0))
Print_button.grid(row = 2, sticky = 'n', padx = (37.5, 0), pady = (65, 0))
Progress_label.grid(row = 2, sticky = 'n', padx = (45, 0), pady = (152.9, 24))

# Function to pack or hide additional widgets when certain buttons are pressed.
def additional_widgets(action):
    # Use the grid geometry manager to pack the widgets if argument is 'pack'.
    if action == 'pack':
        # Use the grid geometry manager to pack the extra labels and widgets
        New_button.grid(row = 2, sticky = 'nw', padx = 7, pady = 7)
        Open_button.grid(row = 2, column = 2, sticky = 'ne', padx = 7, pady = 7)
        Save_db_button.grid(row = 2, sticky = 'ne', padx = 35.5, pady = (105, 0))
        Features.grid(row = 2, sticky = 'nw', padx = (30, 0), pady = (30,0))
        Open_label.grid(row = 2, sticky = 'nw', padx = (212.5,0), pady = (67,0))
        Save_label.grid(row = 2, sticky = 'ne', padx = 150.5, pady = (105, 0))
    # Hide the extra labels and widgets if string argument is hide
    if action == 'hide':
        New_button.grid_forget()
        Open_button.grid_forget()
        Save_db_button.grid_forget()
        Features.grid_forget()
        Open_label.grid_forget()
        Save_label.grid_forget()
        
# Function to pack or hide extra images when the new or print button is pressed.
def extra_images(action):
    # Use the grid geometry manager to pack the images if argument is 'pack'.
    if action == 'pack':
        Movie_label.grid(row=0, sticky = 'se', padx = (0,120), pady = (190, 0))
        Note_label.grid(row=0, sticky = 's', padx = (0,180), pady = (235, 0))
        Hat_label.grid(row = 2, sticky = 'nw', padx = 30, pady = (35, 0))
        Mask_label.grid(row = 2, sticky = 'nw', padx = 140, pady = (35, 0))
        Ticket_label.grid(row = 2, sticky = 'e', padx = (0, 20), pady = (50, 0))
    # Hide the images (excluding film reel & music notes) if string arg is hide.
    if action == 'hide':
        Hat_label.grid_forget()
        Mask_label.grid_forget()
        Ticket_label.grid_forget()

# Pack the extra images into the main window. 
extra_images('pack')

# Load the webpages when the program is opened
load_pages()

# Start the event loop to react to user inputs
main_window.mainloop()
