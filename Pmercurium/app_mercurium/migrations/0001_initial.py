# Generated by Django 3.2 on 2021-07-12 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome Carteira')),
                ('limit', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Limite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('original_value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Valor original')),
                ('type_item', models.CharField(choices=[('Receita', 'Receita'), ('Despesa', 'Despesa')], max_length=50, verbose_name='Tipo')),
                ('date', models.DateField(verbose_name='Data')),
                ('status_payment', models.BooleanField(default=True, verbose_name='Pago')),
                ('date_payment', models.DateField(blank=True, verbose_name='Data Vencimento')),
                ('fees', models.DecimalField(blank=True, decimal_places=1, max_digits=5, verbose_name='Juros')),
                ('status', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mercurium.category', verbose_name='Categoria')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mercurium.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mercurium.wallet'),
        ),
    ]
