import esios_monitor
import argparse
from datetime import date, datetime, timedelta


def parse_datetime(date_string):
    return datetime.fromisoformat(date_string)

parser = argparse.ArgumentParser(prog=__name__)
subparsers = parser.add_subparsers(help='sub-command help')

parser_get = subparsers.add_parser('get', help='get help')
parser_get.add_argument('indicators', nargs='+', type=int, metavar='I', help='Indicators as numbers')
parser_get.add_argument('--start-date', dest='start_date', type=parse_datetime, help='Start date', default=date.today())
parser_get.add_argument(
    '--end-date', dest='end_date', type=parse_datetime, help='End date', default=date.today() + timedelta(days=1))

args = parser.parse_args()

# [10167,10131,10122,10113,10104,10095,10086,10077,10074,10073,10064,25,20,14,15,9,2,1,3,4]
esios_monitor.get_values(args.start_date, args.end_date, args.indicators)