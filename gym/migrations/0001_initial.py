# Generated by Django 3.2.24 on 2024-04-19 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batches',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('batch_name', models.CharField(max_length=225)),
                ('start_time', models.CharField(max_length=225)),
                ('end_time', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='static/media')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('usertype', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='ordermaster',
            fields=[
                ('ordermaster_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='physician',
            fields=[
                ('physician_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('qualification', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.login')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=225)),
                ('product_name', models.CharField(max_length=225)),
                ('amount', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='workout',
            fields=[
                ('workout_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('benefits', models.CharField(max_length=225)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('weight', models.CharField(max_length=225)),
                ('height', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=800)),
                ('goal', models.CharField(max_length=225)),
                ('payment_status', models.CharField(max_length=225)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.batches')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.login')),
            ],
        ),
        migrations.CreateModel(
            name='user_workouts',
            fields=[
                ('user_workout_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=225)),
                ('duration', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.workout')),
            ],
        ),
        migrations.CreateModel(
            name='user_diets',
            fields=[
                ('user_diets_id', models.AutoField(primary_key=True, serialize=False)),
                ('diet_details', models.CharField(max_length=225)),
                ('diet_date', models.CharField(max_length=225)),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.physician')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('subscription_id', models.AutoField(primary_key=True, serialize=False)),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.physician')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.login')),
            ],
        ),
        migrations.CreateModel(
            name='productbooking',
            fields=[
                ('productbooking_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.CreateModel(
            name='product_payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=225)),
                ('payment_for', models.CharField(max_length=225)),
                ('payment_date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('ordermaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.ordermaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.shop'),
        ),
        migrations.CreateModel(
            name='predict_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=225)),
                ('payment_for', models.CharField(max_length=225)),
                ('payment_date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.AddField(
            model_name='ordermaster',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users'),
        ),
        migrations.CreateModel(
            name='orderdetails',
            fields=[
                ('orderdetails_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('qty', models.CharField(max_length=100, null=True)),
                ('ordermaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.ordermaster')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.product')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_description', models.CharField(max_length=225)),
                ('message_reply', models.CharField(max_length=225)),
                ('message_date', models.CharField(max_length=225)),
                ('physician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.physician')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.CreateModel(
            name='gym_instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.login')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_desc', models.CharField(max_length=225)),
                ('feedback_reply', models.CharField(max_length=225)),
                ('feedback_date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('exercise_id', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
                ('user_workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.workout')),
            ],
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=225)),
                ('reply', models.CharField(max_length=225)),
                ('complaint_date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
        migrations.AddField(
            model_name='batches',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.gym_instructor'),
        ),
        migrations.CreateModel(
            name='attendances',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.users')),
            ],
        ),
    ]
