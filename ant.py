import requests
import time
import urllib.parse

# Load semua initData dari file
with open("initdata.txt", "r") as f:
    initdata_list = [line.strip() for line in f if line.strip()]

# Endpoint check-in dan start mining
CHECKIN_URL = "https://api.antcoin.network/api/user/check/in"
MINING_URL = "https://api.antcoin.network/api/mining/start"

# Interval 4 jam (dalam detik)
INTERVAL = 4 * 60 * 60

def extract_token(initdata: str) -> str:
    """Ambil hash dari initData sebagai accept-token"""
    parsed = urllib.parse.parse_qs(initdata)
    return parsed.get("hash", [""])[0]

def do_request(url: str, token: str, idx: int, label: str):
    headers = {
        "accept": "application/json",
        "accept-token": token,
        "content-type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, json={})
        data = response.json()
        print(f"[{idx}] {label} ✅ | Status: {response.status_code} | Response: {data}")
    except Exception as e:
        print(f"[{idx}] {label} ❌ | Error: {e}")

def run_all():
    print("\n🚀 Menjalankan check-in dan mining untuk semua akun...\n")
    for idx, initdata in enumerate(initdata_list):
        token = extract_token(initdata)
        if not token:
            print(f"[{idx}] ❌ Token kosong, lewati.")
            continue

        do_request(CHECKIN_URL, token, idx, "Check-In")
        time.sleep(1)  # jeda sedikit biar aman
        do_request(MINING_URL, token, idx, "Mining")

# Jalankan sekali di awal
run_all()

# Ulangi terus setiap 4 jam
while True:
    print(f"\n⏳ Menunggu 4 jam...\n")
    time.sleep(INTERVAL)
    run_all()
