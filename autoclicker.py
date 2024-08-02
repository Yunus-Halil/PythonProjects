import pyautogui
import time

def autoclick(interval):
    print("Ctrl+c to stop the autoclicker")
    try:
        while True:
            pyautogui.click()
            time.sleep(interval)
    except:
        print("\nAutoclicker stopped.")

if __name__ == "__main__":
    click_interval = float(input("Enter the click interval in seconds: "))
    autoclick(click_interval)




