from django.db import models

# Create your models here.
class Collection(models.Model):
    title=models.CharField(max_length=50)
    # if we delete a product and that product happens to be the 
    # featured product for Collction then we can set it NULL.
    # related_name='+' tells Django ,not to create 
    # reverse relationship. Basically we just declare foreign key 
    # in one table because django automatically maps it with the 
    # related table. But here if we will not write related_name='+',
    # then this error will be shown:
    # store.Collection.featured_product: (fields.E303) Reverse query name 
    # for 'store.Collection.featured_product' clashes with field name 'store.Product.collection'.
    #   HINT: Rename field 'store.Product.collection', or add/change a related_name argument to the definition for field 'store.Collection.featured_product'.
    #store.Product.title: (fields.E120) CharFields must define a 'max_length' attribute.

    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
    
class Promotion(models.Model):
    description=models.CharField(max_length=100)
    discount=models.FloatField()


class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=7,decimal_places=2)
    inventory=models.IntegerField()
    # auto_now_add=true , django will automatically update date
    # according to the last update
    last_update=models.DateTimeField(auto_now=True)
   # collection=models.ForeignKey(Collection,on_delete=models.CASCADE)
    # now we have many to many relationship between Promotion and Product, so to declare that:
    #promotion=models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMEBERSHIP_BRONZE='B'
    MEMEBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMEBERSHIP_SILVER,"Silver"),
        (MEMBERSHIP_GOLD,"Gold"),
        (MEMEBERSHIP_BRONZE,"Bronze")
    ]
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    memebership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMEBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_COMPLETE,"Complete"),
        (PAYMENT_STATUS_PENDING,"Pending"),
        (PAYMENT_STATUS_FAILED,"Failed")
    ]
    placedAt=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_FAILED)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class Address(models.Model):
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=40)
   #for one to one mapping ,syntax will be
   #  customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
   # now to have a customer can have multiple address
    cutomer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()






