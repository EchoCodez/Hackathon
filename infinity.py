import random
import gspread as gs

def main():
    gc = gs.service_account(filename='key.json')
    sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1a3kh0zcaCTJM7blFzkD0S5p1zqyWI-J4wXs4Jl4fMtk/edit?usp=sharing')
    sh2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1a3kh0zcaCTJM7blFzkD0S5p1zqyWI-J4wXs4Jl4fMtk/edit?usp=sharing')

    ws1 = sh1.worksheet('Form Responses 1')
    ws2 = sh2.worksheet('Form Responses 1')
    possible = []

    for i in ws2.get_all_records():
        for j in ws1.get_all_records():
            if j.get("What is your budget?") <= i.get("What is your budget?") and j.get("Zip Code") == i.get("Zip Code"):
                possible.append(j.get("Name:"))
    
    print(random.choice(possible))

main()