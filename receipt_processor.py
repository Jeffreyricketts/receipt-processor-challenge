import math

def process_receipt(receipt_id, receipt_data):
    # Placeholder function to process receipt data
    pass

def calculate_points(receipt):
    total_points = 0

    # Points based on retailer name length
    retailer_name_length = len(receipt['retailer'].replace(" ", ""))
    total_points += retailer_name_length

    # Points based on number of items
    num_items = len(receipt['items'])
    if num_items >= 2:
        points_items = (num_items // 2) * 5
        total_points += points_items

    # Points based on item descriptions length multiple of 3
    for item in receipt['items']:
        trimmed_length = len(item['shortDescription'].strip())
        if trimmed_length % 3 == 0:
            price = float(item['price'])
            points_description = math.ceil(price * 0.2)
            total_points += points_description

    # Points if purchase day is odd
    purchase_day = int(receipt['purchaseDate'].split('-')[2])
    if purchase_day % 2 != 0:
        total_points += 6

    return total_points
