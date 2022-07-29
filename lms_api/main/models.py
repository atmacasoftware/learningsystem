from django.db import models

# Create your models here.

class Teacher(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    mobile_no = models.CharField(max_length=100, null=True)
    skills = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "1. Teachers"

class CourseCategory(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "2. Course Categories"

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "3. Courses"

class Student(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    mobile_no = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    interested_categories = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "4. Students"