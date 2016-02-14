import gateway_locator
import arf8084
import simple

import logging

logger = logging.getLogger(__name__)


def get_coords(data_point):
    coords = None

    try:
        coords = gateway_locator.parse_coords(data_point)
    except:
        logger.debug('Cannot parse coords using Gateway Locator format')

    if coords is None:
        try:
            coords = arf8084.parse_coords(data_point)
        except:
            logger.debug('Cannot parse coords using arf8084 format')

    if coords is None:
        try:
            coords = simple.parse_coords(data_point)
        except:
            logger.debug('Cannot parse coords using simple format')

    return coords
