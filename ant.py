import requests
import time
import urllib.parse

# Load semua initData dari file
with open("initdata.txt", "r") as f:
    initdata_list = [line.strip() for line in f if line.strip()]

# URL endpoint
CHECKIN_URL = "https://api.antcoin.network/api/user/check/in"
MINING_URL = "https://api.antcoin.network/api/mining/start"

# Interval 4 jam (14400 detik)
INTERVAL = 4 * 60 * 60

def extract_token_from_initdata(initdata: str) -> str:
    """Ambil hash dari initData untuk accept-token"""
    parsed = urllib.parse.parse_qs(initdata)
    return parsed.get("hash", [""])[0]

def run():
    print("🚀 Menjalankan check-in dan mining untuk semua akun...\n")
    for idx, initdata in enumerate(initdata_list):
        token = extract_token_from_initdata(initdata)
        if not token:
            print(f"[{idx}] ❌ Token kosong, lewati.")
            continue

        headers = {
            "accept": "application/json",
            "accept-token": token,
            "content-type": "application/json"
        }

        # Check-In
        try:
            r_checkin = requests.post(CHECKIN_URL, headers=headers, json={})
            print(f"[{idx}] ✅ Check-In | Status: {r_checkin.status_code} | Response: {r_checkin.text}")
        except Exception as e:
            print(f"[{idx}] ❌ Error Check-In: {e}")

        # Mining
        try:
            r_mine = requests.post(MINING_URL, headers=headers, json={})
            print(f"[{idx}] ✅ Mining   | Status: {r_mine.status_code} | Response: {r_mine.text}")
        except Exception as e:
            print(f"[{idx}] ❌ Error Mining: {e}")

while True:
    run()
    print("\n⏳ Menunggu 4 jam...\n")
    time.sleep(INTERVAL)
