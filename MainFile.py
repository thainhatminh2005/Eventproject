from tkinter import *
from tkinter.colorchooser import *
from PIL import Image, ImageTk


def chonmau():
    a, b = askcolor()
    print(b)
def manhinhtren():
    back_image = Image.open('back.jpg')
    back_imageTk = ImageTk.PhotoImage(back_image)
    next_image = Image.open('next.jpg')
    next_imageTk = ImageTk.PhotoImage(next_image)

    frame = Frame(window, bg = '#a4ffa4', border = 1, relief = SUNKEN)
    frame.pack_configure(side = TOP, anchor = N, fill = X, padx = 3, pady = 3, expand = True)
    back_button = Button(frame, image=back_imageTk)
    back_button.image = back_imageTk
    back_button.pack_configure(side=LEFT)
    next_button = Button(frame, image=next_imageTk)
    next_button.image = next_imageTk
    next_button.pack_configure(side=RIGHT)


class manhinhchua():
    def __init__(self):
        self.frame = Frame(window, bg = '#000000', height = 269)
        self.frame.pack_configure(fill = BOTH, expand = True)

    def page1st(self):
        frame = Frame(self.frame)
        frame.pack_configure(fill = BOTH, expand  = True)
        label = Label(frame, text = 'Cùng nhau học sự kiện lịch sử')
        label.pack_configure()
        button1st = Button(frame, text = 'Tạo sự kiện', height = 2, width = 15)
        button1st.pack_configure(pady = 2)
        button2nd = Button(frame, text = 'Kiểm tra', height = 2, width = 15)
        button2nd.pack_configure(pady = 2)
    def pagetao(self):
        frame = Frame(self.frame)
        frame.pack_configure(fill=BOTH, expand=True)
        button1st = Button(frame, text='Tạo bộ mới', height=2, width=15)
        button1st.pack_configure(pady=2)
        button2nd = Button(frame, text='Xem các bộ\nsự kiện đã có', height=2, width=15)
        button2nd.pack_configure(pady=2)
    def pagetaosk(self):
        frame = Frame(self.frame)
        frame.pack_configure(fill=BOTH, expand=True)
        label = Label(frame, text='Các bộ sự kiện đã có')
        label.pack_configure()
        frame2 = Frame(frame, width = 300, height = 200, bg = '#00ffff')
        frame2.pack_configure()
        scrollbar = Scrollbar(frame2)
        scrollbar.pack_configure(side = RIGHT, fill = Y)
        listbox = Listbox(frame2, width = 75, yscrollcommand = scrollbar.set)
        for i in range(1,10):
            listbox.insert(END, i)
        listbox.pack_configure(side = LEFT)
        scrollbar.configure(command = listbox.yview)
        button = Button(frame, text = 'Enter')
        button.pack_configure(pady = 5)
    def xemsk(self):
        pass
    def khungtaosk(self):
        frame = Frame(self.frame)
        frame.pack_configure(fill = BOTH, expand = True)
        frame2 = Frame(frame)
        frame2.pack_configure()
        text_sk = Text(frame2, height = 4, width = 50)
        text_sk.pack_configure(side = RIGHT)
        label_sk = Label(frame2, text = 'Nhập sự kiện')
        label_sk.pack_configure(side = LEFT, anchor = N)
        frame3 = Frame(frame)
        frame3.pack_configure()
        label_day = Label(frame3, text = 'Ngày')
        label_day.pack_configure(side = LEFT)
        entry_day = Entry(frame3, width = 2)
        entry_day.pack_configure(side = LEFT)
        label_month = Label(frame3, text='Tháng')
        label_month.pack_configure(side=LEFT)
        entry_month = Entry(frame3, width=2)
        entry_month.pack_configure(side=LEFT)
        label_year = Label(frame3, text='Năm')
        label_year.pack_configure(side=LEFT)
        entry_year = Entry(frame3, width=4)
        entry_year.pack_configure(side=LEFT)
        frame4 = Frame(frame)
        frame4.pack_configure(side = BOTTOM, anchor = E, padx = 10)
        button1 = Button(frame4, text='Tiếp tục')
        button1.pack_configure(pady=5, side = RIGHT)
        button2 = Button(frame4, text = 'hoàn thành')
        button2.pack_configure(side = RIGHT)
    def taobomoi(self):
        frame = Frame(self.frame)
        frame.pack_configure(fill = BOTH, expand = True)
        label_day = Label(frame, text='Nhập tên bộ')
        label_day.pack_configure()
        entry_day = Entry(frame, width = 50)
        entry_day.pack_configure()
        button1 = Button(frame, text='Enter')
        button1.pack_configure(pady=5)
    def chonbokt(self):
        frame = Frame(self.frame)
        frame.pack_configure(fill=BOTH, expand=True)
        label = Label(frame, text='Chọn bộ sự kiện kiểm tra của bạn')
        label.pack_configure()
        frame2 = Frame(frame, width=300, height=200, bg='#00ffff')
        frame2.pack_configure()
        scrollbar = Scrollbar(frame2)
        scrollbar.pack_configure(side=RIGHT, fill=Y)
        listbox = Listbox(frame2, width=75, yscrollcommand=scrollbar.set)
        for i in range(1, 100):
            listbox.insert(END, i)
        listbox.pack_configure(side=LEFT)
        scrollbar.configure(command=listbox.yview)
        button = Button(frame, text='Enter')
        button.pack_configure(pady=5)
        
#TAO MAN HINH
window = Tk()
window.wm_title('History Event')
window.wm_resizable(0,0)
window.wm_geometry('500x300+400+200')
manhinhtren()
manhinhchua().pagetaosk()
window.mainloop()