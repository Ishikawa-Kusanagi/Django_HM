from django.shortcuts import render, reverse
from django.http import JsonResponse, HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe(request, dish):
    recipe_data = DATA.get(dish)
    servings = request.GET.get('servings', 1)

    count_recipe = {ingrid: amount * servings for ingrid, amount in
                    recipe_data.items()}

    return JsonResponse(count_recipe)
