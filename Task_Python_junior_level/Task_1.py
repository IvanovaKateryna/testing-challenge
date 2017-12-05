#        By Python 3
currency = {'UAH': 1, 'RUB': 0.46, 'USD': 27, 'EUR': 32, 'GBP': 36}
products = []
customers = []
result = 0


# Basic class Product
class Product:

    def __init__(self, name, cost_price, price, weight):
        self.name = name
        self.cost_price = cost_price
        self.price = price
        self.weight = weight

    def __str__(self):
        return 'Product: {}. Cost price(in UAH): {}. Price(in UAH): {}.' \
               ' Weight(kg): {}.'.format(self.name, self.cost_price,
                                         self.price, self.weight)

    def registration(self):
        """
        Registration form  of Products
        :return: full registration of Product
        """
        self.name = input("Enter the name of Product: ")
        self.cost_price = float(input('Enter the cost price of product in UAH: '))
        self.price = float(input('Enter the price of product in UAH: '))
        self.weight = float(input('Enter the weight of product in kg: '))
        return 'Successful registration of product!'

    def price_of_customer(self, customer):
        """
        Personal price for customer considering currency
        :param customer: from class Customer
        :return: price  with coefficient of currency
        """
        price_customer = currency[customer.currency]
        return self.price / price_customer


# Basic class Customer
class Customer:

    def __init__(self, name, discount, currency):
        """
        :param name: name of customer
        :param discount: personal discount of customer
        :param currency: customer can choose currency from dict(currency)
        """
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
        """
        Registration form of Customers
        :return: Success registration of Customers
        """
        self.name = input('Enter the name of Customer:  ')
        self.discount = int(input('Enter the percent(%) of discount '
                                  'in the range of 0 to 100%: '))
        self.currency = input('Enter the currency(UAH, RUB, USD, EUR, GBP): ')
        return 'Successful registration of Customer'


# Basic class for Check class and derivative class for Product class
class Buy(Product):

    def __init__(self, product, customer, quantity):
        """
        :param product: from class Product
        :param customer: from class Customer
        :param quantity: number of product
        """
        self.product = product
        self.customer = customer
        self.quantity = quantity

    def __str__(self):
        return 'The quantity of product that you bought: {}.\n' \
               'The price of product:{}.\n' \
               'The full price: {}.\n' \
               'The full weight: {}.'.format(self.quantity, self.price,
                                             self.full_price, self.full_weight)

    def full_price(self):
        """The function that considers full price of bought Product"""
        return (100-self.customer.discount)/100 * \
               (self.quantity * self.product.price_of_customer(self.customer))

    def full_weight(self):
        """The function that considers full weight of bought Product"""
        return self.quantity * self.product.weight


# Derivative class for Buy class
class Check(Buy):

    def __init__(self, buy):
        """:param buy: from class Buy """
        self.buy = buy

    def __str__(self):
        return 'Information about product: {}\n' \
              'Information about buying: {}\n' \
              'Information about customer: {}.'.format(self.buy.product,
                                                       self.buy, self.buy.customer)


def registration_product():
    """The function registration the new product"""
    new_pr = Product(0, 0, 0, 0)
    new_pr.registration()
    return new_pr


def registration_customer():
    """The function registration the new customer"""
    new_cust = Customer(0, 0, 0)
    new_cust.registration()
    return new_cust


def buy_product(customer, product):
    """
    The function reads quantity of items that Customer would like to buy
    :param customer: from class Customer
    :param product: from class Product
    :return: number of items
    """
    quantity = int(input('How much items would you like to buy: '))
    item = Buy(product, customer, quantity)
    return item


def checkin(item):
    """The function displays full information about Product and Buy"""
    check = Check(item)
    return check


while True:
    print('          Menu of SHOP\n'
          'Enter 1  to registration a new Product\n'
          'Enter 2  to registration a new Customer\n'
          'Enter 3 to Buy a Product\n'
          'Enter 4 to see the total information about buying.')

    case = int(input('Enter the number of menu(1-4):   '))
#   Value of cases
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
        number_prod = int(input('Enter number of Product LIST: '))
        number_cust = int(input('Enter number of Customer LIST: '))
        result = buy_product(customers[number_cust], products[number_prod])
        print('\n', result, '\n')
    elif case == 4:
            print(checkin(result))
