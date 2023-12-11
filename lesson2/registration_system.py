class RegistrationSystem:
    def __init__(self):
        # Используем словарь для хранения данных пользователей.
        # Ключом будет email, значением - другой словарь с именем и номером телефона
        self.users = {}

    def register(self, email, name, phone):
        if email in self.users:
            return 'Error! User with this email already exist!'
        self.users[email] = {'email': email, 'name': name, 'phone': phone}
        return 'User was successfully registered!'
    
    def delete_all_users(self):
        self.users = {}
        return 'All users were deleted!'
    
    def delete_user_by_email(self, email):
        if email not in self.users:
            return 'Error! User with this email was not found!'
        del self.users[email]
        return f'User {email} was successfully deleted!'
    
    def view_all_users(self):
        return self.users
    
system = RegistrationSystem()

system.register('andry@email.com', 'Andry', '+315345435234')
print(system.view_all_users())
print(system.delete_user_by_email('andry@email.com'))
print(system.delete_all_users())
