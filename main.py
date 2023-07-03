import sqlite3
import requests
from models import *
from keyboard import *
from bs4 import BeautifulSoup
from telebot import TeleBot, types

bot = TeleBot(token)
adm_chat = -1001859680142
adm = 1633567239
a = [['https://kitopt02.ru/stek-cehl/79379/21589/20805/',
'https://kitopt02.ru/stek-cehl/79379/21589/48818/',
'https://kitopt02.ru/stek-cehl/79379/21589/48814/',
'https://kitopt02.ru/stek-cehl/79379/21589/48816/',
'https://kitopt02.ru/stek-cehl/79379/21589/48812/',
'https://kitopt02.ru/stek-cehl/79379/21589/39777/',
'https://kitopt02.ru/stek-cehl/79379/21589/39779/',
'https://kitopt02.ru/stek-cehl/79379/21589/39781/',
'https://kitopt02.ru/stek-cehl/79379/21589/40326/',
'https://kitopt02.ru/stek-cehl/79379/21589/30853/',
'https://kitopt02.ru/stek-cehl/79379/21589/26133/',
'https://kitopt02.ru/stek-cehl/79379/21589/30852/',
'https://kitopt02.ru/stek-cehl/79379/21589/26471/',
'https://kitopt02.ru/stek-cehl/79379/21589/26470/',
'https://kitopt02.ru/stek-cehl/79379/21589/23947/',
'https://kitopt02.ru/stek-cehl/79379/21589/14233/',
'https://kitopt02.ru/stek-cehl/79379/21589/14234/',
'https://kitopt02.ru/stek-cehl/79379/21589/14232/',
'https://kitopt02.ru/stek-cehl/79379/21589/89772/',
'https://kitopt02.ru/stek-cehl/79379/21589/89771/',
'https://kitopt02.ru/stek-cehl/79379/21589/89770/',
'https://kitopt02.ru/stek-cehl/47818/',
'https://kitopt02.ru/stek-cehl/25958/',
'https://kitopt02.ru/stek-cehl/79379/95311/'],
['https://kitopt02.ru/88543/26015/',
'https://kitopt02.ru/88543/26017/',
'https://kitopt02.ru/88543/27475/'],
['https://kitopt02.ru/14/10545/',
['https://kitopt02.ru/14/16510/47555/',
'https://kitopt02.ru/14/16510/47557/',
'https://kitopt02.ru/14/16510/47556/'],
'https://kitopt02.ru/14/92443/',
['https://kitopt02.ru/14/77804/45102/',
'https://kitopt02.ru/14/77804/96386/',
'https://kitopt02.ru/14/77804/81277/',
'https://kitopt02.ru/14/77804/30426/',
'https://kitopt02.ru/14/77804/79212/',
'https://kitopt02.ru/14/77804/86673/',
'https://kitopt02.ru/14/77804/91893/'],
'https://kitopt02.ru/14/95939/',
'https://kitopt02.ru/14/28238/'],
['https://kitopt02.ru/23100/36967/'],
['https://kitopt02.ru/elem/78111/',
'https://kitopt02.ru/elem/78110/',
'https://kitopt02.ru/elem/78491/',
'https://kitopt02.ru/elem/78841/',
'https://kitopt02.ru/elem/78588/',
'https://kitopt02.ru/elem/78839/',
'https://kitopt02.ru/elem/79008/',
'https://kitopt02.ru/elem/88922/',
'https://kitopt02.ru/elem/88325/',
'https://kitopt02.ru/elem/78834/',
'https://kitopt02.ru/elem/78118/',
'https://kitopt02.ru/elem/28644/'],
['https://kitopt02.ru/17/91900/',
['https://kitopt02.ru/17/14616/91907/',
'https://kitopt02.ru/17/14616/40995/',
'https://kitopt02.ru/17/14616/85301/25595/43265/',
'https://kitopt02.ru/17/14616/85301/25595/43264/',
'https://kitopt02.ru/17/14616/85301/25594/28789/',
'https://kitopt02.ru/17/14616/85301/25594/38155/',
'https://kitopt02.ru/17/14616/88546/',
'https://kitopt02.ru/17/14616/19180/',
'https://kitopt02.ru/17/14616/85211/',
''],
'https://kitopt02.ru/17/92532/',
['https://kitopt02.ru/17/78568/95298/',
'https://kitopt02.ru/17/78568/94771/'],
'https://kitopt02.ru/17/92533/',
['https://kitopt02.ru/17/84726/25922/',
'https://kitopt02.ru/17/84726/93302/',
'https://kitopt02.ru/17/84726/28097/',
'https://kitopt02.ru/17/84726/37325/',
'https://kitopt02.ru/17/84726/25921/',
'https://kitopt02.ru/17/84726/85333/'],
'https://kitopt02.ru/17/94649/'],
['https://kitopt02.ru/auto/14595/',
'https://kitopt02.ru/auto/89251/',
'https://kitopt02.ru/auto/77803/',
['https://kitopt02.ru/auto/79002/53557/',
'https://kitopt02.ru/auto/79002/94310/',
'https://kitopt02.ru/auto/79002/29307/',
'https://kitopt02.ru/auto/79002/85833/'],
['https://kitopt02.ru/auto/78495/26120/',
'https://kitopt02.ru/auto/78495/26121/',],
'https://kitopt02.ru/auto/94773/',
'https://kitopt02.ru/auto/78001/',
'https://kitopt02.ru/auto/88146/',
'https://kitopt02.ru/auto/98472/',
'https://kitopt02.ru/auto/88456/',
'https://kitopt02.ru/auto/85917/',
'https://kitopt02.ru/auto/85911/']
     ]


def member(chat_id, user_id):
    try:
        chat_id = int(chat_id)
        statuss = ['creator', 'administrator']
        user_status = str(bot.get_chat_member(chat_id=chat_id, user_id=user_id).status)
        return user_status in statuss
    except:
        return False


@bot.message_handler(commands=['admin', 'Admin'])
def admin(message):
    if member(adm_chat, message.chat.id):
        bot.send_message(message.chat.id, 'Админ панель', reply_markup=admin_panel)
        bot.register_next_step_handler(message, admins)
    else:
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')


def parser(url, user_id, clas="caption product-info clearfix"):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        p = []
        j = 1
        for product in soup.find_all("div", class_=clas):
            name = product.find("h4").text
            price = product.find("div", class_="price").text.split('\n')[1].split(' р.')[0].split()
            if len(price) >= 2:
                prices = 0
                for i in range(len(price)):
                    prices += float(price[-(i+1)]) * 1000**i
            else:
                prices = price[0]
            count = product.find('div', class_="description").find_all('span', class_="dotted-line_right")[1].text
            p.append([name, int(float(prices)*1.1 * (1 - float(Users.get_percent(user_id, 0))/100)), count])
            if j % 10 == 0:
                products.append(p)
                p = []
            j += 1
        products.append(p)
        return products
    except Exception as e:
        print(e)
        products.append(p)
        return products

def access_order(i):
    if i == 0:
        return 'Открыт'
    elif i == 1:
        return 'Закрыт'
    elif i == 2:
        return 'Временно открыт'
    elif i == 3:
        return 'Временно закрыт'

shipping_options = [
    types.ShippingOption(id='instant', title='WorldWide Teleporter').add_price(types.LabeledPrice('Teleporter', 1000)),
    types.ShippingOption(id='pickup', title='Local pickup').add_price(types.LabeledPrice('Pickup', 300))]

@bot.message_handler(commands=['Buy', 'buy'])
def buy(message):
    price = [types.LabeledPrice(label='Оплата товара', amount=int(message.text.split()[1])*100)]
    bot.send_invoice(message.chat.id, title='Оплата товара',
                    description=f'Оплата товара, на сумму {message.text.split()[1]} руб.',
                    provider_token='410694247:TEST:1f04d098-3fc9-493f-acdf-dac468fe5edc',
                    invoice_payload="test-invoice-payload",
                    currency="rub",
                    prices=price)

@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!\nО, похоже, наши собачьи курьеры прямо сейчас обедают. Попробуйте еще раз позже!')

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
                                                " try to pay again in a few minutes, we need a small rest."
                                                "\nИнопланетяне пытались украсть CVV вашей карты, но мы успешно защитили ваши учетные данные, попробуйте оплатить еще раз через несколько минут, нам нужен небольшой отдых.")
@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id, 'Платёж на сумму `{} {}`, прошёл!'.format(message.successful_payment.total_amount / 100,
                                                                                 message.successful_payment.currency), parse_mode='Markdown')
    bot.send_message(adm_chat, f'Пользователь {message.chat.first_name} {message.chat.last_name} совершил платёж на `{message.successful_payment.total_amount / 100} {message.successful_payment.currency}`',
                     parse_mode='Markdown')

@bot.message_handler(commands=['Start', 'start'])
def start(message):
    if message.chat.username == None:
        bot.send_message(message.chat.id, 'Для использования бота добавьте username')
    elif not Users.user_exists(message.chat.id):
        Users.create_user(message.chat.id)
        splited = message.text.split()
        if len(splited) == 2:
            Users.increase_ref_count(splited[1], message.chat.id)
            Users.choose_ref_id(message.chat.id, splited[1])
            Users.get_percent(message.chat.id, 1)
    elif Users.get_agreement(message.chat.id, 0) == 0:
        bot.send_message(message.chat.id, 'Перед тем, как пользоваться ботом прочитайте правила: https://telegra.ph/Pravila-06-23-34', disable_web_page_preview=True, reply_markup=agree)
        bot.register_next_step_handler(message, agreement)
    else:
        Users.get_page(message.chat.id, 3)
        bot.send_message(message.chat.id, 'Добро пожаловать в бота в котором можно купить товары по оптовой цене', parse_mode='Html', reply_markup=menu)
        bot.send_message(message.chat.id, 'Подпишись на <a href="https://t.me/tovar_kitopt">канал</a>, чтобы быть в курсе всех обновленний и изменений', disable_web_page_preview=True, parse_mode='Html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Купить':
            if Users.get_access_orders(message.chat.id, 0) in [0, 2]:
                bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
                bot.register_next_step_handler(message, tovar_1)
            else:
                bot.send_message(message.chat.id, 'Вы в БАН-листе, вам нельзя заказывать товар.')
        elif message.text == 'Аккаунт':
            bot.send_message(message.chat.id, f'''Ваш аккаунт:
id: {message.chat.id}
Внутренний id: {Users.get_user(message.chat.id)}
Заказы: {Users.get_orders(message.chat.id, 0)}
Отменённые заказы: {Users.get_cancel_orders(message.chat.id, 0)}
Доступ к заказам: {access_order(Users.get_access_orders(message.chat.id, 0))}''')
        elif message.text == 'Реф. система':
            bot.send_message(message.chat.id, f'''Ваша реферальная ссылка: https://t.me/tovarOptomBot?start={message.chat.id}
Кол-во рефералов: {Users.get_ref_count(message.chat.id)}
Скидка: {Users.get_percent(message.chat.id, 0)}%''')
        elif message.text == 'О нас':
            bot.send_message(message.chat.id, f'''Мы купили и доставили {Users.get_orders(1633567239, 0)} заказов.
Мы работаем с помощью совместных оптовых закупках.

Админ: @ilnurKhalikov
По всем вопросам обращаться к нему.

Бот обновляется с 11:00 до 20:00 каждые три часа''')
        else:
            bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def tovar_1(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, text='Добро пожаловать в бота в котором можно купить товары по оптовой цене', parse_mode='Html', reply_markup=menu)
    elif message.text == 'СТЕКЛА, ЧЕХЛЫ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_1_0)
        bot.register_next_step_handler(message, subcategory_1_0_0)
    elif message.text == 'УМНЫЕ и СТИЛЬНЫЕ SMART-ЧАСЫ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_2)
        bot.register_next_step_handler(message, subcategory_2_0_0)
    # elif message.text == 'КАБЕЛИ, З/У, УДЛИНИТЕЛИ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'НОСИТЕЛИ ИНФОРМАЦИИ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    elif message.text == 'ЭЛЕМЕНТЫ ПИТАНИЯ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_4_0)
        bot.register_next_step_handler(message, subcategory_4_0_0)
    elif message.text == 'АКУСТИЧЕСКИЕ СИСТЕМЫ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_5_0)
        bot.register_next_step_handler(message, subcategory_5_0_0)
    # elif message.text == 'КОМПЬЮТЕРНЫЕ АКСЕССУАРЫ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'МОБИЛЬНЫЕ АКСЕCСУАРЫ И ИНСТРУМЕНТЫ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    elif message.text == 'Продукция Xiaomi':
        b = a[3][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    # elif message.text == 'ЭЛЕКТРОНИКА':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    elif message.text == 'АВТОАКСЕССУАРЫ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_6_0)
        bot.register_next_step_handler(message, subcategory_6_0_0)
    elif message.text == 'ФОНАРИ, НОЖИ, РАЦИИ, ТУРИЗМ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_3_0)
        bot.register_next_step_handler(message, subcategory_3_0_0)
    else:
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def subcategory_1_0_0(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'ЧЕХЛЫ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_1_1)
        bot.register_next_step_handler(message, subcategory_1_0_1)
    # elif message.text == 'ЗАЩИТНЫЕ СТЁКЛА':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    elif message.text == 'Кардхолдеры':
        b = a[0][21]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    # elif message.text == 'Ремешки, браслеты':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Чехлы для APods':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    elif message.text == 'Стилусы,прочее':
        b = a[0][22]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    else:
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def subcategory_1_0_1(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_1_0)
        bot.register_next_step_handler(message, subcategory_1_0_0)
    elif message.text == 'Чехлы для iP':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_1_1_1)
        bot.register_next_step_handler(message, subcategory_1_0_2)
    # elif message.text == 'Чехлы для Samsung':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Чехлы для XiaoMi':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Чехлы для Huawei':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Чехлы для Realme':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Чехлы для Tecno':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    elif message.text == 'Чехлы универсальные':
        b = a[0][23]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    else:
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def subcategory_1_0_2(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_1_1)
        bot.register_next_step_handler(message, subcategory_1_0_1)
    elif message.text == 'Чехлы для iP 11':
        b = a[0][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0)//6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14 Pro Max':
        b = a[0][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14 Max':
        b = a[0][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14 Pro':
        b = a[0][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14':
        b = a[0][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13 Pro Max':
        b = a[0][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13 Pro':
        b = a[0][6]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13':
        b = a[0][7]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13 Mini':
        b = a[0][8]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 12 Pro Max':
        b = a[0][9]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 12/12Pro':
        b = a[0][10]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 12 Mini':
        b = a[0][11]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 11 Pro Max':
        b = a[0][12]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 11 Pro':
        b = a[0][13]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP XR':
        b = a[0][14]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP X/XS':
        b = a[0][15]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP XS MAX':
        b = a[0][16]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 7/8 Plus':
        b = a[0][17]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 7/8/SE':
        b = a[0][18]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 6,6 Plus':
        b = a[0][19]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 5/SE':
        b = a[0][20]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_2_0_0(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'Smart Watch (фитнес браслеты) HOCO, BOROFONE, AWEI, XiaoMi':
        b = a[1][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Smart Watch (фитнес браслеты) ОРБИТА, КОПИИ':
        b = a[1][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Аксессуары для Smart Watch (фитнес браслетов)':
        b = a[1][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_3_0_0(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'Термосы':
        b = a[2][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'НОЖИ':
        bot.send_message(message.chat.id, 'Выбирите подкатегорию', reply_markup=subcategory_3_1)
        bot.register_next_step_handler(message, subcategory_3_0_1)
    elif message.text == 'Наборы для выживания':
        b = a[2][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ФОНАРИ':
        bot.send_message(message.chat.id, 'Выбирите подкатегорию', reply_markup=subcategory_3_2)
        bot.register_next_step_handler(message, subcategory_3_0_1)
    elif message.text == 'РАЦИИ':
        b = a[2][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'БИНОКЛИ':
        b = a[2][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_3_0_1(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_3_0)
        bot.register_next_step_handler(message, subcategory_3_0_0)
    elif message.text == 'МУЛЬТИ-НАБОРЫ':
        b = a[2][1][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'СКЛАДНЫЕ НОЖИ, В ЧЕХЛЕ':
        b = a[2][1][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ТРЕНИРОВОЧНЫЕ НОЖИ':
        b = a[2][1][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    #--------------------------------------------------------------------------
    elif message.text == 'РУЧНЫЕ светодиодные на батарейках':
        b = a[2][3][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Фонари для велосипедов':
        b = a[2][3][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'РУЧНЫЕ на аккумуляторе, фонарь-ШОКЕР':
        b = a[2][3][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'НАЛОБНЫЕ светодиодные на батарейках':
        b = a[2][3][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'НАЛОБНЫЕ светодиодные с АКБ':
        b = a[2][3][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'КЕМПИНГОВЫЕ светодиодные, УЛИЧНЫЕ, ОТ СОЛНЦА':
        b = a[2][3][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ФОНАРИ-БРЕЛКИ, ЛАЗЕРЫ':
        b = a[2][3][6]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_4_0_0(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'Мизинчиковые LR/R03 (ААА)':
        b = a[4][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Пальчиковые LR/R06 (АА)':
        b = a[4][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Таблетки SR/CR/LR/PR/AG':
        b = a[4][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Батарейки С (R14/LR14)':
        b = a[4][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Батарейки D (R20/LR20)':
        b = a[4][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Крона (6F22/6LR61)':
        b = a[4][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Для электронных устройств А23, А27, 28L, CR2, CR123, LR1/E90':
        b = a[4][6]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Квадрат 3R12':
        b = a[4][7]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'АККУМУЛЯТОРЫ 10440,14500,16340,18650':
        b = a[4][8]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Аккумуляторы R03/R06/6F22/HR20':
        b = a[4][9]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Зарядные устройства':
        b = a[4][10]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Аккумуляторы универсальные':
        b = a[4][11]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_5_0_0(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'КОЛОНКИ для Компьютера':
        b = a[5][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'НАУШНИКИ, ГАРНИТУРЫ':
        bot.send_message(message.chat.id, 'Выбирете подкатегорию', reply_markup=subcategory_5_1)
        bot.register_next_step_handler(message, subcategory_5_0_1)
    elif message.text == 'РАДИОПРИЁМНИКИ':
        b = a[5][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'МИКРОФОНЫ':
        bot.send_message(message.chat.id, 'Выбирете подкатегорию', reply_markup=subcategory_5_2)
        bot.register_next_step_handler(message, subcategory_5_0_1)
    elif message.text == 'ПОРТАТИВНЫЕ КОЛОНКИ BLUETOOTH':
        b = a[5][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'НАПОЛЬНЫЕ КОЛОНКИ BLUETOOTH':
        bot.send_message(message.chat.id, 'Выбирете подкатегорию', reply_markup=subcategory_5_3)
        bot.register_next_step_handler(message, subcategory_5_0_1)
    elif message.text == 'УСИЛИТЕЛИ ЗВУКА':
        b = a[5][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_5_0_1(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_5_0)
        bot.register_next_step_handler(message, subcategory_3_0_0)
    elif message.text == 'Вакуумные / Вкладыши':
        b = a[5][1][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Гарнитура / Наушники с аудио разъемом Lightning, Type-C (вакуумные / вкладыши)':
        b = a[5][1][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ГАРНИТУРЫ TWS PRO вакуумные':
        b = a[5][1][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ГАРНИТУРЫ TWS вкладыши':
        b = a[5][1][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Awei':
        b = a[5][1][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Гарнитуры MIX':
        b = a[5][1][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'HandsFree Bluetooth':
        b = a[5][1][6]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ПОЛНОРАЗМЕРНЫЕ НАУШНИКИ':
        b = a[5][1][7]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'СЛУХОВЫЕ АППАРАТЫ':
        b = a[5][1][8]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'АКСЕССУАРЫ ДЛЯ НАУШНИКОВ':
        b = a[5][1][9]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    #------------------------------------------------------------------------------------------
    elif message.text == 'Микрофоны для ПК/мобильных устройств':
        b = a[5][3][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Микрофоны караоке':
        b = a[5][3][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    #-------------------------------------------------------------------------------------------
    elif message.text == 'Стойки-штативы под колонки':
        b = a[5][5][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'KIMISO':
        b = a[5][5][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'FUMIKO, HOCO, BOROFONE':
        b = a[5][5][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'CRAZY BOX ELTRONIC':
        b = a[5][5][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Напольные колонки MIX':
        b = a[5][5][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ОРБИТА':
        b = a[5][5][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_6_0_0(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'РАДАР-ДЕТЕКТОРЫ':
        b = a[6][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ВИДЕО РЕГИСТРАТОРЫ':
        b = a[6][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'АВТОМАГНИТОЛЫ':
        b = a[6][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ДЕРЖАТЕЛИ':
        bot.send_message(message.chat.id, 'Выбирете подкатегорию', reply_markup=subcategory_6_1)
        bot.register_next_step_handler(message, subcategory_6_0_1)
    elif message.text == 'РАЗВЕТВИТЕЛИ ПРИКУРИВАТЕЛЯ':
        bot.send_message(message.chat.id, 'Выбирете подкатегорию', reply_markup=subcategory_6_2)
        bot.register_next_step_handler(message, subcategory_6_0_1)
    elif message.text == 'АВТОЗВУК':
        b = a[6][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'FM-МОДУЛЯТОРЫ':
        b = a[6][6]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ДВОРНИКИ':
        b = a[6][7]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'АВТОХИМИЯ':
        b = a[6][8]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'АВТОЭЛЕКТРОНИКА, КОМФОРТ':
        b = a[6][9]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ЧЕХЛЫ для БРЕЛКОВ СИГНАЛИЗАЦИИ':
        b = a[6][10]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'АРОМАТИЗАТОРЫ':
        b = a[6][11]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)

def subcategory_6_0_1(message):
    global b
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_5_0)
        bot.register_next_step_handler(message, subcategory_3_0_0)
    elif message.text == 'ДЕРЖАТЕЛИ С БЕСПРОВОДНОЙ ЗАРЯДКОЙ':
        b = a[6][3][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'МАГНИТНЫЕ ДЕРЖАТЕЛИ':
        b = a[6][3][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ДЕРЖАТЕЛИ на дефлектор, панель, стекло':
        b = a[6][3][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'ДЛЯ РЕГИСТРАТОРОВ И НАВИГАТОРОВ, ИНФОРМАЦИОННЫЕ В АВТО':
        b = a[6][3][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    #--------------------------------------------------------------------------------
    elif message.text == 'Разветвитель прикуривателя AVS, ОРБИТА':
        b = a[6][4][0]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Разветвитель прикуривателя OLESSON, DREAM':
        b = a[6][4][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)


def product(message):
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')
        Users.get_page(message.chat.id, 3)
    elif message.text == 'Следующая страница➡':
        Users.get_page(message.chat.id, 1)
        url = f'{b}?page={Users.get_page(message.chat.id, 0)//6 + 1}'
        msg = parser(url, message.chat.id)
        try:
            for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
                bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0)%6][i][0]}\n{msg[Users.get_page(message.chat.id, 0)%6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0)%6][i][2]}')
            bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
            bot.register_next_step_handler(message, product)
        except:
            bot.send_message(message.chat.id, 'Error: Такой страницы нету', reply_markup=page_2)
            bot.register_next_step_handler(message, product)
    elif message.text == '⬅Предыдущая страница':
        Users.get_page(message.chat.id, 2)
        url = f'{b}?page={Users.get_page(message.chat.id, 0)//6 + 1}'
        msg = parser(url, message.chat.id)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    else:
        bot.send_message(adm_chat, f'Username: @{message.chat.username}\nСкидка: {Users.get_percent(message.chat.id, 0)}%\nUrl: {b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}\nPage: {Users.get_page(message.chat.id, 0)%6}\n{message.text}')
        bot.send_message(message.chat.id, 'Я передам эти данные админу, и если они корректные, то он обязательно свяжется с вами\nОтменить выбор можно написав <a href="https://t.me/ilnurKhalikov">админу</a>', disable_web_page_preview=True, parse_mode="Html")
        Users.get_page(message.chat.id, 3)

def agreement(message):
    if not Users.user_exists(message.chat.id):
        Users.create_user(message.chat.id)
    if message.text == '✔ Подтвердить' or message.text == '#DurtuliTheBest':
        Users.get_agreement(message.chat.id, 1)
        bot.send_message(message.chat.id, text='Добро пожаловать в бота в котором можно купить товары по оптовой цене', parse_mode='Html', reply_markup=menu)
    else:
        bot.send_message(message.chat.id, 'Перед тем, как пользоваться ботом прочитайте правила: https://telegra.ph/Pravila-06-23-34',disable_web_page_preview=True, reply_markup=agree)
        bot.register_next_step_handler(message, agreement)



def admins(message):
    print(message)
    if message.text == 'Отправить сообщение по id':
        bot.send_message(message.chat.id, 'Введите сообщение и на другой строке id ч/з пробел(-ы)')
        bot.register_next_step_handler(message, admins_snd_msg)
    elif message.text == 'Сделать рассылку':
        bot.send_message(message.chat.id, 'Введите сообщение')
        bot.register_next_step_handler(message, admins_rassilka)
    elif message.text == '+1 заказ':
        bot.send_message(message.chat.id, 'Введите id ч/з пробел(-ы)')
        bot.register_next_step_handler(message, admins_order)
    elif message.text == '+1 отменённый заказ':
        bot.send_message(message.chat.id, 'Введите id ч/з пробел(-ы)')
        bot.register_next_step_handler(message, admins_cancel_order)
    elif message.text == 'Изменить доступ к заказам':
        bot.send_message(message.chat.id, 'Введите цифру доступа и с другое строки id ч/з пробел(-ы)')
        bot.send_message(message.chat.id, f'Цифры доступа:\n0 - {access_order(0)}\n1 - {access_order(1)}\n2 - {access_order(2)}\n3 - {access_order(3)}')
        bot.register_next_step_handler(message, admins_access_orders)
    elif message.text == 'Отправить платёж':
        bot.send_message(message.chat.id, 'Введите id и на другой строке сумму в рублях(ТОЛЬКО ЦИФРЫ)')
        bot.register_next_step_handler(message, admins_send_pay)

def admins_snd_msg(message):
    try:
        for id in message.text.split('\n')[1].split():
            bot.send_message(id, message.text.split('\n')[0])
        bot.send_message(message.chat.id, 'Сообщения отправлены!', reply_markup=menu)
    except:
        bot.send_message(message.chat.id, f'Такого юзера нет - {id}', reply_markup=menu)

def admins_rassilka(message):
    db = sqlite3.connect('user.db')
    sql = db.cursor()
    sql.execute("SELECT user_id FROM users")
    id = sql.fetchall()
    for id in id:
        for id in id:
            try:
                bot.send_message(id, f"{message.text}")
            except:
                bot.send_message(adm_chat, f'Пользователь {id} заблокал нашего бота')
    bot.send_message(adm, "Рассылка завершена", reply_markup=menu)
    db.commit()

def admins_order(message):
    try:
        for id in message.text.split():
            Users.get_orders(id, 1)
        bot.send_message(message.chat.id, 'Выполнено!', reply_markup=menu)
    except:
        bot.send_message(message.chat.id, f'Такого юзера нет - {id}', reply_markup=menu)

def admins_cancel_order(message):
    try:
        for id in message.text.split():
            Users.get_cancel_orders(id, 1)
        bot.send_message(message.chat.id, 'Выполнено!', reply_markup=menu)
    except:
        bot.send_message(message.chat.id, f'Такого юзера нет - {id}', reply_markup=menu)

def admins_access_orders(message):
    try:
        for id in message.text.split('\n')[1].split():
            Users.get_access_orders(id, 1, int(message.text.split('\n')[0]))
        bot.send_message(message.chat.id, 'Выполнено!', reply_markup=menu)
    except:
        bot.send_message(message.chat.id, f'Такого юзера нет - {id}', reply_markup=menu)

def admins_send_pay(message):
    try:
        price = [types.LabeledPrice(label='Оплата товара', amount=int(message.text.split('\n')[1]) * 100)]
        bot.send_invoice(int(message.text.split('\n')[0]), title='Оплата товара',
                         description='Оплата товара, на сумму ' + message.text.split("\n")[1] + ' руб.',
                         provider_token='410694247:TEST:1f04d098-3fc9-493f-acdf-dac468fe5edc',
                         invoice_payload="test-invoice-payload",
                         currency="rub",
                         prices=price)
        bot.send_message(int(message.text.split('\n')[0]), 'Надо оплатить товар на сумму: ' + message.text.split("\n")[1] +' руб.')
        bot.send_message(message.chat.id, 'Платёж отправлен!', reply_markup=menu)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Такого юзера нет', reply_markup=menu)

while True:
    # try:
        bot.polling()
    # except Exception as e:
    #     print(f'Error: {e}')
