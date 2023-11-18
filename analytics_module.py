
def analytics_panda(path, choice):
    import pandas as pd
    import matplotlib.pyplot as plt
    import menu_module as menu
    df = pd.read_csv(path, header=0, encoding='utf-8')
    # Create a field with a release year and month
    print("Release date should be in DD-MM-YY format as 28-03-22")
    df['released_date'] = pd.to_datetime(df['released_date'], format='%d-%m-%y')
    df['released_year'] = df['released_date'].dt.year
    df['released_month'] = df['released_date'].dt.month
    df['market_regions'] = df['market_regions'].tolist()
    # print(df)
    match choice:
        # Identify the top 5 regions where a specific band of devices was sold.
        case 4:
            # Step 1: Print name brands to select
            distinct_brands = df['brand'].unique()
            print("Choose the brand from the following:")
            print(distinct_brands)
            # Step 2: Filter rows with the brand specified
            value = menu.input_value("brand")
            brand_df = df.loc[(df['brand'] == value), ['market_regions']]
            # Step 3: Convert string to list
            brand_df['market_regions'] = brand_df['market_regions'].str.split(',')
            # Step 4: Use 'explode' function to populate the dataframe
            df_exploded = brand_df['market_regions'].explode()
            top_elements = df_exploded.value_counts().head(5)
            print("Top 5 regions for", value, "devices:")
            print(top_elements)
        # Analyse the average price of devices within a specific band, all in the same currency.
        case 5:
            value = menu.input_value("brand")  # in the future it better to transfer it
            # Group by 'brand' and 'currency', calculate the average price for each combination
            brand_df = df[df['brand'] == value]
            average_price = brand_df.groupby(['brand', 'price_currency'])['price'].mean()
            print("Average prices for each band and currency:")
            print(average_price)
        # Analyse the average mass for each manufacturer and display the list of average mass for all manufacturers
        case 6:
            average_weight = df.groupby('manufacturer')['weight_gram'].mean()
            print("Average weight for each manufacturer:")
            print(average_weight)
        # Custom - unique selection, distinct from the previous requirements
        case 7:
            # compare what the difference with f.groupby('manufacturer')['weight_gram']
            device_year = df.groupby(['manufacturer' ,'released_year']).size().reset_index(name='count')
            print("Number of devices released by manufacture annually:")
            print(device_year)
        # Proportion of RAM types for devices in the current market
        case 8:
            # Step 1: Find counts for RAM, market and proportion
            distinct_markets = df['market_regions'].unique()
            print("Choose the market (North America by default):")
            print(distinct_markets)
            value = menu.input_value("market_regions")
            if value == "":
                value = "North America"
            market_df = df[df['market_regions'] == value]
            ram_count = market_df['ram_type'].value_counts()
            market_count = len(market_df)
            ram_proportions = ram_count / market_count
            # Step 2: Create a pie chart using matplotlib
            plt.pie(ram_proportions, labels=ram_proportions.index, autopct='%1.1f%%', textprops={'fontsize': 12})
            plt.title(f"Proportion of RAM Types in {value}")
            plt.show()
        # Compare the number of devices for each USB connector type
        case 9:
            usb_count = df['usb_connector'].value_counts()
            # print(usb_count)
            plt.figure(figsize=(8, 8))
            usb_count.plot(kind='bar', color='blue')
            plt.title('Number of Devices for Each USB Connector Type', fontsize=15)
            plt.xlabel('', fontsize=12)
            plt.ylabel('Number of Devices', fontsize=12)
            plt.xticks(rotation=0, fontsize=12)
            plt.show()
        # Monthly average price trends (in GBP) for # devices released in each year from 2020 to 2023
        case 10:
            # Step 1: Filter dataset by GBP
            gbp_df = df[df['price_currency'] == 'GBP']
            # Step 2: Filter dataset by year
            for year in range(2020, 2023):
                year_df = gbp_df[gbp_df['released_year'] == year]
                # Step 3: Average
                print("Average prices in GBP:")
                avg_price_month = year_df.groupby(['released_year','released_month'])['price'].mean()
                # Step 4: Visualize
                plt.figure(figsize=(10, 6))
                avg_price_month.plot(kind='line', marker='o', color='blue')
                plt.title(f'Monthly Average Price (GBP) in {year}', fontsize=16)
                plt.xlabel('Month', fontsize=12)
                plt.ylabel('Average Price in GBP', fontsize=12)
                # plt.xtickps(range(1, 13), [f'{i}' for i in range(1, 13)])
                plt.grid(True)
                plt.show()
        # Trends, behaviours, or patterns, distinct from previous requirements
        case 11:
            print(11)

# if __name__ == "__main__":
#     analytics_panda("device_features.csv",4)
