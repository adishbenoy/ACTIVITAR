from django.db import models

# Create your models here.


class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)

class gym_instructor(models.Model):
    instructor_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    age=models.CharField(max_length=225)
    gender=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    
class physician(models.Model):
    physician_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    
class batches(models.Model):
    batch_id=models.AutoField(primary_key=True)
    instructor=models.ForeignKey(gym_instructor,on_delete=models.CASCADE)
    batch_name=models.CharField(max_length=225)
    start_time=models.CharField(max_length=225)
    end_time=models.CharField(max_length=225)

    

class users(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    batch=models.ForeignKey(batches,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    age=models.CharField(max_length=225)
    gender=models.CharField(max_length=225)
    weight=models.CharField(max_length=225)
    height=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    address=models.CharField(max_length=800)
    goal=models.CharField(max_length=225)
    payment_status=models.CharField(max_length=225)
    
    
class payments(models.Model):
    payment_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    payment_for=models.CharField(max_length=225)
    payment_date=models.CharField(max_length=225)
    
    
class complaints(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    description=models.CharField(max_length=225)
    reply=models.CharField(max_length=225)
    complaint_date=models.CharField(max_length=225)
    
class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    feedback_desc=models.CharField(max_length=225)
    feedback_reply=models.CharField(max_length=225)
    feedback_date=models.CharField(max_length=225)
    

class attendances(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    status=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
    

class equipment(models.Model):
    equipment_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    image=models.ImageField(upload_to='static/media')
    
    
class workout(models.Model):
    workout_id=models.AutoField(primary_key=True)
    equipment=models.ForeignKey(equipment,on_delete=models.CASCADE)
    title=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    benefits=models.CharField(max_length=225)
    
class user_workouts(models.Model):
    user_workout_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    workout=models.ForeignKey(workout,on_delete=models.CASCADE)
    day=models.CharField(max_length=225)
    duration=models.CharField(max_length=225)
    
class subscription(models.Model):
    subscription_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    physician=models.ForeignKey(physician,on_delete=models.CASCADE)
    
class user_diets(models.Model):
    user_diets_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    physician=models.ForeignKey(physician,on_delete=models.CASCADE)
    diet_details=models.CharField(max_length=225)
    diet_date=models.CharField(max_length=225)
    
class message(models.Model):
    message_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    physician=models.ForeignKey(physician,on_delete=models.CASCADE)
    message_description=models.CharField(max_length=225)
    message_reply=models.CharField(max_length=225)
    message_date=models.CharField(max_length=225)
    
class shop(models.Model):
    shop_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    
class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)
    category=models.CharField(max_length=225)
    product_name=models.CharField(max_length=225)
    amount=models.CharField(max_length=225)

    
class productbooking(models.Model):
    productbooking_id=models.AutoField(primary_key=True)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)

class ordermaster(models.Model):
    ordermaster_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    total=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)

class orderdetails(models.Model):
    orderdetails_id=models.AutoField(primary_key=True)
    ordermaster=models.ForeignKey(ordermaster,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100,null=True)
    qty=models.CharField(max_length=100,null=True)
    

class product_payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    ordermaster=models.ForeignKey(ordermaster,on_delete=models.CASCADE)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    payment_for=models.CharField(max_length=225)
    payment_date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)   


class exercise(models.Model):
    exercise_id=models.AutoField(primary_key=True)
    user_workout=models.ForeignKey(workout,on_delete=models.CASCADE)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    details=models.CharField(max_length=225)

class predict_work(models.Model):
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    output=models.CharField(max_length=1000)


    


    

    


    
    







    


