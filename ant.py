import requests
import time

# Load semua bearer token dari file
with open("initdata.txt", "r") as f:
    bearer_list = [line.strip() for line in f if line.strip()]

# Endpoint
CHECKIN_URL = "https://api.antcoin.network/api/user/check/in"
MINING_URL = "https://api.antcoin.network/api/mining/start"

# Interval 4 jam (14400 detik)
INTERVAL = 4 * 60 * 60

def run():
    print("🚀 Menjalankan check-in & mining untuk semua akun...\n")
    for idx, bearer_token in enumerate(bearer_list):
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
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
