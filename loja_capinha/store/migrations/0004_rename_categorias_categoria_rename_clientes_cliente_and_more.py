# Generated by Django 4.1.7 on 2023-02-18 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_customer_clientes_rename_order_pedidos_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
        migrations.RenameModel(
            old_name='Produtos',
            new_name='Produto',
        ),
    ]