def get_total(orders):
    from suma_import import get_totals, calc_total
    
    orders_totals = get_totals(orders)
    
    total = calc_total(orders_totals)
    
  # Tu código aquí 👇
    return total

orders = [
    {
        "customer_name": "Nicolas",
        "total": 100,
        "delivered": True,
    },
    {
        "customer_name": "Zulema",
        "total": 120,
        "delivered": False,
    },
    {
        "customer_name": "Santiago",
        "total": 20,
        "delivered": False,
    }
]

total = get_total(orders)
print(total)