# 8-5. Cities.py
def describe_city(city, nation='france'):
    """Display city and nation"""
    print(f"\n{city.title()} is in {nation.title()}")

describe_city('marseille')
describe_city('paris')
describe_city('birmingham','america')
