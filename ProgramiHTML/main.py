from playwright.sync_api import sync_playwright
import sys

import attributes
import shoes.num_id as num_id
from urls import final_link
from page_check import check_next_page
from domains import DOMAINS


def main():
    """
    Takes args:
    1. type of item
    2. name of item
    3. size of item
    4. --generate (optional, if refresh of data for item needed)
    """

    if len(sys.argv) < 4:
        print("Not enough args")
        return

    item_type = sys.argv[1]
    item_name = sys.argv[2]
    item_size = sys.argv[3]
    regenerate = "--generate" in sys.argv
    if regenerate:
        print("Regenerating")
        num_id.scrape_sizes()

    #domain registry
    filters = DOMAINS[item_type](item_size)

    page_num = 1
    link = final_link(item_name, filters, page_num)
    print(f" Starting link: {link}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(link)
        #Cookies
        try:
            page.click("#onetrust-reject-all-handler", timeout=5000)
        except:
            pass  # no cookies popup

        #First page
        attributes.scrape_attributes(page, item_name, item_size)

        # All other pages (if they exist)
        while check_next_page(page):
            page_num += 1
            link = final_link(item_name, filters, page_num)
            print(f"Page {page_num}: {link}")

            page.goto(link)
            attributes.scrape_attributes(page, item_name, item_size, overwrite=False)

        browser.close()


if __name__ == "__main__":
    main()