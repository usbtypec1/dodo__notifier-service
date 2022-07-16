import models
import views


def test_bonus_system_fraud_text_report():
    bonus_system_fraud = models.CheatedOrders(
        unit_name='Москва 4-1',
        phone_number='+7 906 676-76-75',
        orders=[
            models.CheatedOrder(
                created_at='2022-02-22T22:33:44',
                number='32 - 3',
            )
        ]
    )
    expected = (
        '<b>❗️ МОШЕННИЧЕСТВО ❗️️\n'
        'Москва 4-1</b>\n'
        'Номер: +7 906 676-76-75\n'
        '22:33 - <b>заказ №32 - 3</b>'
    )
    assert views.CheatedOrders(bonus_system_fraud).as_text() == expected


def test_canceled_order():
    canceled_order = models.OrderByUUID(
        unit_name='Москва 4-6',
        uuid='c4db1e0f-8e14-405e-91b5-9abf983d7e7e',
        price=534,
        number='23 - 4',
        type='Доставка',
        created_at='2022-06-22T00:00:00',
        receipt_printed_at='2022-06-23T12:12:12',
    )
    expected = (
        'Москва 4-6 отменён заказ <a href="https://shiftmanager.dodopizza.ru'
        '/Managment/ShiftManagment/Order?orderUUId=c4db1e0f8e14405e91b59abf983d7e7e">№23 - 4</a> в 534₽\n'
        'Тип заказа: Доставка\n'
        'Заказ сделан в 00:00,'
        f' отменён в 12:12\n'
        f'Между заказом и отменой прошло 36 часов и 12 минут'
    )
    assert views.CanceledOrder(canceled_order).as_text() == expected


def test_stop_sales_by_streets():
    stop_sales = models.StopSaleByStreets(
        unit_name='Москва 4-19',
        street_name='Пушкина 15',
        started_at='2022-06-22T00:00:00',
    )
    expected = (
        '❗️ Москва 4-19 в стопе 35 минут (с 00:00) ❗️\n'
        'Улица: Пушкина 15'
    )
    views.StopSaleByStreets.humanized_order_duration = '35 минут'
    assert views.StopSaleByStreets(stop_sales).as_text() == expected


def test_stop_sales_by_sectors():
    stop_sales = models.StopSaleBySectors(
        unit_name='Москва 4-19',
        sector_name='Пушкина 15',
        started_at='2022-06-22T00:00:00',
    )
    expected = (
        '❗️ Москва 4-19 в стопе 35 минут (с 00:00) ❗️\n'
        'Сектор: Пушкина 15'
    )
    views.StopSaleBySectors.humanized_order_duration = '35 минут'
    assert views.StopSaleBySectors(stop_sales).as_text() == expected


def test_stop_sales_by_ingredients():
    stop_sales = models.StopSaleByIngredients(
        unit_name='Москва 4-19',
        ingredient_name='Тесто 35',
        reason='Отключение электричества',
        started_at='2022-06-22T00:00:00',
    )
    expected = (
        '❗️ Москва 4-19 в стопе 35 минут (с 00:00) ❗️'
        '\nИнгредиент: Тесто 35'
        '\nПричина: Отключение электричества'
    )
    views.StopSaleByIngredients.humanized_order_duration = '35 минут'
    assert views.StopSaleByIngredients(stop_sales).as_text() == expected


def test_stop_sales_by_channels():
    stop_sales = models.StopSaleByChannels(
        unit_name='Москва 4-19',
        sales_channel_name='Самовывоз',
        reason='Отключение электричества',
        started_at='2022-06-22T00:00:00',
    )
    expected = (
        'Москва 4-19 в стопе 15 минут (с 00:00)\n'
        'Тип продажи: Самовывоз\n'
        'Причина: Отключение электричества'
    )
    views.StopSaleByChannels.humanized_order_duration = '15 минут'
    views.StopSaleByChannels.is_urgent = False
    assert views.StopSaleByChannels(stop_sales).as_text() == expected
