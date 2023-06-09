from sqlalchemy import create_engine
import openpyxl
import pymysql

engine = create_engine("mysql+pymysql://Backend_PE:Backdoor0122!@192.169.1.7:3306/Ceramic_Data?charset=utf8mb4")

conn = engine.connect()

import pandas as pd

excel_file = pd.ExcelFile("\\backend_nas\\Nasserver_CERDATA\\TTV\\XLS\\BCRE25462JRUX\\0120ADM2ATM#1.xls")

excel_dataframe = excel_file.parse(sheet_name="1")

excel_dataframe.to_sql("1", conn, if_exists="append")