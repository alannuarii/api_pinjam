from db import connection
from flask import request


class Input:
    def upload_data(self):
        status = request.form['status']
        tanggal = request.form['tanggal']
        nama = request.form['nama']
        nilai = request.form['nilai']
        if status == 'pinjam':
            pinjam = nilai
            bayar = 0
        else:
            pinjam = 0
            bayar = nilai

        self.insert_data(tanggal, nama, pinjam, bayar)

    def insert_data(self, tanggal, nama, pinjam, bayar):
        query = f"INSERT INTO data (tanggal, nama, pinjam, bayar) VALUES (%s, %s, %s, %s)"
        value = [tanggal, nama, pinjam, bayar]
        connection(query, 'insert', value)