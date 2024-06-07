# Generated by Django 5.0.6 on 2024-06-07 12:30

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('medical_examination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото')),
                ('groups', models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения предоставлено каждой из их групп.', related_name='custom_user_set', related_query_name='user', to='auth.group', verbose_name='Группы')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Специальные разрешения для этого юзера.', related_name='custom_user_set', related_query_name='user', to='auth.permission', verbose_name='Разрешения для юзера')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('place_of_work', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('ceo', 'Руководитель'), ('hr', 'Кадровик'), ('doctor', 'Врач')], max_length=255)),
                ('wage_rate', models.DecimalField(choices=[(0.25, '0.25'), (0.5, '0.5'), (0.75, '0.75'), (1.0, '1.0'), (1.25, '1.25')], decimal_places=2, default=1, max_digits=3)),
                ('date_of_birth', models.DateField()),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.specialization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileModality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.BooleanField(default=False, null=True)),
                ('modality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_examination.modality')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
            options={
                'unique_together': {('user_profile', 'modality')},
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modality',
            field=models.ManyToManyField(through='users.UserProfileModality', to='medical_examination.modality'),
        ),
    ]
