from celery import shared_task

from users.models import User
from .models import Package, Journal



@shared_task
def update_balance():
    '''
        Задание для обновление баланса пользователей
    '''

    for user in User.objects.all():
        for package in Package.objects.all():
            max_val = package.max_value if package.max_value else float('inf')

            if package.min_value < user.balance and user.balance < max_val:
                old_balance = user.balance
                new_balance = old_balance + old_balance * package.coefficient
                user.balance = new_balance

                journal = Journal.objects.create(user=user, 
                                                package=package, 
                                                old_balance=old_balance,
                                                coefficient=package.coefficient,
                                                new_balance=new_balance)

                user.save()
                break
    
