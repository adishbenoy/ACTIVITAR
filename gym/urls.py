"""gym_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.log,name='log'),
    path('user_reg',views.user_reg,name='user_reg'),
    
#####################ADMIN###################################################################################

    path('admin_home',views.admin_home,name='admin_home'),
    path('reg_employee',views.reg_employee,name='reg_employee'),
    path('admin_update_emp/<ids>',views.admin_update_emp,name='admin_update_emp'),
    path('admin_delete_emp/<ids>',views.admin_delete_emp,name='admin_delete_emp'),
    path('reg_physician',views.reg_physician,name='reg_physician'),
    path('admin_update_physi/<ids>',views.admin_update_physi,name='admin_update_physi'),
    path('admin_delete_physi/<ids>',views.admin_delete_physi,name='admin_delete_physi'),
    path('admin_verify_user',views.admin_verify_user,name='admin_verify_user'),
    path('verify_user/<ids>',views.verify_user,name='verify_user'),
    path('admin_view_feedback',views.admin_view_feedback,name='admin_view_feedback'),
    path('admin_reply/<ids>',views.admin_reply,name='admin_reply'),
    path('admin_view_complaints',views.admin_view_complaints,name='admin_view_complaints'),
    path('admin_reply_complaint/<ids>',views.admin_reply_complaint,name='admin_reply_complaint'),
    path('admin_view_payment',views.admin_view_payment,name='admin_view_payment'),
    path('admin_add_new_batches',views.admin_add_new_batches,name='admin_add_new_batches'),
    path('admin_delete_batch/<ids>',views.admin_delete_batch,name='admin_delete_batch'),
    
##########################EMPLOYEE############################################################################################

    path('employee_home',views.employee_home,name='employee_home'),
    path('employee_manage_equipments',views.employee_manage_equipments,name='employee_manage_equipments'),
    path('emp_update/<ids>',views.emp_update,name='emp_update'),
    path('emp_delete/<ids>',views.emp_delete,name='emp_delete'),
    path('employee_manage_workout_details',views.employee_manage_workout_details,name='employee_manage_workout_details'),
    path('emp_update_work/<ids>',views.emp_update_work,name='emp_update_work'),
    path('emp_delete_work/<ids>',views.emp_delete_work,name='emp_delete_work'),
    path('employee_add_user_details',views.employee_add_user_details,name='employee_add_user_details'),
    path('employee_personalised_workout_details/<ids>',views.employee_personalised_workout_details,name='employee_personalised_workout_details'),
    path('user_workout_id/<ids>',views.user_workout_id,name='user_workout_id'),
    path('employee_add_exercise/<id>/<ids>',views.employee_add_exercise,name='employee_add_exercise'),
    path('employee_add_attendence/<id>',views.employee_add_attendence,name='employee_add_attendence'),
    path('employee_view_work/<id>',views.employee_view_work,name='employee_view_work'),

    
###########################PHYSICIAN######################################################################################################################

    path('physician_home',views.physician_home,name='physician_home'),
    path('physician_view_users',views.physician_view_users,name='physician_view_users'),
    path('calculate_bmi/<ids>',views.calculate_bmi,name='calculate_bmi'),
    path('physician_create_personalised_diet_plan/<ids>',views.physician_create_personalised_diet_plan,name='physician_create_personalised_diet_plan'),
    path('update_diet/<ids>',views.update_diet,name='update_diet'),
    path('physician_view_message_from_users',views.physician_view_message_from_users,name='physician_view_message_from_users'),
    path('phy_send_reply/<ids>',views.phy_send_reply,name='phy_send_reply'),
    path('physician_view_workout/<id>',views.physician_view_workout,name='physician_view_workout'),
    
    
##################################SHOP########################################################################################################################

    path('shop_home',views.shop_home,name='shop_home'),
    path('shop_manage_products',views.shop_manage_products,name='shop_manage_products'),
    path('shop_update/<ids>',views.shop_update,name='shop_update'),
    path('shop_view_booking/<ids>',views.shop_view_booking,name='shop_view_booking'),
    path('shop_view_payment/<ids>',views.shop_view_payment,name='shop_view_payment'),


#################################USER#################################################################################################################################

    path('user_home',views.user_home,name='user_home'),
    path('user_view_batch',views.user_view_batch,name='user_view_batch'),
    path('user_make_payment',views.user_make_payment,name='user_make_payment'),
    path('view_daily_workout',views.view_daily_workout,name='view_daily_workout'),
    path('view_equipments/<ids>',views.view_equipments,name='view_equipments'),
    path('view_physicians',views.view_physicians,name='view_physicians'),
    path('book_physician/<ids>',views.book_physician,name='book_physician'),
    path('view_diet_plan/<ids>',views.view_diet_plan,name='view_diet_plan'),
    path('user_send_messgae/<ids>',views.user_send_messgae,name='user_send_messgae'),
    path('user_send_feedback',views.user_send_feedback,name='user_send_feedback'),
    path('user_view_products',views.user_view_products,name='user_view_products'),
    # path('user_pay_product/<amt>',views.user_pay_product,name='user_pay_product'),
    path('user_booking/<amount>/<id>',views.user_booking,name='user_booking'),
    path('user_view_booking',views.user_view_booking,name='user_view_booking'),
    path('remove_cart/<id>/<amount>/<b_id>',views.remove_cart,name='user_booking'),
    path('user_pay_product/<ids>/<amt>',views.user_pay_product,name='user_pay_product'),
    path('card/<amt>',views.card,name='card'),
    path('user_view_orders',views.user_view_orders,name='user_view_orders'),
    path('view_payment/<ids>/<cat>/<qty>',views.view_payment,name='view_payment'),
    path('view_invoice/<amount>/<date>/<cat>/<qty>',views.view_invoice,name='view_invoice'),
    path('view_exercise/<id>',views.view_exercise,name='view_exercise'),
    path('book_physician_pay/<ids>',views.book_physician_pay,name='book_physician_pay'),
    path('user_view_attendence',views.user_view_attendence,name='user_view_attendence'),
    path('user_predict',views.user_predict,name='user_predict'),
    path('bmi_temp',views.bmi_temp,name='bmi_temp'),
    path('user_view_bmi',views.user_view_bmi,name='user_view_bmi'),
    
    

    
    
    
    
    

    
    



    
]
