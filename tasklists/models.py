from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return self.name

class Users(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    dob = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    sex = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/')
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(1)

    def __str__(self):
        return self.firstname

class TaskType(models.Model):
    name = models.CharField(max_length=150)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    notes = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TaskComment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    
class TaskUser(models.Model):
    status = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_id