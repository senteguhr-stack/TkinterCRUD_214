import tkinter as tk
from tkinter import messagebox
import sqlite3

import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


create_db()

import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def hasil_prediksi():
    nama = entry_nama.get().strip()
    nilai_biologi = entry_biologi.get().strip()
    nilai_fisika = entry_fisika.get().strip()
    nilai_inggris = entry_inggris.get().strip()

    if not nama:
        messagebox.showerror("Error", "Nama siswa harus diisi!")
        return

    if not nilai_biologi:
        messagebox.showerror("Error", "Kolom Biologi harus diisi!")
        return

    if not nilai_fisika:
        messagebox.showerror("Error", "Kolom Fisika harus diisi!")
        return

    if not nilai_inggris:
        messagebox.showerror("Error", "Kolom Inggris harus diisi!")
        return

    try:
        biologi = int(nilai_biologi)
        fisika = int(nilai_fisika)
        inggris = int(nilai_inggris)

        if any(n < 0 or n > 100 for n in [biologi, fisika, inggris]):
            messagebox.showerror(
                "Error", "Nilai harus antara 0 sampai 100!"
            )
            return

import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def hasil_prediksi():
    nama = entry_nama.get().strip()
    nilai_biologi = entry_biologi.get().strip()
    nilai_fisika = entry_fisika.get().strip()
    nilai_inggris = entry_inggris.get().strip()

    if not nama:
        messagebox.showerror("Error", "Nama siswa harus diisi!")
        return

    if not nilai_biologi or not nilai_fisika or not nilai_inggris:
        messagebox.showerror(
            "Error", "Semua nilai mata pelajaran harus diisi!"
        )
        return

    try:
        biologi = int(nilai_biologi)
        fisika = int(nilai_fisika)
        inggris = int(nilai_inggris)

        if any(n < 0 or n > 100 for n in [biologi, fisika, inggris]):
            messagebox.showerror(
                "Error", "Nilai harus antara 0 sampai 100!"
            )
            return

        if biologi > fisika and biologi > inggris:
            prediksi = "Kedokteran"
        elif fisika > biologi and fisika > inggris:
            prediksi = "Teknik"
        elif inggris > biologi and inggris > fisika:
            prediksi = "Bahasa"
        else:
            messagebox.showwarning(
                "Peringatan",
                "Terdapat nilai tertinggi yang sama. "
                "Silakan masukkan nilai yang berbeda."
            )
            return

import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_db():
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def hasil_prediksi():
    nama = entry_nama.get().strip()
    nilai_biologi = entry_biologi.get().strip()
    nilai_fisika = entry_fisika.get().strip()
    nilai_inggris = entry_inggris.get().strip()

    if not nama:
        messagebox.showerror("Error", "Nama siswa harus diisi!")
        return

    if not nilai_biologi or not nilai_fisika or not nilai_inggris:
        messagebox.showerror(
            "Error", "Semua nilai mata pelajaran harus diisi!"
        )
        return

    try:
        biologi = int(nilai_biologi)
        fisika = int(nilai_fisika)
        inggris = int(nilai_inggris)

        if any(n < 0 or n > 100 for n in [biologi, fisika, inggris]):
            messagebox.showerror(
                "Error", "Nilai harus antara 0 sampai 100!"
            )
            return

        if biologi > fisika and biologi > inggris:
            prediksi = "Kedokteran"
        elif fisika > biologi and fisika > inggris:
            prediksi = "Teknik"
        elif inggris > biologi and inggris > fisika:
            prediksi = "Bahasa"
        else:
            messagebox.showwarning(
                "Peringatan",
                "Terdapat nilai tertinggi yang sama. "
                "Silakan masukkan nilai yang berbeda."
            )
            return

        conn = sqlite3.connect("nilai_siswa.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO nilai_siswa
            (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """, (nama, biologi, fisika, inggris, prediksi))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Berhasil",
            "Data siswa berhasil disimpan ke database!"
        )

    except ValueError:
        messagebox.showerror(
            "Error", "Masukkan nilai berupa angka!"
        )

    except sqlite3.Error as e:
        messagebox.showerror(
            "Database Error", f"Gagal menyimpan data: {e}"
        )