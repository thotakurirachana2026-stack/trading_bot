import argparse

from bot.client import get_client
from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import validate_order


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"]
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"]
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    client = get_client()

    try:

        validate_order(
            args.type,
            args.price
        )

        print("\nORDER REQUEST")
        print("-------------")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.price:
            print(f"Price    : {args.price}")

        if args.type == "MARKET":

            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\nORDER RESPONSE")
        print("--------------")
        print(f"Order ID : {response.get('orderId')}")
        print(f"Status   : {response.get('status')}")

        print("\nOrder placed successfully.")

    except Exception as e:

        print(f"\nOrder failed: {e}")


if __name__ == "__main__":
    main()