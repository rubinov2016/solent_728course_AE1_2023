def top_features(df, feature, top_feature, top_number, text):
    import menu_module as menu
    # Step 1: Print feature name to select
    distinct_feature = df[feature].unique()
    print(f"Choose the {feature} from the following:")
    print(distinct_feature)
    # Step 2: Filter rows with the feature specified
    value = menu.input_value(feature)
    feature_df = df.loc[(df[feature] == value), [top_feature]]
    # Step 3: Convert string to list
    feature_df[top_feature] = feature_df[top_feature].str.split(',')
    # Step 4: Use 'explode' function to populate the dataframe
    df_exploded = feature_df[top_feature].explode()
    top_elements = df_exploded.value_counts().head(top_number)
    print(f"{text}", value, "devices:")
    print(top_elements)

def avg_group_two(df, feature, group_feature, avg_feature, text):
    import menu_module as menu
    # Step 1: Filter by feature name
    value = menu.input_value(feature)
    brand_df = df[df[feature] == value]
    # Step 2: Group by feature and 'currency', calculate the average price for each combination
    average_price = round(brand_df.groupby([feature, group_feature])[avg_feature].mean(), 2)
    print(text)
    print(average_price)

def avg_group_one(df, feature, avg_feature, text):
    average_weight = df.groupby(feature)[avg_feature].mean()
    print(text)
    print(average_weight)

def count_annualy(df, feature, count_feature, text):
    # compare what the difference with f.groupby('manufacturer')['weight_gram']
    device_year = df.groupby([feature, count_feature]).size().reset_index(name='count')
    print(text)
    print(device_year)

def analytics_visualize(path, choice):
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
            top_features(df,'brand', 'market_regions', 5, "Top 5 regions for")
        # Analyse the average price of devices within a specific band, all in the same currency.
        case 5:
            avg_group_two(df,'brand', 'price_currency', 'price', "Average prices for each band and currency:")
        # Analyse the average mass for each manufacturer and display the list of average mass for all manufacturers
        case 6:
            avg_group_one(df, 'manufacturer', 'weight_gram', "Average weight for each manufacturer:")
        # Custom - unique selection, distinct from the previous requirements
        case 7:
            count_annualy(df, 'manufacturer', 'released_year', "Number of devices released by manufacture annually:")
        # Proportion of RAM types for devices in the current market
        case 8:
            # Step 1: Filter by market
            distinct_markets = df['market_regions'].unique()
            print("Choose the market (North America by default):")
            print(distinct_markets)
            value = menu.input_value("market_regions")
            if value == "":
                value = "North America"
            market_df = df[df['market_regions'] == value]
            # Step 2: Find counts for RAM, market and proportion
            ram_count = market_df['ram_type'].value_counts()
            market_count = len(market_df)
            ram_proportions = ram_count / market_count
            # Step 3: Create a pie chart using matplotlib
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
                # Step 3: AverageApp
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

if __name__ == "__main__":
    analytics_visualize("device_features.csv",7)
