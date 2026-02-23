import random

def main():
    print("--- Selamat Datang di Game Tebak Angka! ---")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    
    # Komputer memilih angka acak
    angka_rahasia = random.randint(1, 100)
    jumlah_tebakan = 0
    menang = False

    while not menang:
        try:
            # Meminta input dari pemain
            tebakan = int(input("\nMasukkan tebakanmu: "))
            jumlah_tebakan += 1

            if tebakan < angka_rahasia:
                print("Terlalu RENDAH! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu TINGGI! Coba lagi.")
            else:
                menang = True
                print(f"SELAMAT! Kamu berhasil menebak angka {angka_rahasia}")
                print(f"Kamu membutuhkan {jumlah_tebakan} kali percobaan.")
        
        except ValueError:
            print("Ups! Tolong masukkan angka yang valid.")

if __name__ == "__main__":
    main()
