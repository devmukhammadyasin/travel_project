from django.db import models

class Direction(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField("Ma'lumot",blank=True)
    duration = models.PositiveIntegerField("Davomiyligi",default=10)
    price = models.PositiveIntegerField(verbose_name="UZS", default=100)
    price_usd = models.PositiveIntegerField(verbose_name="USD", default=100)
    image = models.ImageField(upload_to='city_images/')
    leave = models.DateField("Ketish sanasi (To'ldirish shart emas)", blank=True,null=True)
    back_to = models.DateField("Qaytish sanasi (To'ldirish shart emas)", blank=True,null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Yo'nalish"    
        verbose_name_plural = "Yo'nalishlar" 

        
class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=250,blank=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xabar" 
        verbose_name_plural = "Xabarlar"

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilik toifasi"    
        verbose_name_plural = "Yangilik toifalari"   

class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="news")
    title = models.CharField(max_length=50, help_text="Yangilik nomimi yozing")
    text = models.TextField(help_text="Yangilik matnini yozing")
    image = models.ImageField(upload_to="news_images")
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"    
        verbose_name_plural = "Yangiliklar"


class Subscribe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Obunachi" 
        verbose_name_plural = "Obuna bo'lganlar"
    