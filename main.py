import tkinter
from tkinter import *
import random

exit = False
name = 'Seldon'
quest_done = True
current_area = "Area: Sewers"
rat_kill_count = 0
permanent_rat_kill_count = 0
bandit_kill_count = 0
permanent_bandit_kill_count = 0
sewers_kill_count = 0
total_kill_count = 0
quest_reward = ""
quest_stage = 1
gold = 0
item = []
drop_chance = 0
key_obtained = False
boss1 = False

#achievements
Splat_found = False
# stats
maxhp = 10
hp = maxhp
level = 1
damage_start = 1
damage_end = 5
xp = 0

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
def Sewers_command():
    global current_area
    current_area = "Area: Sewers"
    continue_function()
sewers_button = Button(root,text="Go to the sewers",command=Sewers_command, borderwidth=0)

def village_command():
    global current_area
    current_area ="Area: Underground Village"
    continue_function()
village_button = Button(root,text="Go to Underground Village", command=village_command, borderwidth=0)

def exit_function():
    root.destroy()

exit_image = PhotoImage(file='exit.png')
exit_button = Button(root, image=exit_image, command=exit_function, borderwidth=0)
exit_button.place(x=0, y=0)

def village_kill_choice_function():
    global quest_stage
    quest_stage = 3.1
    quest()
village_kill_choice_button = Button(root,text="Attack the villagers",command=village_kill_choice_function,borderwidth=0)

def village_peace_choice_function():
    global quest_stage
    quest_stage = 3.2
    print(str(quest_stage))
    quest()
village_peace_choice_button = Button(root,text="Go talk to the chief of the village",command=village_peace_choice_function,borderwidth=0)

def start_function():
    start_button.place_forget()
    Prequel.place(relx=0.5, rely=0.4, anchor=CENTER)
    back_button.place(relx=1.0, rely=0, anchor=NE)
    continue_button.place(relx=0.5, rely=0.7, anchor=CENTER)

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

def Use_key_function():
    global quest_stage
    item.remove("key")
    quest_stage = 2
    quest()
use_key_button = Button(root,text="Use da key",command=Use_key_function,borderwidth=0)

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
        if boss1 == True:
            lose_boss()
        else:
            lose()
        action=""

def erase():
    village_kill_choice_button.place_forget()
    village_peace_choice_button.place_forget()
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
    current_area_label.place_forget()
    sewers_button.place_forget()
    village_button.place_forget()
    bestiary_bandit_label.place_forget()
    bestiary_rat_label.place_forget()
    xp_label.place_forget()
    level_label.place_forget()
    name_label.place_forget()
    total_kill_count_label.place_forget()
    Achievements_Button.place_forget()
    item_label.place_forget()
    use_key_button.place_forget()
    drop_label.place_forget()
#scene
def combat():
    erase()
    global ennemytype,ennemy_level,ennemy_hp,ennemy_damage,hp
    hp=maxhp
    ennemytype = random.choice(["The rat","The Bandit"])
    if boss1 == True:
        ennemytype ="Chief Golem"
    if ennemytype == "The rat":
        ennemy_hp = 10
        ennemy_damage = 2
        ennemy_level = 1
    if ennemytype == "The Bandit":
        ennemy_hp = 7
        ennemy_damage = 5
        ennemy_level = 1
    if ennemytype == "Chief Golem":
        ennemy_damage = 20
        ennemy_hp = 80
        ennemy_level = 7
    ennemy_hp_label["text"]=ennemytype +' have ' + str(ennemy_hp) +" hp"
    ennemy_damage_label["text"]=ennemytype +" will do " + str(ennemy_damage) + " damage"
    ennemy_action_label["text"]=""
    ennemy_level_label["text"]=ennemytype + " is level " + str(ennemy_level)
    ennemy_hp_label.place(x=800,y=300)
    ennemy_damage_label.place(x= 800, y=400)
    ennemy_level_label.place(x=800,y=500)
    ennemy_action_label.place(x=550,y=200)
    hp_label['text']="you have "+str(hp)+" hp"
    hp_label.place(x=300,y=300)
    damage_label['text']='you will do '+str(damage_start)+' to '+str(damage_end)+' damage'
    damage_label.place(x=300,y=400)
    level_label['text']='you are level ' + str(level)
    level_label.place(x=300,y = 500)
    attack_button.place(x=200, y = 600)
    passturn_button.place(x=400,y=600)
def new_quest():
    global Quest,quest_stage,boss1,current_area
    if quest_stage == 1:
        Quest = "You enter the city by the sewer because the entrance is heavily guarded\nhowever, the access are blocked,\na lockpick might be able to pass, or just get the key from monsters."
    if quest_stage == 2:
        current_area = "Area: Underground Village"
        continue_button.place_forget()
        village_kill_choice_button.place(x=450, y=500)
        village_peace_choice_button.place(x=650,y=500)
        Quest = "You enter the lower part of the sewer\n After a long walk you come across what seems to be an underground village\n The villagers haven't saw you and you don't know if they are corrupted or not\n you must go through the village, it will end up in blood or in peace!"
    if quest_stage == 3.1:
        boss1 = True
        combat()
    if quest_stage == 3.2:
        Quest = "You enter the village, people seems surprised to see you but they aren't hostile.\n A guard come see you, look at you for a few seconds and say 'follow me stranger'.\nYou do so and enter a little tent , inside a stone golem awaits you.\nHe explains to you that this is a village of resistant, immune against the corruption.\nThey are trying to retake the control of the city and ask you to join them.\nYou do so since it is also your goal.He asks you to go collect some supplies from the nearby undergound black market.\nBut pay attention Azazel, a general is watching this market"
    if quest_stage == 3.3:
        Quest = "Honestly i didn't expect you would beat that boss so ig gg but i'm too lazy to continue the options so sorry"
    if quest_stage == 3.4:
        Quest = "You wake up in a tent, attached, the golem you faced is in front of you.\nHe notices you woke up and starts talking:\n'Hey, you're not corrupted are you ? Why did you attack us ?'\nYou explain that you thought they were hostile and the chief trusts you.\nHe explains to you that this is a village of resistant, immune against the corruption.\nThey are trying to retake the control of the city and ask you to join them.\nYou do so since it is also your goal.He asks you to go collect some supplies from the nearby undergound black market.\nBut pay attention Azazel, a general is watching this market"

def quest():
    global rat_kill_count,bandit_kill_count,sewers_kill_count
    erase()
    continue_button.place(x=450,y=650)
    new_quest()
    Mission_Label["text"]=Quest
    if quest_stage == 1 or quest_stage == 2 and boss1 == False:
        Mission_Label.place(x=350,y=300)
    if quest_stage == 3.2 or quest_stage == 3.4:
        Mission_Label.place(x=150,y=300)
    if quest_stage == 1 and key_obtained == True:
        use_key_button.place(x=450,y=500)

def area():
    erase()
    sewers_button.place(x=550,y=300)
    if quest_stage > 2:
        village_button.place(x=550,y=400)
    continue_button.place(x=450,y=650)
def inventory():
    erase()
    item_label['text']="You have " + str(item)
    item_label.place(x=500,y=100)
    name_label.place(x=200,y=100)
    hp_label['text']="you have "+str(maxhp)+" hp"
    hp_label.place(x=200,y=200)
    damage_label['text']='you will do '+str(damage_start)+' to '+str(damage_end)+' damage'
    damage_label.place(x=200,y=250)
    total_kill_count_label["text"]="you have killed "+str(total_kill_count)+" monsters in total"
    total_kill_count_label.place(x=200,y=300)
    level_label['text']='you are level ' + str(level)
    level_label.place(x=200,y=350)
    xp_label["text"]="you have "+str(xp)+" xp"
    xp_label.place(x=200,y=380)
    continue_button.place(x=450,y=650)
def shop():
    erase()
    continue_button.place(x=450,y=650)
def bestiary():
    erase()
    bestiary_rat_label['text']='\nThe rat:\nThis annoying pest is the slayer of\nbeginning adventurers.\nThey are much stronger than usually\nbecause of the corruption.\nHp=10\nDamage=2\nLevel=1\n\nyou have killed '+str(permanent_rat_kill_count)+" of them"
    bestiary_rat_label.place(x=100,y=200)
    bestiary_bandit_label['text']="\nThe Bandit:\n Al'banhera being the second most criminal city in the world\na lot of bandit roam the city and the sewers\nit is legal to kill them!\nHp=7\nDamage=5\nLevel=1\n\nyou have killed "+str(permanent_bandit_kill_count)+" of them"
    bestiary_bandit_label.place(x=500,y=200)
    continue_button.place(x=450,y=650)
def achievements():
    erase()
    if Splat_found == True:
        Splat_Label.place(x=550,y=450)
    continue_button.place(x=450,y=650)
Fight_button = Button(root,text="Go fight",command= combat, borderwidth=0)
Quest_Button = Button(root,text='Quests', command=quest,borderwidth=0)
Area_Button = Button(root,text='Change area', command=area,borderwidth=0)
Inventory_Button = Button(root,text="Inventory", command=inventory,borderwidth=0)
Shop_Button = Button(root,text="Go to shop",command=shop,borderwidth=0)
Bestiary_Button = Button(root,text="Bestiary",command=bestiary,borderwidth=0)
Achievements_Button = Button(root,text='Achievements',command=achievements,borderwidth=0)

def menu():
    erase()
    current_area_label["text"]= current_area
    current_area_label.place(x=300,y=100)
    Fight_button.place(x=450,y=200)
    Area_Button.place(x=450,y=300)
    Quest_Button.place(x=450,y=400)
    Inventory_Button.place(x=700,y=200)
    Shop_Button.place(x=700,y=300)
    Bestiary_Button.place(x=700,y=400)
    Achievements_Button.place(x=550,y=500)

def win():
    global rat_kill_count,boss1,quest_stage,key_obtained, bandit_kill_count, sewers_kill_count,xp,permanent_bandit_kill_count,permanent_rat_kill_count, total_kill_count
    erase()
    if ennemytype == "The rat":
        rat_kill_count += 1
        permanent_rat_kill_count +=1
        total_kill_count += 1
        xpgain(random.randint(4,7))
        goldgain(random.randint(0,10))
        drop_chance = random.randint(1,4)
        print(drop_chance)
        if drop_chance == 2 and key_obtained == False:
            drops("key")
            key_obtained = True
            drop_label['text']="You obtained a key"
            drop_label.place(x=555,y=400)
    if ennemytype == "The Bandit":
        bandit_kill_count += 1
        permanent_bandit_kill_count +=1
        total_kill_count +=1
        xpgain(random.randint(4,7))
        goldgain(random.randint(0,10))
    if current_area == "Area: Sewers":
        sewers_kill_count += 1
    win_label.place(x=555,y=300)
    continue_button.place(x=450,y=650)
    if boss1 == True:
        boss1 = False
        quest_stage = 3.3
        quest()

def drops(drop):
    global item
    item.append(drop)
    print(str(item))

def goldgain(amount):
    global gold
    gold += amount

def xpgain(amount):
    global xp
    xp += amount
    if level == 1 and xp > 9:
        levelup()
    if level == 2 and xp > 29:
        levelup()
    if level == 3 and xp > 99:
        levelup()
    if level == 4 and xp > 299:
        levelup()
    if level == 5 and xp > 999:
        levelup()

def levelup():
    global xp,level,maxhp,damage_end,damage_start
    xp = 0
    level += 1
    if level == 2:
        maxhp += 15
        damage_start += 3
        damage_end += 5
    if level == 3:
        maxhp += 20
        damage_start += 7
        damage_end += 5
    if level == 4:
        maxhp += 40
    if level == 5:
        damage_end += 20
        damage_start = damage_end
def lose():
    global quest_stage,boss1
    erase()
    lose_label["text"]=ennemytype+' won'
    lose_label.place(x=555,y=300)
    continue_button.place(x=450,y=650)

def lose_boss():
    global quest_stage,boss1
    erase()
    if boss1 == True:
        boss1 = False
        quest_stage = 3.4
        quest()

# Labels
Title = Label(root, text='EIGHT DRAGON WARS', font='Papyrus 25', bg='white')
Title.place(relx=0.5, rely=0.05, anchor=CENTER)

level_label = Label(root, text='you are level ' + str(level))
ennemy_level_label = Label(root, text=ennemytype+' is level '+str(ennemy_level))
hp_label = Label(root, text='you have '+str(maxhp)+" hp")
damage_label = Label(root, text='you will do '+str(damage_start)+' to '+str(damage_end)+' damage')
ennemy_hp_label = Label(root, text=ennemytype +' have ' + str(ennemy_hp) +" hp")
ennemy_damage_label = Label(root, text=ennemytype +" will do " + str(ennemy_damage) + " damage")
ennemy_action_label = Label(root, text="", bg='white')
win_label = Label(root, text=name+' won, gg')
lose_label = Label(root, text=ennemytype+' won')
Mission_Label = Label(root,text='')
current_area_label = Label(root,text=current_area)
bestiary_rat_label = Label(root, text='\nThe rat:\nThis annoying pest is the slayer of\nbeginning adventurers.\nThey are much stronger than usually\nbecause of the corruption.\nHp=10\nDamage=2\nLevel=1\n\nyou have killed'+str(permanent_rat_kill_count)+" of them",borderwidth=2,relief="solid")
bestiary_bandit_label = Label(root, text="\nThe Bandit:\n Al'banhera being the second most criminal city in the world\na lot of bandit roam the city and the sewers\nit is legal to kill them!\nHp=7\nDamage=5\nLevel=1\n\nyou have killed"+str(permanent_bandit_kill_count)+" of them",borderwidth=2,relief="solid")
name_label = Label(root,text=name,font="Arial 40")
xp_label = Label(root,text="you have "+str(xp)+" xp",font="Arial 10")
total_kill_count_label = Label(root, text="you have killed "+str(total_kill_count)+" monsters in total")
Splat_Label = Label(root,text="GG, you found the golden splatplays")
item_label = Label(root,text="Items:" + str(item))
drop_label = Label(root,text='You obtained' + "")

# Prequel text
Prequel = Label(root, text="You awaken in a cave, you're lost and you don't remember how you got here,\n at least, you know your name, "
+name+".\n The last thing you recall is running from a merchant from which you stole in Al'Banhera, the capital city."
+"\n You finally get up and look around you , you suddenly fall on the ground, terrified."
+"\n In front of you stand a gigantic beast, his claws are glowing and sand is flowing through the scale of the monster."
+"\n you recognize the beast, it's Shar'Gezan, the dragon-god that rules over Al'Banhera..."
+"\n The mighty dragon starts speaking to you :\n''Mortal! I have summoned you.'' (you're too terrified to speak or move)"
+"\n My kingdom is attacked by Zul'Sahar, my sister. I need to retreat and i chose you to receive my blessings."
+"\n You need to become stronger to kill the corrupted creation of Zul'Sahar and to finally slain her."
+"\n You'll have to activate the light sigil on Al'Banhera so that i can return, good luck hero"
+"\n The dragon suddenly disappears and a ray of light suddenly stuns you..."
+"\n You wake up near Al'Banhera but the door is close, you quickly hide from the guards in the sewers"
,borderwidth=0, bg='white', wraplength=screen_width*0.8)

root.mainloop()