from django.db import models
from django.utils import timezone

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     image = models.ImageField(blank = True, upload_to="shop/%Y/%m/%d") # 어디로 업로드 할지 지정
#     thumnail = models.ImageField(blank = True) # 필수입력 해제

#     def __str__(self):
#         return self.title

class Order(models.Model):
    writer = models.CharField(max_length=200, blank=True)
    product = models.CharField(max_length=200, blank=False)
    orderer = models.CharField(max_length=200, blank=False)
    postcode = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=800, blank=False)
    phone1 = models.CharField(max_length=100, blank=False)
    phone2 = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    price = models.IntegerField(blank=True)
    delivery_price = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True)

    potato_price = {'a-5' : 5000, 'a-10' : 9000, 'a-20' : 16000, 'b-5' : 4000, 'b-10' : 7500, 'b-20' : 14000, 'c-5' : 2500, 'c-10' : 4500, 'c-20' : 8000}
    del_price = {'a-5' : 3000, 'a-10' : 4000, 'a-20' : 5000, 'b-5' : 3000, 'b-10' : 4000, 'b-20' : 5000, 'c-5' : 3000, 'c-10' : 4000, 'c-20' : 5000}

    def __str__(self):
        return self.orderer