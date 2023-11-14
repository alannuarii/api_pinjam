from db import connection


class Select:
    def get_pinjaman(self):
        query = f"SELECT nama, pinjaman FROM awal"
        value = []
        result = connection(query, 'select', value)
        return result

    def get_data(self):
        query = f"SELECT nama, SUM(pinjam) AS pinjam, SUM(bayar) AS bayar FROM data GROUP BY nama"
        value = []
        result = connection(query, 'select', value)
        return result