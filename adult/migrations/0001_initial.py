# Generated by Django 2.0.5 on 2018-05-27 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=20)),
                ('fnlwgt', models.IntegerField(default=100000)),
                ('education_num', models.IntegerField(default=20)),
                ('capital_gain', models.IntegerField(default=10)),
                ('capital_loss', models.IntegerField(default=10)),
                ('hours_per_week', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Some-college', 'Some-college'), ('11th', '11th'), ('HS-grad', 'HS-grad'), ('Assoc-acdm', 'Assoc-acdm'), ('9th', '9th'), ('7th-8th', '7th-8th'), ('Masters', 'Masters'), ('1st-4th', '1st-4th'), ('10th', '10th'), ('Doctorate', 'Doctorate'), ('5th-6th', '5th-6th'), ('Preschool', 'Preschool')], max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MartialStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('martialstatus', models.CharField(choices=[('Married-civ-spouse', 'Married-civ-spouse'), ('Divorced', 'Divorced'), ('Never-married', 'Never-married'), ('Separated', 'Separated'), ('Widowed', 'Widowed'), ('Married-spouse-absent', 'Married-spouse-absent'), ('Married-AF-spouse', 'Married-AF-spouse')], max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NativeCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nativecountry', models.CharField(choices=[('United-States', 'United-States'), ('Cambodia', 'Cambodia'), ('England', 'England'), ('Puerto-Rico', 'Puerto-Rico'), ('Canada', 'Canada'), ('Germany', 'Germany'), ('Outlying-US', 'Outlying-US(Guam-USVI-etc)'), ('India', 'India'), ('Japan', 'Japan'), ('Greece', 'Greece'), ('South', 'South'), ('China', 'China'), ('Cuba', 'Cuba'), ('Iran', 'Iran'), ('Honduras', 'Honduras'), ('Philippines', 'Philippines'), ('Italy', 'Italy'), ('Poland', 'Poland'), ('Jamaica', 'Jamaica'), ('Vietnam', 'Vietnam'), ('Mexico', 'Mexico'), ('Portugal', 'Portugal'), ('Ireland', 'Ireland'), ('France', 'France'), ('Dominican-Republic', 'Dominican-Republic'), ('Laos', 'Laos'), ('Ecuador', 'Ecuador'), ('Taiwan', 'Taiwan'), ('Haiti', 'Haiti'), ('Columbia', 'Columbia'), ('Hungary', 'Hungary'), ('Guatemala', 'Guatemala'), ('Nicaragua', 'Nicaragua'), ('Scotland', 'Scotland'), ('Thailand', 'Thailand'), ('Yugoslavia', 'Yugoslavia'), ('El-Salvador', 'El-Salvador'), ('Trinadad&Tobago', 'Trinadad&Tobago'), ('Peru', 'Peru'), ('HongKong', 'HongKong'), ('Holand-Netherlands', 'Holand-Netherlands')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(choices=[('Wife', 'Wife'), ('Own-child', 'Own-child'), ('Husband', 'Husband'), ('Not-in-family', 'Not-in-family'), ('Other-relative', 'Other-relative'), ('Unmarried', 'Unmarried')], max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('White', 'White'), ('Asian-Pac-Islander', 'Asian-Pac-Islander'), ('Amer-Indian-Eskimo', 'Amer-Indian-Eskimo'), ('Other', 'Other'), ('Black', 'Black')], max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(choices=[('Wife', 'Wife'), ('Own-child', 'Own-child'), ('Husband', 'Husband'), ('Not-in-family', 'Not-in-family'), ('Other-relative', 'Other-relative'), ('Unmarried', 'Unmarried')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workclass', models.CharField(choices=[('Private', 'Private'), ('Self-emp-not-inc', 'Self-emp-not-inc'), ('Self-emp-inc', 'Self-emp-inc'), ('Federal-gov', 'Federal-gov'), ('Local-gov', 'Local-gov'), ('State-gov', 'State-gov'), ('Without-pay', 'Without-pay'), ('Never-worked', 'Never-worked')], max_length=17, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='adult',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.Education'),
        ),
        migrations.AddField(
            model_name='adult',
            name='marital_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.MartialStatus'),
        ),
        migrations.AddField(
            model_name='adult',
            name='native_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.NativeCountry'),
        ),
        migrations.AddField(
            model_name='adult',
            name='occupation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.Occupation'),
        ),
        migrations.AddField(
            model_name='adult',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.Race'),
        ),
        migrations.AddField(
            model_name='adult',
            name='relationship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.Relationship'),
        ),
        migrations.AddField(
            model_name='adult',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.Sex'),
        ),
        migrations.AddField(
            model_name='adult',
            name='workclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adult.WorkClass'),
        ),
    ]
