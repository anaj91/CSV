with open("seznam.csv", "r") as seznam_:
    seznam = seznam_.read().splitlines()[:3]

    for row in seznam:
       row_data = row.split(",")
       print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}.")
