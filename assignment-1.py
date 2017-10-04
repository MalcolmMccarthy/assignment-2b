# Created by: Malcolm McCarthy
# Created on: Sep 2017
# Created for: ICS3U
# This program calculates the height of an object dropped from 100m,
#   when you give it the seconds

import ui

def calculate_button_touch_up_inside(sender):
	
 GRAVITY = 9.81

 seconds = int(view['seconds_textbox'].text)	

 height = 100 - 0.5 * GRAVITY * seconds

 view['answer_label'].text = "After " + str(seconds) + 'seconds, the height is:' + str(height) + ' m '

view = ui.load_view()
view.present('sheet')
