# Generated by Django 4.2.5 on 2023-09-08 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_email"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "사용자",
                "verbose_name_plural": "사용자 목록",
            },
        ),
        migrations.AlterField(
            model_name="profile",
            name="nickname",
            field=models.TextField(max_length=30, unique=True, verbose_name="닉네임"),
        ),
        migrations.AddIndex(
            model_name="user",
            index=models.Index(
                fields=["-created_at"], name="users_user_created_5b2332_idx"
            ),
        ),
    ]