from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from gym.models import *
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your views here.

###########################################PUBLIC#########################################################################
def log(request):
    if 'login' in request.POST:
        uname=request.POST['uname']
        psw=request.POST['pass']
        obj1=login.objects.filter(username=uname,password=psw)
        if obj1.exists():
            obj=login.objects.get(username=uname,password=psw)
            if obj:
                request.session['lid']=obj.pk
                if obj.usertype=='admin':
                    return HttpResponse("<script>alert('Login Success');window.location='/admin_home'</script>")
                if obj.usertype=='employee':
                    ob=gym_instructor.objects.get(login=request.session['lid'])
                    if ob:
                        request.session['uid']=ob.pk
                        
                        return HttpResponse("<script>alert('Login Success');window.location='/employee_home'</script>")
                elif obj.usertype=='physician':
                    ob=physician.objects.get(login=request.session['lid'])
                    if ob:
                        request.session['pid']=ob.pk
                        
                        return HttpResponse("<script>alert('Login Success');window.location='/physician_home'</script>")
                elif obj.usertype=='shop':
                    ob=shop.objects.get(login=request.session['lid'])
                    if ob:
                        request.session['sid']=ob.pk
                        
                        return HttpResponse("<script>alert('Login Success');window.location='/shop_home'</script>")
                elif obj.usertype=='user':
                    ob=users.objects.get(login=request.session['lid'])
                    if ob:
                        request.session['uid']=ob.pk
                    
                    return HttpResponse("<script>alert('Login Success');window.location='/user_home'</script>")
        return HttpResponse("<script>alert('wrong info');window.location='/'</script>")
                

    return render(request,'login.html')


def user_reg(request):
    ob1=batches.objects.all()
    if 'submit' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        gender=request.POST['gender']
        weight=request.POST['weight']
        height=request.POST['height']
        phone=request.POST['phone']
        batch=request.POST['batch']
        email=request.POST['email']
        address=request.POST['address']
        goal=request.POST['goal']
        uname=request.POST['user']
        passw=request.POST['pass']
        
        lg=login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/user_reg'</script>")
        else:
            lg=login(username=uname,password=passw,usertype='user')
            lg.save()
            tchr=users(first_name=fname,last_name=lname,age=age,gender=gender,weight=weight,height=height,phone=phone,email=email,address=address,goal=goal,payment_status='pending',batch_id=batch,login=lg)
            tchr.save()
            return HttpResponse("<script>alert('Added Successsfully');window.location='/user_reg'</script>")
    return render(request,'user_reg.html',{'ob1':ob1})
            

####################################ADMIN############################################################

def admin_home(request):
    return render(request,'admin_home.html')       

# def manage_category(request):
#     if 'submit' in request.POST:


def reg_employee(request):
    qa=gym_instructor.objects.all()
    if 'employee' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email=request.POST['email']
        uname=request.POST['user']
        passw=request.POST['pass']
        lg=login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/reg_employee'</script>")
        else:
            lg=login(username=uname,password=passw,usertype='employee')
            lg.save()
            tchr=gym_instructor(first_name=fname,last_name=lname,age=age,gender=gender,phone=phone,email=email,login=lg)
            tchr.save()
            return HttpResponse("<script>alert('Added Successsfully');window.location='/reg_employee'</script>")
    return render(request,'admin_register_employee.html',{'qa':qa})


def admin_update_emp(request,ids):
    qa=gym_instructor.objects.all()
    ob=gym_instructor.objects.get(instructor_id=ids)
    if 'uemployee' in request.POST:
        fname=request.POST['ufname']
        lname=request.POST['ulname']
  
        phone=request.POST['uphone']
        email=request.POST['uemail']
        ob.first_name=fname
        ob.last_name=lname

        ob.phone=phone
        ob.email=email
        ob.save()
        return HttpResponse("<script>alert('Updated');window.location='/reg_employee'</script>")
    return render(request,'admin_register_employee.html',{'qa':qa,'ob':ob})

def admin_delete_emp(request,ids):
    obj=gym_instructor.objects.get(instructor_id=ids)
    obj.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/reg_employee'</script>")


def reg_physician(request):
    qa=physician.objects.all()
    if 'physician' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        quali=request.POST['qualification']
        phone=request.POST['phone']
        email=request.POST['email']
        uname=request.POST['user']
        passw=request.POST['pass']
        lg=login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/reg_physician'</script>")
        else:
            lg=login(username=uname,password=passw,usertype='physician')
            lg.save()
            ob=physician(first_name=fname,last_name=lname,qualification=quali,phone=phone,email=email,login=lg)
            ob.save()
            return HttpResponse("<script>alert('Value Added');window.location='/reg_physician'</script>")
    return render(request,'admin_register_physician.html',{'qa':qa})

def admin_update_physi(request,ids):
    qa=physician.objects.all()
    
    ob=physician.objects.get(physician_id=ids)

    if 'uphysician' in request.POST:
        fname=request.POST['ufname']
        lname=request.POST['ulname']
        phone=request.POST['uphone']
        email=request.POST['uemail']
        ob.first_name=fname
        ob.last_name=lname
        ob.phone=phone
        ob.email=email
        ob.save()
        return HttpResponse("<script>alert('Value Updated');window.location='/reg_physician'</script>")
    return render(request,'admin_register_physician.html',{'qa':qa,'ob':ob})


def admin_delete_physi(request,ids):
    obj=physician.objects.get(physician_id=ids)
    obj.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/reg_physician'</script>")


def admin_verify_user(request):
    obj=users.objects.all()
    return render(request,'admin_verify_user.html',{'obj':obj})

def verify_user(request,ids):
    obj=users.objects.get(user_id=ids)
    obj.payment_status='verified'
    obj.save()
    return HttpResponse("<script>alert('Verified');window.location='/admin_verify_user'</script>")

def admin_view_feedback(request):
    obj=feedback.objects.all()
        
    return render(request,'admin_view_feedback.html',{'obj':obj})

def admin_reply(request,ids):
    obj=feedback.objects.get(feedback_id=ids)
    if 'submit' in request.POST:
        text=request.POST['text']
        obj.feedback_reply=text
        obj.save()
        return HttpResponse("<script>alert('Reply send successfully');window.location='/admin_view_feedback'</script>")
    return render(request,'admin_reply.html')


def admin_view_complaints(request):
    obj=complaints.objects.all()
        
    return render(request,'admin_view_complaint.html',{'obj':obj})


def admin_reply_complaint(request,ids):
    obj=complaints.objects.get(complaint_id=ids)
    if 'submit' in request.POST:
        text=request.POST['text']
        obj.reply=text
        obj.save()
        return HttpResponse("<script>alert('Reply send successfully');window.location='/admin_view_complaints'</script>")
    return render(request,'admin_reply.html')


def admin_view_payment(request):
    obj=payments.objects.all()
    return render(request,'admin_view_payment.html',{'obj':obj})

def admin_add_new_batches(request):
    obj=batches.objects.all()
    ob1=gym_instructor.objects.all()
    if 'batches' in request.POST:
        batch=request.POST['batch']
        stime=request.POST['stime']
        etime=request.POST['etime']
        gym_id=request.POST['instructor_id']
        ob1=gym_instructor.objects.get(instructor_id=gym_id)
        ab=batches(batch_name=batch,start_time=stime,end_time=etime,instructor_id=ob1.pk)
        ab.save()
        return HttpResponse("<script>alert('Value added');window.location='/admin_add_new_batches'</script>")
    return render(request,'admin_add_new_batches.html',{'obj':obj,'ob1':ob1})

def admin_delete_batch(request,ids):
    obj=batches.objects.get(batch_id=ids)
    obj.delete()
    return HttpResponse("<script>alert('Value Deleted');window.location='/admin_add_new_batches'</script>")

##################################EMPLOYEE#######################################################
def employee_home(request):
    return render(request,'employee_home.html')

def employee_manage_equipments(request):
    ob=equipment.objects.all()
    if 'equipment' in request.POST:
        eqname=request.POST['eqname']
        description=request.POST['description']    
        img=request.FILES['image']
        fs=FileSystemStorage()
        vv=fs.save(img.name,img)
        obj=equipment(name=eqname,description=description,image=vv)
        obj.save()
        return HttpResponse("<script>alert('Value Added');window.location='/employee_manage_equipments'</script>")
    return render(request,'employee_manage_equipments.html',{'ob':ob})

def emp_update(request,ids):
    obj=equipment.objects.get(equipment_id=ids)
    ob=equipment.objects.all()
    if 'uequipment' in request.POST:
        ueqname=request.POST['ueqname']
        udescription=request.POST['udescription']
        try:
            img=request.FILES['uimage']
            fs=FileSystemStorage()
            vv=fs.save(img.name,img)
            obj.name=ueqname
            obj.description=udescription
            obj.image=vv
            obj.save()
            return HttpResponse("<script>alert('Value Updated');window.location='/employee_manage_equipments'</script>")

        except:
            obj.name=ueqname
            obj.description=udescription
            obj.save()
            return HttpResponse("<script>alert('Value Updated');window.location='/employee_manage_equipments'</script>")
    return render(request,'employee_manage_equipments.html',{'ob':ob,'obj':obj})

def emp_delete(request,ids):
    obj=equipment.objects.get(equipment_id=ids)
    obj.delete()
    return HttpResponse("<script>alert('Value Deleted');window.location='/employee_manage_equipments'</script>")

def employee_manage_workout_details(request):
    obj=workout.objects.all()
    ob1=equipment.objects.all()
    if 'workout' in request.POST:
        title=request.POST['title']
        eq=request.POST['equipment_id']
        description=request.POST['description']
        benefits=request.POST['benefits']
        ab=workout(title=title,description=description,benefits=benefits,equipment_id=eq)
        ab.save()
        return HttpResponse("<script>alert('Value Added');window.location='/employee_manage_workout_details'</script>")
    return render(request,'employee_manage_workout_details.html',{'obj':obj,'ob1':ob1})

def emp_update_work(request,ids):
    ob2=workout.objects.get(workout_id=ids)
    obj=workout.objects.all()
    ob1=equipment.objects.all()
    if 'uworkout' in request.POST:
        utitle=request.POST['utitle']
        eq_id=request.POST['uequipment_id']
        udescription=request.POST['udescription']
        ubenefits=request.POST['ubenefits']
        ob2.title=utitle
        ob2.description=udescription
        ob2.benefits=ubenefits
        ob2.equipment_id=eq_id
        ob2.save()
        return HttpResponse("<script>alert('Value Updated');window.location='/employee_manage_workout_details'</script>")
    return render(request,'employee_manage_workout_details.html',{'obj':obj,'ob1':ob1,'ob2':ob2})

def emp_delete_work(request,ids):
    ob2=workout.objects.get(workout_id=ids)
    ob2.delete()
    return HttpResponse("<script>alert('Value Deleted');window.location='/employee_manage_workout_details'</script>")
    
        
    
def employee_add_user_details(request):
    try:
        
        ab=batches.objects.filter(instructor=request.session['uid'])
        print(ab,"===================================")
        for i in ab:
            bid=i.pk
            obj=users.objects.filter(batch=bid)
            return render(request,'employee_add_user_details.html',{'obj':obj})
    except:
        return render(request,'employee_add_user_details.html')
    
def employee_view_work(request,id):
    # try:
        q=predict_work.objects.filter(user_id=id).order_by('-id')
        if q.exists():
            qa=q[0]
            print(qa,"=================")
            return render(request,'employee_view_work.html',{'qa':qa})
        else:
            print('ooooooooooooooooooo')
            return render(request,'employee_view_work.html')
    # except:
    #     print('ooooooooooooooooooo')
    #     return render(request,'employee_view_work.html')
    



def employee_personalised_workout_details(request,ids):
    print(ids,"==================================================")
    obj=users.objects.get(user_id=ids)
    ob=user_workouts.objects.filter(user_id=ids)
    ob1=workout.objects.all()

    if 'submit' in request.POST:
        day=request.POST['day']
        duration=request.POST['duration'] 
        workouts=request.POST['workout']
        ab=user_workouts(day=day,duration=duration,user_id=ids,workout_id=workouts)
        ab.save()
        return HttpResponse("<script>alert('Value Added');window.location='/employee_add_user_details'</script>")

    return render(request,'employee_personalised_workout_details.html',{'obj':obj,'ob':ob,'ob1':ob1})

def user_workout_id(request,ids):
    ob=user_workouts.objects.filter(user_workout_id=ids)
    ob.delete()
    return HttpResponse("<script>alert('Value Deleted');window.location='/employee_add_user_details'</script>")
    


#########################################PHYSICIAN#############################################################################################       

def physician_home(request):
    return render(request,'physician_home.html')

# def physician_view_users(request):
#     ab=subscription.objects.filter(physician_id=request.session['pid'])
#     for i in ab:
#         obj=users.objects.filter(user_id=i.pk)

#         return render(request,'physician_view_users.html',{'obj':obj}) 


def physician_view_users(request):
    ab = subscription.objects.filter(physician_id=request.session['pid'])

    return render(request, 'physician_view_users.html', {'obj': ab})









# def physician_view_users(request):
#     obj=users.objects.all()
#     return render(request,'physician_view_users.html',{'obj':obj})      

def calculate_bmi(request,ids):
    obj=users.objects.all()
    obj1=users.objects.get(user_id=ids)

    return render(request,'physician_view_users.html',{'obj':obj,'obj1': obj1})


def physician_create_personalised_diet_plan(request,ids):
    ob1=user_diets.objects.filter(user_id=ids)
    if 'submit' in request.POST:
        diet=request.POST['diet']
        date=request.POST['date']
        ab=user_diets(diet_details=diet,diet_date=date,physician_id=request.session['pid'],user_id=ids)
        ab.save()
        return HttpResponse("<script>alert('Value Added');window.location='/physician_create_personalised_diet_plan"+"/"+str(ids)+"'</script>")

    return render(request,'physician_create_personalised_diet_plan.html',{'ob1':ob1})

def update_diet(request,ids):
    ob1=user_diets.objects.filter(user_diets_id=ids)
    obj=user_diets.objects.get(user_diets_id=ids)
    if 'update' in request.POST:
        diet=request.POST['diet']
        date=request.POST['date']
        obj.diet_details=diet
        obj.diet_date=date
        obj.save()
        
    return render(request,'physician_create_personalised_diet_plan.html',{'ob1':ob1,'obj':obj})

def physician_view_message_from_users(request):
    obj=message.objects.all()
    return render(request,'physician_view_message_from_users.html',{'obj':obj})

def phy_send_reply(request,ids):
    obj=message.objects.get(message_id=ids)
    if 'submit' in request.POST:
        reply=request.POST['reply']
        obj.message_reply=reply
        obj.save()
        return HttpResponse("<script>alert('Reply Added');window.location='/physician_view_message_from_users'</script>")
    return render(request,'phy_send_reply.html')

########################################SHOP###############################################################################


def shop_home(request):
    return render(request,'shop_home.html')

def shop_manage_products(request):
    obj=product.objects.all()
    if 'submit' in request.POST:
        category=request.POST['category']
        name=request.POST['name']
        amt=request.POST['amt']
        ab=product(product_name=name,amount=amt,shop_id=request.session['sid'],category=category)
        ab.save()
        return HttpResponse("<script>alert('Product Added');window.location='/shop_manage_products'</script>")
    return render(request,'shop_manage_products.html',{'obj':obj})

def shop_update(request,ids):
    obj=product.objects.all()
    ob1=product.objects.get(product_id=ids)
    if 'update' in request.POST:
        
        category=request.POST['category']
        name=request.POST['name']
        amt=request.POST['amt'] 
        ob1.category=category
        ob1.product_name=name
        ob1.amount=amt
        ob1.save()
        return HttpResponse("<script>alert('Updated Successfully');window.location='/shop_manage_products'</script>")
    return render(request,'shop_manage_products.html',{'obj':obj,'ob1':ob1})
        
def shop_view_booking(request,ids):
    obj=orderdetails.objects.filter(product_id=ids)
    return render(request,'shop_view_booking.html',{'obj':obj})

def shop_view_payment(request,ids):
    obj=product_payment.objects.get(ordermaster_id=ids)
    return render(request,'shop_view_payment.html',{'obj':obj})


##########################################USER##########################################################################

def user_home(request):
    return render(request,'user_home.html')


def user_view_batch(request):
    ob=users.objects.get(user_id=request.session['uid'])
    request.session['b_id']=ob.batch_id
    
    if ob.payment_status == 'pending':
        val='Payment Pending'
        return render(request,'user_view_batch.html',{'val':val})
    elif ob.payment_status == 'paid':
        val="Wait For verification"
        return render(request,'user_view_batch.html',{'val':val})
    else:
        ab=batches.objects.filter(batch_id=request.session['b_id'])
        return render(request,'user_view_batch.html',{'ab':ab})
    
def user_make_payment(request):
    obj=users.objects.get(user_id=request.session['uid'])
    print(obj,'/////////////////////////////////////////')
    if 'submit' in request.POST:
        amt=request.POST['amt']
        ob=payments(amount=amt,payment_for='fee',payment_date=timezone.now(),user_id=request.session['uid'])
        ob.save()

        obj.payment_status='paid'
        obj.save()

        
        return HttpResponse("<script>alert('Payment Completed');window.location='/user_home'</script>")
    return render(request,'user_make_payment.html',{'amt':500})

def view_daily_workout(request):
    try: 
        obj=users.objects.get(user_id=request.session['uid'],payment_status='verified')
        if obj:
            ob=user_workouts.objects.filter(user_id=request.session['uid'])
            return render(request,'view_daily_workout.html',{'ob':ob})
    except:
        val="Payment or verification is pending"
        return render(request,'view_daily_workout.html',{'val':val})
    
def view_equipments(request,ids):
    obj=equipment.objects.get(equipment_id=ids)
    return render(request,'view_equipments.html',{'obj':obj})


def view_physicians(request):
    obj=physician.objects.all()
    try:
        
    
        ob1=subscription.objects.get(user_id=request.session['uid'])
        return render(request,'view_physicians.html',{'obj':obj,'ob1':ob1})
    except:
        
        
        return render(request,'view_physicians.html',{'obj':obj})












def book_physician(request,ids):
    if 'submit' in request.POST:
        amt=request.POST['amt']
        ob=payments(amount=amt,payment_for='subscription',payment_date=timezone.now(),user_id=request.session['uid'])
        ob.save() 

        obj=subscription(physician_id=ids,user_id=request.session['uid'])
        obj.save()
        return HttpResponse("<script>alert('Payment Completed');window.location='/view_physicians'</script>")
    
    return render(request,'book_physician.html',{'ids':ids})

def view_diet_plan(request,ids):
    obj=user_diets.objects.filter(physician_id=ids,user_id=request.session['uid'])
    return render(request,'view_diet_plan.html',{'obj':obj})

def user_send_messgae(request,ids):
    ob=message.objects.filter(physician_id=ids,user_id=request.session['uid'])
    if 'submit' in request.POST:
        msg=request.POST['msg']
        obj=message(message_description=msg,message_reply='pending',message_date=timezone.now(),physician_id=ids,user_id=request.session['uid'])
        obj.save()
        return HttpResponse("<script>alert('Message Send');window.location='/user_send_messgae"+str(ids)+"</script>")
    return render(request,'user_send_messgae.html',{'ob':ob})

def user_send_feedback(request):
    obj=feedback.objects.filter(user_id=request.session['uid'])
    if 'submit' in request.POST:
        feed=request.POST['feed']
        ob=feedback(feedback_desc=feed,feedback_reply='pending',feedback_date=timezone.now(),user_id=request.session['uid'])  
        ob.save()
        return HttpResponse("<script>alert('Feedback Send');window.location='/user_send_feedback'</script>")
    
    return render(request,'user_send_feedback.html',{'obj':obj})
          
def user_view_products(request):
    obj=product.objects.all()
    return render(request,'user_view_products.html',{'obj':obj})

###################!@#$%^&*()))))))(*&^%$#!@#$%^&*()(*&^%$))


def user_pay_product(request,ids,amt):
    try:

        ab=product_payment.objects.get(ordermaster_id=ids)
        if ab:
            return HttpResponse("<script>alert('Already Paid');window.location='/user_view_booking'</script>")
    except:
        bk=ordermaster.objects.filter(ordermaster_id=ids)
        if request.method=="POST":
            # amount=request.POST['amount']

            ab1=product_payment(amount=amt,payment_for='productpay',payment_date=timezone.now(),user_id=request.session['uid'],ordermaster_id=ids,status='paid')
            ab1.save()
            obj=ordermaster.objects.get(ordermaster_id=ids)
            obj.status='paid'
            obj.save()
            return HttpResponse("<script>alert('Paid');window.location='/user_view_booking'</script>")
        
        return render(request,'user_pay_product.html',{'bk':bk,'amt':amt})
















# def user_pay_product(request,amt):
#     obj=payments(amount=amt,payment_for='productpay',payment_date=timezone.now(),user_id=request.session['uid'])
#     return HttpResponse("<script>alert('Payment completed');window.location='/user_view_products'</script>")

        
    
def user_booking(request,amount,id):
    amount=amount
    if 'add' in request.POST:
        qty=request.POST['qty']
        amount=request.POST['amount']
        ttotal=request.POST['total']

        q=ordermaster.objects.filter(user_id=request.session['uid'],status='pending')
        if q:
            oid=q[0].ordermaster_id
            total=q[0].total
            print("omaster_id...............",oid)
            print("total...............",total)

            q2=orderdetails.objects.filter(ordermaster_id=oid,product_id=id)
            if q2:
                od_id=q2[0].orderdetails_id
                t_qty=q2[0].qty 
                t_amt=q2[0].amount

                oup=orderdetails.objects.get(orderdetails_id=od_id)
                oup.amount=int(t_amt)+int(ttotal)
                oup.qty=int(t_qty)+int(qty)
                oup.save()

                up=ordermaster.objects.get(ordermaster_id=oid)
                up.total=int(total)+int(ttotal)
                up.save() 
                return HttpResponse("<script>alert('Booked....!!');window.location='/user_view_products';</script>")

                print('.....................................................')

            else:
                print('#################################')
                q3=orderdetails(amount=amount,qty=qty,ordermaster_id=oid,product_id=id)
                q3.save()
                up1=ordermaster.objects.get(ordermaster_id=oid)
                up1.total=int(float(total))+int(float(ttotal))
                up1.save()
                print('1111111111111')
                return HttpResponse("<script>alert('Booked....!!');window.location='/user_view_products';</script>")
        
        else:
            oid=ordermaster(total=ttotal,status='pending',user_id=request.session['uid'])
            oid.save()
            q3=orderdetails(amount=amount,qty=qty,ordermaster_id=oid.pk,product_id=id)
            q3.save()
            print('222222222222222')
            return HttpResponse("<script>alert('Booked....!!');window.location='/user_view_products';</script>")
    
        
    return render(request,'user_booking.html',{'amount':amount})

        
  
def user_view_booking(request):
    try:
        v_cart=""
        v=""
        
        v=ordermaster.objects.get(user_id=request.session['uid'],status='pending')
        if v:
            v_cart=orderdetails.objects.filter(ordermaster_id=v.pk)
    except:
        pass
    return render(request,'user_view_booking.html',{'v_cart':v_cart,'v':v})

def remove_cart(request,id,amount,b_id):
    print("$$$$$$$$$$$$$$$$$$$$$$$$")
    print(b_id)
    try:
        od=orderdetails.objects.get(pk=id)
        od.delete()

        od1=orderdetails.objects.filter(ordermaster_id=b_id)
        om=ordermaster.objects.get(pk=b_id)
        if od1:
            om.amount=float(om.amount)-float(amount) 
            om.save()
        else:
            om.delete()
    except:
        pass
   
    return HttpResponse("<script>alert('Sucessfully Removed'); window.location='/user_view_booking'</script>")


def physician_view_workout(request,id):
    ab=user_workouts.objects.filter(user_id=id)
    return render(request,'physician_view_workout.html',{'ab':ab})
        

def card(request,amt):
    obj=users.objects.get(user_id=request.session['uid'])
    print(obj,'/////////////////////////////////////////')
    if 'submit' in request.POST:
        # amt=request.POST['amt']
        ob=payments(amount=amt,payment_for='fee',payment_date=timezone.now(),user_id=request.session['uid'])
        ob.save()

        obj.payment_status='paid'
        obj.save()

        
        return HttpResponse("<script>alert('Payment Completed');window.location='/user_home'</script>")
    return render(request,'card.html',{'amt':amt})


def view_payment(request,ids,cat,qty):
    obj=product_payment.objects.filter(ordermaster_id=ids)
    return render(request,'view_payment.html',{'obj':obj,'cat':cat,'qty':qty})   


def user_view_orders(request):
    orders_with_details = ordermaster.objects.filter(user_id=request.session['uid'], status='paid').prefetch_related('orderdetails_set')

    return render(request, 'user_view_orders.html', {'orders_with_details': orders_with_details})


def view_invoice(request,amount,date,cat,qty):
    obj=users.objects.get(user_id=request.session['uid'])
    return render(request,'invoice.html',{'obj':obj,'amt':amount,'date':date,'cat':cat,'qty':qty})


def employee_add_exercise(request,id,ids):
    if request.method=="POST":
        details=request.POST['details']

        exercise_details=exercise(details=details,user_workout_id=id,user_id=ids)
        exercise_details.save()

        return HttpResponse("<script>alert('Exercise Added');window.location='employee_add_exercise'</script>")
    
    return render(request,'employee_add_exercise.html')

def view_exercise(request,id):
    ve=exercise.objects.filter(user_workout_id=id)
    return render(request,'view_exercise.html',{'ve':ve})


def book_physician_pay(request,ids):
    obj=users.objects.get(user_id=request.session['uid'])
    print(obj,'/////////////////////////////////////////')
    if request.method=="POST":
        # amt=request.POST['amt']
        amt=5000
        ob=payments(amount=5000,payment_for='subscription',payment_date=timezone.now(),user_id=request.session['uid'])
        ob.save()

        obj=subscription(physician_id=ids,user_id=request.session['uid'])
        obj.save()
            
        return HttpResponse("<script>alert('Payment Completed');window.location='/user_home'</script>")

    return render(request,'book_physician_pay.html')


def employee_add_attendence(request,id):
    from datetime import date
    today=date.today()
    try:

        obj=attendances.objects.get(user_id=id,date=today)
        return HttpResponse("<script>alert('Already Marked For Today');window.location='/employee_add_user_details'</script>")
    except:
        obj=attendances(date=today,status='present',user_id=id)
        obj.save()
        return HttpResponse("<script>alert('Attendance Marked ');window.location='/employee_add_user_details'</script>")


def user_view_attendence(request):
    obj=attendances.objects.filter(user_id=request.session['uid'])
    return render(request,'user_view_attendence.html',{'obj':obj})


def bmi_temp(request):
    return render(request,'bmi_value.html')


def user_view_bmi(request):
    # Get the user's data from the database
    user = users.objects.get(user_id=request.session['uid'])
    
    # Retrieve height and weight data
    height = user.height  # Height in meters
    weight = user.weight  # Weight in kilograms

    weight = float(weight)
    height = float(height)

# Check if height is greater than 0 to avoid division by zero
    if height > 0:
        # Calculate BMI
        bmi = weight / (height * height)
        print(bmi,'//////////bbb')
    else:
        # Handle the case where height is 0 or negative
        # You may want to return an error message or handle it according to your requirements
        bmi = None

    return JsonResponse({'bmi': bmi})

def user_predict(request):
    res=""
    from samp import predict

    if 'submit' in request.POST:
        height=request.POST['height']
        weight=request.POST['weight']
        cal=request.POST['cal']
        exercise=request.POST['excercise']
        job=request.POST['job']
        gender=request.POST['gender']

        new_data=[height,weight,cal,exercise,job]

        res=predict(new_data)
        print(res[0],res[1],res[2],res[3],res[4])
        qa=predict_work(user_id=request.session['uid'],output=res[4])
        qa.save()
        return render(request,'user_predict.html',{'res':res[0],'res1':res[1],'res2':res[2],'res3':res[3],'res4':res[4]})

    return render(request,'user_predict.html')