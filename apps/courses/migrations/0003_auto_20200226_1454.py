# Generated by Django 2.2 on 2020-02-26 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_courseorg_course_nums'),
        ('courses', '0002_auto_20200224_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='organizations.CourseOrg', verbose_name='课程机构'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(max_length=300, verbose_name='课程描述'),
        ),
    ]