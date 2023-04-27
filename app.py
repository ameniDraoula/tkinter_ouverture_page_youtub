from tkinter import*
from tkinter import Tk
import webbrowser
def open_chanel():
    webbrowser.open_new("https://www.culturedeconfiture.fr/top-5-chansons-avril-lavigne/")#url
# creation du 1er fenetre
window = Tk()

# personnaliser ma fenetre
window.title("Bonjours les funs")
# donner largeur et hauteur de la fentre
window.geometry("480x360")
#fixer la taille minimale de la fenetre
window.minsize(350,250) 
#changer le couleur d'arrier plan
window.config(background='#283281')
#crer un frame
frame=Frame(window,bg='#283281')
frame.pack(expand=YES)#expand=YES=> pour mettre toujours au centre

#ajout des composant graphic label
label_title=Label(frame,text="bien venu",font=("Courier",40),bg='#283281',fg='white')
label_title.pack()# pour l'impacter et l'afficher 
label_subtitle=Label(frame,text=" Music d'Avril Lavigne",font=("Courier",25),bg='#283281',fg='white')
label_subtitle.pack()

#ajout d'un button
btn=Button(frame , text="ourir youtub",font=("Courier",20),bg='white',fg='#283281',command= open_chanel)
btn.pack(expand=YES)
#window.iconbitmap("examm.ico") # pour changer l'icone

#afficher la fenetre
window.mainloop()
