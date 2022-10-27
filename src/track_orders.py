class TrackOrders:
    def __init__(self):
        self._buckets = []

    def __len__(self):
        return len(self._buckets)

    def add_new_order(self, customer, order, day):
        self._buckets.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        most_ordered = {}
        for client, order, _ in self._buckets:
            if client == customer:
                if order not in most_ordered:
                    most_ordered[order] = 1
                else:
                    most_ordered[order] += 1
        return max(most_ordered, key=most_ordered.get)

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set()
        all_orders = set()
        for client, order, _ in self._buckets:
            all_orders.add(order)
            if client == customer:
                customer_orders.add(order)
        return all_orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        customer_visits = set()
        all_days = set()
        for client, _, day in self._buckets:
            all_days.add(day)
            if client == customer:
                customer_visits.add(day)
        return all_days.difference(customer_visits)

    def get_busiest_day(self):
        busiest_day = {}
        for _, _, day in self._buckets:
            if day not in busiest_day:
                busiest_day[day] = 1
            else:
                busiest_day[day] += 1
        return max(busiest_day, key=busiest_day.get)

    def get_least_busy_day(self):
        least_busy_day = {}
        for _, _, day in self._buckets:
            if day not in least_busy_day:
                least_busy_day[day] = 1
            else:
                least_busy_day[day] += 1
        return min(least_busy_day, key=least_busy_day.get)

    def get_amount_of_orders(self, customer, order):
        n_orders = 0
        for client, order_made, _ in self._buckets:
            if client == customer and order == order_made:
                n_orders += 1
        return n_orders
