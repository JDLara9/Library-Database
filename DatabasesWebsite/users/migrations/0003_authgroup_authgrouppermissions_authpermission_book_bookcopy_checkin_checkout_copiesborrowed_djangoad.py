# Generated by Django 2.1.3 on 2019-04-06 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(db_column='ISBN', max_length=13, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=30, null=True)),
                ('author', models.CharField(blank=True, db_column='Author', max_length=30, null=True)),
                ('genre', models.CharField(blank=True, db_column='Genre', max_length=8, null=True)),
                ('copies', models.IntegerField(db_column='Copies')),
            ],
            options={
                'db_table': 'Book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datecheckedin', models.DateField(db_column='DateCheckedIn')),
            ],
            options={
                'db_table': 'CheckIn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('transactionid', models.IntegerField(db_column='TransactionID', primary_key=True, serialize=False)),
                ('checkoutdate', models.DateField(db_column='CheckOutDate')),
                ('duedate', models.DateField(db_column='DueDate')),
            ],
            options={
                'db_table': 'CheckOut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Finetransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transtype', models.CharField(db_column='TransType', max_length=7)),
                ('transactiondate', models.DateField(db_column='TransactionDate')),
                ('amount', models.DecimalField(db_column='Amount', decimal_places=2, max_digits=4)),
            ],
            options={
                'db_table': 'FineTransactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Holds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holddate', models.DateField(blank=True, db_column='HoldDate', null=True)),
                ('helduntildate', models.DateField(blank=True, db_column='HeldUntilDate', null=True)),
            ],
            options={
                'db_table': 'Holds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemid', models.IntegerField(db_column='itemID', primary_key=True, serialize=False)),
                ('itemtype', models.CharField(blank=True, db_column='ItemType', max_length=5, null=True)),
            ],
            options={
                'db_table': 'Item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('isan', models.CharField(db_column='ISAN', max_length=24, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=30, null=True)),
                ('director', models.CharField(blank=True, db_column='Director', max_length=25, null=True)),
                ('rating', models.CharField(blank=True, db_column='Rating', max_length=5, null=True)),
                ('genre', models.CharField(blank=True, db_column='Genre', max_length=15, null=True)),
                ('copies', models.IntegerField(db_column='Copies')),
            ],
            options={
                'db_table': 'Movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('rolename', models.CharField(db_column='RoleName', max_length=5, primary_key=True, serialize=False)),
                ('role_description', models.CharField(db_column='Role Description', max_length=15)),
            ],
            options={
                'db_table': 'Roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sheetmusic',
            fields=[
                ('ismn', models.CharField(db_column='ISMN', max_length=13, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=30, null=True)),
                ('composer', models.CharField(blank=True, db_column='Composer', max_length=25, null=True)),
                ('genre', models.CharField(blank=True, db_column='Genre', max_length=15, null=True)),
                ('copies', models.IntegerField(db_column='Copies')),
            ],
            options={
                'db_table': 'SheetMusic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.AutoField(db_column='idUser', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=45)),
                ('middlein', models.CharField(blank=True, db_column='MiddleIn', max_length=1, null=True)),
                ('lastname', models.CharField(db_column='LastName', max_length=45)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=15, null=True)),
                ('birthdate', models.DateField(blank=True, db_column='BirthDate', null=True)),
                ('email', models.CharField(db_column='Email', max_length=45)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersCustomuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'users_customuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersCustomuserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'users_customuser_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersCustomuserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'users_customuser_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookcopy',
            fields=[
                ('itemid', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.Item')),
                ('checkedout', models.IntegerField(db_column='CheckedOut')),
            ],
            options={
                'db_table': 'BookCopy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Copiesborrowed',
            fields=[
                ('idUser', models.ForeignKey(db_column='ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.User')),
                ('copies_borrowed', models.IntegerField(db_column='Copies_Borrowed')),
            ],
            options={
                'db_table': 'CopiesBorrowed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Finesrecord',
            fields=[
                ('idUser', models.ForeignKey(db_column='ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.User')),
                ('amount', models.DecimalField(blank=True, db_column='Amount', decimal_places=2, max_digits=4, null=True)),
            ],
            options={
                'db_table': 'FinesRecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logincredentials',
            fields=[
                ('idUser', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.User')),
                ('user_password', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'LoginCredentials',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Moviecopy',
            fields=[
                ('itemid', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.Item')),
                ('checkedout', models.IntegerField(db_column='CheckedOut')),
            ],
            options={
                'db_table': 'MovieCopy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Musiccopy',
            fields=[
                ('itemid', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.Item')),
                ('checkedout', models.IntegerField(db_column='CheckedOut')),
            ],
            options={
                'db_table': 'MusicCopy',
                'managed': False,
            },
        ),
    ]
