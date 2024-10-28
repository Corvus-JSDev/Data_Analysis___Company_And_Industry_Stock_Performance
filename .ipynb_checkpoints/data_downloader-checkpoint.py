company_list = [
    # Technology
    'AAPL',  # Apple Inc.
    'MSFT',  # Microsoft Corporation
    'NVDA',  # NVIDIA Corporation
    'GOOGL', # Alphabet Inc. (Google)
    'INTC',  # Intel Corporation
    '005930.KS',  # Samsung Electronics (Korea Stock Exchange)
    'ADBE',  # Adobe Inc.
    'CRM',   # Salesforce, Inc.
    'ORCL',  # Oracle Corporation
    'TXN',   # Texas Instruments Incorporated

    # Health Care
    'JNJ',   # Johnson & Johnson
    'UNH',   # UnitedHealth Group Incorporated
    'PFE',   # Pfizer Inc.
    'RHHBY', # Roche Holding AG
    'MRK',   # Merck & Co., Inc.
    'ABBV',  # AbbVie Inc.
    'AMGN',  # Amgen Inc.
    'MDT',   # Medtronic plc
    'AZN',   # AstraZeneca plc
    'GILD',  # Gilead Sciences, Inc.

    # Financials
    'JPM',   # JPMorgan Chase & Co.
    'BAC',   # Bank of America Corporation
    'WFC',   # Wells Fargo & Company
    'BRK.B', # Berkshire Hathaway Inc.
    'GS',    # Goldman Sachs Group, Inc.
    'C',     # Citigroup Inc.
    'MS',    # Morgan Stanley
    'AXP',   # American Express Company
    'V',     # Visa Inc.
    'MA',    # Mastercard Incorporated

    # Consumer Discretionary
    'AMZN',  # Amazon.com, Inc.
    'TSLA',  # Tesla, Inc.
    'HD',    # Home Depot, Inc.
    'NKE',   # Nike, Inc.
    'MCD',   # McDonald's Corporation
    'LOW',   # Lowe's Companies, Inc.
    'BKNG',  # Booking Holdings Inc.
    'SBUX',  # Starbucks Corporation
    'GM',    # General Motors Company
    'DIS',   # Walt Disney Company

    # Consumer Staples
    'PG',    # Procter & Gamble Co.
    'KO',    # Coca-Cola Company
    'PEP',   # PepsiCo, Inc.
    'UL',    # Unilever PLC
    'WMT',   # Walmart Inc.
    'NSRGY', # Nestlé S.A.
    'CL',    # Colgate-Palmolive Company
    'MDLZ',  # Mondelez International, Inc.
    'PM',    # Philip Morris International Inc.
    'KMB',   # Kimberly-Clark Corporation

    # Energy
    'XOM',   # Exxon Mobil Corporation
    'CVX',   # Chevron Corporation
    'TOT',   # TotalEnergies SE
    'SHEL',  # Shell plc
    'BP',    # BP p.l.c.
    'COP',   # ConocoPhillips
    'NEE',   # NextEra Energy, Inc.
    'E',     # Eni S.p.A.
    'SLB',   # Schlumberger Limited
    'EQNR',  # Equinor ASA

    # Materials
    'BHP',   # BHP Group
    'RIO',   # Rio Tinto Group
    'DD',    # DuPont de Nemours, Inc.
    'LIN',   # Linde plc
    'BASFY', # BASF SE
    'FCX',   # Freeport-McMoRan Inc.
    'NEM',   # Newmont Corporation
    'GOLD',  # Barrick Gold Corporation
    'SHW',   # Sherwin-Williams Company
    'VALE',  # Vale S.A.

    # Industrials
    'BA',    # Boeing Company
    'HON',   # Honeywell International Inc.
    'CAT',   # Caterpillar Inc.
    'LMT',   # Lockheed Martin Corporation
    'MMM',   # 3M Company
    'GE',    # General Electric Company
    'NOC',   # Northrop Grumman Corporation
    'RTX',   # Raytheon Technologies Corporation
    'SIEGY', # Siemens AG
    'UPS',   # United Parcel Service, Inc.

    # Real Estate
    'PLD',   # Prologis, Inc.
    'AMT',   # American Tower Corporation
    'CCI',   # Crown Castle International Corp.
    'SPG',   # Simon Property Group, Inc.
    'EQR',   # Equity Residential
    'PSA',   # Public Storage
    'AVB',   # AvalonBay Communities, Inc.
    'WELL',  # Welltower Inc.
    'DLR',   # Digital Realty Trust, Inc.
    'VNO',   # Vornado Realty Trust

    # Communication Services
    'META',  # Meta Platforms, Inc. (Facebook)
    'NFLX',  # Netflix, Inc.
    'DIS',   # Walt Disney Company
    'CMCSA', # Comcast Corporation
    'VZ',    # Verizon Communications Inc.
    'T',     # AT&T Inc.
    'TMUS',  # T-Mobile US, Inc.
    'CHTR',  # Charter Communications, Inc.
    'BKNG',  # Booking Holdings Inc.
    'SONY',  # Sony Group Corporation
]


def download_historical_data(company_names=company_list):
    for company in company_names:
        try:
            # Fetch historical data for the company
            stock_data = yf.download(company, period="max")

            # Save the data to a CSV file
            stock_data.to_csv(f"./company_data/{company}_stock_data.csv")
            print(f"SUCCESS: {company}")
        except Exception as e:
            print(f"Could not download data for {company}: {e}")