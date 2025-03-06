class Televisi:
    def __init__(self, ukuran_layar, warna_layar):
        self.ukuran_layar = ukuran_layar
        self.warna_layar = warna_layar
        self.status = "mati"
    
    def dihidupkan(self):
        if self.status == "mati":
            self.status = "hidup"
            return f"Televisi {self.warna_layar} berukuran {self.ukuran_layar} inch telah dihidupkan"
        else:
            return f"Televisi {self.warna_layar} sudah dalam keadaan hidup"
    
    def dimatikan(self):
        if self.status == "hidup":
            self.status = "mati"
            return f"Televisi {self.warna_layar} berukuran {self.ukuran_layar} inch telah dimatikan"
        else:
            return f"Televisi {self.warna_layar} sudah dalam keadaan mati"

# Membuat 2 objek dari class Televisi
tv1 = Televisi(32, "Hitam")
tv2 = Televisi(55, "Silver")

# Memanggil method dan mengakses atribut dari objek tv1
print("Objek tv1:")
print(f"Ukuran layar: {tv1.ukuran_layar} inch")
print(f"Warna layar: {tv1.warna_layar}")
print(tv1.dihidupkan())
print(tv1.dimatikan())

# Memanggil method dan mengakses atribut dari objek tv2
print("\nObjek tv2:")
print(f"Ukuran layar: {tv2.ukuran_layar} inch")
print(f"Warna layar: {tv2.warna_layar}")
print(tv2.dihidupkan())
print(tv2.dihidupkan())  # Mencoba menghidupkan TV yang sudah hidup
print(tv2.dimatikan())