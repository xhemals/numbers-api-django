from rest_framework.response import Response
from rest_framework import status
from utils.conversions import (
    int_to_binary,
    int_to_hex,
    binary_to_int,
    binary_to_hex,
    hex_to_binary,
    hex_to_int,
)


def is_binary(number):
    bin_str = str(number)

    return all(char in "01" for char in bin_str)


def is_hex(number):
    hex_str = int(number, 16)
    return hex_str


def convert_num_api(self, request):
    try:
        typeFrom = request.GET.get("from", "")
        typeTo = request.GET.get("to", "")
        number = request.GET.get("number", "")
    except (TypeError, ValueError):
        return Response(
            {"error": "Please provide valid numbers"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if typeFrom == typeTo:
        return Response(
            {"error": "Please provide different 'from' and 'to' values."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if typeFrom == "binary":
        if not is_binary(number):
            return Response(
                {"error": "Please provide a valid binary number."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if typeTo == "integer" or typeTo == "decimal" or typeTo == "int":
            return Response({"result": binary_to_int(number)})
        if typeTo == "hex":
            return Response({"result": binary_to_hex(number)})

    if typeFrom == "integer" or typeFrom == "decimal" or typeFrom == "int":
        try:
            number = int(number)
        except ValueError:
            return Response(
                {"error": "Please provide a valid integer."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if typeTo == "binary":
            return Response({"result": int_to_binary(number)})
        if typeTo == "hex":
            return Response({"result": int_to_hex(number)})

    if typeFrom == "hex":
        try:
            is_hex(number)
        except ValueError:
            return Response(
                {"error": "Please provide a valid hex number."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if typeTo == "binary":
            return Response({"result": hex_to_binary(number)})
        if typeTo == "integer" or typeTo == "decimal" or typeTo == "int":
            return Response({"result": hex_to_int(number)})
