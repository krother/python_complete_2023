from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.ecosia.org/")
    page.locator("[data-test-id=\"search-form-input\"]").click()
    page.locator("[data-test-id=\"search-form-input\"]").fill("volkswagen infotainment")
    page.locator("[data-test-id=\"search-form-input\"]").press("Enter")
    page.locator("[data-test-id=\"cookie-notice-accept\"]").click()
    page.get_by_role("link", name="ENGLISH - Volkswagen Infotainment").click()
    page.get_by_role("link", name="Agree and continue").click()
    page.get_by_role("link", name="Career").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
