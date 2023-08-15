import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



st.title("Supermarket Sales Dashboard")

st.cache_data
def load_data():
    file_path = "supermarket_sales.csv"
    df = pd.read_csv(file_path)
    return df

data = load_data()

unique_branch = sorted(data["Branch"].unique())
unique_city = sorted(data["City"].unique())
unique_customer = sorted(data["Customer type"].unique())
unique_product = sorted(data["Product line"].unique())
unique_payment = sorted(data["Payment"].unique())

st.sidebar.header("User Input Features")
branch = st.sidebar.multiselect('Branch', unique_branch, unique_branch)
city = st.sidebar.multiselect('City', unique_city, unique_city)
customer = st.sidebar.multiselect('Customer', unique_customer, unique_customer)
gender = st.sidebar.multiselect('Gender', ['Male', 'Female'], ['Male', 'Female'])
product = st.sidebar.multiselect('Product Line', unique_product, unique_product)
payment = st.sidebar.multiselect('Payment type', unique_payment, unique_payment)

df_selected_sales = data[(data["Branch"].isin(branch)) 
                        & (data["City"].isin(city)) 
                        & (data["Customer type"].isin(customer)) 
                        & (data["Gender"].isin(gender))
                        & (data["Product line"].isin(product))
                        & (data["Payment"].isin(payment))]

if st.button("Show Table"):
    st.write(df_selected_sales)


# # Rating by Product Line

# #Groupping Product line by rating
# groupped_product = df_selected_sales.groupby('Product line')['Rating'].mean().reset_index(drop=False)

# #Rounding Rating column to 1 number
# groupped_product_rating = groupped_product.round(1)

# #Sorting by average rating
# groupped_product_rating = groupped_product_rating.sort_values(by= 'Rating' , ascending =False)

# #Chossing palette
# palette = sns.color_palette('Greens_d')
# palette.reverse()

# #Make a horizontal bar graph for rating for each product line
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))
# sns.barplot(y = 'Product line' , x = 'Rating' , data = groupped_product_rating, palette =palette)

# #Showing Values
# ax.bar_label(ax.containers[0])

# #Setting a title
# plt.title('Rating for Product Lines')

# st.pyplot(fig)
if st.button("Average Sales"):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(6, 8))
    # plt.subplots_adjust(wspace=0.2, hspace=0.4)
    ax1 = axes[0][0]
    ax2 = axes[0][1]
    ax3 = axes[1][0]
    ax4 = axes[1][1]
    ax5 = axes[2][0]
    ax6 = axes[2][1]
    
    sns.set(style='ticks') 
    # Chart 1
    #Groupping Product line by rat
    groupped_product_total = df_selected_sales.groupby('Product line')['Total'].mean().reset_index(drop=False)
    #Rounding Rating column to 1 number
    groupped_product_total = groupped_product_total.round(1)
    #Making a scatter plot for Product lines` average sales
    sns.barplot(data = groupped_product_total, x = 'Product line' , y = 'Total', ax = ax1)
    # Data labels
    for p in ax1.patches:
        ax1.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=6)
    #Making a horizontal line for average
    ax1.axhline(y=np.nanmean(df_selected_sales.Total), color='red', linestyle='--', linewidth=1, label='Avg')
    #Setting a title and labels
    ax1.set_ylim(300, 350)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation = 45, fontsize=6)
    ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=6)
    ax1.set_title('Average Sales for Product Lines', fontsize=8)

    # Chart 2
    #Groupping Product line by rat
    groupped_branch_total = df_selected_sales.groupby('Branch')['Total'].mean().reset_index(drop=False)
    #Rounding Rating column to 1 number
    groupped_branch_total = groupped_branch_total.round(1)
    #Making a scatter plot for Product lines` average sales
    sns.barplot(x = 'Branch' , y = 'Total' , data = groupped_branch_total, ax = ax2)
    # Data labels
    for p in ax2.patches:
        ax2.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=6)
    #Making a horizontal line for average
    ax2.axhline(y=np.nanmean(df_selected_sales.Total), color='red', linestyle='--', linewidth=1, label='Avg')
    #Setting a title and labels
    ax2.set_ylim(300, 350)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation = 45, fontsize=6)
    ax2.set_yticklabels(ax2.get_yticklabels(), fontsize=6)
    ax2.set_title('Average Sales for Branch', fontsize=8)
   
    # Chart 3
    #Groupping Product line by rat
    groupped_city_total = df_selected_sales.groupby('City')['Total'].mean().reset_index(drop=False)
    #Rounding Rating column to 1 number
    groupped_city_total = groupped_city_total.round(1)
    #Making a scatter plot for Product lines` average sales
    sns.barplot(x = 'City' , y = 'Total' , data = groupped_city_total, ax = ax3)
    # Data labels
    for p in ax3.patches:
        ax3.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=6)
    #Making a horizontal line for average
    ax3.axhline(y=np.nanmean(df_selected_sales.Total), color='red', linestyle='--', linewidth=1, label='Avg')
    #Setting a title and labels
    ax3.set_ylim(300, 350)
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation = 45, fontsize=6)
    ax3.set_yticklabels(ax3.get_yticklabels(), fontsize=6)
    ax3.set_title('Average Sales for City', fontsize=8)
    

    # Chart 4
    #Groupping Product line by rat
    groupped_customer_total = df_selected_sales.groupby('Customer type')['Total'].mean().reset_index(drop=False)
    #Rounding Rating column to 1 number
    groupped_customer_total = groupped_customer_total.round(1)
    #Making a scatter plot for Product lines` average sales
    sns.barplot(x = 'Customer type' , y = 'Total' , data = groupped_customer_total, ax = ax4)
    # Data labels
    for p in ax4.patches:
        ax4.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=6)
    #Making a horizontal line for average
    ax4.axhline(y=np.nanmean(df_selected_sales.Total), color='red', linestyle='--', linewidth=1, label='Avg')
    #Setting a title and labels
    ax4.set_ylim(300, 350)
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation = 45, fontsize=6)
    ax4.set_yticklabels(ax4.get_yticklabels(), fontsize=6)
    ax4.set_title('Average Sales for Costumer type', fontsize=8)
    

    # Chart 5
    #Groupping Product line by rat
    groupped_gender_total = df_selected_sales.groupby('Gender')['Total'].mean().reset_index(drop=False)
    #Rounding Rating column to 1 number
    groupped_gender_total = groupped_gender_total.round(1)
    #Making a scatter plot for Product lines` average sales
    sns.barplot(x = 'Gender' , y = 'Total' , data = groupped_gender_total, ax = ax5)
    # Data labels
    for p in ax5.patches:
        ax5.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=6)
    #Making a horizontal line for average
    ax5.axhline(y=np.nanmean(df_selected_sales.Total), color='red', linestyle='--', linewidth=1, label='Avg')
    #Setting a title and labels
    ax5.set_ylim(300, 350)
    ax5.set_xticklabels(ax5.get_xticklabels(), rotation = 45, fontsize=6)
    ax5.set_yticklabels(ax5.get_yticklabels(), fontsize=6)
    ax5.set_title('Average Sales for Gender', fontsize=8)


    # Chart 6
    #Groupping Product line by rat
    groupped_payment_total = df_selected_sales.groupby('Payment')['Total'].mean().reset_index(drop=False)
    #Rounding Rating column to 1 number
    groupped_payment_total = groupped_payment_total.round(1)
    #Making a scatter plot for Product lines` average sales
    sns.barplot(x = 'Payment' , y = 'Total' , data = groupped_payment_total, ax = ax6)
    # Data labels
    for p in ax6.patches:
        ax6.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=6)#Making a horizontal line for average
    ax6.axhline(y=np.nanmean(df_selected_sales.Total), color='red', linestyle='--', linewidth=1, label='Avg')
    #Setting a title and labels
    ax6.set_ylim(300, 350)
    ax6.set_xticklabels(ax6.get_xticklabels(), rotation = 45, fontsize=6)
    ax6.set_yticklabels(ax6.get_yticklabels(), fontsize=6)
    ax6.set_title('Average Sales for Product Lines', fontsize=8)
    
    sns.set_style("ticks") 
    plt.tight_layout()
    st.pyplot(fig)

if st.button("Distributions"):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(6, 8))
    # plt.subplots_adjust(wspace=0.2, hspace=0.4)
    ax1 = axes[0][0]
    ax2 = axes[0][1]
    ax3 = axes[1][0]
    ax4 = axes[1][1]
    ax5 = axes[2][0]
    ax6 = axes[2][1]

   
    count_branch = df_selected_sales.groupby('Branch').count()['cogs']
    count_branch.plot(kind='pie', autopct= '%.2f', figsize=(10,7),subplots=True, wedgeprops=dict(width=0.30), ax = ax1, fontsize=8)
    ax1.set_title('Branch', fontsize = 10)
    ax1.set_ylabel('')

    count_city = df_selected_sales.groupby('City').count()['cogs']
    count_city.plot(kind='pie', autopct= '%.2f', figsize=(10,7),subplots=True, wedgeprops=dict(width=0.30), ax = ax2, fontsize=8)
    ax2.set_ylabel('')
    ax2.set_title('City', fontsize = 10)

    count_customer = df_selected_sales.groupby('Customer type').count()['cogs']
    count_customer.plot(kind='pie', autopct= '%.2f', figsize=(10,7),subplots=True, wedgeprops=dict(width=0.30), ax = ax3, fontsize=8)
    ax3.set_title('Customer Type', fontsize = 10)
    ax3.set_ylabel('')

    count_gender = df_selected_sales.groupby('Gender').count()['cogs']
    count_gender.plot(kind='pie', autopct= '%.2f', figsize=(10,7),subplots=True, wedgeprops=dict(width=0.30), ax = ax4, fontsize=8)
    ax4.set_title('Gender', fontsize = 10)
    ax4.set_ylabel('')

    count_product = df_selected_sales.groupby('Product line').count()['cogs']
    count_product.plot(kind='pie', autopct= '%.2f', figsize=(10,7),subplots=True, wedgeprops=dict(width=0.30), ax = ax5, fontsize=8)
    ax5.set_title('Product Line', fontsize = 10)
    ax5.set_ylabel('')

    count_payment = df_selected_sales.groupby('Payment').count()['cogs']
    count_payment.plot(kind='pie', autopct= '%.2f', figsize=(10,7),subplots=True, wedgeprops=dict(width=0.30), ax = ax6, fontsize=8)
    ax6.set_title('Payment Type', fontsize = 10)
    ax6.set_ylabel('')


    st.pyplot(fig)



