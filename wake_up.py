from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

APP_URL = "https://da-tuition-question-generator.streamlit.app/"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(APP_URL, timeout=60000)

        try:
            wake_button = page.get_by_role("button", name="Yes, get this app back up!")
            wake_button.wait_for(state="visible", timeout=10000)
            print("App is asleep — clicking wake button...")
            wake_button.click()
            page.wait_for_timeout(15000)
            print("Wake button clicked, app should be restarting.")
        except PlaywrightTimeoutError:
            print("No wake button found — app is already awake.")

        browser.close()

if __name__ == "__main__":
    main()
