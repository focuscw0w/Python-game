vyska_okna = 800
dlzka_okna = 1000

import tkinter, random, keyboard
canvas = tkinter.Canvas(width = dlzka_okna, height = vyska_okna, bg='lightblue')
canvas.pack()

vajce_x = random.randint(20, 580)
vajce_y = 0
pocet_bodov = 0

letters = ['w', 's', 'g', 'j', 'o', 'm', 'z', 'v', 'q', 'a', 'b', 'x', 'c', 'p', 'y', 'h', 'f', 'l', 'd']
pismenko = random.choice(letters)

def vajce(x,y):
  canvas.create_oval(x - 20,  y - 1, x + 5,  y + 30,  fill='#edb87c', outline='#edb87c')

  # funkcia na zresetovanie vajíčka ak padne dole

def reset():
    global vajce_y, vajce_x, pismenko
    pismenko = random.choice(letters)
    vajce_y = 20
    vajce_x = random.randint(20, 580)

  # funkcia na padanie vajíčka

def padanieVajca():
    global vajce_y, pocet_bodov
    canvas.delete('all')

    vajce_y += 2.5
    vajce(vajce_x, vajce_y)

    canvas.create_text(vajce_x - 8, vajce_y + 12, text = pismenko, fill='#000')
    
  # ak je vajíčko na dolnej hranici, vráti sa naspäť

    if vajce_y == vyska_okna:
        pocet_bodov -= 1
        score.configure( text = f'Počet bodov: {pocet_bodov}')
        reset()

  # funkcia, ktorá kontroluje či sa dané písmenko zhoduje so
  # stlačeným písmenom na klávesnici

    if keyboard.is_pressed(pismenko):
        pocet_bodov += 1
        score.configure( text = f'Počet bodov: {pocet_bodov}')
        reset()
       
    canvas.after(10, padanieVajca)

padanieVajca()


score = tkinter.Label(text = f'Počet bodov: 0')
score.pack()

canvas.mainloop()