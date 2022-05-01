Because I'm lazy and I dont want to get up and open my rack every time I need to boot up my Proxmox/XCP-ng server, I made this.

<p align="center"><img src="img1.png"></p>

It's basically just [this script](http://wiki.bashlinux.com/index.php/Wake-on-LAN) but with a GUI (made with [tkinter](https://docs.python.org/fr/3/library/tkinter.html)) on top of it.

---

**Usage** :  
Simply enter a MAC address and press wake up
<p align="center"><img src="img2.png"></p> 

**TO DO**:
- Make the `saved MAC Addresses` box working, for now it's just a simple (useless) text box.
- Redirect the output of the `arp -a` button in the text box instead of the terminal 
