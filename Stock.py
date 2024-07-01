from tkinter import *
from tkinter import ttk
import io
import sys


class Outlets:
    def __init__(self, number):
        self.storage = []
        self.number = number
        self.money_lost_from_order = 0

    def day_outlets(self):
        quantity_1_product = 0
        quantity_2_product = 0
        quantity_3_product = 0
        quantity_4_product = 0
        quantity_5_product = 0
        quantity_6_product = 0
        quantity_7_product = 0
        quantity_8_product = 0
        quantity_9_product = 0
        quantity_10_product = 0
        quantity_11_product = 0
        quantity_12_product = 0
        quantity_13_product = 0

        for wholesale in self.storage:
            if wholesale.type_product == 1:
                quantity_1_product += 1
            if wholesale.type_product == 2:
                quantity_2_product += 1
            if wholesale.type_product == 3:
                quantity_3_product += 1
            if wholesale.type_product == 4:
                quantity_4_product += 1
            if wholesale.type_product == 5:
                quantity_5_product += 1
            if wholesale.type_product == 6:
                quantity_6_product += 1
            if wholesale.type_product == 7:
                quantity_7_product += 1
            if wholesale.type_product == 8:
                quantity_8_product += 1
            if wholesale.type_product == 9:
                quantity_9_product += 1
            if wholesale.type_product == 10:
                quantity_10_product += 1
            if wholesale.type_product == 11:
                quantity_11_product += 1
            if wholesale.type_product == 12:
                quantity_12_product += 1
            if wholesale.type_product == 13:
                quantity_13_product += 1

        if quantity_1_product > 4:
            print('{} упакововок риса'.format(
                quantity_1_product
            ))
        else:
            print('{} упаковки риса'.format(
                quantity_1_product
            ))
        print()

        if quantity_2_product > 4:
            print('{} упакововок гречки'.format(
                quantity_2_product
            ))
        else:
            print('{} упакововки гречки'.format(
                quantity_2_product
            ))
        print()

        if quantity_3_product > 4:
            print('{} упакововок перловки'.format(
                quantity_3_product
            ))
        else:
            print('{} упаковки перловки'.format(
                quantity_3_product
            ))
        print()

        if quantity_4_product > 4:
            print('{} упакововок пшенки'.format(
                quantity_4_product
            ))
        else:
            print('{} упаковки пшенки'.format(
                quantity_4_product
            ))
        print()

        if quantity_5_product > 4:
            print('{} упакововок спагетти'.format(
                quantity_5_product
            ))
        else:
            print('{} упаковки спагетти'.format(
                quantity_5_product
            ))
        print()

        if quantity_6_product > 4:
            print('{} упакововок овсянки'.format(
                quantity_6_product
            ))
        else:
            print('{} упаковки овсянки'.format(
                quantity_6_product
            ))
        print()

        if quantity_7_product > 4:
            print('{} упакововок вафель'.format(
                quantity_7_product
            ))
        else:
            print('{} упаковки вафель'.format(
                quantity_7_product
            ))
        print()

        if quantity_8_product > 4:
            print('{} упакововок пряников'.format(
                quantity_8_product
            ))
        else:
            print('{} упаковки пряников'.format(
                quantity_8_product
            ))
        print()

        if quantity_9_product > 4:
            print('{} упакововок кукурузных палочек'.format(
                quantity_9_product
            ))
        else:
            print('{} упаковки кукурузныз палочек'.format(
                quantity_9_product
            ))
        print()

        if quantity_10_product > 4:
            print('{} упакововок майонеза'.format(
                quantity_10_product
            ))
        else:
            print('{} упаковки майонеза'.format(
                quantity_10_product
            ))
        print()

        if quantity_11_product > 4:
            print('{} упакововок сока'.format(
                quantity_11_product
            ))
        else:
            print('{} упаковки сока'.format(
                quantity_11_product
            ))
        print()

        if quantity_12_product > 4:
            print('{} упакововок печенья'.format(
                quantity_12_product
            ))
        else:
            print('{} упаковки печенья'.format(
                quantity_12_product
            ))
        print()

        if quantity_13_product > 4:
            print('{} упакововок газировки'.format(
                quantity_13_product
            ))
        else:
            print('{} упаковки газировки'.format(
                quantity_13_product
            ))
        print()

    def add_products_wholesale(self, product_wholesale):
        self.storage.append(product_wholesale)

    def order_to_stock(self, quantity, type_product):
        for i in range(quantity):
            wholesale = Wholesale_pack()
            for j in range(20):
                if type_product == 1:
                    wholesale.add_products((Product(15, 'Рис', 100)))
                    self.money_lost_from_order += 100
                if type_product == 2:
                    wholesale.add_products((Product(15, 'Гречка', 80)))
                    self.money_lost_from_order += 80
                if type_product == 3:
                    wholesale.add_products((Product(15, 'Перловка', 70)))
                    self.money_lost_from_order += 70
                if type_product == 4:
                    wholesale.add_products((Product(15, 'Пшенка', 110)))
                    self.money_lost_from_order += 110
                if type_product == 5:
                    wholesale.add_products((Product(15, 'Спагетти', 200)))
                    self.money_lost_from_order += 200
                if type_product == 6:
                    wholesale.add_products((Product(15, 'Овсянка', 89)))
                    self.money_lost_from_order += 89
                if type_product == 7:
                    wholesale.add_products((Product(15, 'Вафли', 65)))
                    self.money_lost_from_order += 65
                if type_product == 8:
                    wholesale.add_products((Product(15, 'Пряники', 77)))
                    self.money_lost_from_order += 77
                if type_product == 9:
                    wholesale.add_products((Product(15, 'Кукурузные палочки', 78)))
                    self.money_lost_from_order += 78
                if type_product == 10:
                    wholesale.add_products((Product(15, 'Майонез', 89)))
                    self.money_lost_from_order += 89
                if type_product == 11:
                    wholesale.add_products((Product(15, 'Сок', 89)))
                    self.money_lost_from_order += 89
                if type_product == 12:
                    wholesale.add_products((Product(15, 'Печенье', 55)))
                    self.money_lost_from_order += 55
                if type_product == 13:
                    wholesale.add_products((Product(15, 'Газировка', 78)))
                    self.money_lost_from_order += 78
            wholesale.type_product = type_product
            self.storage.append(wholesale)

    def get_money_lost_from_order(self):
        return self.money_lost_from_order


class Product:
    def __init__(self, best_date, name, cost):
        self.name = name
        self.best_date = best_date
        self.cost = cost
        self.quantity = 0

    def decrease_best_date(self):
        self.best_date -= 1

    def get_cost(self):
        return self.cost

    def get_best_date(self):
        return self.best_date

    def check_best_date(self):
        if self.best_date == 0:
            return True
        else:
            return self.best_date


class Wholesale_pack:
    def __init__(self):
        self.pack = []
        self.type_product = 0  # 1 - рис, 2 - гречка, 3 - перловка, 4 - пшенка, 5 - спагетти, 6 - Овсянка, 7 - Вафли, 8 - Пряники, 9 - Кукурузные палочки, 10 - Майонез, 11 - Сок, 12 - Печенье, 13 - Газировка

    def get_pack(self):
        return self.pack

    def type_product(self):
        return self.type_product

    def add_products(self, products):
        self.pack.append(products)


class Stock:
    def __init__(self):
        self.pack_wholesale = []
        self.number_wholesale = 0
        self.quantity_product_decrease_best_date = 0
        self.order_losses = 0
        self.expired_packaging = 0

    def get_pack_wholesale(self):
        return self.pack_wholesale

    def day_stock(self):
        quantity_type_1_product = 0
        quantity_type_2_product = 0
        quantity_type_3_product = 0
        quantity_type_4_product = 0
        quantity_type_5_product = 0
        quantity_type_6_product = 0
        quantity_type_7_product = 0
        quantity_type_8_product = 0
        quantity_type_9_product = 0
        quantity_type_10_product = 0
        quantity_type_11_product = 0
        quantity_type_12_product = 0
        quantity_type_13_product = 0

        self.quantity_product_decrease_best_date = 0

        start_day_wholesale = len(self.pack_wholesale)

        for wholesale in self.pack_wholesale[:]:
            for product in wholesale.get_pack()[:]:
                product.decrease_best_date()
                if product.get_best_date() <= 2:
                    product.cost *= 0.7
                    self.quantity_product_decrease_best_date += 1
                if product.get_best_date() == 0:
                    wholesale.get_pack().remove(product)

            if len(wholesale.get_pack()) <= 0:
                self.pack_wholesale.remove(wholesale)

            if wholesale.type_product == 1:
                quantity_type_1_product += 1
            if wholesale.type_product == 2:
                quantity_type_2_product += 1
            if wholesale.type_product == 3:
                quantity_type_3_product += 1
            if wholesale.type_product == 4:
                quantity_type_4_product += 1
            if wholesale.type_product == 5:
                quantity_type_5_product += 1
            if wholesale.type_product == 6:
                quantity_type_6_product += 1
            if wholesale.type_product == 7:
                quantity_type_7_product += 1
            if wholesale.type_product == 8:
                quantity_type_8_product += 1
            if wholesale.type_product == 9:
                quantity_type_9_product += 1
            if wholesale.type_product == 10:
                quantity_type_10_product += 1
            if wholesale.type_product == 11:
                quantity_type_11_product += 1
            if wholesale.type_product == 12:
                quantity_type_12_product += 1
            if wholesale.type_product == 13:
                quantity_type_13_product += 1

        end_wholesale = len(self.pack_wholesale)

        self.expired_packaging = start_day_wholesale - end_wholesale

        if quantity_type_1_product > 4:
            print('{} упакововок риса'.format(
               quantity_type_1_product
            ))
        else:
            print('{} упаковки риса'.format(
                quantity_type_1_product
            ))
        print()

        if quantity_type_2_product > 4:
            print('{} упакововок гречки'.format(
                quantity_type_2_product
            ))
        else:
            print('{} упакововки гречки'.format(
                quantity_type_2_product
            ))
        print()

        if quantity_type_3_product > 4:
            print('{} упакововок перловки'.format(
                quantity_type_3_product
            ))
        else:
            print('{} упаковки перловки'.format(
                quantity_type_3_product
            ))
        print()

        if quantity_type_4_product > 4:
            print('{} упакововок пшенки'.format(
                quantity_type_4_product
            ))
        else:
            print('{} упаковки пшенки'.format(
                quantity_type_4_product
            ))
        print()

        if quantity_type_5_product > 4:
            print('{} упакововок спагетти'.format(
                quantity_type_5_product
            ))
        else:
            print('{} упаковки спагетти'.format(
                quantity_type_5_product
            ))
        print()

        if quantity_type_6_product > 4:
            print('{} упакововок овсянки'.format(
                quantity_type_6_product
            ))
        else:
            print('{} упаковки овсянки'.format(
                quantity_type_6_product
            ))
        print()

        if quantity_type_7_product > 4:
            print('{} упакововок вафель'.format(
                quantity_type_7_product
            ))
        else:
            print('{} упаковки вафель'.format(
                quantity_type_7_product
            ))
        print()

        if quantity_type_8_product > 4:
            print('{} упакововок пряников'.format(
                quantity_type_8_product
            ))
        else:
            print('{} упаковки пряников'.format(
                quantity_type_8_product
            ))
        print()

        if quantity_type_9_product > 4:
            print('{} упакововок кукурузных палочек'.format(
                quantity_type_9_product
            ))
        else:
            print('{} упаковки кукурузныз палочек'.format(
                quantity_type_9_product
            ))
        print()

        if quantity_type_10_product > 4:
            print('{} упакововок майонеза'.format(
                quantity_type_10_product
            ))
        else:
            print('{} упаковки майонеза'.format(
                quantity_type_10_product
            ))
        print()

        if quantity_type_11_product > 4:
            print('{} упакововок сока'.format(
                quantity_type_11_product
            ))
        else:
            print('{} упаковки сока'.format(
                quantity_type_11_product
            ))
        print()

        if quantity_type_12_product > 4:
            print('{} упакововок печенья'.format(
                quantity_type_12_product
            ))
        else:
            print('{} упаковки печенья'.format(
                quantity_type_12_product
            ))
        print()

        if quantity_type_13_product > 4:
            print('{} упакововок газировки'.format(
                quantity_type_13_product
            ))
        else:
            print('{} упаковки газировки'.format(
                quantity_type_13_product
            ))
        print('============================')

    def stock_order(self, quantity, type_product):
        for i in range(quantity):
            wholesale = Wholesale_pack()
            for j in range(20):
                if type_product == 1:
                    wholesale.add_products((Product(15, 'Рис', 100)))
                    self.order_losses += 100
                if type_product == 2:
                    wholesale.add_products((Product(15, 'Гречка', 80)))
                    self.order_losses += 80
                if type_product == 3:
                    wholesale.add_products((Product(15, 'Перловка', 70)))
                    self.order_losses += 70
                if type_product == 4:
                    wholesale.add_products((Product(15, 'Пшенка', 110)))
                    self.order_losses += 110
                if type_product == 5:
                    wholesale.add_products((Product(15, 'Спагетти', 200)))
                    self.order_losses += 200
                if type_product == 6:
                    wholesale.add_products((Product(15, 'Овсянка', 89)))
                    self.order_losses += 89
                if type_product == 7:
                    wholesale.add_products((Product(15, 'Вафли', 65)))
                    self.order_losses += 65
                if type_product == 8:
                    wholesale.add_products((Product(15, 'Пряники', 77)))
                    self.order_losses += 77
                if type_product == 9:
                    wholesale.add_products((Product(15, 'Кукурузные палочки', 78)))
                    self.order_losses += 78
                if type_product == 10:
                    wholesale.add_products((Product(15, 'Майонез', 89)))
                    self.order_losses += 89
                if type_product == 11:
                    wholesale.add_products((Product(15, 'Сок', 89)))
                    self.order_losses += 89
                if type_product == 12:
                    wholesale.add_products((Product(15, 'Печенье', 55)))
                    self.order_losses += 55
                if type_product == 13:
                    wholesale.add_products((Product(15, 'Газировка', 78)))
                    self.order_losses += 78
            wholesale.type_product = type_product
            self.pack_wholesale.append(wholesale)

    def remove_wholesale(self, quantity, type_product):
        for i in range(quantity):
            for wholesale in self.pack_wholesale[:]:
                if wholesale.type_product == type_product:
                    self.pack_wholesale.remove(wholesale)
                    break

    def check_quantity(self, type_product_check):
        quantity_product = 0
        for wholesale in self.pack_wholesale:
            if wholesale.type_product == int(type_product_check):
                quantity_product += 1
        quantity_product_order = 40 - quantity_product
        return quantity_product_order

    def get_order_losses(self):
        return self.order_losses

    def get_quantity_product_decrease_best_date(self):
        return self.quantity_product_decrease_best_date // 20

    def get_expired_packaging(self):
        return self.expired_packaging


def stock_profit_per_day(stock_losses, outlets_1_losses, outlets_2_losses):
    summ_outlets_losses = outlets_1_losses + outlets_2_losses
    stock_profit = summ_outlets_losses - stock_losses

    print('Количество уценненных упаковок: {}'.format(
        stock.get_quantity_product_decrease_best_date()))
    print('Количество простроченных упаковок: {}'.format(
        stock.get_expired_packaging()
    ))

    if stock_profit > 0:
        print('Прибыль: {}'.format(stock_profit))
    elif stock_profit == 0:
        print('Склад работал в ноль')
    else:
        print('Убыток: {}'.format(stock_profit))
    return True


stock = Stock()
outlets_1 = Outlets(1)
outlets_2 = Outlets(2)



for i in range(13):
    stock.stock_order(10, i+1)

for i in range(13):
    outlets_1.order_to_stock(10, i+1)

for i in range(13):
    outlets_2.order_to_stock(10, i+1)


root = Tk()

root.title('Склад')
root.geometry('600x700')

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

stock_main = ttk.Frame(notebook)
sm_1 = ttk.Frame(notebook)
sm_2 = ttk.Frame(notebook)

stock_main.pack(expand=True, fill=BOTH)
sm_1.pack(expand=True, fill=BOTH)
sm_2.pack(expand=True, fill=BOTH)

notebook.add(stock_main, text='Склад')
notebook.add(sm_1, text='ТТ1')
notebook.add(sm_2, text='TT2')

################################### Скалд
main_stock_cont = ttk.Frame(stock_main)
main_stock_cont.pack(fill=BOTH, side=TOP, expand=True)

stock_1 = ttk.Frame(main_stock_cont, borderwidth=1, relief=SOLID)
stock_2 = ttk.Frame(main_stock_cont, borderwidth=1, relief=SOLID)

stock_2.pack(side="right", fill="both", expand=True)
stock_1.pack(side="left", fill="both", expand=True)

title_stock = ttk.Label(stock_1, text='В наличии на складе', font=20)
title_stock.pack(anchor=CENTER)

text_area_stock = Text(stock_1, wrap='word', width=1)
text_area_stock.pack(expand=True, fill=BOTH)

captured_output = io.StringIO()
sys.stdout = captured_output
stock.day_stock()
output = captured_output.getvalue()
captured_output.close()
text_area_stock.insert(END, output)
captured_output = io.StringIO()
sys.stdout = captured_output
stock_profit_per_day(stock.get_order_losses(), outlets_1.get_money_lost_from_order(), outlets_1.get_money_lost_from_order())
output = captured_output.getvalue()
captured_output.close()
text_area_stock.insert(END, output)


class Product_input:
    def __init__(self):
        self.type_product = 0
        self.quantity_entry = 0

    def is_valid(self, newval):
        if newval == '':
            return True
        try:
            result = int(newval) <= stock.check_quantity(self.type_product)
        except ValueError:
            result = False
        if not result:
            self.errmsg.set('Не хватает места')
        else:
            self.errmsg.set('')
        return result

    def create_stock_2(self, container, row, text, type_product):
        self.errmsg = StringVar()
        check = (root.register(self.is_valid), '%P')
        self.type_product = type_product
        label_name_pruduct = ttk.Label(container, text=text, font=20)
        label_name_pruduct.grid(row=row, column=0, sticky=W)

        self.order_quantity = ttk.Entry(container)
        self.order_quantity.grid(row=row, column=1, sticky=E, padx=4)
        self.order_quantity.config(validate='key', validatecommand=check)

        error_label = ttk.Label(container, textvariable=self.errmsg, foreground='red')
        error_label.grid(row=row + 1, column=1, sticky=E, padx=20)
        return self

    def get_type_product(self):
        return self.type_product

    def get_quantity_entry(self):
        quantity = self.order_quantity.get()
        if quantity == '':
            quantity = 0
            return quantity
        else:
            return int(quantity)


def next_day():
    #Склад
    text_area_stock.delete(0.1, END)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    stock.day_stock()
    output = captured_output.getvalue()
    captured_output.close()
    text_area_stock.insert(END, output)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    stock_profit_per_day(stock.get_order_losses(), outlets_1.get_money_lost_from_order(), outlets_1.get_money_lost_from_order())
    output = captured_output.getvalue()
    captured_output.close()
    text_area_stock.insert(END, output)
    # ТТ1
    text_area_sm_1.delete(0.1, END)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    Outlets(1).day_outlets()
    output = captured_output.getvalue()
    text_area_sm_1.delete(0.1, END)
    captured_output.close()
    text_area_sm_1.insert(END, output)
    # ТТ2
    text_area_sm_2.delete(0.1, END)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    Outlets(2).day_outlets()
    output = captured_output.getvalue()
    text_area_sm_2.delete(0.1, END)
    captured_output.close()
    text_area_sm_2.insert(END, output)


title_stock_order = ttk.Label(stock_2, text='Заказ', font=50)
title_stock_order.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=5)

stock_2.columnconfigure(1, weight=1)

list_entry_input = [Product_input().create_stock_2(stock_2, 1, 'Рис', 1),
                    Product_input().create_stock_2(stock_2, 3, 'Гречка', 2),
                    Product_input().create_stock_2(stock_2, 5, 'Перловка', 3),
                    Product_input().create_stock_2(stock_2, 7, 'Пшенка', 4),
                    Product_input().create_stock_2(stock_2, 9, 'Спагетти', 5),
                    Product_input().create_stock_2(stock_2, 11, 'Овсянка', 6),
                    Product_input().create_stock_2(stock_2, 13, 'Вафли', 7),
                    Product_input().create_stock_2(stock_2, 15, 'Пряники', 8),
                    Product_input().create_stock_2(stock_2, 17, 'Кукурузные палочки', 9),
                    Product_input().create_stock_2(stock_2, 19, 'Гречка', 2),
                    Product_input().create_stock_2(stock_2, 21, 'Перловка', 3),
                    Product_input().create_stock_2(stock_2, 23, 'Пшенка', 4),
                    Product_input().create_stock_2(stock_2, 25, 'Спагетти', 5)]


def order_for_stock():
    type_product = 1
    for input_entry in list_entry_input:
        stock.stock_order(input_entry.get_quantity_entry(), type_product)
        type_product += 1



stock_button_order = ttk.Button(stock_2, text='Заказать', command=lambda: order_for_stock())
stock_button_order.grid(row=27, column=0, columnspan=2, pady=5, ipadx=2, ipady=2)

next_day_button = ttk.Button(stock_main,text='Следующий день', command=lambda: next_day())
next_day_button.pack(anchor=CENTER, side=BOTTOM, pady=4, ipady=4, ipadx=4)

#################################### ТТ 1
sm_add_1 = ttk.Frame(sm_1, borderwidth=1, relief=SOLID)
sm_add_2 = ttk.Frame(sm_1, borderwidth=1, relief=SOLID)

sm_add_1.pack(side=LEFT, fill=BOTH, expand=True)
sm_add_2.pack(side=RIGHT, fill=BOTH, expand=True)

title_sm_1 = ttk.Label(sm_add_1, text='Наличие на ТТ1', font=2)
title_sm_1.pack(anchor=CENTER)

text_area_sm_1 = Text(sm_add_1, wrap='word', width=1)
text_area_sm_1.pack(expand=True, fill=BOTH)

captured_output = io.StringIO()
sys.stdout = captured_output
outlets_1.day_outlets()
output = captured_output.getvalue()
captured_output.close()
text_area_sm_1.insert(END, output)


class Outlets_input:
    def __init__(self):
        self.order_quantity = None
        self.quantity_entry = 0

    def create_sm(self,container, row, text):
        label_name_pruduct = ttk.Label(container, text=text, font=20)
        label_name_pruduct.grid(row=row, column=0, sticky=W, pady=10)

        self.order_quantity = ttk.Entry(container)
        self.order_quantity.grid(row=row, column=1, sticky=E, pady=10)
        return self

    def get_quantity_order(self):
        quantity = self.order_quantity.get()
        if quantity == '':
            quantity = 0
            return quantity
        else:
            return int(quantity)


def order_to_stock_from_sm(num, list):
    type_product = 1
    for entry in list:
        Outlets(num).order_to_stock(entry.get_quantity_order(), type_product)
        stock.remove_wholesale(entry.get_quantity_order(), type_product)
        type_product += 1



title_stock_order = ttk.Label(sm_add_2, text='Заказ', font=50)
title_stock_order.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=5)

sm_add_2.columnconfigure(1, weight=1)

list_entry_input_sm_1 = [Outlets_input().create_sm(sm_add_2, 1, 'Рис'),
                         Outlets_input().create_sm(sm_add_2, 3, 'Гречка'),
                         Outlets_input().create_sm(sm_add_2, 5, 'Перловка'),
                         Outlets_input().create_sm(sm_add_2, 7, 'Пшенка'),
                         Outlets_input().create_sm(sm_add_2, 9, 'Спагетти'),
                         Outlets_input().create_sm(sm_add_2, 11, 'Овсянка'),
                         Outlets_input().create_sm(sm_add_2, 13, 'Вафли'),
                         Outlets_input().create_sm(sm_add_2, 15, 'Пряники'),
                         Outlets_input().create_sm(sm_add_2, 17, 'Кукурузные палочки'),
                         Outlets_input().create_sm(sm_add_2, 19, 'Майонез'),
                         Outlets_input().create_sm(sm_add_2, 21, 'Сок'),
                         Outlets_input().create_sm(sm_add_2, 23, 'Печенье'),
                         Outlets_input().create_sm(sm_add_2, 25, 'Газировка')]

stock_button_order = ttk.Button(sm_add_2, text='Заказать', command=lambda: order_to_stock_from_sm(1,list_entry_input_sm_1))
stock_button_order.grid(row=27, column=0, columnspan=2, pady=5, ipadx=2, ipady=2)

###################################################### ТТ2
sm_2_add_1 = ttk.Frame(sm_2, borderwidth=1, relief=SOLID)
sm_2_add_2 = ttk.Frame(sm_2, borderwidth=1, relief=SOLID)

sm_2_add_1.pack(side=LEFT, fill=BOTH, expand=True)
sm_2_add_2.pack(side=RIGHT, fill=BOTH, expand=True)

title_sm_2 = ttk.Label(sm_2_add_1, text='Наличие на ТТ2', font=2)
title_sm_2.pack(anchor=CENTER)

text_area_sm_2 = Text(sm_2_add_1, wrap='word', width=1)
text_area_sm_2.pack(expand=True, fill=BOTH)

captured_output = io.StringIO()
sys.stdout = captured_output
outlets_2.day_outlets()
output = captured_output.getvalue()
captured_output.close()
text_area_sm_2.insert(END, output)

title_stock_order = ttk.Label(sm_2_add_2, text='Заказ', font=50)
title_stock_order.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=5)

sm_2_add_2.columnconfigure(1, weight=1)

list_entry_input_sm_2 = [Outlets_input().create_sm(sm_2_add_2, 1, 'Рис'),
                         Outlets_input().create_sm(sm_2_add_2, 3, 'Гречка'),
                         Outlets_input().create_sm(sm_2_add_2, 5, 'Перловка'),
                         Outlets_input().create_sm(sm_2_add_2, 7, 'Пшенка'),
                         Outlets_input().create_sm(sm_2_add_2, 9, 'Спагетти'),
                         Outlets_input().create_sm(sm_2_add_2, 11, 'Овсянка'),
                         Outlets_input().create_sm(sm_2_add_2, 13, 'Вафли'),
                         Outlets_input().create_sm(sm_2_add_2, 15, 'Пряники'),
                         Outlets_input().create_sm(sm_2_add_2, 17, 'Кукурузные палочки'),
                         Outlets_input().create_sm(sm_2_add_2, 19, 'Майонез'),
                         Outlets_input().create_sm(sm_2_add_2, 21, 'Сок'),
                         Outlets_input().create_sm(sm_2_add_2, 23, 'Печенье'),
                         Outlets_input().create_sm(sm_2_add_2, 25, 'Газировка')]

button_order_sm_2 = ttk.Button(sm_2_add_2, text='Заказать', command=lambda: order_to_stock_from_sm(2, list_entry_input_sm_2))
button_order_sm_2.grid(row=27, column=0, columnspan=2, pady=5, ipadx=2, ipady=2)


root.mainloop()
