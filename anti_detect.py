import requests
import time
import random

# ====================================================================
# KONFIGURASI
# ====================================================================

# GANTI INI dengan URL yang ingin Anda kirimkan permintaan.
TARGET_URL = "https://httpbin.org/get" 

# Daftar User-Agent dari browser populer (untuk rotasi/pengacakan)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.2210.144"
]

# Rentang waktu jeda acak antara permintaan (dalam detik)
MIN_DELAY = 2
MAX_DELAY = 5

# Jumlah permintaan yang akan dilakukan (simulasi loop)
NUMBER_OF_REQUESTS = 3 

# ====================================================================
# FUNGSI UTAMA
# ====================================================================

def make_stealth_request(url):
    """
    Melakukan permintaan GET dengan teknik dasar anti-deteksi.
    """
    
    selected_user_agent = random.choice(USER_AGENTS)
    
    headers = {
        "User-Agent": selected_user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

    time_delay = random.uniform(MIN_DELAY, MAX_DELAY)
    
    # LOGGING
    print("-" * 40)
    print(f"[{time.strftime('%H:%M:%S')}] Mengirim permintaan ke: {url}")
    print(f"-> Menggunakan User-Agent: {selected_user_agent[:60]}...")
    print(f"-> Menunggu selama {time_delay:.2f} detik...")
    
    time.sleep(time_delay)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 

        print(f"-> Status Kode Berhasil: {response.status_code}")
        
        if "httpbin" in url:
            import json
            data = response.json()
            print(f"-> IP yang Terlihat oleh Server: {data.get('origin', 'N/A')}")
            print(f"-> Headers yang Diterima Server: {data.get('headers', {}).get('User-Agent', 'N/A')}")

        return response.text
        
    except requests.exceptions.RequestException as err:
        print(f"-> ERROR Permintaan: {err}")
        
    return None

# ====================================================================
# EKSEKUSI APLIKASI
# ====================================================================
if name == "main":
    print(f"--- Aplikasi Anti-Deteksi Dasar Dimulai ({NUMBER_OF_REQUESTS}x) ---")
    
    for i in range(NUMBER_OF_REQUESTS):
        print(f"\n[LOOP {i+1}/{NUMBER_OF_REQUESTS}]")
        
        make_stealth_request(TARGET_URL)
        
        if i < NUMBER_OF_REQUESTS - 1:
            time.sleep(random.uniform(1, 3)) 
            
    print("\n--- Aplikasi Selesai ---")