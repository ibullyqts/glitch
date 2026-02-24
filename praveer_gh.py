import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

# Forces logs to appear instantly in the GitHub console
def log(message):
    print(f"[{time.strftime('%H:%M:%S')}] {message}")
    sys.stdout.flush()

def setup_driver():
    log("Initializing Chrome for 10-Agent Matrix...")
    options = Options()
    options.add_argument("--headless=new") # Required for GitHub Actions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    # Real-world User Agent to avoid detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
    
    # Apply stealth to hide headless fingerprints
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
        log(f"MACHINE {machine_id} - Starting Cycle")
        driver = setup_driver()
        
        target_url = os.getenv('GROUP_URL')
        log(f"Navigating to: {target_url}")
        driver.get(target_url)
        
        # Give the page 15 seconds to fully load scripts/chats
        time.sleep(15) 

        # --- SENDING LOGIC ---
        log("Searching for message input field...")
        wait = WebDriverWait(driver, 20)
        
        # Finds common chat input types (divs, inputs, or textareas)
        message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'] | //input[@type='text'] | //textarea")))
        
        # Prepare the message
        content = f"Matrix Agent {machine_id} online. Status: Active. ID: {random.randint(100, 999)}"
        message_box.send_keys(content)
        log("Message typed.")
        
        time.sleep(2)
        
        # Press ENTER key to send (works for most chat platforms)
        message_box.send_keys(u'\ue007') 
        log("✅ Message sent successfully!")
        
    except Exception as e:
        log(f"❌ Error encountered: {e}")
        # Optional: takes a screenshot to help you debug in GitHub artifacts
        # driver.save_screenshot(f"error_machine_{machine_id}.png")
    finally:
        if driver:
            driver.quit()
            log("Browser session closed safely.")

if __name__ == "__main__":
    m_id = os.getenv('MACHINE_ID', '1')
    start_time = time.time()
    
    # 5.5 hours in seconds (19800s) to stay safe under GitHub's 6h limit
    max_duration = 5.5 * 60 * 60 

    log(f"--- 10-AGENT MATRIX STARTING (Machine {m_id}) ---")

    while (time.time() - start_time) < max_duration:
        run_agent(m_id)
        
        # Random sleep between 1 to 3 minutes between sends to look human
        wait_time = random.randint(60, 180)
        log(f"Cycle complete. Waiting {wait_time}s before next attempt...")
        time.sleep(wait_time)

    log("5.5 Hours reached. Preparing for handoff to the next job.")
