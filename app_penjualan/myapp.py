#import library third party
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app_penjualan'

mysql = MySQL(app)

@app.route('/')

def read():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb_produk")
    data = cur.fetchall()
    cur.close()
    return render_template('read.html', tb_produk=data)

@app.route('/menambah', methods=['POST'])
def menambah():
    if request.method == 'POST' and 'nama_barang' in request.form and 'harga' in request.form and 'stok' in request.form and 'kd_supplier' in request.form:
        nama_barang = request.form['nama_barang']
        harga = request.form['harga']
        stok = request.form['stok']
        kd_supplier = request.form['kd_supplier']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_produk (nama_barang, harga, stok, kd_supplier) VALUES ( %s, %s, %s, %s)", (nama_barang, harga, stok, kd_supplier))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('read'))
    return render_template('read.html')

@app.route('/update/<kode_barang>', methods=['POST'])
def update(kode_barang):
    if request.method == 'POST':
        nama_barang = request.form['nama_barang']
        harga = request.form['harga']
        stok = request.form['stok']
        kd_supplier = request.form['kd_supplier']
        
        cursor = mysql.connection.cursor()
        sql = """
        UPDATE tb_produk 
        SET nama_barang = %s, harga = %s, stok = %s, kd_supplier = %s 
        WHERE kode_barang = %s
        """
        values = (nama_barang, harga, stok, kd_supplier, kode_barang)
        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('read'))

@app.route('/delete/<kode_barang>', methods=['POST'])
def delete(kode_barang):
    cursor = mysql.connection.cursor()
    sql = "DELETE FROM tb_produk WHERE kode_barang = %s"
    cursor.execute(sql, (kode_barang,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('read'))

if __name__ == '__main__':
    app.run(debug=True)