import time
from datetime import datetime, timedelta

import re
from datetime import datetime, timedelta


def convert_datetime(datetime_ago):
    matches = re.search(r"(\d+ weeks?,? )?(\d+ days?,? )?(\d+ hours?,? )?(\d+ mins?,? )?(\d+ secs? )?ago", datetime_ago)

    if not matches:
        return None

    date_pieces = {'week': 0, 'day': 0, 'hour': 0, 'min': 0, 'sec': 0}

    for i in range(1, len(date_pieces) + 1):
        if matches.group(i):
            value_unit = matches.group(i).rstrip(', ')
            if len(value_unit.split()) == 2:
                value, unit = value_unit.split()
                date_pieces[unit.rstrip('s')] = int(value)

    d = datetime.today() - timedelta(
        weeks=date_pieces['week'],
        days=date_pieces['day'],
        hours=date_pieces['hour'],
        minutes=date_pieces['min'],
        seconds=date_pieces['sec']
    )

    return d

	
