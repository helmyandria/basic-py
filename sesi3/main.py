import random
from libs import welcome_message

cuypy_position = random.randint(1,4)

welcome_message("WELCOME TO CUYPY GAMES!")

nama_user = input("Masukkan nama kamu : ")

while nama_user == "":
    nama_user = input("Mohon isi nama kamu : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa]* 4 # INI TETAP HARUS KOSONG

goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
goa[cuypy_position-1] = "|0_0|"

goa_kosong = ' '.join(goa_kosong)
goa = ' '.join(goa)

while True:
    print(f'''
    Halo, {nama_user} ! Coba perhatikan goa dibawah ini
    {"".join(goa_kosong)}
    ''')

    pilihan_user = int(input("Menurut kamu di goa nomor berada CUYPYY berada? [1 / 2 / 3 / 4]: "))

    while pilihan_user < 1 or pilihan_user > 4:
        pilihan_user = int(input("Input kamu tidak berada dalam pilihan, pilih goa nomor berada CUYPYY berada? [1 / 2 / 3 / 4]: "))

    confirm_answer = input(f"Apakah kamu yakin denglulan jawaban {pilihan_user} ? [y/n]: ")

    if confirm_answer == "n":
        print("program dihentikan!")
        exit()
    elif confirm_answer == "y":
        if pilihan_user == cuypy_position:
            print(f"{goa} \nSelamat {nama_user} KAMU MENANG! 🏆")
        else:
            print(f"{goa} \nUppss.. KAMU KALAH! 😵")
    else:
        print("Silahkan ulangi programnya")
        exit()
        
    play_again = input("\nApakah ingin melanjutkan gamenya lagi? [y/n]: ")
    if play_again == "n":
        break
    elif play_again == "y":
        # position new cuypy
        goa = goa.split()
        goa[cuypy_position-1] = "|_|"
        cuypy_position = random.randint(1,4)
        goa[cuypy_position-1] = "|0_0|"
        goa = ' '.join(goa)

print("program selesai!")