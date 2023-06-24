import math
from prettytable import PrettyTable

# straight-line depreciation
def straight_line(depreciation_group, entry_price):
    match depreciation_group:
        case "1":
            first_year_depreciation = 20
            other_years = 40
            amortisation_period = 3
        case "2":
            first_year_depreciation = 11
            other_years = 22.25
            amortisation_period = 5
        case "3":
            first_year_depreciation = 5.5
            other_years = 10.5
            amortisation_period = 10
        case "4":
            first_year_depreciation = 2.15
            other_years = 5.15
            amortisation_period = 20
        case "5":
            first_year_depreciation = 1.4
            other_years = 3.4
            amortisation_period = 30
        case "6":
            first_year_depreciation = 1.02
            other_years = 2.02
            amortisation_period = 50

    remainder = entry_price
    corrections = 0 

    table = PrettyTable(["Odpis", "Opravky", "Zůstatek"])
                
    # mathematical operations
    for year in range(amortisation_period):
        if year == 0:
            write_off = math.ceil(entry_price * first_year_depreciation * 0.01)
        else:
            write_off = math.ceil(entry_price * other_years * 0.01)

        corrections += math.ceil(write_off)
        remainder -= write_off
                        
        table.add_row([write_off, corrections, remainder])

    table.add_autoindex("Rok")
    print(table)

# accelerated depreciation
def accelerated(depreciation_group, entry_price):
    match depreciation_group:
        case "1":
            first_year_depreciation = 3
            other_years = 4
            amortisation_period = 3
        case "2":
            first_year_depreciation = 5
            other_years = 6
            amortisation_period = 5
        case "3":
            first_year_depreciation = 10
            other_years = 11
            amortisation_period = 10
        case "4":
            first_year_depreciation = 20
            other_years = 21
            amortisation_period = 20
        case "5":   
            first_year_depreciation = 30
            other_years = 31
            amortisation_period = 30
        case "6":
            first_year_depreciation = 50
            other_years = 51
            amortisation_period = 50

    remainder = entry_price
    corrections = 0

    table = PrettyTable(["Odpis", "Opravky", "Zůstatek"])

    # mathematical operations
    for year in range(amortisation_period):
        if year == 0:
            write_off = math.ceil(remainder / first_year_depreciation)
        else:
            write_off = math.ceil((2 * remainder) / (other_years - year))         

        corrections += math.ceil(write_off)  
        remainder -= write_off

        table.add_row([write_off, corrections, remainder])
    table.add_autoindex("Rok")
    print(table)


def main():
    # inputs
    entry_price = int(input("Zadej vstupní cenu: "))
    depreciation_group = input("Zadej odpisovou skupinu: ")
    typ_odpisu = input("[R]Rovnoměrný / [Z]Zrychlený: ").lower()
    print()

    if typ_odpisu.lower() == "r":
        straight_line(depreciation_group, entry_price)
    else:
        accelerated(depreciation_group, entry_price)

    # repeating cycle
    again = input("Chceš počítat dále? ano/ne ").lower()

    if again != "ano":
        pass
    else:
        main()


if __name__ == "__main__":
    main()
