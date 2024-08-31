from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.api import (
    add_numbers_api,
    subtract_numbers_api,
    multiply_numbers_api,
    divide_numbers_api,
    num_to_word_api,
    convert_num_api,
)
# Create your views here.


class AddNumbersView(APIView):
    def get(self, request):
        return add_numbers_api(self, request)


class SubtractNumbersView(APIView):
    def get(self, request):
        return subtract_numbers_api(self, request)


class MultiplyNumbersView(APIView):
    def get(self, request):
        return multiply_numbers_api(self, request)


class DivideNumbersView(APIView):
    def get(self, request):
        return divide_numbers_api(self, request)


class NumToWordView(APIView):
    def get(self, request):
        return num_to_word_api(self, request)


class ConvertNum(APIView):
    def get(self, request):
        return convert_num_api(self, request)
