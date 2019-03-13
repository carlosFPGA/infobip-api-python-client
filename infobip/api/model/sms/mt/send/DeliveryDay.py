# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from enum import Enum


class DeliveryDay(Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

    @staticmethod
    def get_by_name(name):
        return list(DeliveryDay.values()).intersection({name}).pop()

    @staticmethod
    def values():
        return {
            DeliveryDay.MONDAY,
            DeliveryDay.TUESDAY,
            DeliveryDay.WEDNESDAY,
            DeliveryDay.THURSDAY,
            DeliveryDay.FRIDAY,
            DeliveryDay.SATURDAY,
            DeliveryDay.SUNDAY
        }
