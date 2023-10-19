from faker import Faker
fake = Faker()
standart_login = 'standard_user'
locked_user_login = 'locked_out_user'
problem_user_login = 'problem_user'
prformance_glitch_login = 'performance_glitch_user'
error_user_login = 'error_user'
visual_user_login = 'visual_user'

password = 'secret_sauce'
firstname = fake.name().split()[0]
lastname = fake.name().split()[1]

zipcode = fake.zipcode()
