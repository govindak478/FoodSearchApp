# Generated by Django 4.2.5 on 2023-10-02 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("foodsearchapp", "0003_alter_fooditem_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=255)),
                ("product_description", models.CharField(max_length=255)),
                ("product_category", models.CharField(max_length=100)),
                (
                    "veg_non_veg",
                    models.CharField(
                        choices=[("Veg", "Veg"), ("Non-Veg", "Non-Veg")], max_length=8
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductToppings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foodsearchapp.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                ("rating_id", models.AutoField(primary_key=True, serialize=False)),
                ("rating_value", models.DecimalField(decimal_places=1, max_digits=3)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foodsearchapp.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Toppings",
            fields=[
                ("topping_id", models.AutoField(primary_key=True, serialize=False)),
                ("group_id", models.IntegerField()),
                ("topping_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ToppingsGroups",
            fields=[
                ("group_id", models.AutoField(primary_key=True, serialize=False)),
                ("group_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Cuisine",
        ),
        migrations.RemoveField(
            model_name="foodproductrating",
            name="food_product",
        ),
        migrations.DeleteModel(
            name="Customization",
        ),
        migrations.DeleteModel(
            name="FoodItem",
        ),
        migrations.DeleteModel(
            name="FoodProductRating",
        ),
        migrations.DeleteModel(
            name="Topping",
        ),
        migrations.AddField(
            model_name="producttoppings",
            name="topping",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="foodsearchapp.toppings"
            ),
        ),
    ]
