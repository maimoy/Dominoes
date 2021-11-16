start = int(input())
end = int(input())

def calculate_time(starting, ending):
    periods_passed = 0
    days_per_period = 12
    while starting > ending:
        periods_passed += 1
        starting = starting / 2
    return str(periods_passed*days_per_period)

print(calculate_time(start, end))
