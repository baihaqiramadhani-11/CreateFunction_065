def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32  
    elif unit.upper() == 'F':
        return (value - 32) * 5/9  
    else:
        print("error")

suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan (C/F): ").upper()
hasil = convert_temperature(suhu, satuan)
print("Hasil konversi:", hasil)