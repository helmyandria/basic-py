import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1,4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("Masukkan nama kamu : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa]* 4 # INI TETAP HARUS KOSONG
goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY

goa[cuypy_position-1] = "|0_0|"

print(f'''
Halo, {nama_user} ! Coba perhatikan goa dibawah ini
{"".join(goa_kosong)}
''')

pilihan_user = int(input("Menurut kamu di goa nomor berada CUYPYY berada? [1 / 2 / 3 / 4]: "))

confirm_answer = input(f"Apakah kamu yakin dengan jawaban {pilihan_user} ? [y/n]: ")

if confirm_answer == "n":
    print("program dihentikan!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print(f"{"".join(goa)} \nSelamat {nama_user} KAMU MENANG! posisi CUYPY ada di {cuypy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
    else:
        print(f"{"".join(goa)} \nKAMU KALAH! CUYPY bukan berada disitu, tapi ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}.")
else:
    print("Silahkan ulangi programnya")
    exit()