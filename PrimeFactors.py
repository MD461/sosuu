# coding:utf-8
import math
import random
import tkinter as tk
import tkinter.messagebox as tmsg
import tkinter.ttk as ttk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width = 600, height = 400)
canvas.pack()


# 素数判定
def judge_prime_factor(N):
    i = 2
    flg = True  # True=素数
    PF = "" # 素因数を入れる変数
    while i < N:    # 2から判定する数-1までの数で割る
        if N % i == 0:  #
            PF += f"{i}×"
            N = N // i
            flg = False
        else:
            i += 1

    if flg == True: #1度も割れる数がない場合
        return f"{N}は素数です"
    else:
        return PF + str(N)

# 山札作成(文字、数字、画像)
def make_deck():
    return [(m, n, tk.PhotoImage(file=f"gif/{m}{n}.gif")) for m in ["c","d","h","s"] for n in range(1,14)]

# 山札からランダムに選んだ1枚を手札に加え山札から消す
def draw(hand,n):
    for _ in range(n):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)

# 手札を描写する
def make_hand(hand):
    for i in range(len(hand)):
        card = tk.Button(root, image=hand[i][2], command= click_hand(hand[i][1]))
        card.place(x=60 * (i + 1) - 60, y=300)

def click_hand(e):
    def x():
        label1["text"] += str(e)
    return x

def judge():
    if label1["text"] != "" :
        tmsg.showinfo("判定結果",judge_prime_factor(int(label1["text"])))

def cancel():
    label1["text"] = ""



deck = make_deck()
hand = []
draw(hand,10)

picture = {}


button1 = tk.Button(root, text="判定", command=judge)
button1.place(x=200, y=250)

button2 = tk.Button(root, text="キャンセル", command=cancel)
button2.place(x=300, y=250)

label1 = tk.Label(root, text="")
label1.place(x=200,y=200)

make_hand(hand)

root.mainloop()




