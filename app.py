# from flask import Flask, render_template, request, redirect, url_for
# from web import Mbarang

# application = Flask(__name__, template_folder='templates')
# @application.route('/')
# def index():
#     # form = KomentarForm()
#     model = Mbarang()
#     container = []
#     container = model.selectDB()
#     return render_template('masterbarang.html', container=container)

#     form = KomentarForm()
#     if request.method == 'POST':
#         if form.validate():
#             nama = form.nama.data
#             harga = form.harga.data
#             satuan = form.satuan.data
#             return render_template('masterbarang.html', nama=nama, harga=harga, satuan=satuan)
#         else:
#             errors = form.errors.items()
#             # return render_template('form.html', form=form, errors=errors)


# if __name__ == '__main__':
#     application.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for
# import confiq
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder='templates')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventaris'
mysql = MySQL(app)

db = cursor = None
@app.route("/")
# def login():
#     return render_template('login.html')
def main():
    return render_template('index.html')

@app.route("/masterbarang")
def masterbarang():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM masterbarang")
    barang = cur.fetchall()
    cur.close()
    return render_template('masterbarang.html', menu='master',submenu='barang',data=barang)

@app.route("/formmasterbarang")
def formmasterbarang():
    return render_template('formmasterbarang.html', menu='master',submenu='barang')

@app.route("/simpanformmasterbarang", methods=["POST"])
def simpanformmasterbarang():
    nama = request.form['nama']
    deskripsi = request.form['deskripsi']
    stock = request.form['stock']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO masterbarang(nama, deskripsi, stock) VALUES(%s, %s, %s)", (nama, deskripsi, stock))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterbarang'))

@app.route("/barangmasuk")
def barangmasuk():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM barangmasuk")
    masuk = cur.fetchall()
    cur.close()
    return render_template('barangmasuk.html', menu='master', submenu='masuk', data=masuk)

@app.route("/formbarangmasuk")
def formbarangmasuk():
    return render_template('formbarangmasuk.html', menu='master',submenu='masuk')

@app.route("/simpanformbarangmasuk", methods=["POST"])
def simpanformbarangmasuk():
    nama = request.form['nama']
    tanggal = request.form['tanggal']
    jumlah = request.form['jumlah']
    keterangan = request.form['keterangan']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO barangmasuk(nama, tanggal, jumlah, keterangan) VALUES(%s, %s, %s, %s)", (nama, tanggal, jumlah, keterangan))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('barangmasuk'))

@app.route("/barangkeluar")
def barangkeluar():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM barangkeluar")
    keluar = cur.fetchall()
    cur.close()
    return render_template('barangkeluar.html', menu='master', submenu='keluar', data=keluar)

@app.route("/formbarangkeluar")
def formbarangkeluar():
    return render_template('formbarangkeluar.html', menu='master',submenu='keluar')

@app.route("/simpanformbarangkeluar", methods=["POST"])
def simpanformbarangkeluar():
    tanggal = request.form['tanggal']
    nama = request.form['nama']
    jumlah = request.form['jumlah']
    penerima = request.form['penerima']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO barangkeluar(tanggal, nama, jumlah, penerima) VALUES(%s, %s, %s, %s)", (tanggal, nama, jumlah, penerima))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('barangkeluar'))

# @app.route("/formpembelian")
# def formpembelian():
#     return render_template('formpembelian.html', menu='pembelian', submenu='formpembelian')

# @app.route("/datapembelian")
# def datapembelian():
#     return render_template('datapembelian.html', menu='pembelian', submenu='datapembelian')

# @app.route("/formpenjualan")
# def formpenjualan():
#     return render_template('formpenjualan.html', menu='penjualan', submenu='formpenjualan')

# @app.route("/datapenjualan")
# def datapenjualan():
#     return render_template('datapenjualan.html', menu='penjualan', submenu='datapenjualan')

# MENIT KE 19.50

# @app.route("/index2")
# def index2():
#     return render_template('index2.html')

# @app.route("/index3")
# def index3():
#     return render_template('index3.html')

if __name__=="__main__":
    app.run(debug = True)