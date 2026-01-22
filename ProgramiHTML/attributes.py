import csv
import os
import re
from datetime import datetime

def scrape_attributes(page, itemName, itemSize, overwrite=True):
    """Takes the attributes of each item on a page: 
    price, condition, how many people have it as their favorite.
    Calls the internal function _create_csv(...) to create a csv with all the data"""

    items = page.locator('[data-testid="grid-item"]')
    count = items.count()
    
    result = []

    for i in range(count):
        item = items.nth(i)
        row = []
        fav = 0     #how many people have it as favorite
        # description + id
        desc = item.locator('[data-testid$="description-subtitle"]')
        if desc.count() > 0:
            testid = desc.first.get_attribute("data-testid")
            item_id = re.findall(r"\d+", testid)[0]
            description_text = desc.first.inner_text()

            condition = description_text.split("·")[1].strip()

            row += [item_id, condition]

        # price
        costs = item.locator("span.web_ui__Text__text.web_ui__Text__subtitle")
        if costs.count() > 0:
            val = costs.first.inner_text().replace(",", ".")
            row.append(val[:-2])
        
        # favorite
        fav = item.locator('[data-testid="favourite-count-text"]')
        fave = fav.first.inner_text() if fav.count() > 0 else 0

        if row:
            row.append(fave)
            result.append(row)

    _create_csv(itemName, itemSize, result, overwrite)


def _create_csv(itemName, size, prices, overwrite):
    """An internal function which creates a csv file named size.csv in the folder item/{item_name}
    with rows id, condition, price, favorite"""
    folder = f"../item/{itemName}"
    os.makedirs(folder, exist_ok=True)

    path = f"{folder}/{size}.csv"
    mode = "w" if overwrite else "a"

    with open(path, mode, newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        if mode == "w":
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            wr.writerow(["created_at", now])
            wr.writerow(["id", "condition", "price", "favorite_count"])
        wr.writerows(prices)        