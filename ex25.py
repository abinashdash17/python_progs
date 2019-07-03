class dog:
    health = 'good'
    def __init__(self):
        self.health = 'bad'
print(dog.health)
jackey = dog()
print(jackey.health)
