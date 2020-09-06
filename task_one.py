import data
import random
# exchange is explained later on in the code (rates are not to scale in real life btw).
exchange={
    'euro' : 10,
    'usd' : 9.5,
    'pln' : 7,
    'gbp' : 10
}

class Product(data.ParentProduct):
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    def show_price(self, currency):
        # Below you can find a simple print that meets the requirements from the task.
        print(self.name," price is ", self.price)
        # But, it just bothered me that we didn't use the "currency"
        # that was said to be used as an argument for this func.
        # Since now we have no way of knowing what currency is our price stored we need somehow get an exchange
        # I created something that might be useful on top as you probably already saw,
        # To be clear, in this example i will presume that price is stored in some imaginary and abstract currency
        # (might come in handy when shop decides to start up some affiliate points system)
        exchange_error = True
        return_price = self.price

        for cur, amt in exchange.items():
            if cur == currency:
                exchange_error  = False
                return_price*=amt
        if exchange_error == True:
            print('Sorry but your currency seems to be not supported by our site.')
        else:
            print(self.name," price is ",return_price," ",currency)
        # I might have over done it but hey, worth it.
    def show_amount(self):
        print(self.name," amount is ", self.amount)
    def calculate_total_value(self):
        #im not sure if i was supposed to literally return this but if not here is the print version
        # print(self.amount * self.price)
        return self.amount * self.price
for element in range(len(data.products)):
    min_am = list(list(data.products[element].items())[1][1].items())[0][1]
    max_am = list(list(data.products[element].items())[1][1].items())[1][1]
    min_pr = list(list(data.products[element].items())[2][1].items())[0][1]
    max_pr = list(list(data.products[element].items())[2][1].items())[1][1]
    data.products[element]["amount"] = random.randint(min_am, max_am)
    data.products[element]["price"] = random.uniform(min_pr, max_pr)

for element in range(len(data.products)):
    data.obj_list.append(Product(data.products[element]["name"], data.products[element]["amount"], data.products[element]["price"]))
summary_value = []
for element in range(len(data.obj_list)):
    summary_value.append(data.obj_list[element].amount * data.obj_list[element].price)
    # Or we can use our beautiful func from before ( ͡o ͜ʖ ͡o)
    # summary_value.append(dataobj_list[element].calculate_total_value()
with open('results_01.txt', 'w') as f:
    for element in summary_value:
        f.write("|Summary value: {0}|\n".format(element))
    for element in range(len(data.products)):
        f.write("|Name: {0}| |Price: {1}| |Amount: {2}|\n".format(data.products[element]["name"],data.products[element]["price"],data.products[element]["amount"]))
    # I don't quite understand what should i write to the result file since obj_list is a list of object
    # I don't have any better ideas so i will save it even tho it's going to look identical to the one above
    for element in range(len(data.obj_list)):
        f.write("|Name: {0}| |Price: {1}| |Amount:{2}|\n".format(data.obj_list[element].name,data.obj_list[element].price, data.obj_list[element].amount))