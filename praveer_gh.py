# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (VISIBILITY FIX)
# 📅 STATUS: FORCED VIEWPORT | 2 AGENTS | 200ms

import os, sys, asyncio, json, time, random
from playwright.async_api import async_playwright

SID = os.getenv("SESSION_ID")
URL = os.getenv("GROUP_URL")
TARGET = os.getenv("TARGET_NAME", "Target")
CREDITS = "SCRIPT BY PRAVEER"

total_sent = 0
counter_lock = asyncio.Lock()

def get_random_payload(target):
    bloat_chars = ["‎", "‏", "‌", "‍"]
    bloat = "".join(random.choice(bloat_chars) for _ in range(random.randint(300, 600)))
    zalgo = "p̸r̸a̸v̸e̸e̸r̸" * random.randint(5, 10)
    return f"({target}) {bloat}\n{zalgo}\n" + "🛑" * random.randint(5, 10)

async def worker(context, agent_id, stop_event):
    global total_sent
    page = await context.new_page()
    try:
        print(f"Agent {agent_id} | 🚀 Connecting...")
        # Navigation with wider timeout for GH Runners
        await page.goto(URL, wait_until='networkidle', timeout=90000)
        
        # FIX: Selector targeting more specific class to find the hidden box
        msg_input = page.locator('div[role="textbox"][aria-label="Message"]')
        
        # Wait for existence, then force it to be visible
        await msg_input.wait_for(state="attached", timeout=45000)
        
        # Some GH runners need a scroll to "see" the element
        await msg_input.scroll_into_view_if_needed()

        while not stop_event.is_set():
            payload = get_random_payload(TARGET)
            
            # Using fill instead of innerText for better hidden-element handling
            await msg_input.fill(payload)
            await page.keyboard.press("Enter")
            
            async with counter_lock:
                total_sent += 1
                print(f"[{total_sent}] Agent {agent_id} Sent | {CREDITS}")
            
            await asyncio.sleep(0.2)
            
    except Exception as e:
        print(f"Agent {agent_id} Exception: {str(e)[:100]}")

async def main():
    if not SID or not URL: return

    while True:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
            
            # FIX: Forced Viewport Size (1920x1080) to stop Instagram from hiding the chat box
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            
            await context.add_cookies([{"name": "sessionid", "value": SID, "domain": ".instagram.com", "path": "/", "secure": True}])

            stop_event = asyncio.Event()
            tasks = [asyncio.create_task(worker(context, 1, stop_event)),
                     asyncio.create_task(worker(context, 2, stop_event))]

            print(f"\n♻️ SESSION START | Viewport: 1080p | Target: {TARGET}")
            await asyncio.sleep(120) 
            
            print(f"\n🕒 RELOAD | TOTAL: {total_sent}")
            stop_event.set()
            await asyncio.gather(*tasks, return_exceptions=True)
            await browser.close()
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
