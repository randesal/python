import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel(r"C:\Users\BackendPE\Desktop\BCRE565PNUX\0419DFU2ATM#1.xls", sheet_name="1")
data = data
print(data)

#data.subplot(kind = 'scatter', x = 'Lot No', y = 'A1')

fig, ax = plt.subplots()
ax.plot(data["Lot No"], data["A1"], label='A1')
ax.plot(data["Lot No"], data["A2"], label='A2')
ax.plot(data["Lot No"], data["A3"], label='A3')
ax.plot(data["Lot No"], data["A4"], label='A4')
ax.set_xlabel('Lot No')
ax.set_ylabel('thickness')
ax.set_title("TTV Thickness")
ax.legend()

plt.show()

d = input()