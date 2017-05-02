from peach.filters import BaseFilter
from datetime import datetime


class DateFilter(BaseFilter):

    name = 'date'
    value_type = datetime
    allow_multiple = False

    @classmethod
    def condition(cls, date_value, **kwargs):
        return {'date': [date_value.year, date_value.month, date_value.day]}


class DateRangeFilter(BaseFilter):

    name = 'date_range'
    value_type = datetime
    allow_multiple = True

    @classmethod
    def condition(cls, from_date, to_date, **kwargs):
        return {'date': [[from_date.year, from_date.month, from_date.day],
                         [to_date.year, to_date.month, to_date.day]]}


class NameFilter(BaseFilter):

    name = 'name'
    value_type = str
    allow_multiple = True

    @classmethod
    def condition(cls, *names):
        return {'name': names}
