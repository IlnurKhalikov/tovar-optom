import requests
from telebot import types
from bs4 import BeautifulSoup

# def parser(url):
#     response = requests.get(url)
#
#     # Парсинг HTML страницы
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Извлечение данных о продуктах и ценах
#     products = []
#     for product in soup.find_all("a", class_="product-layout product-list col-xs-12"):
#         name = product.find("span").text
#         # price = product.find("div", class_="price").text.split('\n')[1]
#         products.append(name)
#     return products

admin_panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Отправить сообщение по id')
btn2 = types.KeyboardButton('Сделать рассылку')
btn3 = types.KeyboardButton('+1 заказ')
btn4 = types.KeyboardButton('+1 отменённый заказ')
btn5 = types.KeyboardButton('Изменить доступ к заказам')
btn6 = types.KeyboardButton('Отправить платёж')
admin_panel.row(btn1, btn2)
admin_panel.row(btn3, btn4)
admin_panel.row(btn5, btn6)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Купить')
btn2 = types.KeyboardButton('Аккаунт')
btn3 = types.KeyboardButton('Реф. система')
btn4 = types.KeyboardButton('О нас')
menu.row(btn1)
menu.row(btn2, btn3)
menu.row(btn4)

agree = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('✔ Подтвердить')
btn2 = types.KeyboardButton('❌ Отмена')
agree.row(btn1, btn2)

category = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('СТЕКЛА, ЧЕХЛЫ')
btn2 = types.KeyboardButton('УМНЫЕ и СТИЛЬНЫЕ SMART-ЧАСЫ')
btn3 = types.KeyboardButton('КАБЕЛИ, З/У, УДЛИНИТЕЛИ')
btn4 = types.KeyboardButton('НОСИТЕЛИ ИНФОРМАЦИИ')
btn5 = types.KeyboardButton('ЭЛЕМЕНТЫ ПИТАНИЯ')
btn6 = types.KeyboardButton('АКУСТИЧЕСКИЕ СИСТЕМЫ')
btn7 = types.KeyboardButton('КОМПЬЮТЕРНЫЕ АКСЕССУАРЫ')
btn8 = types.KeyboardButton('МОБИЛЬНЫЕ АКСЕCСУАРЫ И ИНСТРУМЕНТЫ')
btn9 = types.KeyboardButton('Продукция Xiaomi')
btn10 = types.KeyboardButton('ЭЛЕКТРОНИКА')
btn11 = types.KeyboardButton('АВТОАКСЕССУАРЫ')
btn12 = types.KeyboardButton('ФОНАРИ, НОЖИ, РАЦИИ, ТУРИЗМ')
btn13 = types.KeyboardButton('⬅ Назад')
category.row(btn1, btn2)
# category.row(btn3, btn4)
category.row(btn5, btn6)
# category.row(btn7, btn8)
category.row(btn9)#, btn10)
category.row(btn11, btn12)
category.row(btn13)

subcategory_1_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('ЧЕХЛЫ')
btn2 = types.KeyboardButton('ЗАЩИТНЫЕ СТЁКЛА')
btn3 = types.KeyboardButton('Кардхолдеры')
btn4 = types.KeyboardButton('Ремешки, браслеты')
btn5 = types.KeyboardButton('Чехлы для APods')
btn6 = types.KeyboardButton('Стилусы,прочее')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_1_0.row(btn1)#, btn2)
subcategory_1_0.row(btn3)#, btn4)
subcategory_1_0.row(btn6)#btn5, btn6)
subcategory_1_0.row(btn13)

subcategory_1_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Чехлы для iP')
btn2 = types.KeyboardButton('Чехлы для Samsung')
btn3 = types.KeyboardButton('Чехлы для XiaoMi')
btn4 = types.KeyboardButton('Чехлы для Huawei')
btn5 = types.KeyboardButton('Чехлы для Realme')
btn6 = types.KeyboardButton('Чехлы для Tecno')
btn7 = types.KeyboardButton('Чехлы универсальные')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_1_1.row(btn1)#, btn2)
# subcategory_1_1.row(btn3, btn4)
# subcategory_1_1.row(btn5, btn6)
subcategory_1_1.row(btn7)
subcategory_1_1.row(btn13)

subcategory_1_1_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Чехлы для iP 11')
btn2 = types.KeyboardButton('Чехлы для iP 14 Pro Max')
btn3 = types.KeyboardButton('Чехлы для iP 14 Max')
btn4 = types.KeyboardButton('Чехлы для iP 14 Pro')
btn5 = types.KeyboardButton('Чехлы для iP 14')
btn6 = types.KeyboardButton('Чехлы для iP 13 Pro Max')
btn7 = types.KeyboardButton('Чехлы для iP 13 Pro')
btn8 = types.KeyboardButton('Чехлы для iP 13')
btn9 = types.KeyboardButton('Чехлы для iP 13 Mini')
btn10 = types.KeyboardButton('Чехлы для iP 12 Pro Max')
btn11 = types.KeyboardButton('Чехлы для iP 12/12Pro')
btn12 = types.KeyboardButton('Чехлы для iP 12 Mini')
btn13 = types.KeyboardButton('Чехлы для iP 11 Pro Max')
btn14 = types.KeyboardButton('Чехлы для iP 11 Pro')
btn15 = types.KeyboardButton('Чехлы для iP XR')
btn16 = types.KeyboardButton('Чехлы для iP X/XS')
btn17 = types.KeyboardButton('Чехлы для iP XS MAX')
btn18 = types.KeyboardButton('Чехлы для iP 7/8 Plus')
btn19 = types.KeyboardButton('Чехлы для iP 7/8/SE')
btn20 = types.KeyboardButton('Чехлы для iP 6,6 Plus')
btn21 = types.KeyboardButton('Чехлы для iP 5/SE')
btn22 = types.KeyboardButton('⬅ Назад')
subcategory_1_1_1.row(btn1, btn2)
subcategory_1_1_1.row(btn3, btn4)
subcategory_1_1_1.row(btn5, btn6)
subcategory_1_1_1.row(btn7, btn8)
subcategory_1_1_1.row(btn9, btn10)
subcategory_1_1_1.row(btn11, btn12)
subcategory_1_1_1.row(btn13, btn14)
subcategory_1_1_1.row(btn15, btn16)
subcategory_1_1_1.row(btn17, btn18)
subcategory_1_1_1.row(btn19, btn20)
subcategory_1_1_1.row(btn21)
subcategory_1_1_1.row(btn22)

subcategory_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Smart Watch (фитнес браслеты) HOCO, BOROFONE, AWEI, XiaoMi')
btn2 = types.KeyboardButton('Smart Watch (фитнес браслеты) ОРБИТА, КОПИИ')
btn3 = types.KeyboardButton('Аксессуары для Smart Watch (фитнес браслетов)')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_2.row(btn1, btn2)
subcategory_2.row(btn3)
subcategory_2.row(btn13)

subcategory_3_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Термосы')
btn2 = types.KeyboardButton('НОЖИ')
btn3 = types.KeyboardButton('Наборы для выживания')
btn4 = types.KeyboardButton('ФОНАРИ')
btn5 = types.KeyboardButton('РАЦИИ')
btn6 = types.KeyboardButton('БИНОКЛИ')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_3_0.row(btn1, btn2)
subcategory_3_0.row(btn3, btn4)
subcategory_3_0.row(btn5, btn6)
subcategory_3_0.row(btn13)

subcategory_3_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('МУЛЬТИ-НАБОРЫ')
btn2 = types.KeyboardButton('СКЛАДНЫЕ НОЖИ, В ЧЕХЛЕ')
btn3 = types.KeyboardButton('ТРЕНИРОВОЧНЫЕ НОЖИ')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_3_1.row(btn1, btn2)
subcategory_3_1.row(btn3)
subcategory_3_1.row(btn13)

subcategory_3_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('РУЧНЫЕ светодиодные на батарейках')
btn2 = types.KeyboardButton('Фонари для велосипедов')
btn3 = types.KeyboardButton('РУЧНЫЕ на аккумуляторе, фонарь-ШОКЕР')
btn4 = types.KeyboardButton('НАЛОБНЫЕ светодиодные на батарейках')
btn5 = types.KeyboardButton('НАЛОБНЫЕ светодиодные с АКБ')
btn6 = types.KeyboardButton('КЕМПИНГОВЫЕ светодиодные, УЛИЧНЫЕ, ОТ СОЛНЦА')
btn7 = types.KeyboardButton('ФОНАРИ-БРЕЛКИ, ЛАЗЕРЫ')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_3_2.row(btn1, btn2)
subcategory_3_2.row(btn3, btn4)
subcategory_3_2.row(btn5, btn6)
subcategory_3_2.row(btn7)
subcategory_3_2.row(btn13)

subcategory_4_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Мизинчиковые LR/R03 (ААА)')
btn2 = types.KeyboardButton('Пальчиковые LR/R06 (АА)')
btn3 = types.KeyboardButton('Таблетки SR/CR/LR/PR/AG')
btn4 = types.KeyboardButton('Батарейки С (R14/LR14)')
btn5 = types.KeyboardButton('Батарейки D (R20/LR20)')
btn6 = types.KeyboardButton('Крона (6F22/6LR61)')
btn7 = types.KeyboardButton('Для электронных устройств А23, А27, 28L, CR2, CR123, LR1/E90')
btn8 = types.KeyboardButton('Квадрат 3R12')
btn9 = types.KeyboardButton('АККУМУЛЯТОРЫ 10440,14500,16340,18650')
btn10 = types.KeyboardButton('Аккумуляторы R03/R06/6F22/HR20')
btn11 = types.KeyboardButton('Зарядные устройства')
btn12 = types.KeyboardButton('Аккумуляторы универсальные')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_4_0.row(btn1, btn2)
subcategory_4_0.row(btn3, btn4)
subcategory_4_0.row(btn5, btn6)
subcategory_4_0.row(btn7, btn8)
subcategory_4_0.row(btn9, btn10)
subcategory_4_0.row(btn11, btn12)
subcategory_4_0.row(btn13)

subcategory_5_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('КОЛОНКИ для Компьютера')
btn2 = types.KeyboardButton('НАУШНИКИ, ГАРНИТУРЫ')
btn3 = types.KeyboardButton('РАДИОПРИЁМНИКИ')
btn4 = types.KeyboardButton('МИКРОФОНЫ')
btn5 = types.KeyboardButton('ПОРТАТИВНЫЕ КОЛОНКИ BLUETOOTH')
btn6 = types.KeyboardButton('НАПОЛЬНЫЕ КОЛОНКИ BLUETOOTH')
btn7 = types.KeyboardButton('УСИЛИТЕЛИ ЗВУКА')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_5_0.row(btn1, btn2)
subcategory_5_0.row(btn3, btn4)
subcategory_5_0.row(btn5, btn6)
subcategory_5_0.row(btn7)
subcategory_5_0.row(btn13)

subcategory_5_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Вакуумные / Вкладыши')
btn2 = types.KeyboardButton('Гарнитура / Наушники с аудио разъемом Lightning, Type-C (вакуумные / вкладыши)')
btn3 = types.KeyboardButton('ГАРНИТУРЫ TWS PRO вакуумные')
btn4 = types.KeyboardButton('ГАРНИТУРЫ TWS вкладыши')
btn5 = types.KeyboardButton('Awei')
btn6 = types.KeyboardButton('Гарнитуры MIX')
btn7 = types.KeyboardButton('HandsFree Bluetooth')
btn8 = types.KeyboardButton('ПОЛНОРАЗМЕРНЫЕ НАУШНИКИ')
btn9 = types.KeyboardButton('СЛУХОВЫЕ АППАРАТЫ')
btn10 = types.KeyboardButton('АКСЕССУАРЫ ДЛЯ НАУШНИКОВ')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_5_1.row(btn1, btn2)
subcategory_5_1.row(btn3, btn4)
subcategory_5_1.row(btn5, btn6)
subcategory_5_1.row(btn7, btn8)
subcategory_5_1.row(btn9, btn10)
subcategory_5_1.row(btn13)

subcategory_5_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Микрофоны для ПК/мобильных устройств')
btn2 = types.KeyboardButton('Микрофоны караоке')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_5_2.row(btn1, btn2)
subcategory_5_2.row(btn13)

subcategory_5_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Стойки-штативы под колонки')
btn2 = types.KeyboardButton('KIMISO')
btn3 = types.KeyboardButton('FUMIKO, HOCO, BOROFONE')
btn4 = types.KeyboardButton('CRAZY BOX ELTRONIC')
btn5 = types.KeyboardButton('Напольные колонки MIX')
btn6 = types.KeyboardButton('ОРБИТА')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_5_3.row(btn1, btn2)
subcategory_5_3.row(btn3, btn4)
subcategory_5_3.row(btn5, btn6)
subcategory_5_3.row(btn13)

subcategory_6_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('РАДАР-ДЕТЕКТОРЫ')
btn2 = types.KeyboardButton('ВИДЕО РЕГИСТРАТОРЫ')
btn3 = types.KeyboardButton('АВТОМАГНИТОЛЫ')
btn4 = types.KeyboardButton('ДЕРЖАТЕЛИ')
btn5 = types.KeyboardButton('РАЗВЕТВИТЕЛИ ПРИКУРИВАТЕЛЯ')
btn6 = types.KeyboardButton('АВТОЗВУК')
btn7 = types.KeyboardButton('FM-МОДУЛЯТОРЫ')
btn8 = types.KeyboardButton('ДВОРНИКИ')
btn9 = types.KeyboardButton('АВТОХИМИЯ')
btn10 = types.KeyboardButton('АВТОЭЛЕКТРОНИКА, КОМФОРТ')
btn11 = types.KeyboardButton('ЧЕХЛЫ для БРЕЛКОВ СИГНАЛИЗАЦИИ')
btn12 = types.KeyboardButton('АРОМАТИЗАТОРЫ')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_6_0.row(btn1, btn2)
subcategory_6_0.row(btn3, btn4)
subcategory_6_0.row(btn5, btn6)
subcategory_6_0.row(btn7, btn8)
subcategory_6_0.row(btn9, btn10)
subcategory_6_0.row(btn11, btn12)
subcategory_6_0.row(btn13)

subcategory_6_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('ДЕРЖАТЕЛИ С БЕСПРОВОДНОЙ ЗАРЯДКОЙ')
btn2 = types.KeyboardButton('МАГНИТНЫЕ ДЕРЖАТЕЛИ')
btn3 = types.KeyboardButton('ДЕРЖАТЕЛИ на дефлектор, панель, стекло')
btn4 = types.KeyboardButton('ДЛЯ РЕГИСТРАТОРОВ И НАВИГАТОРОВ, ИНФОРМАЦИОННЫЕ В АВТО')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_6_1.row(btn1, btn2)
subcategory_6_1.row(btn3, btn4)
subcategory_6_1.row(btn13)

subcategory_6_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Разветвитель прикуривателя AVS, ОРБИТА')
btn2 = types.KeyboardButton('Разветвитель прикуривателя OLESSON, DREAM')
btn13 = types.KeyboardButton('⬅ Назад')
subcategory_6_2.row(btn1, btn2)
subcategory_6_2.row(btn13)


page = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Следующая страница➡')
btn22 = types.KeyboardButton('⬅ Назад')
page.row(btn1)
page.row(btn22)

page_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('⬅Предыдущая страница')
btn2 = types.KeyboardButton('Следующая страница➡')
btn22 = types.KeyboardButton('⬅ Назад')
page_1.row(btn1, btn2)
page_1.row(btn22)

page_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('⬅Предыдущая страница')
btn22 = types.KeyboardButton('⬅ Назад')
page_2.row(btn1)
page_2.row(btn22)
