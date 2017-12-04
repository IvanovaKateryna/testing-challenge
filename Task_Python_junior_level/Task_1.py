currency = {'UAH': 1, 'RUB': 0.46, 'USD': 27, 'EUR': 32, 'GBP':36}
products = []
customers = []
result = 0

class Product:
   #_products = []

    def __init__(self, name, cost_price, price, weight):
        self.name = name
        self.cost_price = cost_price
        self.price = price
        self.weight = weight
        #self._products.append(self)

    def __str__(self):
        return 'Product: {}. Cost price(in UAH): {}. Price(in UAH): {}.' \
               ' Weight(kg): {}.'.format(self.name, self.cost_price,
                                         self.price, self.weight)

    def registration(self):
        self.name = input("Enter the name of Product: ")
        self.cost_price = float(input('Enter the cost price of product in UAH: '))
        self.price = float(input('Enter the price of product in UAH '))
        self.weight = float(input('Enter the weight of product in kg '))
        return 'Successful registration of product'

    def price_of_customer(self, customer):
        price_customer = currency[customer.currency]
        return self.price / price_customer


'''@classmethod
    def get_products(cls):
        return cls._products'''


class Customer:
    #_customers = []

    def __init__(self, name, discount, currency):
        self.name = name
        self.discount = discount
        self.currency = currency

    def __str__(self):
        return 'Customer: {}. Discount: {}. Currency: {}'.format(
            self.name,
            self.discount,
            self.currency
        )

    def registration(self):
        self.name = input('Enter the name of Customer')
        self.discount = int(input('Enter the percent(%) of discount '
                                  'in the range of 0 to 100%: '))
        self.currency = input('Enter the currency(UAH, RUB, USD, EUR, GBP): ')

'''   @classmethod
    def get_customers(cls):
        return cls._customers'''


class Buy(Product):
    def __init__(self, product, customer, quantity):
        self.product = product
        self.customer = customer
        self.quantity = quantity

    def __str__(self):
        return 'The quantity of product that you bought: {}.\n' \
               'The price of product:{}.\n' \
               'The full price: {}.\n' \
               'The full weight: {}.'.format(
            self.quantity,
            self.price,
            self.full_price,
            self.full_weight
        )

    def full_price(self):
        return (100-self.customer.discount)/100*\
               (self.quantity * self.product.price_of_customer(self.customer))

    def full_weight(self):
        return self.quantity * self.product.weight

class Check(Buy):
    def __init__(self,buy):
        self.buy = buy

    def __str__(self):
       return 'Information about product: {}\n' \
              'Information about buying: {}\n' \
              'Information about customer: {}.'.format(
           self.buy.product,
           self.buy,
           self.buy.customer
       )


def registration_product():
    new_pr = Product()
    new_pr.registration()
    return new_pr


def registration_customer():
    new_cust = Customer(0, 0, 0, 0)
    new_cust.registration()
    return new_cust


def buy_product(customer, product):
    quantity = int(input('How much would you like to buy: '))
    item = Buy(product, customer, quantity)
    return item


def checkin(item):
    check = ckeck(item)
    return check


while True:
    print('          Menu of SHOP\n'
          'Enter 1  to registration a new Product\n'
          'Enter 2  to registration a new Customer\n'
          'Enter 3 to Buy a Product\n'
          'Enter 4 to see the total information about buying.')

    case = int(input('Enter the number of menu(1-4):   '))
    if case == 1:
        new_pr = registration_product()
        print('New Product: ', new_pr)
        products.append(new_pr)
    elif case == 2:
        new_cust = registration_customer()
        print('New Customer: ', new_cust)
        customers.append(new_cust)
    elif case == 3:
        print('The list of Products\n')
        for pr in xrange(len(products)):
            print(pr, '.', products[pr])
        print('The list of Customers\n')
        for cs in xrange(len(customers)):
            print(cs, '.', customers[cs])
        quantity_prod = int(input('Enter number of Product LIST'))
        quantity_cust = int(input('Enter number of Customer LIST'))
        result = buy_product(customers[quantity_cust],products[quantity_prod])
        print('\n',result,'\n')
    elif case == 4:
            print(checkin(result))