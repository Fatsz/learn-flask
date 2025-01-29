#import library third party
from flask import Flask, render_template, session, request, redirect, url_for
from flask_mysqldb import MySQL
#init main app
app = Flask(__name__)
# kunci rahasia agar session bisa berjalan
app.secret_key = '!@#$%'

#database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'
#init mysql
mysql = MySQL(app)
# set route default dan http method yang diizinkan
@app.route('/', methods=['GET', 'POST'])
# function login
def login():
    #cek jika method post dan ada form data maka proses login
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form:
        # buat variabel untuk memudahkan pengolahan data
        email = request.form['inpEmail']
        password = request.form['inpPass']
        #cursor koneksi mysql
        cur = mysql.connection.cursor()
        #eksekusi kueri
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        #fetch hasil kueri
        result = cur.fetchone()
        #cek hasil kueri
        if result:
            # jika login valid buat data session
            session['is_logged_in'] = True
            session['username'] = result[1]
            #redirect ke halaman home
            return redirect(url_for('home'))
        else:
            # jika login invalid kembalikan ke login form
            return render_template('login.html')
    else:
        #jika method selain POST tampilkan form login
        return render_template('login.html')

#set route default
@app.route('/home')
#function home
def home():
    # cek session apakah sudah login
    if 'is_logged_in' in session:
        #cursor koneksi mysql
        cur = mysql.connection.cursor()
        #eksekusi kueri
        cur.execute("SELECT * FROM users")
        #fetch hasil kueri masukkan ke var data
        data = cur.fetchall()
        #tutup koneksi
        cur.close()
        #render aray data sebagai users bersama template
        return render_template('home.html', users=data)
    else:
        return redirect(url_for('login'))
# route logout
@app.route('/logout')
def logout():
    # hapus data session
    session.pop('is_logged_in', None)
    session.pop('username', None)
    # redirect ke halaman login
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form and 'inpName' in request.form and 'inpAlamat' in request.form and 'inpNomorTelepon' in request.form:
        email = request.form['inpEmail']
        password = request.form['inpPass']
        username = request.form['inpName']
        alamat = request.form['inpAlamat']
        nomor_telepon = request.form['inpNomorTelepon']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, email, password, alamat, nomor_telepon) VALUES (%s, %s, %s, %s, %s)", (username, email, password, alamat, nomor_telepon))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

#debug dan auto reload
if __name__ == '__main__':
    app.run(debug=True)