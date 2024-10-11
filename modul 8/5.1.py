class User():
    private_key= 'password'
    def set_private_key(self, private_key):
        self.private_key = private_key
    def show_private_key(self):
        print(f'Приватный ключ пользователя: {self.private_key}')
