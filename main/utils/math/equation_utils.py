from num2words import num2words


def add_numbers(numbers):
    # add the numbers
    result = sum(numbers)

    # if the result is a full number, remove the decimal
    if str(result)[-2:] == ".0":
        result = int(result)

    return result


def subtract_numbers(numbers):
    result = numbers[0]
    # subtract the numbers
    for num in numbers:
        if num == numbers[0]:
            continue
        result -= num

    # if the result is a full number, remove the decimal
    if str(result)[-2:] == ".0":
        result = int(result)

    return result


def multiply_numbers(numbers):
    result = numbers[0]
    # multiply the numbers
    for num in numbers:
        if num == numbers[0]:
            continue
        result *= num

    # if the result is a full number, remove the decimal
    if str(result)[-2:] == ".0":
        result = int(result)

    return result


def divide_numbers(numbers):
    result = numbers[0]
    # divide the numbers
    for num in numbers:
        if num == numbers[0]:
            continue
        result /= num
    if str(result)[-2:] == ".0":
        result = int(result)

    return result


def view_sum(numbers, operation):
    # if the user wants the sum, return the sum and remove any decimals if they are a full number
    questionSum = ""
    for num in numbers:
        if str(num)[-2:] == ".0":
            num = int(num)
        questionSum += str(num) + f" {operation} "
    questionSum = questionSum[:-3]

    return questionSum


def num_to_words(number, lang):
    try:
        return num2words(number, lang=lang)
    except (NotImplementedError, TypeError):
        raise ValueError(f"Language {lang} is not supported.")
