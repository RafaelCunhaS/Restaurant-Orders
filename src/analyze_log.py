import csv
from track_orders import TrackOrders


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    track_orders = TrackOrders()
    try:
        with open(path_to_file, 'r') as file:
            data = csv.reader(file)
            for customer, order, day in data:
                track_orders.add_new_order(customer, order, day)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(f"""{track_orders.get_most_ordered_dish_per_customer('maria')}
{track_orders.get_amount_of_orders('arnaldo', 'hamburguer')}
{track_orders.get_never_ordered_per_customer('joao')}
{track_orders.get_days_never_visited_per_customer('joao')}""")
