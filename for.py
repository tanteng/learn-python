"""优化前"""
for item in items:
	if is_for_sale(item):
		cost = compute_cost(item)
		if cost <= wallet.money:
			buy(item)

"""优化后"""
for item in items:
	if not is_for_sale(item):
		continue
	cost = compute_cost(item)
	if cost > wallet.money:
		continue
	buy(item)