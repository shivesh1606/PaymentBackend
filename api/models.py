from django.db import models



# Create your models here.

action_category=(
    ('Buy','Buy'),
    ('Sell', 'Sell')
    )
class User_Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='transactions')
    date_of_transaction= models.DateTimeField(auto_now_add=True)
    type_of_transaction= models.CharField(max_length=30, choices=type_of_user_flow, default='Subscription')
    amount=models.IntegerField()
        
    
    class Meta:
        verbose_name_plural = "User Transactions"

    def __str__(self):
        return self.user.name + ' ' + str(self.date_of_transaction)

