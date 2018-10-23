from user import User

#my_user = User('finisher1017@gmail.com', 'Jonathan', 'Seubert', None)

my_user = User.load_from_db_by_email('finisher1017@gmail.com')

print(my_user)