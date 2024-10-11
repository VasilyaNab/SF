class PasswordChecker():
    def set_password_range(self, min_len, max_len):
        self.min_len= min_len
        self.max_len= max_len
    def check_passwords(self,passwords):
        map(passwords)
        #return list(map(lambda i: self.min_len<=len(i)<=self.max_len,passwords))