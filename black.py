#!/ysr/bin/python3
# Black-Webbrowser v2.0 (New)
#
# ------------------------Black Webbrowser--------------------------
# |                             ⬛⬛⬛                              |
# | Github: https://github.com/black-software-com                  |
# | Instagram: https://instagram.com/black_software_company        |
# | Telgeram: t.me/blacksoftware3                                  |
# | Twitter: @blacksoftware3                                       |
# ------------------------------------------------------------------
#

from os import system as command
from time import sleep
from subprocess import getoutput,SubprocessError
from sys import argv
import sys
from random import shuffle
from platform import system
from webbrowser import open_new_tab
from datetime import datetime
try:
  from requests import get
except (Exception,ImportError,):
  getoutput("python -m pip install requests")
try:
  from speedtest import Speedtest
except (Exception,ImportError,):
  getoutput("python -m pip install speedtest-cli")
try:
  from colorama import Fore,init
  init()
except (Exception,ImportError,):
  getoutput("python -m pip install colorama")
try:
  from wget import download
except (Exception,ImportError,):
  getoutput("python -m pip install wget")
try:
  from PyQt5.QtCore import QUrl,pyqtSlot,pyqtSignal,QThread
  from PyQt5.QtWidgets import QMainWindow,QLabel,QPushButton,QTextEdit,QLineEdit,QAction,QMenuBar,QStatusBar,QToolBar,QApplication,QMessageBox,QProgressBar,QWidget,QVBoxLayout,QRadioButton,QStyleFactory,QMenu
  from PyQt5.QtGui import QIcon,QKeySequence,QFont
  from PyQt5 import QtGui, QtCore
except (Exception,ImportError,):
  getoutput("python -m pip install pyqt5-tools")
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
except (Exception,ImportError,):
  getoutput("python -m pip install PyQtWebEngine")
try:
  from tkinter import *
  from tkinter.ttk import *
  from tkinter.scrolledtext import ScrolledText
  from tkinter.messagebox import showinfo,showerror,askyesno
except (Exception,ImportError):
  getoutput("python -m pip install tk-tools")
try:
  from tkhtmlview import HTMLLabel
except (Exception,ImportError,):
  getoutput("python -m pip install tkhtmlview")
try:
  from ttkbootstrap import Style
except (Exception,ImportError,):
  getoutput("python -m pip install ttkbootstrap")
try:
  from googlesearch import search
except (Exception,ImportError,):
  getoutput("python -m pip install googlesearch-python")
def run_bw_o():
        file_checkvi = open("./Core/check_vi","r+").read()
        bmess = '''
Black-Webbrowser v2.0
Property:

  Search speed
  Search graphics High quality
  System security
        '''
        if file_checkvi == 'True' or file_checkvi == 'True\n':
          try:
            ch = get('https://google.com')
            if ch.status_code == 200:
              # ap = QApplication(sys.argv)
              # app.setApplicationName('Black Webbrowser')
              window = Window()
              window.vi()
              # ap.exec_()
          except (ConnectionError,Exception,):
            showerror(title='Cannot Running',message='Please, Check Internet!')
            print(False)
        else:
          try:
            ch = get('https://google.com')
            if ch.status_code == 200:
              # ap = QApplication(sys.argv)
              # ap.setApplicationName('Black Webbrowser')
              window = Window()
              # ap.exec_()
          except (ConnectionError,Exception,):
            showerror(title='Cannot Running',message='Please, Check Internet!')
            print(False)
class Window(QMainWindow):
  def __init__(self):
     super(Window, self).__init__()
     self.time_zone = datetime.now()
     print(f"\nStart Black-Webbrowser At: {self.time_zone}\n")
     self.main()
  def main(self):
     global searchfile,g1,t,f,h
     file_check_sd = open("./Core/check_sd","r").read()
     if file_check_sd == '0' or file_check_sd == '0\n' or file_check_sd == '1' or file_check_sd == '1\n' or file_check_sd == '2' or file_check_sd == '2\n':
      n = int(file_check_sd)
      n+=1
      file_check_sd = open("./Core/check_sd","w")
      file_check_sd.write(str(n))
      file_check_sd.close()
     else:
      open_new_tab('https://idpay.ir/mrprogrammer2938')
      sleep(6)
     QApplication.setStyle(QStyleFactory.create('windowsvista'))
     # self.browser = QWebEngineView(self)
     # self.browser.setUrl(QUrl('https://google.com'))
     # self.browser.urlChanged.connect(self.update_AddressBar)
     # self.setStyleSheet('background-color: black;')
     self.setGeometry(100,60,1800,1000)
     self.setWindowIcon(QIcon('./Scr/black.png'))
     self.update_banner = ""
     # self.setCentralWidget(self.browser)
     self.status_bar = QStatusBar(self)
     self.setStatusBar(self.status_bar)
     self.navigation_bar = QToolBar('Navigation Toolbar')
     self.navigation_bar.move(150,30)
     self.addToolBar(self.navigation_bar)
     back_button = QAction("Back", self)
     back_button.setStatusTip('Go to previous page you visited')
     # back_button.triggered.connect(self.browser.back)
     self.navigation_bar.addAction(back_button)
     next_button = QAction("Next", self)
     next_button.setStatusTip('Go to next page')
     # next_button.triggered.connect(self.browser.forward)
     self.navigation_bar.addAction(next_button)
     home_button = QAction("Home", self)
     home_button.setStatusTip('Go to home page (Google page)')
     home_button.triggered.connect(self.go_to_home)
     self.navigation_bar.addAction(home_button)
     refresh_button = QAction("Refresh", self)
     refresh_button.setStatusTip('Refresh this page')
     # refresh_button.triggered.connect(self.browser.reload)
     self.navigation_bar.addAction(refresh_button)
     self.navigation_bar.addAction(home_button)
     self.navigation_bar.addSeparator()
     self.URLBar = QLineEdit(self)
     self.URLBar.returnPressed.connect(self.search)
     self.lb = QLabel('Black Webbrowser',self)
     self.lb.setGeometry(640,50,500,500)
     self.lb.setFont(QFont('Arial',30))
     self.lb.setStyleSheet('color: green')
     self.word_k = QLineEdit(self)
     self.word_k.setGeometry(530,350,700,30)
     self.word_k.returnPressed.connect(self.search_key)
     g1 = QLabel('<a href="https://github.com/black-software-com" target="_blank"> Github </a>',self)
     g1.move(50,950)
     g1.setOpenExternalLinks(True)
     t = QLabel('<a href="https://github.com/black-software-com" target="_blank"> Tools </a>',self)
     t.move(100,950)
     t.setOpenExternalLinks(True)
     f = QLabel('<a href="https://github.com/black-software-Com/Black-Webbrowser/issues" target="_blank"> Send FeedBack </a>',self)
     f.move(140,950)
     # f.setOpenExtenralLinks(True)
     h = QLabel('<a href="https://black-software-com.github.io/Black-Help/" target="_blank"> Help </a>',self)
     h.move(240,950)
     # h.setOpenExtenralLinks(True)
     self.navigation_bar.addWidget(self.URLBar)
     self.addToolBarBreak()
     menu = QMenuBar(self)
     self.setMenuWidget(menu)
     aboutfile = menu.addMenu('About')
     searchfile = menu.addMenu('Search')
     browserm = menu.addMenu('Browser')
     reconm = menu.addMenu('Recon')
     shellm = menu.addMenu('Shell')
     helpm = menu.addMenu('Help')
     black_m = QAction('Black',self)
     black_m.setShortcut('F1')
     black_m.triggered.connect(self.black)
     help_m = QAction('Help',self)
     help_m.setShortcut('F2')
     help_m.triggered.connect(self.help)
     aboutfile.addActions([black_m,help_m])
     aboutfile.addSeparator()
     exit_m = QAction('Exit',self)
     exit_m.setShortcut('Ctrl+F4')
     exit_m.triggered.connect(quit)
     aboutfile.addAction(exit_m)
     fastsearch = QAction('Fast Search',self)
     fastsearch.triggered.connect(self.fastsearch)
     ipchanger = QAction('Ip Changer',self)
     ipchanger.triggered.connect(self.ipchanger)
     ipset = QAction('Ip Set',self)
     ipset.triggered.connect(self.setip)
     searchfile.addActions([fastsearch,ipchanger,ipset])
     searchfile.addSeparator()
     recon = QAction('Recon',self)
     recon.triggered.connect(self.recon)
     wget_m = QAction('Wget',self)
     wget_m.triggered.connect(self.wget)
     req = QAction('Request',self)
     req.triggered.connect(self.request)
     reconm.addActions([recon,wget_m,req])
     history = QAction('history',self)
     history.triggered.connect(self.history)
     history.setShortcut(QKeySequence('Ctrl+H'))     
     searchfile.addAction(history)
     bookmarks_toolbar = QToolBar('Bookmarks', self)
     self.addToolBar(bookmarks_toolbar)
     blacksoftware = QAction("Black-Software",self)
     blacksoftware.setStatusTip('Go To Black Software')
     blacksoftware.triggered.connect(self.black)
     bookmarks_toolbar.addAction(blacksoftware)
     google = QAction('google',self)
     google.triggered.connect(lambda : self.search_2('https://www.google.com'))
     bing = QAction('Bing',self)
     bing.triggered.connect(lambda : self.search_2('https://www.bing.com'))
     duck = QAction('Duck Duck Go',self)
     duck.triggered.connect(lambda : self.search_2('https://www.duckduckgo.com'))
     yahoo = QAction('Yahoo',self)
     yahoo.triggered.connect(lambda: self.search_2('https://en-maktoob.yahoo.com/?p=us&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAALUS4UUgOxL2QbS5jSlMecrNJ5R8XR2tT-YW1132GwhfyCLl7cyWI6tfLRzRtdzka_fZHRkUkNKauXLKZet84V5nyPONeX5-0gSXi7IafB4lmCUvvHll8F_P6Q1UY36uldjPDPj6zTaR1Lrh-T7rGcpd39BRDtXurs7jYOXFZCnU'))
     zarebin = QAction('Zarebin',self)
     zarebin.triggered.connect(lambda: self.search_2('https://zarebin.ir'))
     browserm.addActions([google,bing,duck,yahoo,zarebin  ])
     shella = QAction('shell',self)
     shella.triggered.connect(self.shell)
     shellm.addAction(shella)
     help_mm = QAction('Help',self)
     help_mm.triggered.connect(self.help)
     helpm.addAction(help_mm)
     feedbackm = QAction('Send FeedBack',self)
     feedbackm.triggered.connect(self.send_feedback)
     helpm.addAction(feedbackm)
     helpm.addSeparator()
     inst = QAction('Join Us on Instagram',self)
     inst.triggered.connect(self.instagram)
     helpm.addAction(inst)
     helpm.addSeparator()
     donate_mm = QAction('donate',self)
     donate_mm.setShortcut('Ctrl+D')
     donate_mm.triggered.connect(self.donate)
     helpm.addAction(donate_mm)
     helpm.addSeparator()
     about_hm = QAction('About',self)
     about_hm.triggered.connect(self.about)
     helpm.addAction(about_hm)
     facebook = QAction("Facebook", self)
     facebook.setStatusTip("Go to Facebook")
     facebook.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.facebook.com")))
     bookmarks_toolbar.addAction(facebook)
     linkedin = QAction("LinkedIn", self)
     linkedin.setStatusTip("Go to LinkedIn")
     linkedin.triggered.connect(lambda: self.go_to_URL(QUrl("https://in.linkedin.com")))
     bookmarks_toolbar.addAction(linkedin)
     instagram = QAction("Instagram", self)
     instagram.setStatusTip("Go to Instagram")
     instagram.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.instagram.com")))
     bookmarks_toolbar.addAction(instagram)
     twitter = QAction("Twitter", self)
     twitter.setStatusTip('Go to Twitter')
     twitter.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.twitter.com")))
     bookmarks_toolbar.addAction(twitter)
     self.show()
  def search_key(self):
    self.word = self.word_k.text()
    url = QUrl(f'https://zarebin.ir/search?q={self.word}')
    self.word_k.close()
    g1.close()
    t.close()
    h.close()
    f.close()
    self.browser = QWebEngineView(self)
    self.browser.setUrl(url)
    self.browser.urlChanged.connect(self.update_AddressBar)
    self.setCentralWidget(self.browser)
    self.update_AddressBar(url)
  def donate(self):
    self.go_to_URL(QUrl('https://idpay.ir/mrprogrammer2938'))
  def recon(self):
      global user
      win = Tk()
      win.title('Black-Webbrowser/Recon')
      win.geometry("500x400+300+100")
      photo = PhotoImage(file='black.png')
      win.iconphoto(False,photo)
      s = Style("darkly")
      ul = Label(win,text='Enter User: ',foreground='white')
      ul.place(bordermode=INSIDE,x=50,y=25)
      user = Entry(win,borderwidth=3,width=25)
      user.place(bordermode=INSIDE,x=145,y=25)
      click = Button(win,text='Scan',width=9,height=3,command=self.recon_r)
      click.place(bordermode=OUTSIDE,x=210,y=70)
      exit = Button(win,text='Exit',width=9,height=3,command=win.destroy)
      exit.place(bordermode=OUTSIDE,x=210,y=145)
      win.resizable(0,0)
      win.bind("<Return>",self.recon_r)
      win.mainloop()
  def update_blackwebbrowser(self): 
    self.title_update()
    self.cls()
    print(self.update_banner)
    if system() == 'Linux':
      getoutput("cd .. && rm -r Black-Webbrowser && git clone https://github.com/black-software-com/black-webbrowser && cd black-webbrowser && python black")
    else:
      print("Download Black-Webbrowser.zip")
      open_new_tab("https://github.com/black-software-Com/Black-Webbrowser/archive/refs/heads/master.zip")
  def recon_r(self,event=None):
        global ccmenu,textt,scrollbarr
        mylist = []
        for i in search(user.get()):
            mylist.append(f'{i} \n')
        win = Tk()
        win.title('Black-Webbrowser/History')
        win.geometry("500x400+300+100")
        win.resizable(0,0)
        menu = Menu(win,tearoff=0)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=win.destroy)
        menu.add_cascade(label='File',menu=filemenu)
        win.configure(menu=menu)
        ccmenu = Menu(win,tearoff=0)
        ccmenu.add_command(label='Cut',accelerator='Ctrl+X',command=self.cccut)
        ccmenu.add_command(label='Copy',accelerator='Ctrl+C',command=self.cccopy)
        ccmenu.add_command(label='Paste',accelerator='Ctrl+V',command=self.ccpaste)
        ccmenu.add_command(label='Reload',accelerator='Ctrl+R',command=self.ccreload)
        ccmenu.add_separator()
        ccmenu.add_command(label='Delete',accelerator='Ctrl+D',command=self.ccdelete)
        ccmenu.add_separator()
        ccmenu.add_command(label='Select All',accelerator='Ctrl+A',command=self.cselectall_text)
        ccmenu.add_separator()
        ccmenu.add_command(label='Exit',accelerator='Ctrl+F4',command=win.destroy)
        s = Style('darkly')
        textt = Text(win, height=50,width=60)
        textt.grid(row=0, column=0, sticky='ew')
        scrollbarr = Scrollbar(win, orient='vertical', command=textt.yview)
        scrollbarr.grid(row=0, column=1, sticky='ns')
        textt['state'] = 'normal' 
        textt.insert(END,mylist)       
        textt['state'] = 'disabled'
        win.bind("<Control-a>",self.cselectall_text)
        win.bind("<Control-r>",self.creload)
        win.bind("<Control-d>",self.cdelete)
        win.bind("<Button-3>",self.doo_popup)
        win.mainloop()
  def cls(self):
    if system() == 'Windows':
      command("cls")
    else:
      command("clear")
  def title(self):
    if system() == 'Linux':
      command("printf '\033]2;Black-Webbrowser\a'")
    else:
      command("title Black-Webbrowser")
  def title_update(self):
    if system() == 'Linux':
      command("printf '\033]2;Black-Webbrowser/Update\a'")
    else:
      command("title Black-Webbrowser/Update")

  def wget(self): 
      global link,click,exit_b,txt,window,wmenu
      window = Tk()
      wmenu = Menu(window,tearoff=0)
      wfilemenu = Menu(wmenu,tearoff=0)
      wfilemenu.add_command(label='Scan',command=self.wget_r)
      wfilemenu.add_command(label='Reset',command=self.clear_dw)
      wfilemenu.add_separator()
      wfilemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=window.destroy)
      wrfilemenu = Menu(wmenu,tearoff=0)
      wrfilemenu.add_command(label='Scan',command=self.wget_r)
      wrfilemenu.add_command(label='Reset',command=self.clear_dw)
      wrfilemenu.add_separator()
      wrfilemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=window.destroy)
      wmenu.add_cascade(label='Options',menu=wfilemenu)
      window.config(menu=wmenu)
      window.title('Black-Webbrowser/Wget')
      window.geometry("750x525+300+100")
      s = Style("darkly")
      photo = PhotoImage(file='black.png')
      window.iconphoto(False,photo)
      label = Label(window,text='Enter Link: ',foreground='white')
      label.place(bordermode=INSIDE,x=25,y=25)
      link = Entry(window,borderwidth=3,width=65)
      link.place(bordermode=INSIDE,x=118,y=25)
      click = Button(window,text='Scan',width=9,height=1,command=self.wget_r)
      click.place(bordermode=OUTSIDE,x=390,y=60)
      exit_b = Button(window,text='Exit',width=9,height=1,command=window.destroy)
      exit_b.place(bordermode=OUTSIDE,x=295,y=60)
      txt = ScrolledText(window)
      txt['width'] = 70
      txt['height'] = 20
      txt.place(bordermode=INSIDE,x=40,y=95)
      txt['state'] = 'disabled'
      window.bind("<Button-3>",self.do_popupw)
      window.resizable(0,0)
      window.bind("<Return>",self.wget_r)
      window.mainloop()
  def do_popupw(self,event):
      try:
          wmenu.tk_popup(event.x_root,event.y_root)
      finally:
          wmenu.grab_release()
  def wget_r(self,event=None):
      d = download(link.get())
      txt['state'] = 'normal'
      txt.insert(INSERT,d)
      txt['state'] = 'disabled'  
      click.place(bordermode=OUTSIDE,x=350,y=60)
      exit_b.place(bordermode=OUTSIDE,x=253,y=60)
      clear = Button(window,text='Clear',width=9,height=1,foreground='white',command=self.clear_dw)
      clear.place(bordermode=OUTSIDE,x=447,y=60)
  def clear_dw(self):
      global txt
      link.delete(0,END)
      txt.destroy()
      txt = ScrolledText(window)
      txt['width'] = 70
      txt['height'] = 20
      txt.place(bordermode=INSIDE,x=40,y=95)
  def request(self):
      global host
      win = Tk()
      win.title('Black-Webbrowser/Request')
      win.geometry("500x400+300+100")
      photo = PhotoImage(file='black.png')
      win.iconphoto(False,photo)
      s = Style("darkly")
      hl = Label(win,text='Enter Host: ',foreground='white')
      hl.place(bordermode=INSIDE,x=50,y=25)
      host = Entry(win,borderwidth=3,width=25)
      host.place(bordermode=INSIDE,x=145,y=25)
      click = Button(win,text='Scan',width=9,height=3,command=self.request_r)
      click.place(bordermode=OUTSIDE,x=210,y=70)
      exit = Button(win,text='Exit',width=9,height=3,command=win.destroy)
      exit.place(bordermode=OUTSIDE,x=210,y=145)
      win.resizable(0,0)
      win.bind("<Return>",self.request_r)
      win.mainloop()
  def request_r(self,event=None):
      if host.get()[0:8] == 'https://' or host.get()[0:7] == 'http://':
          r = get(host.get())
      else:
          r = get(f'https://{host.get()}')
      showinfo(title='Request',message=f'Ping: {r.status_code}')
  def set_ip(self,event=None):
      self.ip_i = ip_i.get()
      try:
        askq = askretrycancel(title='Black-Webbrowser/Ip-Set',message='Do You Want To Set Ip?')
        if askq:
            getoutput(f"netsh interface ip set address name=”Local Area Connection” static {self.ip_i} 255.255.255.0 {self.ip_i}")
            getoutput(f"netsh interface ip set address name=”Local Area Connection” source=dhcp")
            getoutput(f"netsh interface ip set dns name=”Local Area Connection” static {self.ip}")
            getoutput(f"netsh interface ip add dns name=”Local Area Connection” 8.8.8.8 index=2")
            getoutput(f"netsh interface ip set dnsservers name=”Local Area Connection” source=dhcp")
            print(f"\nIp Set: {Fore.GREEN}{self.ip_i}{self.end}\n")
            searchfile.add_command(label='My-Ip',command=self.my_ip)
            win_i.destroy()
        else:
          print(False)
      except (Exception,SubprocessError,) as err:
        print(err)
          # showerror(title='Error',message='Cannot Running This Program!')
          # print(False)
  def setip(self):
      global win_i,ip_i
      win_i = Tk()
      s = Style("sandstone")
      win_i.title('Black-Webbrowser/Set-Ip')
      win_i.geometry("400x300+300+100")
      win_i.resizable(0,0)
      label = Label(win_i,text='Enter Ip:')
      label.place(bordermode=INSIDE,x=45,y=10)
      ip_i = Entry(win_i,width=20)
      ip_i.place(bordermode=INSIDE,x=120,y=10)
      click = Button(win_i,text='Set',width=9,command=self.set_ip)
      click.place(bordermode=OUTSIDE,x=165,y=60)
      exit_b = Button(win_i,text='Exit',width=9,command=win_i.destroy)
      exit_b.place(bordermode=OUTSIDE,x=165,y=120)
      win_i.bind("<Return>",self.set_ip)
      win_i.mainloop()
  def ipchanger(self):
        myn1 = []
        myn2 = []
        myn3 = []
        mynall = []
        myn1.append(self.my_nums[0:3])
        myn2.append(self.my_nums[3:6])
        myn3.append(self.my_nums[6:10])
        for num in myn1:
            mynall.append(num)
        for num2 in myn2:
            mynall.append(num2)
        for num3 in myn3:
            mynall.append(num3)
        shuffle(mynall)
        a = ""
        for i in mynall:
            for j in i:
                a+=str(j)
        self.ip = f"{a[0:3]}.{a[3:6]}.{a[6:9]}"
        try:
            getoutput(f"netsh interface ip set address name=”Local Area Connection” static {self.ip} 255.255.255.0 {self.ip}")
            getoutput(f"netsh interface ip set address name=”Local Area Connection” source=dhcp")
            getoutput(f"netsh interface ip set dns name=”Local Area Connection” static {self.ip}")
            getoutput(f"netsh interface ip add dns name=”Local Area Connection” 8.8.8.8 index=2")
            getoutput(f"netsh interface ip set dnsservers name=”Local Area Connection” source=dhcp")
            print(f"\nIp Set: {Fore.GREEN}{self.ip}{self.end}\n")
            searchfile.add_command(label='My-Ip',command=self.my_ip)
            self.after(900000,self.change_ip)
        except (Exception,SubprocessError,):
            showerror(title='Error',message='Cannot Running This Program!')
            print(False)
  def fastsearch(self):
      sp = Speedtest() 
      if system() == 'Windows':
            try:
               command = getoutput("Netsh int tcp show global");print(command)
               command2 = getoutput("Netsh int tcp set chimney=enabled");print(command2)
               command3 = getoutput("Netsh int tcp set global autotuninglevel=normal");print(command3)
               command4 = getoutput("Netsh int set global congestionprovider=ctcp");print(command4)
               print(True)
               showinfo(title='Internet Speed',message=f'Your Speed: \nDownload: {sp.download()}\nUpload: {sp.upload()}')
            except SubprocessError:
                print(False)
                showerror(title='Error',message='Cannot Running This Program!')   
      else:
            return # Linux
  @pyqtSlot()
  def history(self):
      file_ch = open("./Core/check_hp","r+").read()
      if file_ch == 'False' or file_ch == 'False\n':
        global text,scrollbar,cmenu
        win = Tk()
        win.title('Black-Webbrowser/History')
        win.geometry("500x400+300+100")
        win.resizable(0,0)
        photo = PhotoImage(file='black.png')
        win.iconphoto(False,photo)
        menu = Menu(win,tearoff=0)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='Clear',command=self.clear_history)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=win.destroy)
        menu.add_cascade(label='File',menu=filemenu)
        win.configure(menu=menu)
        cmenu = Menu(win,tearoff=0)
        cmenu.add_command(label='Cut',accelerator='Ctrl+X',command=self.ccut)
        cmenu.add_command(label='Copy',accelerator='Ctrl+C',command=self.ccopy)
        cmenu.add_command(label='Paste',accelerator='Ctrl+V',command=self.cpaste)
        cmenu.add_command(label='Reload',accelerator='Ctrl+R',command=self.creload)
        cmenu.add_separator()
        cmenu.add_command(label='Select All',accelerator='Ctrl+A',command=self.selectall_text)
        cmenu.add_separator()
        cmenu.add_command(label='Delete',accelerator='Ctrl+D',command=self.cdelete)
        cmenu.add_command(label='Clear',command=self.clear_history)
        cmenu.add_separator()
        cmenu.add_command(label='Exit',accelerator='Ctrl+F4',command=win.destroy)
        s = Style('darkly')
        file_h = open("./Core/history.txt","r+").read()
        text = Text(win, height=50,width=60)
        text.grid(row=0, column=0, sticky='ew')
        scrollbar = Scrollbar(win, orient='vertical', command=text.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        text['state'] = 'normal' 
        text.insert(END,file_h)       
        text['state'] = 'disabled'
        win.bind("<Control-a>",self.selectall_text)
        win.bind("<Control-r>",self.creload)
        win.bind("<Control-d>",self.cdelete)
        win.bind("<Button-3>",self.do_popup)
        file_ch = open("./Core/check_hp","r+")
        file_ch.write("True")
        file_ch.close()
        win.mainloop()
        try:
            if win.destroy():
                file_ch = open("./Core/check_hp","r+")
                file_ch.write("False")
                file_ch.close()
            else:
                print(False)
        except (Exception,):
            file_ch = open("./Core/check_hp","r+")
            file_ch.write("False")
            file_ch.close()
      else:
          pass
  def about(self):
      global amenu
      root = Tk()
      root.title('Black-Webbrowser/About')
      root.geometry("700x600+550+130")
      root.resizable(0,0)
      txt_a = '''
Black Webbrowser is a search engine.
Property:
Search speed
System security
      '''
      photo = PhotoImage(file='./Scr/black.png')
      root.iconphoto(False,photo)
      amenu = Menu(root,tearoff=0)
      filemenu = Menu(amenu,tearoff=0)
      filemenu.add_command(label='Help',command=self.help)
      filemenu.add_separator()
      filemenu.add_command(label='Exit',command=root.destroy)
      amenu.add_cascade(label='Options',menu=filemenu)
      root.config(menu=amenu)
      label_i = Label(root,text='Black Webbrowser',foreground='black',font=("None",28))
      label_i.place(bordermode=INSIDE,x=130,y=15)
      label_t = Label(root,text=txt_a,foreground='black',font=("None",10))
      label_t.place(bordermode=INSIDE,x=175,y=65)
      b = HTMLLabel(root,html='<a href="https://black-software-com.github.io/Black-Software/" taregt="_blank"> Black </a>')
      b.place(bordermode=INSIDE,x=20,y=200)
      g = HTMLLabel(root,html='<a href="https://github.com/black-software-com" target="_blank"> Github </a>')
      g.place(bordermode=INSIDE,x=20,y=230)
      f = HTMLLabel(root,html='<a href="https://www.facebook.com/profile.php?id=100071465381949" target="_blank"> Facebook </a>')
      f.place(bordermode=INSIDE,x=20,y=260)
      i = HTMLLabel(root,html='<a href="https://instagram.com/black_software_company" target="_blank"> Instagram</a>')
      i.place(bordermode=INSIDE,x=20,y=290)
      t = HTMLLabel(root,html='<a href="https://twitter.com/blacksoftware3" target="_blank"> Twitter </a>')
      t.place(bordermode=INSIDE,x=20,y=320)
      tl = HTMLLabel(root,html='<a href="https://t.me/blacksoftware3" target="_blank"> Telegram </a>')
      tl.place(bordermode=INSIDE,x=20,y=350)
      z = HTMLLabel(root,html='<a href="https://zil.ink/blacksoftware" target="_blank"> ZLink </a>')
      z.place(bordermode=INSIDE,x=20,y=380)
      fl = Label(root,text='© Black Software')
      fl.place(bordermode=INSIDE,x=280,y=530)
      root.bind("<Button-3>",self.do_popupa)
      root.mainloop()
  def do_popupa(self,event):
      try:
          amenu.tk_popup(event.x_root,event.y_root)
      finally:
          amenu.grab_release()
  def send_feedback(self):
      self.go_to_URL(QUrl('https://github.com/black-software-Com/Black-Webbrowser/issues'))
  def instagram(self):
      self.go_to_URL(QUrl('https://instagram.com/black_software_company'))
  def selectall_text(self,event=None):
      text.event_generate("<<SelectAll>>")
  def cselectall_text(self,event=None):
      textt.event_generate("<<SelectAll>>")
  def ccut(self):
      textt.event_generate("<<Cut>>")
  def ccopy(self):
      textt.event_generate("<<Copy>>")
  def cpaste(self):
      textt.event_generate("<<Paste>>")
  def creload(self,event=None):
      textt.event_generate("<<Reload>>")
  def cdelete(self,event=None):
      textt.event_generate("<<Delete>>")
  def cccut(self):
      textt.event_generate("<<Cut>>")
  def cccopy(self):
      textt.event_generate("<<Copy>>")
  def ccpaste(self):
      textt.event_generate("<<Paste>>")
  def ccreload(self,event=None):
      textt.event_generate("<<Reload>>")
  def ccdelete(self,event=None):
      textt.event_generate("<<Delete>>")
  def do_popup(self,event):
      try:
          cmenu.tk_popup(event.x_root,event.y_root)
      finally:
          cmenu.grab_release()
  def doo_popup(self,event):
      try:
          ccmenu.tk_popup(event.x_root,event.y_root)
      finally:
          ccmenu.grab_release()
  def clear_history(self):
      global text,scrollbar
      q = askyesno(title='Clear History',message='Do You Want To Clear History? ')
      if q:
          file_h = open("./Core/history.txt","w")
          file_h.write("")
          file_h.close()
          file_h = open("./Core/history.txt","r+").read()
          text['state'] = 'normal'
          text.delete("1.0",END)
          text.insert(END,file_h)       
          text['state'] = 'disabled'
          print(True)
      else:
          print(False)
  def shell(self):
    shell_command_help = """
Black-Webbrowser Shell Command:
               
               search <Url>
               version
               help
    """
    self.title()
    self.cls()
    try:
      while True:
        inp = input("\nBlack-Webbrowser ~# ").split()
        if inp == []:
          pass
        elif inp[0] == 'version' or inp[0].lower() == 'version':
          print(version)
        elif inp[0] == 'help' or inp[0].lower() == 'help':
          print(shell_command_help)
        elif inp[0] == 'search':
          if len(inp) < 2:
            print("search <Url>")
          else:
            app = QApplication(sys.argv)
            url = inp[1]
            w = QMainWindow()
            w.setWindowTitle(f'Black-Webbrowser/{url}') 
            w.setWindowIcon(QIcon('./Scr/black.png'))
            w.setGeometry(250,100,1500,900)
            browser = QWebEngineView(w)
            browser.setUrl(QUrl(url))
            w.setCentralWidget(browser)
            w.show()
            app.exec_()
        elif inp[0] == 'black'.lower() or inp[0].lower() == 'start':
          file_chvi = open("./Core/check_vi","r").read()
          if file_chvi == 'True' or file_chvi == 'True\n':
            app = QApplication(sys.argv)            
            window = Window()
            window.vi()
            app.exec_()
          else:
            app = QApplication(sys.argv)
            window = Window()
            app.exec_()
        elif inp[0] == 'update' or inp[0].lower() == 'update':
          self.update_blackwebbrowser()
        elif inp[0] == 'exit' or inp[0].lower() == 'exit' or inp[0] == 'quit' or inp[0].lower() == 'quit':
          exit()
        else:
          y = " ".join(inp)
          print(f'\n{y} Not Found!')
    except (Exception,):
      showerror(title='Cannot Running',message='Cannot Running This Program!')
      print(False)
  def help(self):
      self.go_to_URL(QUrl('https://black-software-com.github.io/Black-Help/'))
  def black(self):
      self.go_to_URL(QUrl('https://black-software-com.github.io/Black-Software/'))
  def go_to_home(self):
    self.close()
    window = Window()
  def search(self):
    url = QUrl(self.URLBar.text())
    self.browser = QWebEngineView(self)
    self.browser.urlChanged.connect(self.update_AddressBar)
    self.setCentralWidget(self.browser)
    self.update_AddressBar(url)
    self.go_to_URL_2(url)
  def search_2(self,url):
    url = QUrl(url)
    self.browser = QWebEngineView(self)
    self.browser.urlChanged.connect(self.update_AddressBar)
    self.setCentralWidget(self.browser)
    self.update_AddressBar(url)
    self.go_to_URL_3(url)
  def go_to_URL_3(self,url):
    self.browser.setUrl(url)
    self.update_AddressBar(url)
  def go_to_URL(self):
     try:
      self.word_k.close()
      g1.close()
      t.close()
      h.close()
      f.close()
     except (Exception,):
      pass    
     if url.url().find(".com") == -1 and url.scheme() == '':
            self.browser.setUrl(f'https://zarebin.ir/search?q={url.url()}')
            self.update_AddressBar(url)
            file_h = open("./Core/history.txt","a")
            file_h.write(f'{url.url()}\n')
            file_h.close()
     elif url.scheme() == '' and url.url().find(".com"):
        self.browser.setUrl(QUrl(f'https://{url.url()}'))
        self.update_AddressBar(url)
        file_h = open("./Core/history.txt","a")
        file_h.write(f'{url.url()}\n')
        file_h.close()
     else:
            self.browser.setUrl(QUrl(url.url()))
            self.update_AddressBar(url)
            file_h = open("./Core/history.txt","a")
            file_h.write(f'{url.url()}\n')
            file_h.close()
  def go_to_URL_2(self, url):
     try:
      self.word_k.close()
      g1.close()
      t.close()
      h.close()
      f.close()
     except (Exception,):
      pass
     if url.url().find(".com") == -1 and url.scheme() == '':
            self.browser.setUrl(QUrl(f'https://zarebin.ir/search?q={url.url()}'))
            self.update_AddressBar(url)
            file_h = open("./Core/history.txt","a")
            file_h.write(f'{url.url()}\n')
            file_h.close()
     elif url.scheme() == '' and url.url().find(".com"):
        self.browser.setUrl(QUrl(f'https://{url.url()}'))
        self.update_AddressBar(url)
        file_h = open("./Core/history.txt","a")
        file_h.write(f'{url.url()}\n')
        file_h.close()
     else:
            self.browser.setUrl(QUrl(url.url()))
            self.update_AddressBar(url)
            file_h = open("./Core/history.txt","a")
            file_h.write(f'{url.url()}\n')
            file_h.close()
  def update_AddressBar(self, url):
     self.URLBar.setText(url.toString())
     self.URLBar.setCursorPosition(0)
  def vi(self):
      mess = QMessageBox()
      mess.setWindowTitle('Black-Webbrowser/Note')
      mess.setWindowIcon(QIcon('black.png'))
      mess.setText(bmess)
      re = mess.exec_()
      file_checkvi = open("./Core/check_vi","w")
      file_checkvi.write("False")
      file_checkvi.close()
      mess.exec_()
class Thread(QThread):
    _signal = pyqtSignal(int)
    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(100):
            sleep(0.1)
            self._signal.emit(i)
class color():
  green = '\033[92m;'
  red = '\033[91m'
  cyan = '\033[94m'
  orange = '\033[33m'
  blue = '\033[34m'
  endline = '\033[4m'
  end = '\033[0m'
class black_webbrowser_installing(Tk):
    def __init__(self):
        super(black_webbrowser_installing,self).__init__()
        global i_menu
        self.style = Style("darkly").master
        self.title('Black-Webbrowser/Installing')
        self.geometry("650x600+500+100")
        self.photo = PhotoImage(file = './Scr/black.png')
        i_menu = Menu(self,tearoff=0)
        filemenu = Menu(i_menu,tearoff=0)
        filemenu.add_command(label='About',accelerator='F1',command=self.about)
        filemenu.add_command(label='Black',accelerator='F2',command=self.black)
        filemenu.add_separator()
        filemenu.add_command(label='Help',accelerator='F3',command=self.black_help)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=self.destroy)
        i_menu.add_cascade(label='Options',menu=filemenu)
        self.config(menu=i_menu)
        label_l = Label(self,text='Black-Webbrowser',background='gray13',foreground='green',font=("None",30))
        label_l.place(bordermode=INSIDE,x=110,y=20)
        self.install_b = Button(self,text='Install',width=9,command=self.install)
        self.install_b.place(bordermode=OUTSIDE,x=255,y=110)
        self.exit_b = Button(self,text='Exit',width=9,command=self.destroy)
        self.exit_b.place(bordermode=OUTSIDE,x=255,y=150)
        self.iconphoto(False,self.photo)
        self.resizable(False,False)
        self.config(menu=i_menu)
        self.bind("<F1>",self.about)
        self.bind("<F2>",self.black)
        self.bind("<F3>",self.black_help)
        self.bind("<Button-3>",self.do_popupib)
        self.mainloop()
    def do_popupib(self,event):
       try:
          i_menu.tk_popup(event.x_root,event.y_root)
       finally:
          i_menu.grab_release()
    def black(self,event=None):
        win = Tk()
        win.title('Black-Webbrowser/Black')
        win.geometry("600x500")
        try: 
            w = tkinterweb.HtmlFrame(win)
            w.load_website('https://black-software-com.github.io/Black-Software/')
            w.pack(fill='both',expand=True)
        except (Exception,):
            print(False)
            win.destroy()
        win.mainloop()
    def about(self,event=None):
        win = Tk()
        win.title('Black-Webbrowser/About')
        win.geometry("600x500")
        try:
            w = tkinterweb.HtmlFrame(win)
            w.load_website('https://github.com/black-software-com')
            w.pack(fill='both',expand=True)
        except (Exception,):
            print(False)
            win.destroy()
        win.mainloop()
    def black_help(self,event=None):
        win = Tk()
        win.title('Black-Webbrowser/Black-Help')
        win.geometry("600x500")
        try:
            w = tkinterweb.HtmlFrame(win)
            w.load_website('https://black-software-com.github.io/Black-Help')
            w.pack(fill='both',expand=True)
        except (Exception,):
            print(False)
            win.destroy()
        win.mainloop()
    def install(self):
        global pr
        pr = Progressbar(self,orient='horizontal',mode='determinate',length=230)
        pr.place(bordermode=INSIDE,x=193,y=78)
        pr.start(50)
        pr.after(5700,self.install_2)
    def install_2(self):
            global bmess
            bmess = '''
Black-Webbrowser v2.0
Property:

  Search speed
  Search graphics High quality
  System security
        '''
            pr.stop()
            if system() == 'Linux':
                getoutput("chmod +x black")
                getoutput("cp /Core/black /usr/local/bin && cp /Core/black /usr/bin")
                getoutput("bash ./Core/install.sh")
                file_chi = open("./Core/file_chi","w")
                file_chi.write("True")
                file_chi.close()
            else:
                getoutput("copy /Core/black C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs")
                file_chi = open("./Core/file_chi","w")
                file_chi.write("True")
                file_chi.close()
            pr.stop()
            pr.destroy()
            self.install_b.destroy()
            self.start_b = Button(self,text='Start',width=9,command=self.run_bw)
            self.start_b.place(bordermode=OUTSIDE,x=255,y=110)
            self.exit_b.place(bordermode=OUTSIDE,x=255,y=150)
            label_mess = Label(self,text='Complete!',foreground='green',background='gray13')
            label_mess.place(bordermode=INSIDE,x=258,y=83)
    def ext(self):
        self.destroy()
        self.quit()
        quit()
    def run_bw(self):
        self.destroy()
        file_checkvi = open("./Core/check_vi","r+").read()
        bmess = '''
Black-Webbrowser v2.0
Property:

  Search speed
  Search graphics High quality
  System security
        '''
        if file_checkvi == 'True' or file_checkvi == 'True\n':
          try:
            ch = get('https://google.com')
            if ch.status_code == 200:
              # app = QApplication(sys.argv)
              # app.setApplicationName('Black Webbrowser')
              window = Window()
              window.vi()
              # ap.exec_()
          except (ConnectionError,Exception,):
            showerror(title='Cannot Running',message='Please, Check Internet!')
            print(False)
        else:
          try:
            ch = get('https://google.com')
            if ch.status_code == 200:
              # ap = QApplication(sys.argv)
              # ap.setApplicationName('Black Webbrowser')
              window = Window()
              # ap.exec_()
          except (ConnectionError,Exception,):
            showerror(title='Cannot Running',message='Please, Check Internet!')
            print(False)
class black_installing_l(QWidget):
    def __init__(self):
        super(black_installing_l, self).__init__()
        global license,txt,icd,ic
        self.setWindowTitle('Black-Webbrowser/Installing')
        self.setWindowIcon(QIcon('./Scr/black.png'))
        menu = QMenuBar(self)
        filemenu = menu.addMenu('Options')
        about_m = QAction('About',self)
        about_m.setShortcut('F1')
        about_m.triggered.connect(self.about)
        black_m = QAction('Black',self)
        black_m.setShortcut('F2')
        black_m.triggered.connect(self.black)
        help_m = QAction('Help',self)
        help_m.setShortcut('F3')
        help_m.triggered.connect(self.help)
        filemenu.addActions([about_m,black_m,help_m])
        filemenu.addSeparator()
        exit_m = QAction('Exit',self)
        exit_m.setShortcut('Ctrl+F4')
        exit_m.triggered.connect(quit)
        filemenu.addAction(exit_m)
        license = '''
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
        '''
        txt = QTextEdit(self)
        txt.setText(license)
        txt.setReadOnly(True)
        txt.setGeometry(30,30,750,600)
        ic = QRadioButton("I accept the license",self)
        ic.toggled.connect(self.icf)
        ic.move(400,655)
        icd = QRadioButton("No, I do not like licenses",self)
        icd.setChecked(True)
        icd.toggled.connect(self.icdf)
        icd.move(200,655)
        self.next_b = QPushButton('Next',self)
        self.next_b.clicked.connect(self.next_r)
        self.next_b.setGeometry(660,710,93,28)
        self.next_b.setEnabled(False)
        self.exit_b = QPushButton('Exit',self)
        self.exit_b.setGeometry(560,710,93,28)
        self.exit_b.clicked.connect(quit)
        self.setGeometry(500,100,800,760)
        self.show()
    def contextMenuEvent(self,event):
        menu_r = QMenu(self)
        filemenu = menu_r.addMenu('Options')
        about_m = QAction('About',self)
        about_m.setShortcut('F1')
        about_m.triggered.connect(self.about)
        black_m = QAction('Black',self)
        black_m.setShortcut('F2')
        black_m.triggered.connect(self.black)
        help_m = QAction('Help',self)
        help_m.setshortcut('F3')
        help_m.triggered.connect(self.help)
        filemenu.addActions([about_m,black_m,help_m])
        filemenu.addSeparator()
        exit_m = QAction('Exit',self)
        exit_m.setshortcut('Ctrl+F4')
        exit_m.triggered.connect(quit)
        filemenu.addAction(exit_m)
        action = menu_r.exec_(self.mapToGlobal(event.pos()))
        if action == about_m:
          self.about()
        elif action == black_m:
          self.black()
        elif action == help_m:
          self.help()
        elif action == exit_m:
          quit()
    def next_r(self):
      self.destroy()
      self.close()
      window = black_webbrowser_installing()

    def icf(self):
      self.next_b.setEnabled(True)
    def icdf(self):
      self.next_b.setEnabled(False)
    def about(self):
      global amenu
      root = Tk()
      root.title('Black-Webbrowser/About')
      root.geometry("700x600+550+130")
      root.resizable(0,0)
      txt_a = '''
Black Webbrowser is a search engine.
Property:
Search speed
System security
      '''
      photo = PhotoImage(file='./Scr/black.png')
      root.iconphoto(False,photo)
      amenu = Menu(root,tearoff=0)
      filemenu = Menu(amenu,tearoff=0)
      filemenu.add_command(label='Help',command=self.help)
      filemenu.add_separator()
      filemenu.add_command(label='Exit',command=root.destroy)
      amenu.add_cascade(label='Options',menu=filemenu)
      root.config(menu=amenu)
      label_i = Label(root,text='Black Webbrowser',foreground='black',font=("None",28))
      label_i.place(bordermode=INSIDE,x=130,y=15)
      label_t = Label(root,text=txt_a,foreground='black',font=("None",10))
      label_t.place(bordermode=INSIDE,x=175,y=65)
      b = HTMLLabel(root,html='<a href="https://black-software-com.github.io/Black-Software/" taregt="_blank"> Black </a>')
      b.place(bordermode=INSIDE,x=20,y=200)
      g = HTMLLabel(root,html='<a href="https://github.com/black-software-com" target="_blank"> Github </a>')
      g.place(bordermode=INSIDE,x=20,y=230)
      f = HTMLLabel(root,html='<a href="https://www.facebook.com/profile.php?id=100071465381949" target="_blank"> Facebook </a>')
      f.place(bordermode=INSIDE,x=20,y=260)
      i = HTMLLabel(root,html='<a href="https://instagram.com/black_software_company" target="_blank"> Instagram</a>')
      i.place(bordermode=INSIDE,x=20,y=290)
      t = HTMLLabel(root,html='<a href="https://twitter.com/blacksoftware3" target="_blank"> Twitter </a>')
      t.place(bordermode=INSIDE,x=20,y=320)
      tl = HTMLLabel(root,html='<a href="https://t.me/blacksoftware3" target="_blank"> Telegram </a>')
      tl.place(bordermode=INSIDE,x=20,y=350)
      z = HTMLLabel(root,html='<a href="https://zil.ink/blacksoftware" target="_blank"> ZLink </a>')
      z.place(bordermode=INSIDE,x=20,y=380)
      fl = Label(root,text='© Black Software')
      fl.place(bordermode=INSIDE,x=280,y=530)
      root.bind("<Button-3>",self.do_popupa)
      root.mainloop()
    def black(self):
        window_black = Tk()
        window_black.title('Black-Webbrowser/Black')
        window_black.geometry("600x500")
        try:
          frame_dev = tkinterweb.HtmlFrame(window_black)
          frame_dev.load_website('https://black-software-com.github.io/Black-Webbrowser/')
          frame_dev.pack(fill='both',expand=True)
        except (Exception,):
          print(False)
        window_black.mainloop()
    def help(self):
        window_black = Tk()
        window_black.title('Black-Webbrowser/Help')
        window_black.geometry("600x500")
        try:
          frame_dev = tkinterweb.HtmlFrame(window_black)
          frame_dev.load_website('https://black-software.ir')
          frame_dev.pack(fill='both',expand=True)
        except (Exception,):
          print(False)
        window_black.mainloop()
    def do_popup(self,event):
      try:
          wmenu.tk_popup(event.x_root,event.y_root)
      finally:
          wmenu.grab_release()
if __name__ == '__main__':
   if system() == 'Linux':
    if os.getuid() != 0:
      showerror(title='Cannot Running',message='Please, Run This Program as Root!')
      print("\nPlease, Run This Program as Root!\n")
      exit()
    else:
      print(True)
   else:
    pass
   global app
   def cls():
    if system() == 'Windows':
      command("cls")
    else:
      command("clear")
   def title():
    if system() == 'Linux':
      command("printf '\033]2;Black-Webbrowser\a'")
    else:
      command("title Black-Webbrowser")
   def title_update():
    if system() == 'Linux':
      command("printf '\033]2;Black-Webbrowser/Update\a'")
    else:
      command("title Black-Webbrowser/Update")
   def update_blackwebbrowser(): 
    title_update()
    cls()
    print(update_banner)
    if system() == 'Linux':
      getoutput("cd .. && rm -r Black-Webbrowser && git clone https://github.com/black-software-com/black-webbrowser && cd black-webbrowser && python black")
    else:
      print("Download Black-Webbrowser.zip")
      open_new_tab("https://github.com/black-software-Com/Black-Webbrowser/archive/refs/heads/master.zip")
   def setip():
    title()
    cls()
    ip = input("Enter Ip: ")
    print("\n") 
    print("Loading...\n")
    sleep(2)
    getoutput(f"netsh interface ip set address name=”Local Area Connection” static {ip} 255.255.255.0 {ip}")
    getoutput(f"netsh interface ip set address name=”Local Area Connection” source=dhcp")
    getoutput(f"netsh interface ip set dns name=”Local Area Connection” static {ip}")
    getoutput(f"netsh interface ip add dns name=”Local Area Connection” 8.8.8.8 index=2")
    getoutput(f"netsh interface ip set dnsservers name=”Local Area Connection” source=dhcp")
    print(f"\nIp Set: {Fore.GREEN}{ip}{self.end}\n")
    try1()
   def black_webbrowser_shell():
    shell_command_help = """
Black-Webbrowser Shell Command:
               
               search <Url>
               version
               help
    """
    title()
    cls()
    try:
      while True:
        inp = input("\nBlack-Webbrowser ~# ").split()
        if inp == []:
          pass
        elif inp[0] == 'version' or inp[0].lower() == 'version':
          print(version)
        elif inp[0] == 'help' or inp[0].lower() == 'help':
          print(shell_command_help)
        elif inp[0] == 'search':
          if len(inp) < 2:
            print("search <Url>")
          else:
            app = QApplication(sys.argv)
            url = inp[1]
            w = QMainWindow()
            w.setWindowTitle(f'Black-Webbrowser/{url}') 
            w.setWindowIcon(QIcon('./Scr/black.png'))
            w.setGeometry(250,100,1500,900)
            browser = QWebEngineView(w)
            browser.setUrl(QUrl(url))
            w.setCentralWidget(browser)
            w.show()
            app.exec_()
        elif inp[0] == 'black'.lower() or inp[0].lower() == 'start':
          file_chvi = open("./Core/check_vi","r").read()
          if file_chvi == 'True' or file_chvi == 'True\n':
            app = QApplication(sys.argv)            
            window = Window()
            window.vi()
            app.exec_()
          else:
            app = QApplication(sys.argv)
            window = Window()
            app.exec_()
        elif inp[0] == 'update' or inp[0].lower() == 'update':
          update_blackwebbrowser()
        elif inp[0] == 'exit' or inp[0].lower() == 'exit' or inp[0] == 'quit' or inp[0].lower() == 'quit':
          exit()
        # Add Color On Text And Input
        else:
          y = " ".join(inp)
          print(f'\n{y} Not Found!')
          pass
    except (Exception,) as err:
      print(err)
      # showerror(title='Cannot Running',message='Please, Cannot Running This Program!')
      # print(False)
   def try1():
    try_again = input("Co You Want To Try Again? [y/n] ")
    if try_again.lower() == 'y' or try_again.lower() == 'yes':
      setip()
    elif try_again.lower() == 'n' or try_again.lower() == 'no':
      ext()
    else:
      try1()
   help = """
Black-Webbrowser Arguments:
            black

            --url <URL>
            --version
            --help
            --setip
            --update

   """
   version = "Black-Webbrowser v2.0"
   try:
    try:
      if sys.argv[0] == '--url':
          app = QApplication(sys.argv)
          w = QMainWindow()
          url = sys.argv[2]
          w.setWindowTitle(f'Black-Webbrowser/{url}') 
          w.setGeometry(500,100,600,500)
          browser = QtWebEngineWidgets(w)
          browser.setUrl(QUrl(url))
          browser.setCentralWidget(browser)
          w.update_AddressBar(url)
          w.show()
          app.exec_()
      elif sys.argv[1].lower() == '--help' or sys.argv[1].lower() == 'help':
        print(help)
        exit()
      elif sys.argv[1].lower() == '--shell' or sys.argv[1].lower() == 'shell':
        black_webbrowser_shell()
      elif sys.argv[1].lower() == '--version' or sys.argv[1].lower() == 'version':
        print(version)
        exit()
      elif sys.argv[1].lower() == '--setip':
        setip()
      elif sys.argv[1].lower() == '--update' or sys.argv[1].lower() == 'update':
        update_blackwebbrowser()
      else:
         file_chi = open("./Core/file_chi","r+").read()
         if file_chi == 'False' or file_chi == 'False\n':
           if system() == 'Linux':
             getoutput("bash ./Core/install.sh")
             app = QApplication(argv)
             i = black_installing_l()
             i.show()
             app.exec_()
           else:
            app = QApplication(argv)
            i = black_installing_l()
            i.show()
            app.exec_()
         else:
                file_checkvi = open("./Core/check_vi","r+").read()
                bmess = '''
Black-Webbrowser v2.0
Property:

  Search speed
  Search graphics High quality
  System security
        '''
                if file_checkvi == 'True' or file_checkvi == 'True\n':
                  try:
                    ch = get('https://google.com')
                    if ch.status_code == 200:
                      app = QApplication(argv)
                      app.setApplicationName('Black-Webbrowser')
                      window = Window()
                      window.vi()
                      app.exec_()
                  except (Exception,ConnectionError):
                    showerror(title="Cannot Running",message='Please, Check Internet!')
                    print(False)
                else:
                  try:
                    ch = get('https://google.com')
                    if ch.status_code == 200:
                      app = QApplication(argv)
                      app.setApplicationName('Black-Webbrowser')
                      window = Window()
                      app.exec_()
                  except (Exception,ConnectionError,) as err:
                    print(err)
                    # showerror(title='Cannot Running',message='Please, Check Internet!')
    except (IndexError,):
                file_checkvi = open("./Core/check_vi","r+").read()
                bmess = '''
Black-Webbrowser v2.0
Property:

  Search speed
  Search graphics High quality
  System security
        '''
                if file_checkvi == 'True' or file_checkvi == 'True\n':
                  try:
                    ch = get('https://google.com')
                    if ch.status_code == 200:
                      app = QApplication(argv)
                      app.setApplicationName('Black-Webbrowser')
                      window = Window()
                      window.vi()
                      app.exec_()
                  except (Exception,ConnectionError):
                    showerror(title="Cannot Running",message='Please, Check Internet!')
                    print(False)
                else:
                  try:
                    ch = get('https://google.com')
                    if ch.status_code == 200:
                      app = QApplication(argv)
                      app.setApplicationName('Black-Webbrowser')
                      window = Window()
                      app.exec_()
                  except (Exception,ConnectionError,) as err:
                    print(err)
                    # showerror(title='Cannot Running',message='Please, Check Internet!')
   except (Exception,) as err:
      print(err)
      showerror(title='Cannot Running',message='Cannot Running This Program!')
      print(False)
      

# C:\ProgramData\Microsoft\Windows\Start Menu\Programs
