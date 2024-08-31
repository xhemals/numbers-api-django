from rest_framework.response import Response
from rest_framework import status
from utils.math import (
    num_to_words,
)


def num_to_word_api(self, request):
    try:
        number = float(request.GET.get("number", ""))
        lang = request.GET.get("lang", "en")
    except (TypeError, ValueError):
        return Response(
            {"error": "Please provide a valid number."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        inWords = num_to_words(number, lang)
    except ValueError:
        return Response(
            {"error": f"Language {lang} is not supported."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response({"result": inWords})
