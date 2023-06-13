import requests
# from parser import *
from models import *
from keyboard import *
from bs4 import BeautifulSoup
from telebot import TeleBot, types

bot = TeleBot('6014555057:AAHwPHa9kYDoD4iZfgdIvOH__0SoQ_a0HI0')
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
'https://kitopt02.ru/stek-cehl/79379/21589/89770/'],
['https://kitopt02.ru/88543/26015/',
'https://kitopt02.ru/88543/26017/',
'https://kitopt02.ru/88543/27475/']]


def parser(url, clas="caption product-info clearfix"):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        products = []
        p = []
        i = 1
        for product in soup.find_all("div", class_=clas):
            name = product.find("h4").text
            price = product.find("div", class_="price").text.split('\n')[1].split(' р.')[0].split()
            print(price)
            if len(price) >= 2:
                prices = 0
                for i in range(len(price)):
                    print(i)
                    prices += float(price[-(i+1)]) * 1000**i
            else:
                prices = price[0]
            count = product.find('div', class_="description").find_all('span', class_="dotted-line_right")[1].text
            p.append([name, int(float(prices)*1.1), count])
            if i % 10 == 0:
                products.append(p)
                p = []
            i += 1
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
    elif Users.get_agreement(message.chat.id, 0) == 0:
        bot.send_message(message.chat.id, 'Перед тем, как пользоваться ботом прочитайте правила: https://telegra.ph/Pravila-05-13-29', disable_web_page_preview=True, reply_markup=agree)
        bot.register_next_step_handler(message, agreement)
    else:
        bot.send_message(message.chat.id, text='Добро пожаловать в бота в котором можно купить товары по оптовой цене', parse_mode='Html', reply_markup=menu)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Купить':
            bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
            bot.register_next_step_handler(message, tovar_1)
        elif message.text == 'Аккаунт':
            bot.send_message(message.chat.id, f'''Ваш аккаунт:
id: {message.chat.id}
Внутренний id: {Users.get_user(message.chat.id)}
Заказы: {Users.get_orders(message.chat.id, 0)}
Отменённые заказы: {Users.get_cancel_orders(message.chat.id, 0)}
Доступ к заказам: {access_order(Users.get_access_orders(message.chat.id, 0))}''')
        elif message.text == 'Реф. система':
            if Users.get_ref_count(message.chat.id) > 90:
                a = 9
            else:
                a = Users.get_ref_count(message.chat.id) / 10
            bot.send_message(message.chat.id, f'''Ваша реферальная ссылка: https://t.me/tovarOptomBot?start={message.chat.id}
Кол-во рефералов: {Users.get_ref_count(message.chat.id)}
Скидка: {a}%''')
        elif message.text == 'О нас':
            bot.send_message(message.chat.id, f'''Мы купили и доставили {Users.get_orders(1633567239, 0)} заказов.
Мы работаем с помощью совместных оптовых закупках.
Админ: @ilnurKhalikov
По всем вопросам обращаться к нему.''')
        else:
            bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def tovar_1(message):
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
    # elif message.text == 'ЭЛЕМЕНТЫ ПИТАНИЯ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'АКУСТИЧЕСКИЕ СИСТЕМЫ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'КОМПЬЮТЕРНЫЕ АКСЕССУАРЫ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'МОБИЛЬНЫЕ АКСЕCСУАРЫ И ИНСТРУМЕНТЫ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Продукция Xiaomi':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'ЭЛЕКТРОНИКА':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'АВТОАКСЕССУАРЫ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'ФОНАРИ, НОЖИ, РАЦИИ, ТУРИЗМ':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    else:
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def subcategory_1_0_0(message):
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=category)
        bot.register_next_step_handler(message, tovar_1)
    elif message.text == 'ЧЕХЛЫ':
        bot.send_message(message.chat.id, 'Выберите подкатегорию', reply_markup=subcategory_1_1)
        bot.register_next_step_handler(message, subcategory_1_0_1)
    # elif message.text == 'ЗАЩИТНЫЕ СТЁКЛА':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Кардхолдеры':
    #     bot.send_message(message.chat.id, 'Выберите товар')
    # elif message.text == 'Ремешки, браслеты':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Чехлы для APods':
    #     bot.send_message(message.chat.id, 'Выберите подкатегорию')
    # elif message.text == 'Стилусы,прочее':
    #     bot.send_message(message.chat.id, 'Выберите товар')
    else:
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')

def subcategory_1_0_1(message):
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
    # elif message.text == 'Чехлы универсальные':
    #     bot.send_message(message.chat.id, 'Выберите товар')
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
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14 Pro Max':
        b = a[0][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14 Max':
        b = a[0][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14 Pro':
        b = a[0][3]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 14':
        b = a[0][4]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13 Pro Max':
        b = a[0][5]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13 Pro':
        b = a[0][6]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13':
        b = a[0][7]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 13 Mini':
        b = a[0][8]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 12 Pro Max':
        b = a[0][9]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 12/12Pro':
        b = a[0][10]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 12 Mini':
        b = a[0][11]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 11 Pro Max':
        b = a[0][12]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 11 Pro':
        b = a[0][13]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP XR':
        b = a[0][14]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP X/XS':
        b = a[0][15]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP XS MAX':
        b = a[0][16]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 7/8 Plus':
        b = a[0][17]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 7/8/SE':
        b = a[0][18]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 6,6 Plus':
        b = a[0][19]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id,
                             f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                         reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Чехлы для iP 5/SE':
        b = a[0][20]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
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
        msg = parser(url)
        if msg == []:
            bot.send_message(adm, 'YES')
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Smart Watch (фитнес браслеты) ОРБИТА, КОПИИ':
        b = a[1][1]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)
    elif message.text == 'Аксессуары для Smart Watch (фитнес браслетов)':
        b = a[1][2]
        url = f'{b}?page={Users.get_page(message.chat.id, 0) // 6 + 1}'
        msg = parser(url)
        for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
            bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
        bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
        bot.register_next_step_handler(message, product)


def product(message):
    if message.text == '⬅ Назад':
        bot.send_message(message.chat.id, 'Error: начните заново(/start)')
        Users.get_page(message.chat.id, 3)
    elif message.text == 'Следующая страница➡':
        Users.get_page(message.chat.id, 1)
        url = f'{b}?page={Users.get_page(message.chat.id, 0)//6 + 1}'
        msg = parser(url)
        if msg == []:
            bot.send_message(message.chat.id, 'Error: Такой страницы нету', reply_markup=page_2)
            bot.register_next_step_handler(message, product)
        else:
            for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
                bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0)%6][i][0]}\n{msg[Users.get_page(message.chat.id, 0)%6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0)%6][i][2]}')
            bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):',
                             reply_markup=page_1)
            bot.register_next_step_handler(message, product)
    elif message.text == '⬅Предыдущая страница':
        Users.get_page(message.chat.id, 2)
        url = f'{b}?page={Users.get_page(message.chat.id, 0)//6 + 1}'
        msg = parser(url)
        if msg == []:
            bot.send_message(message.chat.id, 'Error: Такой страницы нету', reply_markup=page_2)
            bot.register_next_step_handler(message, product)
        else:
            for i in range(len(msg[Users.get_page(message.chat.id, 0) % 6])):
                bot.send_message(message.chat.id, f'{i + 1}.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][0]}\n{msg[Users.get_page(message.chat.id, 0) % 6][i][1]} руб.\n{msg[Users.get_page(message.chat.id, 0) % 6][i][2]}')
            bot.send_message(message.chat.id, 'Выберите товар(введите номер товара и кол-во, которое хотите приобрести):', reply_markup=page_1)
            bot.register_next_step_handler(message, product)
    else:
        bot.send_message(adm_chat, f'Username: {message.chat.username}\nUrl: {b}\nPage: {Users.get_page(message.chat.id, 0)}\n{message.text}')
        bot.send_message(message.chat.id, 'Я передам эти данные админу, и если они корректные, то он обязательно свяжется с вами')
        Users.get_page(message.chat.id, 3)

def agreement(message):
    if not Users.user_exists(message.chat.id):
        Users.create_user(message.chat.id)
    if message.text == '✔ Подтвердить':
        Users.get_agreement(message.chat.id, 1)
        bot.send_message(message.chat.id, text='Добро пожаловать в бота в котором можно купить товары по оптовой цене', parse_mode='Html', reply_markup=menu)
    else:
        bot.send_message(message.chat.id, 'Перед тем, как пользоваться ботом прочитайте правила: https://telegra.ph/Pravila-05-13-29',disable_web_page_preview=True, reply_markup=agree)
        bot.register_next_step_handler(message, agreement)

bot.polling()