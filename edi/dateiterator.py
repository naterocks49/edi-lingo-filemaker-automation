import datetime


class DateIterator:
    def __init__(self, start_date, end_date):
        self.start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y%m%d')
        self.current_date = self.start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_date > self.end_date:
            raise StopIteration
        else:
            current_date_str = self.current_date.strftime('%Y%m%d')
            self.current_date += datetime.timedelta(days=1)
            return current_date_str
