import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1,4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("Masukkan nama kamu : ")

print(f'''
Halo, {nama_user} ! Coba perhatikan goa dibawah ini
|_| |_| |_| |_|
''')

pilihan_user = int(input("Menurut kamu di goa nomor berada CUYPYY berada? [1 / 2 / 3 / 4]: "))

if pilihan_user > 4 or pilihan_user < 1:
    print(f'''Pilihan {nama_user} di luar batas pilihan goa yang tersedia! [1 / 2 / 3 / 4]
********* GAME END **********
''')
else:
    konfirmasi_jawaban = input(f"Apakah kamu yakin dengan jawaban {pilihan_user} ? [y/n]: ")

    if konfirmasi_jawaban == "y":
        if pilihan_user == cuypy_position:
            print(f"Selamat {nama_user} KAMU MENANG! posisi CUYPY ada di {cuypy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
        else:
            print(f"KAMU KALAH! CUYPY bukan berada disitu, tapi ada di goa nomor {cuypy_position}. Sedangkan kamu memilih goa nomor {pilihan_user}.")
    else:
        print("********* GAME END **********")