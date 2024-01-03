# Returns the most popular values after parsing words from string
def top_features(df, filter_feature, count_feature, top_number, text):
    # df - dataset
    # filter_feature - feature to filter the dataset
    # count_feature - feature to counter the rows after filtering of dataset
    # top_number - how many rows to return
    # text - output text
    import menu_module as menu
    # Request for a feature name
    value = menu.input_feature(df, filter_feature)
    df_filter = df.loc[(df[filter_feature] == value), [count_feature]]
    # Convert string to list
    df_filter[count_feature] = df_filter[count_feature].str.split(',')
    # Use 'explode' function to populate the dataframe
    df_exploded = df_filter[count_feature].explode()
    top_elements = df_exploded.value_counts().head(top_number)
    print(f"{text}", value, "devices:")
    print(top_elements)


# Returns an average of the feature by grouping & filtering the other two feature
def avg_group_filter(df, filter_feature, group_feature, avg_feature, text):
    # df - dataset
    # filter_feature - feature to filter the dataset
    # group_feature - feature to group the dataset
    # avg_feature - these values should be averaged
    # text - output text
    import menu_module as menu
    # Request for a feature name
    value = menu.input_feature(df, filter_feature)
    df_filter = df[df[filter_feature] == value]
    # Group by group_feature, calculate the average price for each combination
    avg_group(df_filter, group_feature, avg_feature, text)


# Returns an average of the feature by grouping the another feature
def avg_group(df, group_feature, avg_feature, text):
    # df - dataset
    # group_feature - feature to group the dataset
    # avg_feature - these values should be averaged
    # text - output text
    average = round(df.groupby([group_feature])[avg_feature].mean(), 2)
    sorted_average = average.sort_values()
    print(text)
    print(sorted_average)


# Counts a feature by grouping two features
def count_group_two(df, count_feature1, count_feature2, text):
    # df - dataset
    # count_feature1, count_feature2 - features to group the dataset
    # text - output text
    device_year = df.groupby([count_feature1, count_feature2]).size().reset_index(name='count')
    print(text)
    print(device_year)


# Visualises a pie chart with proportions
def pie_chart_filtered(df, filter_feature, count_feature, fontsize, fig_width, fig_height, title):
    # df - dataset
    # filter_feature - feature to filter the dataset
    # count_feature - feature to count the dataset
    # text - output text
    import menu_module as menu
    import matplotlib.pyplot as plt
    # Filter by filter_feature
    value = menu.input_feature(df, filter_feature)
    market_df = df[df[filter_feature] == value]
    # Counts for count_feature and length of the whole dataset
    count_1 = market_df[count_feature].value_counts()
    count_2 = len(market_df)
    ram_proportions = count_1 / count_2
    # Pie chart using matplotlib
    plt.figure(figsize=(fig_width, fig_height))
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.1)
    plt.title(label=f"{title} {value}", fontsize=fontsize + 5)
    plt.pie(ram_proportions, labels=ram_proportions.index, autopct='%1.1f%%',  textprops={'fontsize': fontsize})
    plt.show()


# Visualises a bar chart
def chart_counted(df, count_feature, fontsize, fig_width, fig_height, y_label, title):
    # df - dataset
    # count_feature - feature to count the dataset
    # title - chart title
    import matplotlib.pyplot as plt
    count = df[count_feature].value_counts()
    plt.figure(figsize=(fig_width, fig_height))
    plt.title(title, fontsize=fontsize)
    count.plot(kind='bar', color='blue')
    plt.xlabel(xlabel='', fontsize=fontsize)
    plt.ylabel(y_label, fontsize=fontsize)
    plt.xticks(rotation=0, fontsize=fontsize)
    plt.show()


# Visualises several annual charts, each for a specific year
def chart_monthly_price(
        df,
        filter_feature,
        filter_value,
        min_year,
        max_year,
        count_feature1,
        count_feature2,
        average_feature,
        fontsize,
        fig_width,
        fig_height,
        x_label,
        y_label,
        title
):
    # df - dataset
    # filter_feature - feature to filter the dataset
    # min_year, max_year - range to filter and group the dataset
    # count_feature - features to group the dataset
    # average_feature - feature to average the dataset
    # fontsize, fig_width, fig_height, x_label, y_label - to draw the chart
    # title - chart title
    import matplotlib.pyplot as plt
    df_filtered = df[df[filter_feature] == filter_value]
    # Filter dataset by year
    for year in range(min_year, max_year+1):
        df_year = df_filtered[df_filtered[count_feature1] == year]
        avg_price_month = df_year.groupby([count_feature1, count_feature2])[average_feature].mean()
        # Visualize
        plt.figure(figsize=(fig_width, fig_height))
        avg_price_month.plot(kind='line', marker='o', color='blue')
        plt.title(label=f'{title} {year}', fontsize=fontsize + 2)
        plt.tick_params(axis='x', labelsize=6)
        plt.xlabel(x_label, fontsize=fontsize)
        plt.ylabel(y_label, fontsize=fontsize)
        plt.grid(True)
        plt.show()


# Visualises three metrics of two brands
def chart_metrics_three(
        df,
        device_category,
        device_category_value,
        price_category,
        price_category_value,
        released_year,
        brand,
        metrics1,
        metrics2,
        metrics3,
        metrics_name1,
        metrics_name2,
        metrics_name3,
        metrics_group1,
        metrics_group2,
        metrics_group3,
        fig_width,
        fig_height,
        fontsize,
        x_label,
        title
):
    import matplotlib.pyplot as plt
    print()
    phone_df = df.loc[(df[device_category] == device_category_value) & (df[price_category] == price_category_value)]
    grouped_df = phone_df.groupby([released_year, brand]).agg({
        metrics1: metrics_group1,
        metrics2: metrics_group2,
        metrics3: metrics_group3
    }).reset_index()
    input_line = input("Enter two brands separated by a single comma: ")
    try:
        brand1, brand2 = input_line.split(',')
        # Separate data for each brand
        brand1_data = grouped_df[grouped_df[brand] == brand1]
        brand2_data = grouped_df[grouped_df[brand] == brand2]

        # Plotting
        fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(fig_width, fig_height), sharex=True)
        plt.subplots_adjust(right=0.8)
        metrics = [metrics1, metrics2, metrics3]
        metrics_name = [metrics_name1, metrics_name2, metrics_name3]
        all_years = sorted(set(brand1_data[released_year]).union(set(brand2_data[released_year])))

        for i, metric in enumerate(metrics):
            axes[i].set_title(f'{title} {metrics_name[i]}', fontsize=fontsize + 2)
            axes[i].bar(brand1_data[released_year], brand1_data[metric], width=0.4, label=brand1, align='edge')
            axes[i].bar(brand2_data[released_year], brand2_data[metric], width=-0.4, label=brand2, align='edge')
            axes[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
            axes[i].set_xticks(all_years)
            axes[i].set_xticklabels(all_years)
            axes[i].margins(x=0.10)

        plt.xlabel(x_label)
        plt.tight_layout()
        plt.show()
    except ValueError:
        print("Error: Please ensure you enter two brands separated by a single comma")


# Main entry function
def analytics_visualize(path, choice, fontsize, fig_width, fig_height):
    # path - filename of dataset
    # choice - menu option selected
    # fontsize, fig_width, fig_height - values for charts
    import pandas as pd
    try:
        df = pd.read_csv(path, header=0, encoding='utf-8')
        # Reformat fields
        df['released_date'] = pd.to_datetime(df['released_date'], format='%d-%m-%y')
        df['released_year'] = df['released_date'].dt.year
        df['released_month'] = df['released_date'].dt.month
        df['market_regions'] = df['market_regions'].tolist()
        # Main case/loop for menu options
        match choice:
            # Identify the top 5 regions where a specific brand of devices was sold.
            case 4:
                top_features(
                    df=df,
                    filter_feature='brand',
                    count_feature='market_regions',
                    top_number=5,
                    text="Top 5 regions for")
            # Analyse the average price of devices within a specific brand, all in the same currency.
            case 5:
                avg_group_filter(
                    df=df,
                    filter_feature='brand',
                    group_feature='price_currency',
                    avg_feature='price',
                    text='Average price within a specific brand in the same currency:')
            # Analyse the average mass for each manufacturer and display the list of average mass for all manufacturers
            case 6:
                avg_group(
                    df=df,
                    group_feature='manufacturer',
                    avg_feature='weight_gram',
                    text='Average weight for each manufacturer:')
            # Count the number of released devices by hardware designer
            case 7:
                count_group_two(
                    df=df,
                    count_feature1='hardware_designer',
                    count_feature2='released_year',
                    text='Number of devices released by hardware designer annually:')
            # Proportion of RAM types for devices in the current market
            case 8:
                pie_chart_filtered(
                    df,
                    filter_feature='market_regions',
                    count_feature='ram_type',
                    fontsize=fontsize,
                    fig_width=fig_width,
                    fig_height=fig_height,
                    title="Proportion of RAM Types in")
            # Compare the number of devices for each USB connector type
            case 9:
                chart_counted(
                    df,
                    count_feature='usb_connector',
                    fontsize=fontsize,
                    fig_width=fig_width,
                    fig_height=fig_height,
                    y_label='Number of Devices',
                    title='Number of Devices for Each USB Connector Type'
                )
            # Monthly average price trends (in GBP) for # devices released in each year from 2020 to 2023
            case 10:
                chart_monthly_price(
                    df,
                    filter_feature='price_currency',
                    filter_value='GBP',
                    min_year=2020,
                    max_year=2023,
                    count_feature1='released_year',
                    count_feature2='released_month',
                    average_feature='price',
                    fontsize=fontsize,
                    fig_width=fig_width,
                    fig_height=fig_height,
                    x_label='Month',
                    y_label='Average Price in GBP',
                    title='Monthly Average Price (GBP) in'
                )
            # Visualise the average price, weight and memory for two brands
            case 11:
                chart_metrics_three(
                    df=df,
                    device_category='device_category',
                    device_category_value='Smartphone',
                    price_category='price_currency',
                    price_category_value='USD',
                    released_year='released_year',
                    brand='brand',
                    metrics1='price',
                    metrics2='weight_gram',
                    metrics3='non_volatile_memory_capacity',
                    metrics_group1='max',
                    metrics_group2='median',
                    metrics_group3='median',
                    metrics_name1='Max price (USD)',
                    metrics_name2='Median weight (grams)',
                    metrics_name3='Median memory capacity (Gb)',
                    fig_width=fig_width,
                    fig_height=fig_height,
                    fontsize=fontsize,
                    x_label='Year',
                    title='Comparison of 2 brands:'
                )

    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    except IOError:
        print(f"Error: IO error occurred while opening {path} ")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

