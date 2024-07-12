import tkinter
from tkinter import *
import random

exit = False
name = 'Seldon'
quest_done = True
current_area = "Area: Goblin Caves"
rat_kill_count = 0
goblin_kill_count = 0
goblincaves_kill_count = 0

# stats
hp = 10
level = "1"
damage_start = 1
damage_end = 5
flee_chance = "100%"

ennemytype = ' The rat'
ennemy_level = 1
ennemy_hp = 10
ennemy_damage = 2

# main
root = Tk()
root.title("Eight Dragon Wars")
root.attributes('-fullscreen', True)
root.option_add("*font", ("Arial"))
root["bg"] = "white"

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Function to toggle fullscreen
def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

# Bind F11 key to toggle fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', lambda e: root.quit())

# Buttons 
def exit_function():
    root.destroy()

exit_image = PhotoImage(file='exit.png')
exit_button = Button(root, image=exit_image, command=exit_function, borderwidth=0)
exit_button.place(x=0, y=0)

def start_function():
    start_button.place_forget()
    Prequel.place(relx=0.5, rely=0.5, anchor=CENTER)
    back_button.place(relx=1.0, rely=0, anchor=NE)
    continue_button.place(relx=0.5, rely=0.9, anchor=CENTER)

start_image = PhotoImage(file='start.png')
start_button = Button(root, image=start_image, command=start_function, borderwidth=0)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

def back_function():
    erase()
    back_button.place_forget()
    start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

back_image = PhotoImage(file="back.png")
back_button = Button(root, image=back_image, command=back_function, borderwidth=0)

def continue_function():
    erase()
    menu()

continue_image = PhotoImage(file="continue.png")
continue_button = Button(root, image=continue_image, command=continue_function, borderwidth=0)

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
    Bestiary_Button.place_forget()
    Inventory_Button.place_forget()
    Shop_Button.place_forget()
    Mission_Label.place_forget()
    cuurent_area_label.place_forget()
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

def new_quest():
    global Mission_Label, quest_done, Quest
    if quest_done == True:
        Quest = random.choice(["slay 5 rat","slay 5 goblin","slay 8 monsters in goblin caves"])
        Mission_Label = Label(root,text=Quest)
        quest_done = False

def quest():
    global rat_kill_count,goblin_kill_count,goblincaves_kill_count,quest_done
    erase()
    new_quest()
    print(Quest)
    print(rat_kill_count)
    if Quest == "slay 5 rat" and rat_kill_count > 1:
        rat_kill_count = 0
        quest_done = True
        new_quest()
        print("done")
    if Quest == "slay 5 goblin" and goblin_kill_count > 1:
        goblin_kill_count = 0
        quest_done = True
        new_quest()
    if Quest == "slay 8 monsters in goblin caves" and goblincaves_kill_count > 1:
        goblincaves_kill_count = 0
        quest_done = True
        new_quest()
    Mission_Label.place(x=550,y=300)
    continue_button.place(x=550,y=700)
def area():
    erase()
    
    continue_button.place(x=550,y=700)
def inventory():
    erase()
    continue_button.place(x=550,y=700)
def shop():
    erase()
    continue_button.place(x=550,y=700)
def bestiary():
    erase()
    continue_button.place(x=550,y=700)
Fight_button = Button(root,text="Go fight",command= combat, borderwidth=0)
Quest_Button = Button(root,text='Quests', command=quest,borderwidth=0)
Area_Button = Button(root,text='Change area', command=area,borderwidth=0)
Inventory_Button = Button(root,text="Inventory", command=inventory,borderwidth=0)
Shop_Button = Button(root,text="Go to shop",command=shop,borderwidth=0)
Bestiary_Button = Button(root,text="Bestiary",command=bestiary,borderwidth=0)

def menu():
    erase()
    cuurent_area_label.place(x=300,y=100)
    Fight_button.place(x=550,y=150)
    Area_Button.place(x=550,y=250)
    Quest_Button.place(x=550,y=350)
    Inventory_Button.place(x=550,y=450)
    Shop_Button.place(x=550,y=550)
    Bestiary_Button.place(x=550,y=650)
    

def win():
    global rat_kill_count, goblin_kill_count, goblincaves_kill_count
    erase()
    if ennemytype == "The rat":
        rat_kill_count += 1
    if ennemytype == "The goblin":
        goblin_kill_count += 1
    if current_area == "Area: Goblin Caves":
        goblincaves_kill_count += 1
    win_label.place(x=555,y=300)
    continue_button.place(x=550,y=700)

def lose():
    erase()
    lose_label.place(x=555,y=300)
    continue_button.place(x=550,y=700)

# Labels
Title = Label(root, text='EIGHT DRAGON WARS', font='Papyrus 25', bg='white')
Title.place(relx=0.5, rely=0.05, anchor=CENTER)

level_label = Label(root, text='you are level ' + level)
ennemy_level_label = Label(root, text=ennemytype+' is level '+str(ennemy_level))
hp_label = Label(root, text='you have '+str(hp)+" hp")
damage_label = Label(root, text='you will do '+str(damage_start)+' to '+str(damage_end)+' damage')
ennemy_hp_label = Label(root, text=ennemytype +' have ' + str(ennemy_hp) +" hp")
ennemy_damage_label = Label(root, text=ennemytype +" will do " + str(ennemy_damage) + " damage")
ennemy_action_label = Label(root, text="", bg='white')
win_label = Label(root, text=name+' won, gg')
lose_label = Label(root, text=ennemytype+' won')
Mission_Label = Label(root,text='')
cuurent_area_label = Label(root,text=current_area)

# Prequel text
Prequel = Label(root, text=("You awaken in a cave, you're lost and you don't remember how you got here,\n at least, you know your name, "
+name+".\n The last thing you recall is running from a merchant from which you stole in Al'Banhera, the capital city."
+"\n You finally get up and look around you , you suddenly fall on the ground, terrified."
+"\n In front of you stand a gigantic beast, his claws are glowing and sand is flowing through the scale of the monster."
+"\n you recognize the beast, it's Shar'Gezan, the dragon-god that rules over Al'Banhera...")
+"\n The mighty dragon starts speaking to you :\n''Mortal! I have summoned you.'' (you're too terrified to speak or move)"
+"\n My kingdom is attacked by Zul'Sahar, my sister. I need to retreat and i chose you to recieve my blessings."
+"\n You need to become stronger to kill the corrupted creation of Zul'Sahar and to finally slain her."
+"\n The dragon suddenly disappears and a ray of light suddenly stuns you..."
, borderwidth=0, bg='white', wraplength=screen_width*0.8)

root.mainloop()