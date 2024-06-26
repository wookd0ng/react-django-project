from django.db import models

class IDRecord(models.Model):
    id_value = models.CharField(max_length=255, unique=True)
    content = models.TextField()  # content 필드 추가
    category = models.CharField(max_length=255)  # category 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_value
