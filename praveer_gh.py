import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

# This forces the logs to show up immediately in GitHub Actions
def log(message):
    print(f"[{time.strftime('%H:%M:%S')}] {message}")
    sys.stdout.flush()

def setup_driver():
    log("Initializing Chrome Options...")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    
    log("Starting Driver...")
    driver = webdriver.Chrome(options=options)
    
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True)
    
    driver.set_page_load_timeout(60)
    return driver

def run_agent(machine_id):
    driver = None
    try:
        log(f"MACHINE {machine_id} - Opening Browser...")
        driver = setup_driver()
        
        # --- YOUR CORE LOGIC START ---
        target_url = os.getenv('GROUP_URL')
        log(f"Navigating to: {target_url}")
        driver.get(target_url)
        
        log("Page loaded. Taking a 10s breath...")
        time.sleep(10) 
        # Add your message sending logic here
        # --- YOUR CORE LOGIC END ---
        
    except Exception as e:
        log(f"CRITICAL ERROR: {e}")
    finally:
        if driver:
            driver.quit()
            log("Browser session closed safely.")

if __name__ == "__main__":
    m_id = os.getenv('MACHINE_ID', 'Unknown')
    log(f"STARTING 24/7 AGENT ON MACHINE {m_id}")
    
    start_time = time.time()
    # Run for 5 hours and 40 minutes (leaving buffer for GitHub's 6h limit)
    max_duration = 5.6 * 60 * 60 

    while (time.time() - start_time) < max_duration:
        run_agent(m_id)
        wait_time = random.randint(45, 90)
        log(f"Cycle complete. Sleeping for {wait_time}s...")
        time.sleep(wait_time)
