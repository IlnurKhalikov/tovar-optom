# Импортируем библиотеки
from peewee import *
from datetime import datetime

now = datetime.now()  # Работа с временем

db = SqliteDatabase(
    'user.db')  # Указываем с какой базой данных будем работать. Она обязательно должна быть в той папке в которой находится этот файл


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True, default=0)
    ref = IntegerField(default=0)
    ref_id = IntegerField(default=0)
    agreement = IntegerField(default=0)
    orders = IntegerField(default=0)
    cancel_orders = IntegerField(default=0)
    access_orders = IntegerField(default=0)
    last_msg_sec = IntegerField(default=0)
    last_msg_min = IntegerField(default=0)
    page = IntegerField(default=0)

    # Получение данных user-а
    @classmethod
    def get_user(cls, user_id):
        return cls.get(Users.user_id == user_id)

    # Получение кол-ва рефералов
    @classmethod
    def get_ref_count(cls, user_id):
        return cls.get(Users.user_id == user_id).ref

    #
    @classmethod
    def get_ref_id(cls, user_id):
        return cls.get(Users.user_id == user_id).ref_id

    @classmethod
    def get_agreement(cls, user_id, i):
        if i == 1:
            agree = cls.get_user(user_id)
            agree.agreement = 1
            agree.save()
        else:
            return cls.get(Users.user_id == user_id).agreement

    @classmethod
    def get_orders(cls, user_id, i):
        if i == 1:
            ord = cls.get_user(user_id)
            ord.orders += 1
            ord.save()
        else:
            return cls.get(Users.user_id == user_id).orders

    @classmethod
    def get_cancel_orders(cls, user_id, i):
        if i == 1:
            ord = cls.get_user(user_id)
            ord.cancel_orders += 1
            ord.save()
        else:
            return cls.get(Users.user_id == user_id).cancel_orders

    @classmethod
    def get_access_orders(cls, user_id, i):
        if i == 1:
            ord = cls.get_user(user_id)
            ord.access_orders += 1
            ord.save()
        else:
            return cls.get(Users.user_id == user_id).access_orders

    @classmethod
    def get_last_msg_time(cls, user_id, i, sec_or_min):
        if i == 1:
            return cls.get(Users.user_id == user_id).last_msg_sec
        elif i == 2:
            return cls.get(Users.user_id == user_id).last_msg_min
        elif i == 3:
            sec = cls.get_user(user_id)
            sec.last_msg_sec = sec_or_min
            sec.save()
        elif i == 4:
            min = cls.get_user(user_id)
            min.last_msg_min = sec_or_min
            min.save()

    #
    @classmethod
    def increase_ref_count(cls, user_id, ref_id):
        user = cls.get_user(user_id)
        user.ref += 1
        user.save()
        c = cls.get_user(ref_id)
        c.ref_id = user_id
        c.save()

    @classmethod
    def choose_ref_id(cls, user_id, id):
        l = cls.get_user(user_id)
        l.ref_id = id
        l.save()

    @classmethod
    def get_page(cls, user_id, i):
        if i == 1:
            ord = cls.get_user(user_id)
            ord.page += 1
            ord.save()
        elif i == 2:
            ord = cls.get_user(user_id)
            if ord.page >= 1:
                ord.page -= 1
            ord.save()
        elif i == 3:
            ord = cls.get_user(user_id)
            ord.page = 0
            ord.save()
        else:
            return cls.get(Users.user_id == user_id).page

    #
    @classmethod
    def user_exists(cls, user_id):
        try:
            query = cls().select().where(cls.user_id == user_id)
            return query.exists()
        except:
            return False

    #
    @classmethod
    def create_user(cls, user_id):
        user, created = cls.get_or_create(user_id=user_id)



#-----------------------------------------------------------------------------------------------------------------------



db = SqliteDatabase('product.db')  # Указываем с какой базой данных будем работать. Она обязательно должна быть в той папке в которой находится этот файл


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = TextField(unique=True, default='')
    price = IntegerField(default=0)

    @classmethod
    def get_product(cls, name):
        return cls.get(Product.name == name)

    @classmethod
    def get_name(cls, name, new_name, i):
        if i == 1:
            agree = cls.get_product(name)
            agree.name = new_name
            agree.save()
        else:
            return cls.get_product(name).name

    @classmethod
    def get_price(cls, name, new_price, i):
        if i == 1:
            agree = cls.get_product(name)
            agree.price = new_price
            agree.save()
        else:
            return cls.get_product(name).price

    #
    @classmethod
    def user_exists(cls, user_id):
        try:
            query = cls().select().where(cls.user_id == user_id)
            return query.exists()
        except:
            return False

    #
    @classmethod
    def create_product(cls, name):
        user, created = cls.get_or_create(name=name)

    @classmethod
    def delete_user(cls, names):
        q = Product.delete().where(Product.name == names)
        q.execute()
