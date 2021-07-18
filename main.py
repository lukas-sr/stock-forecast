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

if __name__ == "__main__":
    stock_names, stock_files = StockNameImportation()
    
    # create a dictionary with the ticker information
    # 
    # fund = {
    #       "ABEV3": statement_ABEV3,
    #       "MGLU3": statement_MGLU3
    #       ...
    #       }

    fund = {}

    for file_name in stock_files:

        name = file_name[3:8]
        
        if "11" in name:
            name = file_name[3:9]

        balanco = pd.read_excel(f'statements/{file_name}', sheet_name=0)
        
        # first column place the title as the name of the company
        balanco.iloc[0,0] = name 

        # turn first line into a header and exclude the duplicated
        balanco.columns = balanco.iloc[0]
        balanco = balanco[1:]

        balanco = balanco.set_index(name)
     
        # do the same to the 'dre's
        dre = pd.read_excel(f'statements/{file_name}', sheet_name=1)
    
        dre.iloc[0,0] = name

        dre.columns = dre.iloc[0]
        dre = dre[1:]

        dre = dre.set_index(name)

        fund[name] = balanco.append(dre)
        
        print(fund)
        break

