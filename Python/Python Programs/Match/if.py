month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("a weekend in april")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("a weekend in May")
    case _:
        print("no match")