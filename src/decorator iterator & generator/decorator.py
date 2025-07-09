def log_function(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with arguments {args}")
        result = func(*args)
        print(f"{func.__name__} finished, result: {result}")
        return result
    return wrapper

@log_function
def calculate_total_sales(sales):
    return sum(sales)

# Use the decorated function
sales = [100, 200, 300]
total = calculate_total_sales(sales)
print(f"Total Sales: ${total}")