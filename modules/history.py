# modules/history.py
import sqlite3
import os

def get_history():
    """Coleta o histórico de navegação do Chrome."""
    history_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    if not os.path.exists(history_path):
        return []
    
    conn = sqlite3.connect(history_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url, title, last_visit_time FROM urls")
    history_data = cursor.fetchall()
    conn.close()
    
    return [{"url": url, "title": title, "last_visit_time": time} for url, title, time in history_data]
