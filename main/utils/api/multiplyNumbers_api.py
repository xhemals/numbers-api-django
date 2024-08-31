from rest_framework.response import Response
from rest_framework import status
from utils.math import (
    multiply_numbers,
    view_sum,
    num_to_words,
)


def multiply_numbers_api(self, request):
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

    result = multiply_numbers(numbers)

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
        "sum": view_sum(numbers, "x") if viewSum else None,
    }

    # Remove keys with None values
    response_data = {
        key: value for key, value in response_data.items() if value is not None
    }

    return Response(response_data)
