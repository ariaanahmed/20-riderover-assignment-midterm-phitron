from django.db import models
from django.contrib.auth.models import User
from brands.models import Brands

class Car(models.Model):
    car_img = models.ImageField(upload_to='add_car/media/car_images/')
    car_title = models.CharField(max_length=100)
    car_description = models.TextField()
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"car: {self.car_title}"

class UserCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.car_title}"
    
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented: {self.name}"
