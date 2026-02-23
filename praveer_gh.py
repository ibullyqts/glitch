# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (V100 HYPER-SPEED)
# 📅 STATUS: SELENIUM STEALTH | 2 THREADS | 120s RESTART

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor

# 📦 SELENIUM + STEALTH
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION (V100 LOGIC) ---
THREADS = 2             # Double Agent
TOTAL_DURATION = 21600  # 6 Hours (Max GH Action time)
BURST_SPEED = (0.1, 0.3) 
SESSION_LIMIT = 120     # 2 Minutes Restart

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

# Force UTF-8 for GH Logs
sys.stdout.reconfigure(encoding='utf-8')

def log_status(agent_id, msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] Agent {agent_id}: {msg}", flush=True)

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        time.sleep(2) 
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # iPhone X Mobile Emulation
        mobile_emulation = {
            "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"v100_gh_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")

        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Linux armv8l", 
            webgl_vendor="ARM",
            renderer="Mali-G76",
            fix_hairline=True,
        )
        driver.custom_temp_path = temp_dir
        return driver

def find_mobile_box(driver):
    selectors = ["//textarea", "//div[@role='textbox']"]
    for xpath in selectors:
        try: 
            el = driver.find_element(By.XPATH, xpath)
            if el.is_displayed(): return el
        except: continue
    return None

def adaptive_inject(driver, element, text):
    try:
        driver.execute_script("arguments[0].click();", element)
        driver.execute_script("""
            var el = arguments[0];
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, element, text)
        time.sleep(0.1)
        element.send_keys(Keys.ENTER)
        return True
    except:
        return False

# THE GLITCH PAYLOAD GENERATOR
def get_glitch_payload(target):
    bloat = "".join(random.choice(["‎", "‏", "‌", "‍"]) for _ in range(random.randint(400, 700)))
    zalgo = "p̸r̸a̸v̸e̸e̸r̸" * random.randint(5, 12)
    return f"({target}) {bloat}\n{zalgo}\n🛑"

def run_life_cycle(agent_id, cookie, target):
    global GLOBAL_SENT
    start_time = time.time()

    while (time.time() - start_time) < TOTAL_DURATION:
        driver = None
        temp_path = None
        session_start = time.time()
        
        try:
            log_status(agent_id, "🚀 Launching Stealth Browser...")
            driver = get_driver(agent_id)
            temp_path = getattr(driver, 'custom_temp_path', None)
            
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(5)
            
            msg_box = find_mobile_box(driver)
            if not msg_box:
                log_status(agent_id, "❌ Box Not Found. Refreshing...")
                continue

            # 2 MINUTE SESSION LOOP
            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_glitch_payload(os.getenv("TARGET_NAME", "User"))
                
                if adaptive_inject(driver, msg_box, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
                    if GLOBAL_SENT % 10 == 0:
                        log_status(agent_id, f"⚡ Sent: {GLOBAL_SENT} | SCRIPT BY PRAVEER")
                
                time.sleep(random.uniform(*BURST_SPEED))

        except Exception as e:
            log_status(agent_id, f"⚠️ Error: {str(e)[:50]}")
        
        finally:
            log_status(agent_id, "♻️ 2 Minute Limit - Cleaning RAM...")
            if driver: driver.quit()
            if temp_path and os.path.exists(temp_path):
                shutil.rmtree(temp_path, ignore_errors=True)
            gc.collect()
            time.sleep(2)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target = os.environ.get("GROUP_URL", "").split('/')[-2] # Extracts ID from URL
    
    if not cookie or not target:
        print("❌ MISSING SECRETS (SESSION_ID or GROUP_URL)")
        return

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
