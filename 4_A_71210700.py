#Catatan pemesanan dan penghitung pengeluaran pelanggan

#defenisi data test case 1 dan 2
Ikanbakar = 25000
Esdoger = 6000
Rujakcingur = 8000

#Penyelesaian
print("====MASUKAN JUMLAH MAKANAN YANG DIPESAN====")
menu1 = int(input("IKAN BAKAR     Rp 25.000,00  : "))
menu2 = int(input("ES DOGER       Rp 6.000,00   : "))
menu3 = int(input("RUJAK CINGUR   Rp 8.000,00   : "))

#Total harga menu
x = Ikanbakar*menu1
y = Esdoger*menu2
z = Rujakcingur*menu3

print("====TOTAL====")
print("TOTAL IKAN BAKAR     : Rp ",x)
print("TOTAL ES DOGER       : Rp ",y)
print("TOTAL RUJAK CINGUR   : Rp ",z)

#Total semua menu

total = x+y+z
print("Jumlah total biaya yang harus dibayar adalah Rp",total)


