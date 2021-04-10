import pyautogui
import time 

# Used to click onto the tab with Spotify
# This will be different for you
pyautogui.click(1153,21)
time.sleep(1)

def checkScreen():
    if pyautogui.locateOnScreen("ads2.png", confidence = 0.9, grayscale = True):
        print("ad found")
        pyautogui.click(1153,21) # same idea as above, different coordinates for your screen
        time.sleep(1)
        # Refreshes the page in order to cancel the advertisement
        pyautogui.hotkey("ctrl", "r")
        time.sleep(10) 
        print("restarting")
        time.sleep(1)
        # Clicks on the play button
        playButton = pyautogui.locateOnScreen("playButton.png", grayscale=True)
        but_x = playButton[0] + 10
        but_y = playButton[1] + 10
        pyautogui.click(but_x, but_y)

while True:
    # Checks every 5 seconds (this is by no means mandatory)
    time.sleep(5)
    checkScreen()