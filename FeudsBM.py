import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
import random
import sys
import os

winMessage = ""

class BattleInputs(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.rows = 7

        layout_a1 = BoxLayout(orientation="vertical")
        self.add_widget(layout_a1)
        layout_a1.add_widget(Label(text="Army 1", size_hint=(2, 1), font_size=20))

        self.add_widget(Label(text="", size_hint=(0,0)))

        layout_a2 = BoxLayout(orientation="vertical")
        self.add_widget(layout_a2)
        layout_a2.add_widget(Label(text="Army 2", size_hint=(2, 1), font_size=20))

        self.add_widget(Label(text="", size_hint=(0,0)))

        self.add_widget(Label(text="Swordsmen:"))
        self.swordsmen1 = TextInput(text="", multiline=False)
        self.add_widget(self.swordsmen1)

        self.add_widget(Label(text="Swordsmen:"))
        self.swordsmen2 = TextInput(text="", multiline=False)
        self.add_widget(self.swordsmen2)

        self.add_widget(Label(text="Archers:"))
        self.archers1 = TextInput(text="", multiline=False)
        self.add_widget(self.archers1)

        self.add_widget(Label(text="Archers"))
        self.archers2 = TextInput(text="", multiline=False)
        self.add_widget(self.archers2)

        self.add_widget(Label(text="Pikemen"))
        self.pikemen1 = TextInput(text="", multiline=False)
        self.add_widget(self.pikemen1)

        self.add_widget(Label(text="Pikemen"))
        self.pikemen2 = TextInput(text="", multiline=False)
        self.add_widget(self.pikemen2)

        self.add_widget(Label(text="Calvary"))
        self.calvary1 = TextInput(text="", multiline=False)
        self.add_widget(self.calvary1)

        self.add_widget(Label(text="Calvary"))
        self.calvary2 = TextInput(text="", multiline=False)
        self.add_widget(self.calvary2)

        self.add_widget(Label(text="Knights"))
        self.knights1 = TextInput(text="", multiline=False)
        self.add_widget(self.knights1)

        self.add_widget(Label(text="Knights"))
        self.knights2 = TextInput(text="", multiline=False)
        self.add_widget(self.knights2)

        self.layout = BoxLayout(orientation="vertical")
        self.add_widget(self.layout)
        self.submit = Button(text="Submit", size_hint=(4, 1), font_size=20)
        self.layout.add_widget(self.submit)
        self.submit.bind(on_press=self.submit_button)

    def submit_button(self, instance):
        f1 = int(self.swordsmen1.text)
        f2 = int(self.swordsmen2.text)
        a1 = int(self.archers1.text)
        a2 = int(self.archers2.text)
        p1 = int(self.pikemen1.text)
        p2 = int(self.pikemen2.text)
        c1 = int(self.calvary1.text)
        c2 = int(self.calvary2.text)
        k1 = int(self.knights1.text)
        k2 = int(self.knights2.text)

        troopList = []

        troopList.append(f1)
        troopList.append(a1)
        troopList.append(c1)
        troopList.append(p1)
        troopList.append(k1)

        troopList.append(f2)
        troopList.append(a2)
        troopList.append(c2)
        troopList.append(p2)
        troopList.append(k2)

        #Calculations#

        runs = 0
        
        while True:
            if troopList[runs] == 0:
                troopList[runs] = .01
            runs = runs + 1
            if runs > 9:
                break
            else:
                continue
        
        army1total = f1 + a1 + c1 + p1 + k1
        army2total = f2 + a2 + c2 + p2 + k2

        army1adv = []
        army2adv = []

        runs1 = 0
        runs2 = 5

        while True:
            if troopList[runs1] > troopList[runs2]:
                army1adv.append(float(troopList[runs1]/troopList[runs2]))
                army2adv.append(0.0)
            elif troopList[runs1] < troopList[runs2]:
                army1adv.append(0.0)
                army2adv.append(float(troopList[runs2]/troopList[runs1]))
            elif troopList[runs1] == troopList[runs2]:
                army1adv.append(0.0)
                army2adv.append(0.0)
            else:
                sys.exit()

            runs1 = runs1 + 1
            runs2 = runs2 + 1

            if runs1 < 5:
                continue
            else:
                break

        advTotal1 = army1adv[0] + army1adv[1] + army1adv[2] + army1adv[3] + army1adv[4]
        advTotal2 = army2adv[0] + army2adv[1] + army2adv[2] + army2adv[3] + army2adv[4]

        for y in range(1):
            army1cas = random.randint(1,int(army1total + 1))
        for i in range(1):
            army2cas = random.randint(1,int(army2total + 1))
        basecas1 = int(army1cas)/5 + 3            
        basecas2 = int(army2cas)/5 + 3
        
        for i in range(1):
            army1fcas = random.randint(1,int(basecas1))
            army1acas = random.randint(1,int(basecas1))
            army1ccas = random.randint(1,int(basecas1))
            army1pcas = random.randint(1,int(basecas1))
            army1kcas = random.randint(1,int(basecas1))
            army1totalcas = army1fcas + army1acas + army1ccas + army1pcas + army1kcas
            army1rem = army1total - army1totalcas

        for i in range(1):
            army2fcas = random.randint(1,int(basecas2))
            army2acas = random.randint(1,int(basecas2))
            army2ccas = random.randint(1,int(basecas2))
            army2pcas = random.randint(1,int(basecas2))
            army2kcas = random.randint(1,int(basecas2))
            army2totalcas = army2fcas + army2acas + army2ccas + army2pcas + army2kcas
            army2rem = army2total - army2totalcas

        finalScore = advTotal1 + advTotal2 + 1
        for i in range(1):
            winningScore = random.randint(1,int(finalScore))
        
        global winMessage
        #winMessage = ""

        if winningScore > advTotal2:
            winMessage = ("""Army 1 ({24}) Is Victorious With {0} Casualties and {1} Troops Remaining.
Details On Army 1 Casualties:
{2}: {3}
{4}: {5}
{6}: {7}
{8}: {9}
{10}: {11}

Army 2 ({25}) Have {12} Casualties And Have {13} Troops Remaining.
Details On Army 2 Casualties:
{14}: {15}
{16}: {17}
{18}: {19}
{20}: {21}
{22}: {23}
            """).format(army1totalcas, army1rem, "Archers", army1fcas, "Swordsmen", army1acas, "Pikemen", army1ccas, "Calvary", army1pcas, "Knights", army1kcas, army2totalcas, army2rem, "Archers", army2fcas, "Swordsmen", army2acas, "Pikemen", army2ccas, "Calvary", army2pcas, "Knights", army2kcas, "Army 1", "Army 2")
            bm.battle_outcomes.update_info(winMessage)
        elif winningScore < advTotal2:
            winMessage = ("""Army 1 ({24}) Have {0} Casualties and {1} Troops Remaining.
Details On Army 1 Casualties:
{2}: {3}
{4}: {5}
{6}: {7}
{8}: {9}
{10}: {11}

Army 2 ({25}) Is Victorious With {12} Casualties And Have {13} Troops Remaining.
Details On Army 2 Casualties:
{14}: {15}
{16}: {17}
{18}: {19}
{20}: {21}
{22}: {23}
            """).format(army1totalcas, army1rem, "Archers", army1fcas, "Swordsmen", army1acas, "Pikemen", army1ccas, "Calvary", army1pcas, "Knights", army1kcas, army2totalcas, army2rem, "Archers", army2fcas, "Swordsmen", army2acas, "Pikemen", army2ccas, "Calvary", army2pcas, "Knights", army2kcas, "Army 1", "Army 2")
            bm.battle_outcomes.update_info(winMessage)
        else:
            winMessage = ("""Army 1 ({24}) Have {0} Casualties and Have {1} Troops Remaining.
Details On Army 1 Casualties:
{2}: {3}
{4}: {5}
{6}: {7}
{8}: {9}
{10}: {11}

Army 2 ({25}) Have {12} Casualties And Have {13} Troops Remaining.
Details On Army 2 Casualties:
{14}: {15}
{16}: {17}
{18}: {19}
{20}: {21}
{22}: {23}

A Draw Has Been Reached
            """).format(army1totalcas, army1rem, "Archers", army1fcas, "Swordsmen", army1acas, "Pikemen", army1ccas, "Calvary", army1pcas, "Knights", army1kcas, army2totalcas, army2rem, "Archers", army2fcas, "Swordsmen", army2acas, "Pikemen", army2ccas, "Calvary", army2pcas, "Knights", army2kcas, "Army 1", "Army 2")
            bm.battle_outcomes.update_info(winMessage)

        bm.screen_manager.current = "Outcomes"

class BattleOutcome(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.message = Label(halign="center", valign="middle", font_size=20)
        self.message.text = winMessage
        self.add_widget(self.message)   

    def update_info(self, message):
        self.message.text = message


class Application(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.battle_inputs = BattleInputs()
        screen = Screen(name="Inputs")
        screen.add_widget(self.battle_inputs)
        self.screen_manager.add_widget(screen)

        self.battle_outcomes = BattleOutcome()
        screen = Screen(name="Outcomes")
        screen.add_widget(self.battle_outcomes)
        self.screen_manager.add_widget(screen)

        self.title = "Feuds Battlemanager V0.1"

        #Window.borderless=True

        return self.screen_manager


if __name__ == "__main__":
    bm = Application()
    bm.run()

