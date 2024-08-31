from django.urls import path
from .views import (
    AddNumbersView,
    SubtractNumbersView,
    MultiplyNumbersView,
    DivideNumbersView,
    NumToWordView,
    ConvertNum,
)

urlpatterns = [
    path("add/", AddNumbersView.as_view(), name="add-numbers"),
    path("subtract/", SubtractNumbersView.as_view(), name="subtract-numbers"),
    path("multiply/", MultiplyNumbersView.as_view(), name="multiply-numbers"),
    path("divide/", DivideNumbersView.as_view(), name="divide-numbers"),
    path("num-to-word/", NumToWordView.as_view(), name="num-to-word"),
    path("convert/", ConvertNum.as_view(), name="convert-num"),
]
