from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
# Create your models here.


class first_user (models.Model):
    user_id = models.AutoField
    password = models.CharField(max_length=20)


class detail_of_worker(models.Model):
        id = models.AutoField(primary_key=True)
        name_worker = models.CharField(max_length=50)
        headname_worker = models.CharField(max_length=50)
        address_worker = models.CharField(max_length=100)
        mobile_worker = models.BigIntegerField()
        addhar_worker = models.BigIntegerField()
        gender_worker = models.CharField(max_length=6)
        dob_worker = models.DateField()
        age_worker = models.PositiveIntegerField()
        image_worker = models.ImageField(upload_to='static/worker_photo')
        state_worker = models.CharField(max_length=30)
        distric_worker = models.CharField(max_length=30)
        block_worker = models.CharField(max_length=30)
        panchayat_worker = models.CharField(max_length=30)
        account_worker = models.BigIntegerField()
        ifsc_worker = models.CharField(max_length=11)
        bank_worker = models.CharField(max_length=35)
        ap_no_worker = models.BigIntegerField(unique=True)
        card_no = models.CharField(max_length=16, default='not issued')
        card_status = models.CharField(max_length=15, default='not issued')
        verify_name = models.CharField(max_length=50, default='rejected due to name not matched')
        verify_addhar = models.CharField(max_length=50, default='rejected due to addhar not matched')
        verify_gender = models.CharField(max_length=50, default='rejected due to gender not matched')
        verify_image = models.CharField(max_length=50, default='rejected due to image not matched')
        verify_address = models.CharField(max_length=50, default='rejected due to address not matched')
        verify_account = models.CharField(max_length=50, default='rejected due to account not matched')
        verify_bank = models.CharField(max_length=50, default='rejected due to bank not matched')
        verify_ifsc = models.CharField(max_length=50, default='rejected due to ifsc code not matched')


class photo(models.Model):
        id = models.AutoField(primary_key=True)
        worker_name = models.CharField(max_length=50,null=True,blank=True)
        worker_jobcard_no = models.CharField(max_length=16,null=True,blank=True)
        worker_app_no = models.BigIntegerField()
        image1 = models.ImageField(null=True,blank=True)
        image2 = models.ImageField(null=True,blank=True)
        image3 = models.ImageField(null=True,blank=True)
        image4 = models.ImageField(null=True,blank=True)
        image5 = models.ImageField(null=True,blank=True)
        image6 = models.ImageField(null=True,blank=True)
        image7 = models.ImageField(null=True,blank=True)
        image8 = models.ImageField(null=True,blank=True)
        image9 = models.ImageField(null=True,blank=True)
        image10 = models.ImageField(null=True,blank=True)
        image11 = models.ImageField(null=True,blank=True)
        image12 = models.ImageField(null=True,blank=True)
        image13 = models.ImageField(null=True,blank=True)
        image14 = models.ImageField(null=True,blank=True)
        image15 = models.ImageField(null=True,blank=True)
        image_status = models.CharField(max_length=20, default='not captured')


# class User(AbstractUser):
#         is_office = models.BooleanField(default=False)
#         is_onfield = models.BooleanField(default=False)

# class onfield(models.Model):
#         user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=10000,blank=True)
#         password = models.CharField(max_length=16, blank=False)
#         name = models.CharField(max_length=30, default='hello')
#         gender = models.CharField(max_length=10, blank=False, default='male')
#         mobile_no = models.BigIntegerField(default='10')
#         addhar_no = models.BigIntegerField(default='10')
#         office_id = models.BigIntegerField(default=10000)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         onfield.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class attendence(models.Model):
        worker = models.ForeignKey(detail_of_worker, on_delete=models.CASCADE, related_name='worker')
        date = models.DateField(default=datetime.now().strftime("%Y.%M.%D"))
        time = models.TimeField(auto_now_add=True)
        mark_attendence = models.CharField(max_length=10, default='absent')

class attends(models.Model):
        id= models.AutoField(primary_key=True)
        worker_ap_no = models.BigIntegerField()
        date = models.DateField()
        time = models.TimeField(auto_now_add=True)
        mark_attendence = models.CharField(max_length=10, default='absent')
        worker_names = models.CharField(max_length=35)
        worker_job_no = models.CharField(max_length=20)
        mobile_worker = models.BigIntegerField()


class work(models.Model):
        worker_app = models.BigIntegerField()
        worker_job = models.CharField(max_length=20)
        date =models.DateField(null=True)
        grampanchayat =models.CharField(max_length=30)
        work = models.CharField(max_length=90)

class State(models.Model):
        state = models.CharField(max_length=30)

class District(models.Model):
        district = models.CharField(max_length=60)
        state = models.ForeignKey(State, on_delete=models.CASCADE)




# # class office(AbstractBaseUser):
# #         user_id = models.IntegerField(unique=True)
# #         password = models.CharField(max_length=16)
# #         name = models.CharField(max_length=30)
# #
# #         USERNAME_FIELD = 'user_id'
# #         REQUIRED_FIELDS = ['password']
# #         is_admin = models.BooleanField(default=False)
# #         is_active =models.BooleanField(default=True)
# #         is_staff =models.BooleanField(default=False)
# #         is_superuser =models.BooleanField(default=False)