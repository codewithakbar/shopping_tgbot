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
# Sozlamaga kirganda javob beradi
settings = """
<b>Umumiy dastur boshqaruvi:</b>

<i>Navigatsiya:</i>

-<b>({}) - </b><i>orqaga</i>
-<b>({}) - </b><i>oldinga</i>
-<b>({}) - </b><i>ko'paytirish</i>
-<b>({}) - </b><i>pasaytirish</i>
-<b>({}) - </b><i>keyingisi</i>
-<b>({}) - </b><i>oldingi</i>

<i>Maxsus tugmalar:</i>

-<b>({}) - </b><i>o\'chirish</i>
-<b>({}) - </b><i>buyurtma</i>
-<b>({}) - </b><i>Hisob-kitob</i>

<i>Umumiy ma\'lumot:</i>

-<b>Dastur versiyasi: - </b><i>({})</i>
-<b>Ishlab chiqaruvchi(Dasturchi): - </b><i><a href="http://t.me/satipoff">({})</a></i>


<b>{} Akbar Satipov</b>

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
Tanlangan maxsulot:

{}
{}
Narxi: {} so\'m

buyurtmaga qo'shiladi!!!

Zaxirada {} ta birlik qoldi.
"""
# ответ пользователю при посещении блока с заказом
order = """

<i>Nomi:</i> <b>{}</b>

<i>Ta\'rif:</i> <b>{}</b>

<i>Narxi:</i> <b>1 dona uchun {} so\'m.</b>

<i>Pozitsiyalar soni:</i> <b>{} dona.</b> 
"""

order_number = """

<b>Buyurtma raqami. № </b> <i>{}</i>

"""
# ответ пользователю, когда заказа нет
no_orders = """
<b>Buyurtma yo'q !!!</b>
"""
# ответ пользователю при подтверждении оформления заказа
applay = """
<b>Buyurtmangiz qabul qilindi !!!</b>

<i>Buyurtmaning umumiy qiymati:</i> <b>{} so\'m</b>

<i>Jami pozitsiyalar soni:</i> <b>{} dona.</b>

<b>Buyurtma omborga yuborildi,
UNING QADOQLASH UCHUN !!!</b>
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
