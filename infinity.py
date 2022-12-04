import gspread as gs
import pandas as pd

gc = gs.service_account(filename='key.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1a3kh0zcaCTJM7blFzkD0S5p1zqyWI-J4wXs4Jl4fMtk/edit?usp=sharing')

ws = sh.worksheet('Form Responses 1')
df = pd.DataFrame(ws.get_all_records())
df.head()

print(df)