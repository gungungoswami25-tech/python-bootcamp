
def calculate_library_fine(days_overdue, book_type="standard", is_premium=False):

    if days_overdue <= 0:
        return 0.0

    if book_type == "standard":
        if days_overdue <= 5:
            fine = days_overdue * 5
        else:
            fine = (5 * 5) + ((days_overdue - 5) * 10)

    elif book_type == "reference":
        fine = days_overdue * 20

    else:
        print("Invalid book type")
        return 0.0

    if is_premium == True:
        fine = fine - (fine * 20 / 100)

    return float(fine)


print("Test 1:", calculate_library_fine(3, "standard", False))
print("Test 2:", calculate_library_fine(7, "standard", False))
print("Test 3:", calculate_library_fine(4, "reference", False))
print("Test 4:", calculate_library_fine(7, "standard", True))
