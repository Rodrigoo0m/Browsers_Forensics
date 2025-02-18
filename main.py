import os
import json
from modules import history, cookies, credentials
import sqlite3

def save_output(filename, data):
    """Salva os dados extraídos em formato JSON na pasta outputs."""
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"[+] Dados salvos em {output_dir}/{filename}")

def main():
    print("\n===== Forense de Navegador =====")
    
    print("[+] Coletar histórico de navegação...")
    history_data = history.get_history()
    save_output("history.json", history_data)
    
    print("[+] Extrair cookies...")
    cookies_data = cookies.get_cookies()
    save_output("cookies.json", cookies_data)
    
    print("[+] Recuperar credenciais salvas...")
    credentials_data = credentials.get_credentials()
    save_output("credentials.json", credentials_data)
    
    print("\n[+] Coleta concluída!")

if __name__ == "__main__":
    main()
