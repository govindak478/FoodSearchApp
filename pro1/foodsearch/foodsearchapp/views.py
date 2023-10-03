from django.shortcuts import render
from foodsearchapp.models import Product, ToppingsGroups,Rating,ProductToppings
from django.db.models import Min, Max, Avg  # Import Min, Max, and Avg

def product_filter(request):
    if request.method == 'POST':
        veg_non_veg = request.POST.get('veg_non_veg')
        category = request.POST.get('category')

        # Filter products based on selected filters
        if veg_non_veg in ('Veg', 'Non-Veg') and category:
            products = Product.objects.filter(
                product_category=category,
                veg_non_veg=veg_non_veg
            )
        elif category:
            products = Product.objects.filter(product_category=category)
        else:
            products = Product.objects.all()

        # Get price range for the selected category
        price_range = products.aggregate(
            min_price=Min('price'),  # Use Min for minimum price
            max_price=Max('price')  # Use Max for maximum price
        )

        # Get ratings for products in the selected category
        product_ratings = {}
        for product in products:
            ratings = Rating.objects.filter(product=product)
            if ratings.exists():
                avg_rating = ratings.aggregate(Avg('rating_value'))['rating_value__avg']  # Use Avg for average rating
                product_ratings[product] = avg_rating
            else:
                product_ratings[product] = None
        
        #is_customizable = ToppingsGroups.objects.filter(group_name=category).exists()
        
        # Get toppings for the selected category (if customizable)
        toppings = []
        #if is_customizable:
            # Retrieve all toppings related to each product
        for product in products:
                product_toppings = ProductToppings.objects.filter(product=product)
                toppings_for_product = [pt.topping for pt in product_toppings]
                toppings.append((product, toppings_for_product))
                print(toppings)
        context = {
            'veg_non_veg_choices': [('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')],
            'category_choices': Product.objects.values_list('product_category', flat=True).distinct(),
            'selected_veg_non_veg': veg_non_veg,
            'selected_category': category,
            'products': products,
            'price_range': price_range,
            'product_ratings': product_ratings,
            'toppings': toppings,
            #'is_customizable': is_customizable,
        }
        return render(request, 'foodsearchapp/index.html', context)
    else:
        # Handle initial GET request
        context = {
            'veg_non_veg_choices': [('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')],
            'category_choices': Product.objects.values_list('product_category', flat=True).distinct(),
        }
        return render(request, 'foodsearchapp/index.html', context)
