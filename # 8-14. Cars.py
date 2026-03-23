# 8-14. Cars.py
def car_info( mfg, year, **other):
    """make dictionary"""
    return {'mfg':mfg, 'year':year, **other}


my_car = car_info('pontiac', 1946, type = 'station wagon', color ='blue')
print(my_car)



