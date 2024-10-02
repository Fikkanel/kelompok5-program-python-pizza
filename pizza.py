PizzaSize = ""
PizzaTopping = ""
PizzaCrust = ""
PizzaVarian = ""
HargaTotal = 0

print("---------------Selamat Datang di Python Pizza----------------------")

# Pilih Varian Pizza
print("Pilih varian pizza:\n"
      "1. Chicken Lovers          Rp 50.000\n"
      "2. American Frankie Sausage  Rp 55.000\n"
      "3. Extravaganza             Rp 60.000\n"
      "4. Grilled Beef Supreme     Rp 65.000\n"
      "5. Supreme Cheese           Rp 70.000\n"
      "6. Meat & Meat              Rp 75.000")

PizzaVarianInput = input("Silahkan pilih: ")

if PizzaVarianInput == '1':
    PizzaVarian = "Chicken Lovers"
    HargaTotal += 50000
elif PizzaVarianInput == '2':
    PizzaVarian = "American Frankie Sausage"
    HargaTotal += 55000
elif PizzaVarianInput == '3':
    PizzaVarian = "Extravaganza"
    HargaTotal += 60000
elif PizzaVarianInput == '4':
    PizzaVarian ="Grilled Beef Supreme"
    HargaTotal += 65000
elif PizzaVarianInput == '5':
    PizzaVarian = "Supreme Cheese"
    HargaTotal += 70000
elif PizzaVarianInput == '6':
    PizzaVarian = "Meat & Meat"
    HargaTotal += 75000
else:
    print("Varian yang dipilih tidak tersedia, silahkan ulangi pesanan anda")
    exit()

# Pilihan topping
print("Pilih Topping:\n"
      "1. Beef       Rp 10.000\n"
      "2. Pepperoni  Rp 12.000\n"
      "3. Mushroom   Rp 8.000\n"
      "4. Sausage    Rp 15.000")

PizzaToppingInput = input("Silahkan Pilih (1/2/3/4): ")

if PizzaToppingInput == '1':
    PizzaTopping = "Beef"
    HargaTotal += 10000
elif PizzaToppingInput == '2':
    PizzaTopping = "Pepperoni"
    HargaTotal += 12000
elif PizzaToppingInput == '3':
    PizzaTopping = "Mushroom"
    HargaTotal += 8000
elif PizzaToppingInput == '4':
    PizzaTopping = "Sausage"
    HargaTotal += 15000
else:
    print("Toping yang dipilih tidak tersedia, silahkan ulangi pesanan anda.")
    exit()

# Pilihan crust
print("Pilih jenis crust:\n"
      "1. Thin crust      Rp 5.000\n"
      "2. Pan crust       Rp 7.000\n"
      "3. Stuffed crust   Rp 10.000\n"
      "4. Sausage crust   Rp 12.000")

PizzaCrustInput = input("Pilih crust yang diinginkan (1/2/3/4): ")

if PizzaCrustInput == '1':
    PizzaCrust = "Thin crust"
    HargaTotal += 5000
elif PizzaCrustInput == '2':
    PizzaCrust = "Pan crust"
    HargaTotal += 7000
elif PizzaCrustInput == '3':
    PizzaCrust = "Stuffed crust"
    HargaTotal += 10000
elif PizzaCrustInput == '4':
    PizzaCrust = "Sausage crust"
    HargaTotal += 12000
else:
    print("Crust yang dipilih tidak tersedia, silahkan ulangi pesanan anda")
    exit()

# Pilihan ukuran pizza
print("Pilih ukuran pizza:\n"
      "1. Pizza Kecil    Rp 50.000\n"
      "2. Pizza Sedang   Rp 75.000\n"
      "3. Pizza Besar    Rp 100.000")

PizzaSizeInput = input("Pilih ukuran yang diinginkan (1/2/3): ")

if PizzaSizeInput == '1':
    PizzaSize = "Pizza Kecil"
    HargaTotal += 50000
elif PizzaSizeInput == '2':
    PizzaSize = "Pizza Sedang"
    HargaTotal += 75000
elif PizzaSizeInput == '3':
    PizzaSize = "Pizza Besar"
    HargaTotal += 100000
else:
    print("Ukuran yang dipilih tidak tersedia, silahkan ulangi pesanan anda")
    exit()

# Pilihan extra cheese
print("Apakah Anda ingin menambahkan extra cheese seharga Rp 13.000?\n""1. Iya\n""2. Tidak")

ExtraCheeseInput = input("Silahkan Pilih(1/2): ")

if ExtraCheeseInput.lower() == '1':
    print("Menambahkan extra cheese")
    HargaTotal += 13000
elif ExtraCheeseInput.lower() == '2':
    print("Tidak menambahkan extra cheese")
else:
    print("Pilihan tidak valid. Pilih antara iya atau tidak.")

# Tampilkan ringkasan pesanan
print(f"\n--------------- Ringkasan Pesanan Anda ---------------\n"
      f"Varian Pizza  : {PizzaVarian}\n"
      f"Topping       : {PizzaTopping}\n"
      f"Crust         : {PizzaCrust}\n"
      f"Ukuran        : {PizzaSize}\n"
      f"Extra Cheese  : {'Iya' if ExtraCheeseInput.lower() == 'iya' else 'Tidak'}\n"
      f"Total Harga   : Rp {HargaTotal:,.0f}\n"
      "------------------------------------------------------")

print("\nPILIH METODE PEMBAYARAN\n"
      "1. Cash\n""2. Qris")

MetodePembayaran = input("Silahkan Pilih Metode Pembayaran: ")

# Simulasi pembayaran
if MetodePembayaran == '1':
    print("Metode pembayaran: Cash")
    Bayar = int(input("Masukkan jumlah uang tunai yang dibayarkan: "))
    
    if Bayar >= HargaTotal:
        Kembalian = Bayar - HargaTotal
        print(f"Pembayaran berhasil. Kembalian Anda: Rp {Kembalian:,.0f}")
    else:
        print("Uang yang Anda berikan kurang. Silahkan coba lagi.")
elif MetodePembayaran == '2':
    print("Metode pembayaran: QRIS")
    # Simulasi kode QR
    KodeQR = "PYTHON_PIZZA_001"
    print(f"\nScan kode QR berikut untuk pembayaran: {KodeQR}\n"
            "Pembayaran berhasil. Terima kasih telah memesan di Python Pizza!")
else:
    print("Pilihan tidak valid. Pilih antara 1 (Cash) atau 2 (QRIS).")
