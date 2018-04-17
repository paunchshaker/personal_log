#!/usr/bin/env python3

import sys
import time
import datetime
import click

def to_hours(duration):
    values = duration.split(':')
    hour = 0
    second = 0
    if len(values) == 1:
        minute = values[0]
    elif len(values) == 2:
        minute, second = values
    elif len(values) == 3:
        hour, minute, second = values
    else:
        raise RuntimeError('Unable to translate duration {0}'.format(duration))
    d = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
    return d.total_seconds() / 60 / 60

@click.command()
@click.argument('distance')
@click.argument('duration')
def main(distance, duration):
    hours = to_hours(duration)
    print("curl -i -X POST 'http://localhost:8086/write?db=cycle' --data-binary 'cycle distance={dist},hours={hrs}'".format(dist=distance, hrs=hours))

if __name__ == '__main__':
    main()
