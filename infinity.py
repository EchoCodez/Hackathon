import gspread as gs

def main():
    gc = gs.service_account(filename='key.json')
    sh1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1tZ__iSIROR3HE--qbX9LJuHyO9gOd2BjHHYRzc5gIDM/edit?usp=sharing')
    sh2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1nBn0PNpBSNdH_207MV_FLfSQ-l1FlsM5G6h6RqzRPPE/edit?usp=sharing')

    ws1 = sh1.worksheet('Form Responses 1')
    ws2 = sh2.worksheet('Form Responses 1')
    possible = []

    for i in ws2.get_all_records():
        for j in ws1.get_all_records():
            if int(str(j.get("I am willing to spend ______ on gifts for people in need.(Budget)"))) >= int(str(i.get("Total Cost:"))) and j.get("Zip Code:") == i.get("Zip code of homeless shelter"):
                print(j.get("Email:") + ": " + i.get("Full name of person receiving gift:"))

main()