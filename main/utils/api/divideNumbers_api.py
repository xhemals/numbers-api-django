from rest_framework.response import Response
from rest_framework import status
import random
from utils.math import (
    divide_numbers,
    view_sum,
    num_to_words,
)
from api.models import dividedByZero


def get_counter():
    # Assuming there's only one instance, get_or_create will create it if it doesn't exist
    counter, created = dividedByZero.objects.get_or_create(pk=1)
    return counter


def increment_counter():
    counter = get_counter()
    counter.timesDividedByZero += 1
    counter.save()


divide_by_zero_errors = [
    "You really tried to divide by zero?",
    "Can't divide by zero. Even my code knows that’s a no-go!",
    "Zero? Really? That's not a number you can divide by. Try again!",
    "Please don't think you are smart enough to divide by zero. You're not!",
    "You thought you could divide by zero, but you were wrong. Try again!",
    "Lame attempt to try and break the system. You're not smart enough to divide by zero!",
]


def divide_numbers_api(self, request):
    try:
        numbers = [
            float(number) for number in request.GET.get("numbers", "").split(",")
        ]
        viewSum = "viewSum" in request.GET
        toWords = "toWords" in request.GET
        lang = request.GET.get("lang", "en")
    except (TypeError, ValueError):
        return Response(
            {"error": "Please provide valid numbers"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if len(numbers) == 1:
        return Response(
            {"error": "Please provide more than one number."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if 0 in numbers:
        timesDividedByZero = get_counter().timesDividedByZero
        increment_counter()
        return Response(
            {
                "error": random.choice(divide_by_zero_errors),
                "times_someones_has_divided_by_zero": timesDividedByZero,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    result = divide_numbers(numbers)

    try:
        inWords = num_to_words(result, lang) if toWords else None
    except ValueError:
        return Response(
            {"error": f"Language {lang} is not supported."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    response_data = {
        "result": result,
        "word": inWords if toWords else None,
        "sum": view_sum(numbers, "÷") if viewSum else None,
    }

    # Remove keys with None values
    response_data = {
        key: value for key, value in response_data.items() if value is not None
    }

    return Response(response_data)
