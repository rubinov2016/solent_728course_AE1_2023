'''
4. Identify the top 5 regions where a specific band of devices was sold.
5. Analyse the average price of devices within a specific band, all in the same currency.
6. Analyse the average mass for each manufacturer and display the list of average mass
for all manufacturers.
7. Analyse the data to derive meaningful insights based on your unique selection,
distinct from the previous requirements.
'''


def analytics_panda(path, choice):
    import pandas as pd
    import menu_module as menu
    df = pd.read_csv(path, header=0, encoding='utf-8')
    print(df)
    match choice:
        case 4:
            print(4)
            distinct_brands = df['brand'].unique()
            print("Select the brand from the following:")
            print(distinct_brands)
            value = menu.input_value("brand") # in future I should be able to transfer it
            brand_df = df[df['brand'] == value]
            region_counts = brand_df['market_regions'].value_counts()
            # Display the top 5 regions
            top_5_regions = region_counts.head(5)
            print("Top 5 regions for", value, "devices:")
            print(top_5_regions)
        case 5:
            print(5)
            value = menu.input_value("brand")  # in future I should be able to transfer it
            # currency = menu.input_value("currency")
            # Group by 'Band' and 'Currency', calculate the average price for each combination
            brand_df = df[df['brand'] == value]
            average_price = brand_df.groupby(['brand', 'price_currency'])['price'].mean()
            # Display the average prices
            print("Average prices for each band and currency:")
            print(average_price)
        case 6:
            print(6)
            average_weight = df.groupby('manufacturer')['weight_gram'].mean()
            print("Average weight for each manufacturer:")
            print(average_weight)

# if __name__ == "__main__":
#     analytics_panda("device_features.csv",4)

