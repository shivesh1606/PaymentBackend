from django.db import models
# from ant_farm.users.models import User

# import uuid
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

action_category = (
    ('Credit', 'Credit'),
    ('Debit', 'Debit')
)

desc_category = (
    ("Gold", "Gold"),
    ("Grossary", "Grossary"),
    ("Investment", "Investment"),
    ("mutual fund", "mutual fund")
)


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    date_of_transaction = models.DateTimeField(auto_now_add=True)
    type_of_transaction = models.CharField(
        max_length=30, choices=action_category, default='Credit')
    description = models.CharField(
        max_length=30, choices=desc_category, default='Gold')
    stripe_id = models.CharField(max_length=200)
    recieved_user = models.ForeignKey(User, related_name='reciever',
                                      on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.order_id is None and self.made_on and self.id:
    #         self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
    #     return super().save(*args, **kwargs)


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=30)
    account_type = models.CharField(max_length=30)
