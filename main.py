from os import listdir
import pandas as pd

def StockNameImportation():
    stock_list = listdir('statements')
    new = []
    
    for name in stock_list:
        if (name[8] == '1'):
            new.append(name[3:9])
        else: 
            new.append(name[3:8])

    return new, stock_list

def main():
    stock_names, stock_files = StockNameImportation()

    # create a dictionary with the ticker information removed from the statements folder 
    # fund = {
    #       "ABEV3": statement_ABEV3,
    #       "MGLU3": statement_MGLU3
    #       ...
    #       }

    fund = {}
    
    for file_name in stock_files:
        balanco = pd.read_excel(f'statements/{file_name}', sheet_name=0)
        dre = pd.read_excel(f'statements/{file_name}', sheet_name=1)
        
        # turn first line into a header
        balanco.columns = balanco.iloc[0]
        balanco = balanco[1:]

        # first column place the title as the name of the company
        balanco.iloc[0,0] = 

main()
