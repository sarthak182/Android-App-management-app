from flask import Flask, render_template, request, jsonify
import sqlite3

def initialize_db():
    conn = sqlite3.connect("appinfo.db")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY,
        appname TEXT,
        appid TEXT,
        appfeatures TEXT
    )''')
    curr.execute('''CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT,
        device_model TEXT,
        os_version TEXT,
        memory TEXT,
        linked_app_id INTEGER,
        FOREIGN KEY (linked_app_id) REFERENCES apps(id)
    )''')
    conn.commit()
    conn.close()


def delete_app_by_appid(appid):
    conn = sqlite3.connect("appinfo.db")
    curr = conn.cursor()
    curr.execute("DELETE FROM apps WHERE appid = ?", (appid,))
    conn.commit()
    conn.close()


def get_app_data():
    conn = sqlite3.connect("appinfo.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM apps")
    app_data = curr.fetchall()
    conn.close()
    return app_data

def get_device_data():
    conn = sqlite3.connect("appinfo.db")
    curr = conn.cursor()
    curr.execute("SELECT * FROM devices")
    device_data = curr.fetchall()
    conn.close()
    return device_data

def insertintodev(data):
    conn = sqlite3.connect("appinfo.db")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT,
    device_model TEXT,
    os_version TEXT,
    memory TEXT,
    linked_app_id INTEGER,
    FOREIGN KEY (linked_app_id) REFERENCES apps(id))''')
    curr.execute('''INSERT INTO devices (device_id, device_model, os_version, memory, linked_app_id)
                    VALUES (?, ?, ?, ?, ?)''', 
                    (data['device_id'], data['device_model'], data['os_version'], data['memory'], data['linked_app_id']))
    
    conn.commit()
    conn.close()

def insertintoapp(data):
    conn = sqlite3.connect("appinfo.db")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS apps (id INTEGER PRIMARY KEY, appname TEXT, appid TEXT, appfeatures TEXT)''')
    curr.execute("INSERT INTO apps (appname, appid, appfeatures) VALUES (?,?,?)", (data['appname'], data['appid'], data['appfeatures']))
    conn.commit()
    conn.close()

app = Flask(__name__)
initialize_db()
@app.route('/')
def home():
    app_data=get_app_data()
    device_data=get_device_data()
    return render_template('index.html', app_data=app_data, device_data=device_data)

@app.route('/deleteapp', methods=['POST'])
def delete_app():
    data = request.get_json()
    appid = data.get('appid')
    if appid:
        delete_app_by_appid(appid)
        return jsonify({"message": "App deleted successfully"})
    return jsonify({"error": "No appid provided"}), 400


@app.route('/submitdeviceinfo', methods=['POST'])
def insertdatadev():
    data=request.get_json()
    insertintodev(data)
    return jsonify({"message":"Data Received"})

@app.route('/submitappinfo', methods=['POST'])
def insertdata():
    data = request.get_json()
    insertintoapp(data)
    return jsonify({"message": "Data Received"})

if __name__ == '__main__':
    app.run(debug=True)