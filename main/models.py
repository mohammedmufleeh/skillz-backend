



from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

from teacher_app.models import Course,Teacher
# Create your models here.

# 

class MyAccountManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Please Enter Email')
        if not password:
            raise ValueError('Please Enter Password')    
        user = self.model(
            email = self.normalize_email(email),

        )    
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.is_verified = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password
        )
    
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.is_verified=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    mobile = models.CharField(max_length=10,unique=True,null=True)
    password = models.CharField(max_length=200,blank=False,null=False)
    profile_dp = models.ImageField(upload_to='photos/users_dp/',blank=True)
    bio = models.TextField(blank=True,null=True)
    interests = models.TextField(max_length=100,null=True,blank=True)
    
    courses_entrolled = models.IntegerField(default=0)

    joined_date = models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(auto_now=True)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=False)
    is_verified     =models.BooleanField(default=False)
    is_superuser   =models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['password']

    objects =MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,add_label):
        return True

class FavoriteCourse(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student =models.ForeignKey(Account,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="7. student favorite Course"
    
    def __str__(self):
        return f"{self.course}.{self.student}"
    
    

class CourseRating(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    rating=models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    review_time=models.DateTimeField(auto_now_add=True)
    demo = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.course}.{self.student}.{self.rating}"

class StudentAssignment(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200,blank=True)
    file=models.FileField(upload_to='assigment/',blank=True)
    detail = models.TextField(null=True)
    add_time=models.DateTimeField(auto_now_add=True)
    is_submitted=models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.title}.{self.student}"

class AssignmentAnswer(models.Model):
    assignment = models.ForeignKey(StudentAssignment,on_delete=models.CASCADE)
    detail = models.TextField(null=True)
    file=models.FileField(upload_to='assigmentanswer/',blank=True)
   
    

    def __str__(self):
        return f"{self.assignment}"







