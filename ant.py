import requests
import time
import urllib.parse

# Load semua initData dari file
with open("initdata.txt", "r") as f:
    initdata_list = [line.strip() for line in f if line.strip()]

# Endpoint check-in & mining
checkin_url = "https://api.antcoin.network/api/user/check/in"
mining_url = "https://api.antcoin.network/api/mining/start"

# Interval 4 jam (14400 detik)
INTERVAL = 4 * 60 * 60

def extract_token_from_initdata(initdata: str) -> str:
    """Ambil hash dari initData untuk jadi token"""
    parsed = urllib.parse.parse_qs(initdata)
    return parsed.get("hash", [""])[0]

def run_all():
    print("🚀 Menjalankan check-in dan mining untuk semua akun...\n")
    for idx, initdata in enumerate(initdata_list):
        token = extract_token_from_initdata(initdata)
        if not token:
            print(f"[{idx}] ❌ Token kosong atau salah format.")
            continue

        headers = {
            "accept": "application/json",
            "accept-token": token,
            "content-type": "application/json"
        }

        # Check-in
        try:
            r_checkin = requests.post(checkin_url, headers=headers, json={})
            print(f"[{idx}] Check-In ✅ | Status: {r_checkin.status_code} | Response: {r_checkin.json()}")
        except Exception as e:
            print(f"[{idx}] Check-In ❌ Error: {e}")

        # Mining
        try:
            r_mining = requests.post(mining_url, headers=headers, json={})
            print(f"[{idx}] Mining ✅ | Status: {r_mining.status_code} | Response: {r_mining.json()}")
        except Exception as e:
            print(f"[{idx}] Mining ❌ Error: {e}")

# Jalankan pertama kali
run_all()

# Loop tiap 4 jam
while True:
    print("\n⏳ Menunggu 4 jam...\n")
    time.sleep(INTERVAL)
    run_all()
