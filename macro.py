import pyautogui as ui
import pyperclip as cp
import time
import sys
import pandas as pd

df = pd.read_excel('감정단어사전0603.xlsx', sheet_name='Sheet1')
good_words = df[df['감정범주'].isin(['기쁨','흥미'])].sort_values(by='감정정도M', ascending=False)[:50][['단어']].values.flatten()
bad_words = df[df['감정범주'].isin(['공포','놀람','분노','슬픔','통증','혐오'])].sort_values(by='감정정도M', ascending=False)[:50][['단어']].values.flatten()

print(good_words)
print(bad_words)

def click(x, y):
    time.sleep(0.5)
    ui.moveTo(x, y)
    ui.click(clicks=1)
    # time.sleep(0.5)

def regist(words, x, y):
    for i in range(len(words)):
        # 데이터 추가 버튼
        click(x, y)
        # 데이터 입력칸
        click(620, 929)
        cp.copy(words[i])
        ui.hotkey('ctrl', 'v')
        # 추가 버튼
        click(875, 1041)

regist(good_words, 381, 1306)
regist(bad_words, 1133, 1303)
