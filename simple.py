"""
Parse data from simple LAT/LON pair
"""

def parse_coords(data_point):
    if 'data_plain' not in data_point:
        raise ValueError('Invalid GPS data')

    # Convert raw coordinate encoding into DMS and then decimal
    raw = data_point['data_plain']
    if 'fix' in raw:
        return None
    elems = raw.split(',')
    lon = float(elems[1])
    lat = float(elems[0])
    return (lon, lat)
