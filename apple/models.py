from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    runnumber = models.CharField(max_length=50, default="#")
    studentID = models.CharField(max_length=50, blank=True, null=True)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    Firstname = models.CharField(max_length=255, blank=True, null=True)
    Lastname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("studentID",)

    def __str__(self):
        return f"{self.studentID or '-'} - {self.Firstname or ''} {self.Lastname or ''}".strip()