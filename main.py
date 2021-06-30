import json
import logging

logging.basicConfig(format='%(levelname)s - %(message)s')


def calculate_market_auction(id, year):
    """Calculate market value and auction value from a json file.

    The formula for market value is:
    MarketValue = {cost} * {marketRatio}

    The formula auction value is:
    AuctionValue = {cost} * {auctionRatio}
    """
    result = {}
    id = str(id)
    year = str(year)
    try:
        with open('api-response.json') as json_file:
            data = json.load(json_file)
        cost = data[id]['saleDetails']['cost']
    except KeyError as e:
        logging.error(f'ID:{e} doesn\'t exist')
    else:
        try:
            year_values = data[id]['schedule']['years'][year]
            result['market_value'] = cost * year_values['marketRatio']
            result['auction_value'] = cost * year_values['auctionRatio']
        except KeyError as e:
            logging.error(f'Year:{e} doesn\'t exist')

    return result


if __name__ == '__main__':
    exit = 'n'
    while exit == 'n':
        equipment_id = input('Please, enter the equipment ID:')
        year = input('Please, enter the year: ')
        r = calculate_market_auction(equipment_id, year)
        print(r)
        exit = input('Do you want to exit ? (y/n)')
