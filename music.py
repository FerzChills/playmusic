#SCRIPT PYTHON PLAY MUSIK SEDERHANA JIKA MUSIK TIDAK MUNCUL DI APLIKASI MUSIC
#AH AH AH AKU CINTA DENIS
#AUTHOR FERZCHILLS
#RECODE BOLEH JAN HAPUS AUTHOR

import pygame
import datetime
import time
import os
import random
from colorama import init, Fore, Back, Style

# List warna yang tersedia
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Inisialisasi colorama
init()

# Inisialisasi Pygame
pygame.mixer.init()

#variable Waktu
waktu = datetime.datetime.now()

# Pilih warna acak dari list
selected_color = random.choice(colors)

#Variable Menjelaskan
def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

# Meminta input path dari pengguna
os.system("clear")
type_text(selected_color + "Ini Adalah Script Memutar Lagu Yang Saya Buat Karna Saya Sering Terkena Bug Saat Memutar Music" + Style.RESET_ALL)
os.system("sleep 5")
os.system("clear")
print(selected_color + "AUTHOR: FERZCHILLS" + Style.RESET_ALL)
print(selected_color + "AGE   : 14" + Style.RESET_ALL)
print(selected_color + "TIME  :" + Style.RESET_ALL, waktu)
music_path = input(selected_color + "Masukan Lokasi Path Musik Yang Ingin Di Putar: " + Style.RESET_ALL)

# Load file musik
pygame.mixer.music.load(music_path)

# Memutar musik
pygame.mixer.music.play()

# Menunggu sampai musik selesai dimainkan
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    