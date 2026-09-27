from fastapi import APIRouter, Request, HTTPException

calculaterouter = APIRouter(prefix="/calculate")


@calculaterouter.post("/")
async def calculate(request: Request):

    request_json = await request.json()

    operation = request_json.get("Operation")
    numbers = request_json.get("Numbers")

    if not isinstance(numbers, list) or not numbers:
        raise HTTPException(
            status_code=400,
            detail="Numbers must be a non-empty list"
        )

    if operation == "Addition":
        result = await get_addition(numbers)

    elif operation == "Substraction":
        result = await get_substraction(numbers)

    elif operation == "Multiplication":
        result = await get_multiplication(numbers)

    elif operation == "Division":
        result = await get_division(numbers)

    else:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid operation name"
        )

    return {"result": result}


async def get_addition(numbers):

    total = 0

    for number in numbers:
        total += number

    return total


async def get_substraction(numbers):

    total = numbers[0]

    for number in numbers[1:]:
        total -= number

    return total


async def get_multiplication(numbers):

    total = 1

    for number in numbers:
        total *= number

    return total


async def get_division(numbers):

    total = numbers[0]

    for number in numbers[1:]:

        if number == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )

        total /= number

    return total