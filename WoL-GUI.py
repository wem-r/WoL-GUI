from distutils import cmd
import sys
from tkinter import *
import struct, socket
import os
#import subprocess
#from subprocess import Popen, PIPE
from sqlalchemy import true

class sim(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        myfont = family = ("Century Gothic", 8)
        Green = "#00FF80"
        Red = '#F44336'
        Yellow = '#FF9800'
        # White Square Block
        canvas = Canvas(self, bg="#222529")
        #canvas.create_rectangle(10, 20, 630, 200, width=1, outline="white", fill='#222529')
        canvas.pack(fill=BOTH, expand=1)
        # Text Label
        self.label = Label(master, font=("Century Gothic", 9), text="MAC Address or IP", bg='#222529', fg='white')
        self.label.place(x=35, y=10)

        # Wake-On-LAN
        #
        # Copyright (C) 2002 by Micro Systems Marc Balmer
        # Written by Marc Balmer, marc@msys.ch, http://www.msys.ch/
        # This code is free software under the GPL
        #
        # Source : http://wiki.bashlinux.com/index.php/Wake-on-LAN
        macaddr= 'd0:50:99:76:34:00'
        def WakeOnLan(ethernet_address):
            # Construct a six-byte hardware address
            addr_byte = ethernet_address.split(':')
            hw_addr = struct.pack('BBBBBB', int(addr_byte[0], 16),
                int(addr_byte[1], 16),
                int(addr_byte[2], 16),
                int(addr_byte[3], 16),
                int(addr_byte[4], 16),
                int(addr_byte[5], 16))
            # Build the Wake-On-LAN "Magic Packet"...
            msg = b'\xff' * 6 + hw_addr * 16
            # ...and send it to the broadcast address using UDP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(msg, ('<broadcast>', 9))
            s.close()

        def arp_req():
            arpp = os.system("arp -a")
            cmdbox.insert('end', arpp,'\n')

        def GetMacInput():
            mac_inp = macbox.get(1.0, "end-1c")
            if mac_inp:
                WakeOnLan(mac_inp)
                cmdbox.insert('end', "Waking up "+mac_inp+'\n')
            else:
                cmdbox.insert('end', f"You need to enter a MAC Address first\nseparated by ':' not '-'\n")
            #WakeOnLan(macaddr)

        def GetIPInput():
            ip_inp = macbox.get(1.0, "end-1c")
            if ip_inp:
                arp_n = os.system("arp -i eth0 "+ ip_inp)
                cmdbox.insert('end', arp_n)
            else:
                cmdbox.insert('end', f"You need to enter an IP Address first\n")
            #WakeOnLan(macaddr)

        def ClearCmdbox():
            cmdbox.delete(1.0, 'end')

        # Button
        self.button1 = Button(root, font=myfont, bg='#dbdbdb', text="Wake Up", command=GetMacInput, height=1, width=19, borderwidth=0, relief=SOLID)
        self.button1.place(x=10, y=65)
        self.button2 = Button(root, font=myfont, bg='#dbdbdb', text="arp -a", command=arp_req, height=1, width=7, borderwidth=0, relief=SOLID)
        self.button2.place(x=10, y=100)
        self.button2 = Button(root, font=myfont, bg='#dbdbdb', text="arp -s <IP>", command=GetIPInput, height=1, width=7, borderwidth=0, relief=SOLID)
        self.button2.place(x=92, y=100)
        self.button3 = Button(root, font=myfont, bg='#dbdbdb', text="Clear Output", command=ClearCmdbox, height=1, width=19, borderwidth=0, relief=SOLID)
        self.button3.place(x=10, y=185)

        macbox = Text(root, height=1, width=19, relief="sunken")
        macbox.place(x=10, y=30)
        
        #output = "Waking up "
        cmdbox = Text(root, height=13, width=63, relief="sunken", wrap='char', font=('Consolas', 9), bg='#000000', fg=Green)
        cmdbox.place(x=180, y=10)
        #cmdbox.config(state='disabled')

        #sb = Scrollbar(root)
        #sb.pack(side=RIGHT, fill=BOTH)
        #cmdbox.config(yscrollcommand=sb.set)
        #sb.config(command=cmdbox.yview)
        

root = Tk()
mygui = sim(root).configure(bg='#222529')
root.wm_title("Wake on LAN GUI - Wemy")
#root.configure(bg='#222529')
root.geometry("640x220")
root.resizable(width=False, height=False)
root.eval('tk::PlaceWindow . center')
root.mainloop()

