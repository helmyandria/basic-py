import random
import main

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa]* 4 # INI TETAP HARUS KOSONG

        cuypy_position = random.randint(1,4)

        goa = goa_kosong.copy() # INI ADALAH TEMPAT BARU UNTUK SI CUYPY
        goa[cuypy_position-1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)
        
        print(f'Coba perhatikan goa dibawah ini\n\n{goa_kosong}\n')

        pilihan_user = int(input("Menurut kamu di goa nomor berada CUYPYY berada? [1 / 2 / 3 / 4]: "))

        if pilihan_user == cuypy_position:
            print(f"{goa} \nSelamat KAMU MENANG! 🏆")
        else:
            print(f"{goa} \nUppss.. KAMU KALAH! 😵")
                
        play_again = input("\nApakah ingin melanjutkan gamenya lagi? [y/n]: ")
        if play_again == "n":
            main.menu()

    print("program selesai!")
    
if __name__ == '__main__':
    start()