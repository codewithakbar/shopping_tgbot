from .config import KEYBOARD, VERSION, AUTHOR

# Dokon haqda mal'umot beradi
trading_store = """

<b>SatipoffStore!!! Botiga xush ko'rdik</b>

Ushbu dastur ishlab chiqilgan 
ayniqsa savdo vakillari uchun,
keyingi <i>(TP/SV)</i>,shuningdek omborchilar uchun, 
tijorat tashkilotlari
ulgurji va chakana savdo.

SATIPOFFSTORE dasturidan foydalanish,
qulay intuitiv shaklda ular quyidagilarga qodir
mijozdan buyurtmani qabul qilish juda qiyin.
Oziq-ovqat do'koni buyurtmani shakllantirishga yordam beradi
va qulay shaklda omborga murojaat qiladi 
buyurtmani keyingi sotib olish uchun firmalar.

"""
# ответ пользователю при посещении блока "Настройки"
settings = """
<b>Общее руководство приложением:</b>

<i>Навигация:</i>

-<b>({}) - </b><i>назад</i>
-<b>({}) - </b><i>вперед</i>
-<b>({}) - </b><i>увеличить</i>
-<b>({}) - </b><i>уменьшить</i>
-<b>({}) - </b><i>следующий</i>
-<b>({}) - </b><i>предыдующий</i>

<i>Специальные кнопки:</i>

-<b>({}) - </b><i>удалить</i>
-<b>({}) - </b><i>заказ</i>
-<b>({}) - </b><i>Оформить заказ</i>

<i>Общая информация:</i>

-<b>версия программы: - </b><i>({})</i>
-<b>разработчик: - </b><i>({})</i>


<b>{}Ваше имя</b>

""".format(
    KEYBOARD['<<'],
    KEYBOARD['>>'],
    KEYBOARD['UP'],
    KEYBOARD['DOUWN'],
    KEYBOARD['NEXT_STEP'],
    KEYBOARD['BACK_STEP'],
    KEYBOARD['X'],
    KEYBOARD['ORDER'],
    KEYBOARD['APPLAY'],
    VERSION,
    AUTHOR,
    KEYBOARD['COPY'],
)
# ответ пользователю при добавлении товара в заказ
product_order = """
Выбранный товар:

{}
{}
Cтоимость: {} руб

добавлен в заказ!!!

На складе осталось {} ед. 
"""
# ответ пользователю при посещении блока с заказом
order = """

<i>Название:</i> <b>{}</b>

<i>Описание:</i> <b>{}</b>

<i>Cтоимость:</i> <b>{} руб за 1 ед.</b>

<i>Количество позиций:</i> <b>{} ед.</b> 
"""

order_number = """

<b>Позиция в заказе № </b> <i>{}</i>

"""
# ответ пользователю, когда заказа нет
no_orders = """
<b>Заказ отсутствует !!!</b>
"""
# ответ пользователю при подтверждении оформления заказа
applay = """
<b>Ваш заказ оформлен !!!</b>

<i>Общая стоимость заказа составляет:</i> <b>{} руб</b>

<i>Общее количество позиций составляет:</i> <b>{} ед.</b>

<b>ЗАКАЗ НАПРАВЛЕН НА СКЛАД,
ДЛЯ ЕГО КОМПЛЕКТОВКИ !!!</b>
"""
# словарь ответов пользователю
MESSAGES = {
    'trading_store': trading_store,
    'product_order': product_order,
    'order': order,
    'order_number': order_number,
    'no_orders': no_orders,
    'applay': applay,
    'settings': settings
}
