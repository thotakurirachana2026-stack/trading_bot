from binance.enums import *
from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    try:
        client = get_client()
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Market Order: {order}")
        print("✅ Market order placed successfully!")

        return order

    except Exception as e:

        logger.error(str(e))
        raise


def place_limit_order(symbol, side, quantity, price):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"limit order:{order}")

        return order
    
    except Exception as e:

        logger.error(str(e))
        raise

