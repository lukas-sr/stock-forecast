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
    
    # stock_names = ["ABEV3", "AZUL4", "BTOW3", "B3SA3", "BBSE3", "BRML3", "BBDC4", "BRAP4", "BBAS3", "BRKM5", "BRFS3", "BPAC11",
    # "CRFB3", "CCRO3", "CMIG4", "HGTX3", "CIEL3", "COGN3", "CPLE6", "CSAN3", "CPFE3", "CVCB3", "CYRE3", "ECOR3", "ELET6", "EMBR3",
    # "ENBR3", "ENGI11", "ENEV3", "EGIE3", "EQTL3", "EZTC3", "FLRY3", "GGBR4", "GOAU4", "GOLL4", "NTCO3", "HAPV3", "HYPE3", "IGTA3", 
    # "GNDI3", "ITSA4", "ITUB4", "JBSS3", "JHSF3", "KLBN11", "RENT3", "LCAM3", "LAME4", "LREN3", "MGLU3", "MRFG3", "BEEF3", "MRVE3",
    # "MULT3", "PCAR3", "PETR4", "BRDT3", "PRIO3", "QUAL3", "RADL3", "RAIL3", "SBSP3", "SANB11", "CSNA3", "SULA11", "SUZB3",
    # "TAEE11", "VIVT3", "TIMS3", "TOTS3", "UGPA3", "USIM5", "VALE3", "VVAR3", "WEGE3", "YDUQ3"] 
    # 
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

        statem = pd.read_excel(f'statements/{file_name}', sheet_name=0)
        
        # first column place the title as the name of the company
        statem.iloc[0,0] = name 

        # turn first line into a header and exclude the duplicated
        statem.columns = statem.iloc[0]
        statem = statem[1:]

        statem = statem.set_index(name)
     
        # do the same to the 'dre's
        dre = pd.read_excel(f'statements/{file_name}', sheet_name=1)
    
        dre.iloc[0,0] = name

        dre.columns = dre.iloc[0]
        dre = dre[1:]

        dre = dre.set_index(name)

        fund[name] = statem.append(dre)
        
    # to print all the dictionary called fund uncoment
    # ================================================
    # print(fund)
    

    # Add the Quotation dataframe
    # Format of the standard dataframe
    # Columns:
    # | Date | High | Low | Open | Close | Volume | AdjClose | Company
    # 
    # 'Adj Close' is the value of the stock, adjusted by the company
    # dividends and another distributions
    # 'Adj Close' so, will be our reference
    quotation_df = pd.read_excel('Quotations.xlsx')

    # Create a dictionary for quotations filtred by company
    quotation = {}

    for company in quotation_df["Company"].unique():
        quotation[company] = quotation_df.loc[quotation_df['Company']==company, :]
    # to print all the dictionary called quotation uncoment
    # =====================================================
    # print(quotation)

    # TODO to exclude all the empty lines in Quotation and Fundamentus
    for company in stock_names:
        if (quotation[company].isnull().values.any()):
            quotation.pop(company)
            fund.pop(company)

    # Update stock names list
    stock_names = list(quotation.keys())
    print(len(stock_names))
