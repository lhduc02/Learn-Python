import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Đọc dữ liệu từ website
url = "https://worldpopulationreview.com/country-rankings/ef-english-proficiency-index-by-country"
tables = pd.read_html(url)  # Trả về danh sách các bảng trên trang
df = tables[0]  # Chọn bảng đầu tiên

# Kiểm tra số lượng cột trong DataFrame
print(df.columns)  # Xem các cột hiện có để đảm bảo đúng với dữ liệu thực tế

# Đặt lại tên các cột (điều chỉnh lại theo số cột thực tế)
df.columns = ['COUNTRY', 'EF SCORE 2023', 'EF PROFICIENCY BAND 2023']

# Standardize country names in the dataframe to match the geospatial dataset
df['COUNTRY'] = df['COUNTRY'].replace({
    'United States of America': 'United States',
    'Russian Federation': 'Russia',
    'Korea (Republic of)': 'South Korea'
})

# Merge the EF proficiency data with the world map data
world = world.merge(df, how="left", left_on="name", right_on="COUNTRY")

# Create a dictionary to map proficiency bands to colors
proficiency_colors = {
    'Very High': '#1a9641',    # Dark Green
    'High': '#a6d96a',         # Light Green
    'Moderate': '#fdae61',     # Light Orange
    'Low': '#f46d43',          # Orange
    'Very Low': '#d73027',     # Red
    None: '#ffffff'            # White for countries with no data
}

# Create the plot with proficiency bands mapped to color
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
world.plot(column='EF PROFICIENCY BAND 2023', ax=ax, legend=True, 
           cmap='RdYlGn', missing_kwds={'color': 'lightgrey', "label": "No data"})

# Customize legend and title
plt.title("EF English Proficiency Index by Country (2023)", fontsize=16)
plt.show()