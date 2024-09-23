# %%
pip install streamlit pandas


# %%
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# %%
df = pd.read_csv("housing.csv")
df

# %%
def load_data():
    df = pd.read_csv("housing.csv")
    return df
data = load_data()

# %%
st.sidebar.header("Filters")
price_filter = st.sidebar.slider('Select Median House Value Range', int(data['median_house_value'].min()), int(data['median_house_value'].max()), (50000, 300000))

# %%
# 位置类型选择器
ocean_proximity = st.sidebar.multiselect(
    'Select Location Type',
    options=data['ocean_proximity'].unique(),
    default=data['ocean_proximity'].unique()
)

# %%
# 收入水平选择器
income_level = st.sidebar.radio(
    "Select Income Level",
    ('Low', 'Medium', 'High')
)

# %%
# 筛选数据
filtered_data = data[
    (data['median_house_value'] >= price_filter[0]) & 
    (data['median_house_value'] <= price_filter[1]) &
    (data['ocean_proximity'].isin(ocean_proximity))
]

# %%
# 通过收入水平筛选
if income_level == 'Low':
    filtered_data = filtered_data[filtered_data['median_income'] <= 2.5]
elif income_level == 'Medium':
    filtered_data = filtered_data[(filtered_data['median_income'] > 2.5) & (filtered_data['median_income'] < 4.5)]
else:
    filtered_data = filtered_data[filtered_data['median_income'] > 4.5]


# %%
# 显示地图
st.map(filtered_data)

# %%

st.subheader("Histogram of Median House Value")
plt.hist(filtered_data['median_house_value'], bins=30)
st.pyplot(plt)

# %%
pip install streamlit


