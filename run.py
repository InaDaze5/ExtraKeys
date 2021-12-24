import os,sys,time
from time import sleep

os.system('clear')
print('\t\033[90m\====================/\n            \033[32;1m| TERMUX TOD | \n\t\033[90m/====================\ \033[00m\n \033[32;1m(\033[37;1m●\033[32;1m) \033[34;1mTOOLS PEMASANG TOMBOL TAMBAHAN TERMUX\n \033[32;1m(\033[37;1m●\033[32;1m) By     : RAMADHANI\n \033[32;1m(\033[37;1m●\033[32;1m) Github : RAMA-XD\n \033[32;1m(\033[37;1m●\033[32;1m)\033[31;1m Note   : UDAH ENAK TINGGAL MAKE JAN DI RECODE')
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
ainx = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
ainx.write(key)
ainx.close()
sleep (2)
os.system('termux-reload-settings')
print ("\033[32;1m (\033[33;1m●\033[32;1m)\033[36;1m Pemasagan Sukses.....")
sleep (1)
os.system ("xdg-open https://youtube.com/channel/UC_TtsAzujNHgM2TZzCMopkQ")
sys.exit()
