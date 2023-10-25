# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pylab as pl
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
from playsound import playsound


class Grid:
    def __init__(self):
        self.__lines = np.array([])
        
class Game:
    def __init__(self):
        self.__p1_ships = np.array([]) #stores ships carrier,battleship,submarine,frigate,uboat
        self.__p2_ships = np.array([])
        self.__p1_shots = np.array([]) # stores shots
        self.__p2_shots = np.array([])
        self.__p1_h = np.array([])
        self.__p2_h = np.array([])
        self.__p1_turns = 0
        self.__p2_turns = 0
        self.__p1_hits = 0
        self.__p2_hits = 0
        
    def start(self):
        Game.taketurn(self,1)
        
    def taketurn(self,player):
        if player == 1:
            print("It is player 1's turn")
            if self.__p1_turns == 0:
                Game.placeships(self,1)
            else:
                Game.take_shot(self,1)
            self.__p1_turns += 1
        else:
            print("It is player 2's turn")
            if self.__p2_turns == 0:
                Game.placeships(self,2)
            else:
                Game.take_shot(self,2)
            self.__p2_turns += 1
        Game.endturn(self,player)
    def endturn(self,player):
        if self.__p1_hits == 17:
            print("Congratulations, player 1 has won")
            playsound("/Users/hansd/OneDrive/Documents/Python Scripts/sound effects/allah.wav")
        elif self.__p2_hits == 17:
            print("Congratulations, player 2 has won")
            playsound("/Users/hansd/OneDrive/Documents/Python Scripts/sound effects/allah.wav")
        else:
            if player ==1:
                Game.taketurn(self,2)
            else:
                Game.taketurn(self,1)
    def take_shot(self,player):
        if player == 1:
            Game.animate_shots(self,1)
            count = 0
            while count == 0:
                shot_x = input("Enter your x coordinate for your shot player 1: ")
                shot_y = input("Enter your y coordinate for your shot player 1: ")
                while shot_x != int or shot_y != int:
                    print("Incorrect input, please enter coordiantes again")
                    shot_x = input("Enter your x coordinate for your shot player 1: ")
                    shot_y = input("Enter your y coordinate for your shot player 1: ")
                while shot_x<1 or shot_x>10 or shot_y<1 or shot_y>10:
                    print("Shot is out of bounds, please enter coordinates again")
                    shot_x = input("Enter your x coordinate for your shot player 1: ")
                    shot_y = input("Enter your y coordinate for your shot player 1: ")
                count = 1
                for i in range(0,len(self.__p1_shots)-1,2):
                    if self.__p1_shots[i] == shot_x and self.__p1_shots[i+1] == shot_y:
                        count = 0
                        print("You have already taken a shot here, please enter again")
            shot = [shot_x,shot_y]
            self.__p1_shots = np.append(self.__p1_shots,shot)
            hit = 0
            for i in range(0,len(self.__p2_ships)-1,2):
                if self.__p2_ships[i] == shot_x and self.__p2_ships[i+1] == shot_y:
                    print("Congratulations, that was a hit")
                    hit =1
            if hit ==1:
                self.__p1_h = np.append(self.__p1_h,shot)
                self.__p1_hits += 1
                playsound("/Users/hansd/OneDrive/Documents/Python Scripts/sound effects/explosion3.wav")
            else:
                print("You missed, unlucky")
                playsound("/Users/hansd/OneDrive/Documents/Python Scripts/sound effects/water_drop.wav")
            
        else:
            Game.animate_shots(self,2)
            count = 0
            while count == 0:
                shot_x = int(input("Enter your x coordinate for your shot player 2: "))
                shot_y = int(input("Enter your y coordinate for your shot player 2: "))
                while shot_x != int or shot_y != int:
                    print("Incorrect input, please enter coordiantes again")
                    shot_x = input("Enter your x coordinate for your shot player 2: ")
                    shot_y = input("Enter your y coordinate for your shot player 2: ")
                while shot_x<1 or shot_x>10 or shot_y<1 or shot_y>10:
                    print("Shot is out of bounds, please enter coordinates again")
                    shot_x = input("Enter your x coordinate for your shot player 2: ")
                    shot_y = input("Enter your y coordinate for your shot player 2: ")
                count = 1
                for i in range(0,len(self.__p2_shots)-1,2):
                    if self.__p2_shots[i] == shot_x and self.__p2_shots[i+1] == shot_y:
                        count = 0
                        print("You have already taken a shot here, please enter again")
            shot = [shot_x,shot_y]
            self.__p2_shots = np.append(self.__p2_shots,shot)
            hit = 0
            for i in range(0,len(self.__p1_ships)-1,2):
                if self.__p1_ships[i] == shot_x and self.__p1_ships[i+1] == shot_y:
                    print("Congratulations, that was a hit")
                    hit =1
            if hit == 1:
                self.__p2_h = np.append(self.__p2_h,shot)
                self.__p2_hits += 1
                playsound("/Users/hansd/OneDrive/Documents/Python Scripts/sound effects/explosion3.wav")
            else:
                print("You missed, unlucky")
                playsound("/Users/hansd/OneDrive/Documents/Python Scripts/sound effects/water_drop.wav")
                
    def placeships(self,player):
        if player == 1:
            for i in range(1,6):
                self.__p1_ships = np.append(self.__p1_ships,Game.entercoords(self,i,1))
                Game.animate_ships(self,1)
        if player == 2:
            for i in range(1,6):
                self.__p2_ships = np.append(self.__p2_ships,Game.entercoords(self,i,2))
                Game.animate_ships(self,2)
    def entercoords(self,ship,player):
        if ship == 1:
            name = "Carrier"
            number = 4
        if ship == 2:
            name = "Battleship"
            number = 3
        if ship == 3:
            name = "Submarine"
            number = 2
        if ship == 4:
            name = "Frigate"
            number = 2
        if ship == 5:
            name = "U-boat"
            number = 1
        check = 0
        values = np.array([])
        while check == 0:
            val_x = float(input("Enter the starting x coordinate for your %.10s: "%name))
            while val_x <1 or val_x>10:
                print("This value is out of bounds")
                val_x = int(input("Enter the starting x coordinate for your %.10s: "%name))
            val_y = float(input("Enter the starting y coordinate for your %.10s: "%name))
            while val_y <1 or val_y>10:
                print("This value is out of bounds")
                val_y = int(input("Enter the starting y coordinate for your %.10s: "%name))
            
            checker = 0
            ori = 0
            ori = input("Enter the orientation of your %.10s (N/S/E/W): "%name)
            while checker == 0:
                if ori == 'N' or ori == 'S' or ori =='E' or ori == 'W':
                    checker = 1
                    break
                else:
                    print("Please use one of the four orientations: N,S,E or W")
                    ori = input("Enter the orientation of your %.10s (N/S/E/W): "%name)
            while checker ==1:
                if ori == 'N' and val_y+number < 11 :
                    checker = 2
                    break
                if ori == 'S' and val_y-number> 0 :
                    checker = 2
                    break
                if ori == 'E' and val_x+number <11:
                    checker = 2
                    break
                if ori == 'W' and val_x-number>0:
                    checker = 2
                    break
                print("You cannot use this orientation")
                ori = input("Enter the orientation of your %.10s (N/S/E/W): "%name)
            val = np.array([val_x,val_y])
            for i in range(1,number+1):
                if ori == 'N':
                    val = np.append(val,[val_x,val_y + i])
                if ori == 'S':
                    val = np.append(val,[val_x,val_y - i])
                if ori == 'E':
                    val = np.append(val,[val_x + i,val_y])
                if ori == 'W':
                    val = np.append(val,[val_x - i,val_y])
            counter = 0
            if player == 1:
                for j in range(0,len(self.__p1_ships)-1,2):
                    for i in range(0,len(val)-1,2):
                        if self.__p1_ships[j]==val[i] and self.__p1_ships[j+1]==val[i+1]:
                            counter+=1
                            if counter == 1:
                                print("Ship overlaps, please input coordinates again")
                            break
            if player == 2:
                for j in range(0,len(self.__p2_ships)-1,2):
                    for i in range(0,len(val)-1,2):
                        if self.__p2_ships[j]==val[i] and self.__p2_ships[j+1]==val[i+1]:
                            counter+=1
                            if counter == 1:
                                print("Ship overlaps, please input coordinates again")
                            break
            if counter == 0:
                check =1
        return val
                

    def animate_ships(self,player):
        plt.figure(facecolor='lightblue')
        ax = plt.axes()
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)
        ticks = np.arange(0,11,1)
        
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.grid(color='black')
        ax.set_title("Battleship Grid")
        
        ax.set_facecolor("lightblue")
        if player == 1:
            array = self.__p1_ships
        else:
            array = self.__p2_ships
        for i in range(0,len(array)-1,2):
            ax.add_patch(pl.Rectangle([array[i]-1,array[i + 1]-1],1,1,ec='gray',fc='gray'))
        plt.show()
        
    def animate_shots(self,player):
        plt.figure(facecolor='lightblue')
        ax = plt.axes()
        ax.set_xlim(0,10)
        ax.set_ylim(0,10)
        ticks = np.arange(0,11,1)
        
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.grid(color='black')
        #ax.set_title("Battleship Grid")
        
        ax.set_facecolor("lightblue")
        
        if player==1:
            ax.set_title("Player 1 shots")
            array1=self.__p1_shots
            array2 =self.__p1_h
        else:
            ax.set_title("Player 2 shots")
            array1=self.__p2_shots
            array2 =self.__p2_h
        for i in range(0,len(array1)-1,2):
            ax.add_patch(pl.Circle([array1[i]-0.5,array1[i + 1]-0.5],0.5,ec='black',fc='white'))
        for i in range(0,len(array2)-1,2):
            ax.add_patch(pl.Circle([array2[i]-0.5,array2[i + 1]-0.5],0.5,ec='black',fc='red'))
        plt.show()
    
    def ships(self):
        print(self.__p1_ships)
#%%    
val = "get"
val1= int(input("gr %.10s :"%val))


        
        

        
        

#%%
"""
checker = 0
car_or = 0
car_val_x = 4
car_val_y =10
        car_val_x = int(input("Enter the starting x coordinate for your carrier: "))
        while car_val_x <1 or car_val_x>10:
            print("This value is out of bounds")
            car_val_x = int(input("Enter the starting x coordinate for your carrier: "))
        car_val_y = int(input("Enter the starting y coordinate for your carrier: "))
        while car_val_y <1 or car_val_y>10:
            print("This value is out of bounds")
            car_val_y = int(input("Enter the starting y coordinate for your carrier: "))
        
        checker = 0
        car_or = 0
        car_or = input("Enter the orientation of your carrier (N/S/E/W): ")
        while checker == 0:
            if car_or == 'N' or car_or == 'S' or car_or =='E' or car_or == 'W':
                checker = 1
                break
            else:
                print("Please use one of the four orientations: N,S,E or W")
                car_or = input("Enter the orientation of your carrier (N/S/E/W): ")
        while checker ==1:
            if car_or == 'N' and car_val_y+4 < 11 :
                checker = 2
                break
            if car_or == 'S' and car_val_y-4> 0 :
                checker = 2
                break
            if car_or == 'E' and car_val_x+4 <11:
                checker = 2
                break
            if car_or == 'W' and car_val_x-4>0:
                checker = 2
                break
            print("You cannot use this orientation")
            car_or = input("Enter the orientation of your carrier (N/S/E/W): ")
        if car_or == 'N':
            car = np.array([[car_val_x,car_val_y],[car_val_x,car_val_y+1],[car_val_x,car_val_y+2],[car_val_x,car_val_y+3],[car_val_x,car_val_y+4]])
        if car_or == 'S':
            car = np.array([[car_val_x,car_val_y],[car_val_x,car_val_y-1],[car_val_x,car_val_y-2],[car_val_x,car_val_y-3],[car_val_x,car_val_y-4]]) 
        if car_or == 'E':
            car = np.array([[car_val_x,car_val_y],[car_val_x+1,car_val_y],[car_val_x+2,car_val_y],[car_val_x+3,car_val_y],[car_val_x+4,car_val_y]])
        if car_or == 'W':
            car = np.array([[car_val_x,car_val_y],[car_val_x-1,car_val_y],[car_val_x-2,car_val_y],[car_val_x-3,car_val_y],[car_val_x-4,car_val_y]])
"""
#%%
val = input("jjfe")
#%%
#arr1 = np.array([3. 1. 3. 2. 3. 3. 3. 4. 3. 5. 2. 1. 3. 1. 4. 1. 5. 1. 3. 1. 4. 1. 5. 1.])
arr2 = [3,1,3,2,3,3,4,4]

g=Game()
Game.taketurn(g,1)
arr1 = Game.ships(g)
print(arr1)

for i in range(0,len(arr1)-1,2):
    for j in range(0,len(arr2)-1,2):
        if arr2[j]==arr1[i] and arr2[j+1]==arr1[i+1]:
            print("Ship overlaps, please input coordinates again")
            break
#%%
plt.figure(facecolor='lightblue')
ax = plt.axes()
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ticks = np.arange(0,11,1)


ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.grid(color='black')
ax.set_title("Battleship Grid")

ax.set_facecolor("lightblue")

plt.show()