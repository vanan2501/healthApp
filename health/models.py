from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['id']

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Người dùng cá nhân'),
        ('expert', 'Chuyên gia dinh dưỡng/huấn luyện viên'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Vai trò
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to= 'user/%Y/%m/', null= True)



class HealthProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(help_text="Chiều cao (cm)")
    weight = models.FloatField(help_text="Cân nặng (kg)")
    age = models.IntegerField(help_text="Tuổi")
    health_target = models.TextField(help_text="Mục tiêu sức khỏe", blank=True)
    bmi = models.FloatField(help_text="Chỉ số BMI", blank=True, null=True)
    daily_water_intake = models.FloatField(help_text="Số lượng nước uống hàng ngày (lít)", blank=True, null=True)
    steps = models.IntegerField(help_text="Số bước đi hàng ngày", blank=True, null=True)
    heart_rate = models.IntegerField(help_text="Nhịp tim", blank=True, null=True)  # Kết nối thiết bị đeo


class ExercisePlan(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100, help_text="Tên bài tập")
    duration = models.IntegerField(help_text="Thời gian tập luyện (phút)")
    calories_burned = models.FloatField(help_text="Lượng calo tiêu thụ")



class DietPlan(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diet_name = models.CharField(max_length=100, help_text="Tên thực đơn")
    calories = models.FloatField(help_text="Lượng calo")
    protein = models.FloatField(help_text="Lượng protein (g)")
    fat = models.FloatField(help_text="Lượng chất béo (g)")
    carbs = models.FloatField(help_text="Lượng carbohydrate (g)")
    image = models.ImageField(upload_to= 'diet/%Y/%m/', null=True)


class Reminder(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_type = models.CharField(max_length=50, help_text="Loại nhắc nhở: uống nước, tập luyện, nghỉ ngơi")
    time = models.TimeField(help_text="Thời gian nhắc nhở")
    message = models.TextField(help_text="Nội dung nhắc nhở")



class HealthLog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.TextField(help_text="Cảm nhận sau buổi tập")
    notes = models.TextField(help_text="Ghi chú khác", blank=True)


class Chat(BaseModel):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField(help_text="Tin nhắn")
    timestamp = models.DateTimeField(auto_now_add=True)


class Statistics(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weekly_progress = models.JSONField(help_text="Tiến độ hàng tuần: thời gian tập luyện, lượng calo tiêu thụ, ...")
    monthly_progress = models.JSONField(help_text="Tiến độ hàng tháng")
    yearly_progress = models.JSONField(help_text="Tiến độ hàng năm")