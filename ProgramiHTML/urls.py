def final_link(itemName,filters=None,page=1):
    ### Connects everything into one final link
    name = "search_text=" + itemName.replace(" ", "%20")
    curr_page = f"page={page}"
    params = [name, curr_page]
    params.extend(filters)
    return "https://www.vinted.hr/catalog?" + "&".join(params)