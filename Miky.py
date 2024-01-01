from tkinter import HIDDEN, NORMAL, Tk, Canvas

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'White' else 'White'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)


def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)


root = Tk()
c = Canvas(root, width=450, height=500)
c.configure(bg='Yellow', highlightthickness=0)
c.body_color = 'White'
# เส้นขอบรอบตัวการตูน
c.create_oval(120, 150, 230, 340, outline='black', width=10)
c.create_oval(195, 150, 295, 340, outline='black', width=10)
c.create_oval(78, 290, 350, 415, outline='black', width=10)
c.create_oval(55, 265, 170, 360, outline='black', width=10)
c.create_oval(250, 265, 369, 360, outline='black', width=10)
c.create_oval(115, 215, 310, 435, outline='black', width=10)

ear_left = c.create_oval(1, 1, 190, 190, outline='Black', fill='Black')
ear_right = c.create_oval(240, 1, 430, 190, outline='Black', fill='Black')
face = c.create_oval(55, 110, 370, 420, outline='Black', fill='Black')
Skin1 = c.create_oval(120, 150, 230, 340, outline='#ffebcd', fill='#ffebcd')
Skin2 = c.create_oval(195, 150, 295, 340, outline='#ffebcd', fill='#ffebcd')
Skin3 = c.create_oval(78, 290, 350, 415, outline='#ffebcd', fill='#ffebcd')
Skin4 = c.create_oval(55, 265, 170, 360, outline='#ffebcd', fill='#ffebcd')
Skin5 = c.create_oval(250, 265, 369, 360, outline='#ffebcd', fill='#ffebcd')
Skin6 = c.create_oval(115, 215, 310, 435, outline='#ffebcd', fill='#ffebcd')
eye_left = c.create_oval(165, 170, 200, 270, outline='black', fill='White')
eye_right = c.create_oval(230, 170, 265, 270, outline='black', fill='White')
pupil_left = c.create_oval(175, 225, 195, 270, outline='Black', fill='Black')
pupil_right = c.create_oval(235, 225, 255, 270, outline='Black', fill='Black')
nose = c.create_oval(170, 280, 265, 350, outline='Black', fill='Black')
line_mouse = c.create_line(120, 345, 210, 425, 315, 345, smooth=1, width=6, state=NORMAL)
line_mouse2 = c.create_line(160,375, 215, 465, 265, 375, smooth=1, width=6, state=NORMAL)


c.pack()
root.after(1000, blink)
root.mainloop()
