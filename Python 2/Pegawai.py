import tkinter as tk
from tkinter import ttk

# Class Induk: Pegawai
class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

# Class Anak: Pegawai Tetap
class PegawaiTetap(Pegawai):
    def __init__(self, nama, gaji, bonus):
        super().__init__(nama, gaji)
        self.bonus = bonus

# Class Anak: Pegawai Harian
class PegawaiHarian(Pegawai):
    def __init__(self, nama, gaji, jam_kerja):
        super().__init__(nama, gaji)
        self.jam_kerja = jam_kerja

# Class Anak: Pegawai Kontrak
class PegawaiKontrak(Pegawai):
    def __init__(self, nama, gaji, durasi_kontrak):
        super().__init__(nama, gaji)
        self.durasi_kontrak = durasi_kontrak

def tambah_pegawai():
    nama = entry_nama.get()
    gaji = float(entry_gaji.get())
    jenis_pegawai = var_jenis.get()

    if jenis_pegawai == "Pegawai Tetap":
        bonus = float(entry_bonus.get())
        pegawai = PegawaiTetap(nama, gaji, bonus)
        output_text = f"Nama: {pegawai.nama}, Gaji: {pegawai.gaji}, Bonus: {pegawai.bonus}"
    elif jenis_pegawai == "Pegawai Harian":
        jam_kerja = float(entry_jam_kerja.get())
        pegawai = PegawaiHarian(nama, gaji, jam_kerja)
        output_text = f"Nama: {pegawai.nama}, Gaji: {pegawai.gaji}, Jam Kerja: {pegawai.jam_kerja}"
    else:
        durasi_kontrak = int(entry_durasi_kontrak.get())
        pegawai = PegawaiKontrak(nama, gaji, durasi_kontrak)
        output_text = f"Nama: {pegawai.nama}, Gaji: {pegawai.gaji}, Durasi Kontrak: {pegawai.durasi_kontrak}"

    output_label.config(text=output_text)

app = tk.Tk()
app.title("Implementasi Inheritance Python")

frame_input = ttk.LabelFrame(app, text="Input Data Pegawai")
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_nama = ttk.Label(frame_input, text="Nama Pegawai:")
label_nama.grid(row=0, column=0, sticky="w")
entry_nama = ttk.Entry(frame_input)
entry_nama.grid(row=0, column=1)

label_gaji = ttk.Label(frame_input, text="Gaji:")
label_gaji.grid(row=1, column=0, sticky="w")
entry_gaji = ttk.Entry(frame_input)
entry_gaji.grid(row=1, column=1)

var_jenis = tk.StringVar()
label_jenis = ttk.Label(frame_input, text="Jenis Pegawai:")
label_jenis.grid(row=2, column=0, sticky="w")
combobox_jenis = ttk.Combobox(frame_input, textvariable=var_jenis, values=["Pegawai Tetap", "Pegawai Harian", "Pegawai Kontrak"])
combobox_jenis.grid(row=2, column=1)

label_bonus = ttk.Label(frame_input, text="Bonus:")
label_bonus.grid(row=3, column=0, sticky="w")
entry_bonus = ttk.Entry(frame_input)
entry_bonus.grid(row=3, column=1)

label_jam_kerja = ttk.Label(frame_input, text="Jam Kerja (jam):")
label_jam_kerja.grid(row=4, column=0, sticky="w")
entry_jam_kerja = ttk.Entry(frame_input)
entry_jam_kerja.grid(row=4, column=1)

label_durasi_kontrak = ttk.Label(frame_input, text="Durasi Kontrak (bulan):")
label_durasi_kontrak.grid(row=5, column=0, sticky="w")
entry_durasi_kontrak = ttk.Entry(frame_input)
entry_durasi_kontrak.grid(row=5, column=1)

tombol_tambah = ttk.Button(app, text="Tambah Data Pegawai", command=tambah_pegawai)
tombol_tambah.grid(row=1, column=0, padx=10, pady=10, sticky="w")

output_label = tk.Label(app, text="", wraplength=400, justify="left")
output_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

app.mainloop()
