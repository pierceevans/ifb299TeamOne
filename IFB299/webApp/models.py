# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Car(models.Model):
    car_id = models.IntegerField(db_column='Car_ID', primary_key=True)  # Field name made lowercase.
    car_make_key = models.ForeignKey('Make', models.DO_NOTHING, db_column='Car_Make_Key', blank=True, null=True)  # Field name made lowercase.
    car_series_year = models.IntegerField(db_column='Car_Series_Year', blank=True, null=True)  # Field name made lowercase.
    car_pricenew = models.IntegerField(db_column='Car_PriceNew', blank=True, null=True)  # Field name made lowercase.
    car_enginesize = models.CharField(db_column='Car_EngineSize', max_length=4, blank=True, null=True)  # Field name made lowercase.
    car_fuelsystem = models.CharField(db_column='Car_FuelSystem', max_length=25, blank=True, null=True)  # Field name made lowercase.
    car_tankcapacity = models.CharField(db_column='Car_TankCapacity', max_length=6, blank=True, null=True)  # Field name made lowercase.
    car_power = models.CharField(db_column='Car_Power', max_length=5, blank=True, null=True)  # Field name made lowercase.
    car_seatingcapacity = models.IntegerField(db_column='Car_SeatingCapacity', blank=True, null=True)  # Field name made lowercase.
    car_standardcapacity = models.CharField(db_column='Car_StandardCapacity', max_length=5, blank=True, null=True)  # Field name made lowercase.
    car_bodytype = models.CharField(db_column='Car_BodyType', max_length=15, blank=True, null=True)  # Field name made lowercase.
    car_drive = models.CharField(db_column='Car_Drive', max_length=3, blank=True, null=True)  # Field name made lowercase.
    car_wheelbase = models.CharField(db_column='Car_Wheelbase', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'car'


class Customer(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=25)  # Field name made lowercase.
    customer_phone = models.CharField(db_column='Customer_Phone', max_length=30)  # Field name made lowercase.
    customer_address = models.CharField(db_column='Customer_Address', max_length=35)  # Field name made lowercase.
    customer_birthday = models.DateField(db_column='Customer_Birthday')  # Field name made lowercase.
    customer_occupation = models.CharField(db_column='Customer_Occupation', max_length=20)  # Field name made lowercase.
    customer_gender = models.CharField(db_column='Customer_Gender', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    location_id = models.IntegerField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
    store_state = models.CharField(db_column='Store_State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_city = models.CharField(db_column='Store_City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_address = models.CharField(db_column='Store_Address', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class Make(models.Model):
    car_make_key = models.IntegerField(db_column='Car_Make_Key', primary_key=True)  # Field name made lowercase.
    car_make_name = models.CharField(db_column='Car_Make_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    car_model = models.CharField(db_column='Car_Model', max_length=25, blank=True, null=True)  # Field name made lowercase.
    car_series = models.CharField(db_column='Car_Series', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'make'


class Order(models.Model):
    order_id = models.IntegerField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID')  # Field name made lowercase.
    car = models.ForeignKey(Car, models.DO_NOTHING, db_column='Car_ID')  # Field name made lowercase.
    pickup_store = models.ForeignKey('Store', models.DO_NOTHING, db_column='Pickup_Store_ID', related_name="return_store")  # Field name made lowercase.
    return_store = models.ForeignKey('Store', models.DO_NOTHING, db_column='Return_Store_ID', related_name="pickup_store")  # Field name made lowercase.
    order_create_date = models.ForeignKey('Time', models.DO_NOTHING, db_column='Order_Create_Date_ID', related_name="pickup_date")  # Field name made lowercase.
    pickup_date = models.ForeignKey('Time', models.DO_NOTHING, db_column='Pickup_Date_ID', related_name="return_date")  # Field name made lowercase.
    return_date = models.ForeignKey('Time', models.DO_NOTHING, db_column='Return_Date_ID', related_name="order_create_date")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Store(models.Model):
    store_id = models.IntegerField(db_column='Store_ID', primary_key=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='Store_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    store_phone = models.CharField(db_column='Store_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class Time(models.Model):
    time_id = models.IntegerField(db_column='Time_ID', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month')  # Field name made lowercase.
    day = models.IntegerField(db_column='Day')  # Field name made lowercase.
    date = models.IntegerField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time'
