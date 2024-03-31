import requests
from django.conf import settings
import logging
import traceback

logger = logging.getLogger(__name__)

def send_order_to_telegram(order):
    """
    Функция для отправки информации о заказе в Телеграм
    """
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID

    order_items = order.orderitem_set.all()
    order_details = "Новый заказ:\n\n"
    order_details += "Покупатель: " + order.first_name + " " + order.last_name + "\n"
    if order.delivery_address:
        order_details += "Адрес доставки: " + order.delivery_address + "\n"
    order_details += "Оплата при получении: " + ("Да" if order.payment_on_get else "Нет") + "\n\n"
    order_details += "Заказанные товары:\n"

    for item in order_items:
        order_details += "- " + item.name + " (x" + str(item.quantity) + ") - " + str(item.products_price()) + " грн\n"

    order_details += "\nОбщая сумма: " + str(order.orderitem_set.total_price()) + " грн"

    logger.info(f"Содержимое сообщения: {order_details}")

    try:
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={order_details}")
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения о заказе в Telegram: {e}")
        logger.error(traceback.format_exc())
