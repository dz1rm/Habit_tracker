
from datetime import date

# Data kebiasaan awal
habits = {
    "Membaca": {},
    "Olahraga": {},
    "Belajar": {}
}

# Menampilkan judul
def garis():
    print("︵‿୨♡୧‿︵" * 2)

def tampilkan_judul():
    garis()
    print("HABIT TRACKER HARIAN")
    garis()


# 1. Ringkasan Hari Ini
def ringkasan():
    hari_ini = str(date.today())

    total = len(habits)
    selesai = 0

    for nama in habits:
        if habits[nama].get(hari_ini, False):
            selesai += 1

    print("\n✦ Ringkasan Hari Ini")
    print(f"Kebiasaan selesai: {selesai} / {total}")


# 2. Progress Mingguan
def progress_mingguan():
    print("\n✦ Progress Mingguan")

    for nama in habits:
        progress = []

        for i in range(7):
            tanggal = str(date.fromordinal(
                date.today().toordinal() - 6 + i
            ))

            if habits[nama].get(tanggal, False):
                progress.append("☑")
            else:
                progress.append("☐")

        print(f"{nama:<12} {' '.join(progress)}")


# 3. Catat Kebiasaan Hari Ini
def catat_kebiasaan():
    hari_ini = str(date.today())

    print("\n✦ Catat Kebiasaan Hari Ini")

    if not habits:
        print("Belum ada kebiasaan.")
        return

    daftar = list(habits.keys())

    for i, nama in enumerate(daftar, 1):
        status = habits[nama].get(hari_ini, False)

        tanda = "☑" if status else "☐"

        print(f"{i}. {nama} [{tanda}]")

    pilihan = input("\nPilih nomor kebiasaan: ")

    if pilihan.isdigit():
        nomor = int(pilihan)

        if 1 <= nomor <= len(daftar):
            nama = daftar[nomor - 1]
            habits[nama][hari_ini] = True

            print(f"\n{nama} berhasil diselesaikan!")

        else:
            print("Nomor tidak tersedia.")

    else:
        print("Masukkan angka yang benar.")


# 4. Lihat Semua Kebiasaan
def lihat_kebiasaan():
    print("\n✦ Daftar Semua Kebiasaan")

    if not habits:
        print("Belum ada kebiasaan.")
        return

    for i, nama in enumerate(habits, 1):
        print(f"{i}. {nama}")


# 5. Tambah Kebiasaan
def tambah_kebiasaan():
    print("\n✦ Tambah Kebiasaan")

    nama = input("Masukkan nama kebiasaan: ").strip()

    if not nama:
        print("Nama kebiasaan tidak boleh kosong.")

    elif nama in habits:
        print("Kebiasaan sudah tersedia.")

    else:
        habits[nama] = {}
        print(f"Kebiasaan '{nama}' berhasil ditambahkan!")


# 6. Hapus Kebiasaan
def hapus_kebiasaan():
    lihat_kebiasaan()

    if not habits:
        return

    nama = input("\nMasukkan nama kebiasaan yang ingin dihapus: ")

    if nama in habits:
        del habits[nama]
        print(f"Kebiasaan '{nama}' berhasil dihapus.")

    else:
        print("Kebiasaan tidak ditemukan.")

def lihat_riwayat():
    print("\n✦ Riwayat Kebiasaan")

    ada_riwayat = False

    for nama, riwayat in habits.items():
        for tanggal, status in riwayat.items():

            if status:
                print(f"{tanggal} - {nama} ☑")
                ada_riwayat = True

    if not ada_riwayat:
        print("Belum ada riwayat aktivitas.")


while True:

    tampilkan_judul()

    ringkasan()
    progress_mingguan()

    print("\n✦ MENU")
    print("1. Catat Kebiasaan Hari Ini")
    print("2. Lihat Semua Kebiasaan")
    print("3. Tambah Kebiasaan")
    print("4. Hapus Kebiasaan")
    print("5. Lihat Riwayat")
    print("6. Keluar")

    pilihan = input("\nPilih Menu: ")

    if pilihan == "1":
        catat_kebiasaan()

    elif pilihan == "2":
        lihat_kebiasaan()

    elif pilihan == "3":
        tambah_kebiasaan()

    elif pilihan == "4":
        hapus_kebiasaan()

    elif pilihan == "5":
        lihat_riwayat()

    elif pilihan == "6":
        print("\nTerima kasih telah menggunakan Habit Tracker!")
        print("Tetap konsisten dan semangat! ♡")
        break

    else:
        print("\nPilihan tidak valid!")

    input("\nTekan ENTER untuk kembali ke menu...")
