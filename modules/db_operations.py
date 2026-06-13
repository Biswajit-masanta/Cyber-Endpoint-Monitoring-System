import sqlite3

def save_device(data):

    connection = sqlite3.connect('monitoring.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT OR REPLACE INTO devices
    (hostname, os, version, cpu, memory, disk, timestamp)

    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["hostname"],
        data["os"],
        data["version"],
        data["cpu"],
        data["memory"],
        data["disk"],
        data["timestamp"]
    ))

    connection.commit()
    connection.close()


def get_devices():

    connection = sqlite3.connect('monitoring.db')

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM devices")

    rows = cursor.fetchall()

    connection.close()

    return rows