# Imports
import argparse
import sys
from date import current_time, set_time, advance_time
from main import buy, sold, reset, find_product
from table import table


# Create the parser
def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog='SuperPy',
        usage='%(prog)s options',
        description='Supermarket inventory',
        epilog='Enjoy the program! :)',
        prefix_chars='-'
        )

    subparser = parser.add_subparsers(dest='command', title='commands')


    # Program settings
    parser.add_argument('--reset',
    action='store_true',
    help='reset the program')


    # Date settings
    dateparser = subparser.add_parser('date', usage='%(prog)s')

    dateparser.add_argument(
        '-c',
        '--current',
        action='store_true',
        help='returns the current date'
        )
    dateparser.add_argument(
        '-ad',
        '--advance',
        type=int,
        metavar='x',
        help='advance time with x days'
    )
    dateparser.add_argument(
        '-st',
        '--set-time',
        action='store_true',
        help='sets time to today'
    )

    # Buy products
    buyparser = subparser.add_parser('buy', usage='%(prog)s')

    buyparser.add_argument(
        '-pn',
        '--product-name',
        metavar='product',
        help='product to buy',
        required= True
    )

    buyparser.add_argument(
        '-exp',
        '--expiration-date',
        metavar='[YYYY-MM-DD]',
        help='product expiration date',
        required= True
    )

    buyparser.add_argument(
        '-a',
        '--amount',
        metavar='x',
        default=1,
        help='x amount of product, default = 1'
    )

    buyparser.add_argument(
        '-p',
        '--price',
        metavar='x',
        default=1,
        help='price of purchase, default = 1'
    )


    # Sell products
    sellparser = subparser.add_parser('sell', usage='%(prog)s')
    sellparser.add_argument(
        '-pn',
        '--product-name',
        metavar='product',
        help='product to sell',
        required= True
    )

    sellparser.add_argument(
        '-a',
        '--amount',
        metavar='x',
        default=1,
        help='x amount of product, default = 1'
    )

    sellparser.add_argument(
        '-p',
        '--price',
        metavar='x',
        default=1,
        help='price of product, default = 1'
    )


    # Reports
    reportparser = subparser.add_parser('report', usage='%(prog)s')
    reportparser.add_argument(
        '-pn',
        '--product-name',
        metavar='product',
        default= '0',
        help='productname'
    )

    reportparser.add_argument(
        '-m',
        '--mode',
        metavar='mode',
        default='inventory',
        help='inventory/revenue/buy/sell'
    )
    
    
    # Execute the parse_args() method
    args = parser.parse_args(argv)

    if args.reset:
        reset()
        print('reset done')


    if args.command == 'date':
        if args.current:
            print(current_time())

        elif args.advance:
            print(advance_time(args.advance))

        elif args.set_time:
            print(set_time())


    if args.command == 'buy':
        print(buy(args.product_name, args.expiration_date, args.amount, args.price))


    if args.command == 'sell':
        print(sold(args.product_name, float(args.amount), float(args.price)))

# working on:
    if args.command == 'report':
        if args.mode == 'inventory':
            filename = 'inventory.csv'
        elif args.mode == 'buy':
            filename = 'bought.csv'
        elif args.mode == 'sell':
            filename = 'sold.csv'
        list = find_product(args.product_name, filename)
        print(table(list))
        


if __name__ == '__main__':
    sys.exit(parse_args())
