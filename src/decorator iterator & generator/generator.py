def revenue_projection(start, months, growth_rate):
    current = start
    for _ in range(months):
        yield current
        current *= (1 + growth_rate)

projections = revenue_projection(1000, 5, 0.1)
for month, revenue in enumerate(projections, 1):
    print(f"Month {month}: ${revenue:.2f}")