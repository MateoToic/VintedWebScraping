def check_next_page(page):
    ### Checks if there is a next page
    check = page.locator('[data-testid="catalog-pagination--next-page"]')
    if check.count()==0:
        return False
    if check.get_attribute("aria-disabled") == "true":
        return False
    return True