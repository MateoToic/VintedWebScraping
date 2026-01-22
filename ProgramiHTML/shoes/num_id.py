from playwright.sync_api import sync_playwright
import csv

def check_num(text):
    ###Checks if given text is a num
    try:
        num = float(text.replace(",","."))
        return True
    except ValueError:
        return False
    
def scrape_sizes():
    ###Scrapes the avaliable shoe sizes and their ids
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.vinted.hr/")
        page.click("#onetrust-reject-all-handler")  #cookies
        #Men:
        btn = page.locator('[data-testid="first-category-5"]')
        btn.click()
        page.get_by_text("Obuća").click()

        #Size
        btn = page.locator('[data-testid="catalog--size-filter--trigger"]').first
        btn.wait_for(state="visible")

        for _ in range(4):      #if the button never loaded correctly
            btn.click()
            try:
                page.wait_for_selector(".u-overflow-auto", timeout=1000)
                break
            except:
                pass

        dropdown = page.locator(".u-overflow-auto").last
        items = dropdown.locator("ul.pile > li.pile__element")

        nums = {}
        count = items.count()
        for i in range(count):
            el = items.nth(i)
            num = el.inner_text()
            testid_el = el.locator("[data-testid]").first
            testid = testid_el.get_attribute("data-testid")
            lista = testid.split("-")
            if check_num(num):
                nums[num] = lista[-1]

        browser.close()
    return _create_csv(nums)

def _create_csv(numId):
    with open("../info/numsId.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # header
        writer.writerow(["size", "testid"])
        for broj, testid in numId.items():
            novBroj = broj.replace(",",".")
            writer.writerow([novBroj, testid])