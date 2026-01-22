from shoes.size_ids import load_size_id

def build_filters(itemSize):
    size_id = load_size_id(itemSize)
    return [f"size_ids[]={size_id}"]