class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self,percent):
        if(percent>=100):
            self.price = 0
        else:
            self.price = self.price * (1 - percent/100)
        return self.price
        
    
    def __str__(self):
        return (f"{self.title} by {self.author} - {self.price}€")