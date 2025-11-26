import Bangun_ruang as br
import Bangun_datar as bd

print("--- BANGUN RUANG ---")
print(f"Volume kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volume balok adalah {br.balok(4, 5, 2)}")
print(f"Volume prisma segitiga adalah {br.prisma(5, 4, 5)}")
print(f"Volume tabung adalah {br.tabung(7, 10):.2f}")
print(f"Volume kerucut adalah {br.krucut(7, 10):.2f}")

print("--- BANGUN DATAR ---")
print(f"Luas Persegi adalah {bd.persegi(5)}")
print(f"Luas Persegi Panjang adalah {bd.persegi_panjang(6, 4)}")
print(f"Luas Segitiga adalah {bd.segitiga(8, 6)}")
print(f"Luas Lingkaran adalah {bd.lingkaran(7):.2f}")
print(f"Luas Jajar Genjang adalah {bd.jajar_genjang(10, 5)}")