import tkinter
from tkinter import *
import random

exit = False
#name = input("what's your name, hero? (you need to write in console)\n")
name = 'Seldon'

#stats
hp = 10
level = "1"
damage_start = 1
damage_end = 5
flee_chance = "100%"

ennemytype = ' The rat'
ennemy_level = 1
ennemy_hp = 10
ennemy_damage = 2

#main
root = Tk()
root.attributes('-fullscreen',True)
root.title("main")
root.resizable(height= False, width = False)
root.option_add("*font",("Arial"))
root["bg"] = "white"

#Buttons 

def exit_function():
    root.destroy()
exit_image = PhotoImage(file='exit.png')
exit_button = Button(root,image = exit_image, command= exit_function,borderwidth=0)
exit_button.place(x=0,y=0)

def start_function():
    start_button.place_forget()
    Prequel.place(x=200,y=200)
    back_button.place(x=1000,y=0)
    continue_button.place(x=500,y=600)
start_image = PhotoImage(file='start.png')
start_button = Button(root, image=start_image, command= start_function, borderwidth=0)
start_button.place(x=550,y=300)

def back_function():
    erase()
    back_button.place_forget()
    start_button.place(x=530,y=300)
back_image = PhotoImage(file="back.png")
back_button = Button(root,image=back_image, command= back_function, borderwidth=0)

def continue_function():
    erase()
    menu()


continue_image = PhotoImage(file="continue.png")
continue_button = Button(root,image=continue_image, command=continue_function ,borderwidth= 0)

def attack_function():
    global ennemy_hp
    ennemy_hp -= random.randint(damage_start,damage_end)
    ennemy_hp_label["text"]=ennemytype +' have ' + str(ennemy_hp) +" hp"
    ennemy_turn()
attack_image=PhotoImage(file='attack.png')
attack_button = Button(root,image=attack_image,command=attack_function,borderwidth=0)

def passturn_function():
    ennemy_turn()
passturn_image = PhotoImage(file='pass turn.png')
passturn_button = Button(root, image=passturn_image, command= passturn_function,borderwidth=0)

#functions
def ennemy_turn():
    global hp, ennemy_hp,ennemy_damage
    action = random.choice(['attacked','healed','sharpened himself'])
    if ennemy_hp < 1:
        win()
        action = ""
    if action == 'attacked':
        hp -= ennemy_damage
        hp_label["text"]='you have '+str(hp)+" hp"
    if action == 'healed':
        ennemy_hp += ennemy_damage
        ennemy_hp_label["text"]=ennemytype +' have ' + str(ennemy_hp) +" hp"
    if action == 'sharpened himself':
        ennemy_damage *= 1.5
        ennemy_damage = int(ennemy_damage)
        ennemy_damage_label["text"]=ennemytype +" will do " + str(ennemy_damage) + " damage"
    ennemy_action_label["text"]= ennemytype+" "+action
    if hp < 1:
        lose()
        action=""

def erase():
    Prequel.place_forget()
    continue_button.place_forget()
    ennemy_damage_label.place_forget()
    level_label.place_forget()
    ennemy_level_label.place_forget()
    ennemy_hp_label.place_forget()
    hp_label.place_forget()
    damage_label.place_forget()
    ennemy_action_label.place_forget()
    attack_button.place_forget()
    passturn_button.place_forget()
    start_button.place_forget()
    Area_Button.place_forget()
    Fight_button.place_forget()
    Quest_Button.place_forget()
    win_label.place_forget()
    lose_label.place_forget()
#scene
def combat():
    erase()
    global hp,level,damage_start,damage_end,ennemytype,ennemy_level,ennemy_hp,ennemy_damage
    hp = 10
    level = "1"
    damage_start = 1
    damage_end = 5
    ennemytype = random.choice(["The rat","The goblin"])
    ennemy_level = 1
    if ennemytype == "The rat":
        ennemy_hp = 10
        ennemy_damage = 2
    if ennemytype == "The goblin":
        ennemy_hp = 7
        ennemy_damage = 5
    hp_label["text"]='you have '+str(hp)+" hp"
    ennemy_hp_label["text"]=ennemytype +' have ' + str(ennemy_hp) +" hp"
    ennemy_damage_label["text"]=ennemytype +" will do " + str(ennemy_damage) + " damage"
    ennemy_action_label["text"]=""
    hp_label.place(x=300,y=300)
    damage_label.place(x=300,y=400)
    ennemy_hp_label.place(x=800,y=300)
    ennemy_damage_label.place(x= 800, y=400)
    level_label.place(x=300,y = 500)
    ennemy_level_label.place(x=800,y=500)
    attack_button.place(x=200, y = 600)
    passturn_button.place(x=400,y=600)
    ennemy_action_label.place(x=550,y=200)

def quest():
    erase()
    continue_button.place(x=550,y=700)
def area():
    erase()
    continue_button.place(x=550,y=700)
Fight_button = Button(root,text="Go fight",command= combat, borderwidth=0)
Quest_Button = Button(root,text='Quests', command=quest,borderwidth=0)
Area_Button = Button(root,text='Change area', command=area,borderwidth=0)

def menu():
    erase()
    Fight_button.place(x=550,y=200)
    Quest_Button.place(x=550,y=300)
    Area_Button.place(x=550,y=400)

def win():
    erase()
    win_label.place(x=555,y=300)
    continue_button.place(x=550,y=700)

def lose():
    erase()
    lose_label.place(x=555,y=300)
    continue_button.place(x=550,y=700)


#Labels
Title = Label(root,text=('EIGHT DRAGON WARS'), font='Papyrus 25', bg='white' )
Title.place(x=450,y=20)
level_label = Label(root, text='you are level ' + level)
ennemy_level_label = Label(root,text=ennemytype+' is level '+str(ennemy_level))
hp_label = Label(root,text='you have '+str(hp)+" hp")
damage_label = Label(root, text='you will do '+str(damage_start)+' to '+str(damage_end)+' damage')
ennemy_hp_label = Label(root, text=ennemytype +' have ' + str(ennemy_hp) +" hp")
ennemy_damage_label = Label(root,text=ennemytype +" will do " + str(ennemy_damage) + " damage")
ennemy_action_label = Label(root, text="",bg='white')
win_label = Label(root,text=name+' won, gg')
lose_label = Label(root,text=ennemytype+' won')

#prequel text
Prequel = Label(root, text=("You awaken in a cave, you're lost and you don't remember how you got here,\n at least, you know your name, "
+name+".\n The last thing you recall is running from a merchant from which you stole in Al'Banhera, the capital city."
+"\n You finally get up and look around you , you suddenly fall on the ground, terrified."
+"\n In front of you stand a gigantic beast, his claws are glowing and sand is flowing through the scale of the monster."
+"\n you recognize the beast, it's Shar'Gezan, the dragon-god that rules over Al'Banhera...")
+"\n The mighty dragon starts speaking to you :\n''Mortal! I have summoned you.'' (you're too terrified to speak or move)"
+"\n My kingdom is attacked by Zul'Sahar, my sister. I need to retreat and i chose you to recieve my blessings."
+"\n You need to become stronger to kill the corrupted creation of Zul'Sahar and to finally slain her."
+"\n The dragon suddenly disappears and a ray of light suddenly stuns you..."
, borderwidth=0,bg='white')

root.mainloop()
