##################################
# groupe MI 3
# Edgar BAGHDASARYAN
# Ali HARGAS
# Hatim ZELAMTA
# Anis FETOUAB
# https://github.com/uvsq22102013/projet_tas_de_sable/settings/interaction_limits
##################################

import tkinter as tk
import random

HEIGHT = 600
WIDTH = 600
obj = []

p = HEIGHT/500

racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width=WIDTH, bg = "white")
canvas.grid(row = 0, column = 0)
l3=[[0,0,0]]
for j in range(10):
    for i in range(10):
        l2=[]
        canvas.create_rectangle(((i*50)*p,(0+50*j)*p),((50+i*50)*p,(50+50*j)*p), outline = "black")
        l2.append(i)
        l2.append(j)
        if 3 <i< 6 and 3 <j< 6 :
            l2.append(random.randint(4,5))
        else :
            l2.append(random.randint(1,3))
        l3.append(l2)

decal_x = [10,20,30,10,30]
decal_y = [10,20,10,30,30]
decal_a = [30,20,10,30,10]
decal_b = [30,20,30,10,10]
e = 0
for v in range(1,101):
    for r in range(l3[v][2]):
        obj.append(canvas.create_oval((l3[v][0]*50*p+decal_x[r]*p,0+50*l3[v][1]*p+decal_y[r]*p),(50*p+l3[v][0]*50*p-decal_a[r]*p,50*p+50*l3[v][1]*p-decal_b[r]*p), fill ="yellow"))

def changement_config():
    global l3, obj
    for v in range(1,101):
        if l3[v][0] == 0 and l3[v][1]== 0 and l3[v][2] >= 4:
            l3[v][2] -= 2
            l3[v+1][2] += 1
            l3[v+10][2] += 1
        elif l3[v][0] == 9 and l3[v][1]== 0 and l3[v][2] >= 4:
            l3[v][2] -= 2
            l3[v-1][2] += 1
            l3[v+10][2] += 1
        elif l3[v][0] == 0 and l3[v][1]== 9 and l3[v][2] >= 4:
            l3[v][2] -= 2
            l3[v+1][2] += 1
            l3[v-10][2] += 1
        elif l3[v][0] == 9 and l3[v][1]== 9 and l3[v][2] >= 4:
            l3[v][2] -= 2
            l3[v-1][2] += 1
            l3[v-10][2] += 1
        elif l3[v][0] == 0 and l3[v][2] >= 4:
            l3[v][2] -= 3
            l3[v-10][2] += 1
            l3[v+10][2] += 1
            l3[v+1][2] += 1
        elif l3[v][0] == 9 and l3[v][2] >= 4:
            l3[v][2] -= 3
            l3[v-10][2] += 1
            l3[v+10][2] += 1
            l3[v-1][2] += 1
        elif l3[v][1] == 0 and l3[v][2] >= 4:
            l3[v][2] -= 3
            l3[v+10][2] += 1
            l3[v-1][2] += 1
            l3[v+1][2] += 1
        elif l3[v][1] == 9 and l3[v][2] >= 4:
            l3[v][2] -= 3
            l3[v-10][2] += 1
            l3[v+1][2] += 1
            l3[v-1][2] += 1
        elif l3[v][2] >= 4:
            l3[v][2] -= 4
            l3[v+10][2] += 1
            l3[v-10][2] += 1
            l3[v+1][2] += 1
            l3[v-1][2] += 1
    for n in range(len(obj)):
        canvas.delete(obj[n])
    decal_x = [10,20,30,10,30]
    decal_y = [10,20,10,30,30]
    decal_a = [30,20,10,30,10]
    decal_b = [30,20,30,10,10]
    e = 0
    for v in range(1,101):
        for r in range(l3[v][2]):
            obj.append(canvas.create_oval((l3[v][0]*50*p+decal_x[r]*p,0+50*l3[v][1]*p+decal_y[r]*p),(50*p+l3[v][0]*50*p-decal_a[r]*p,50*p+50*l3[v][1]*p-decal_b[r]*p), fill ="yellow"))

bouton1 = tk.Button(racine, text="change config", command = changement_config)
bouton1.grid(row=1, column= 0)

racine.mainloop()