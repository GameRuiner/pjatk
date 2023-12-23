import streamlit as st
import pandas as pd

st.title("Dashboard")
st.header('Diamonds dataset - PAD final project')

df = pd.read_csv('cleaned_data.csv')

# taking columns from modeling part
# ['carat', 'clarity_I1', 'clarity_SI1', 'clarity_SI2', 'cut_Premium']
st.subheader('Diamond Grading - Clarity Grades')
st.markdown('The clarity of a diamond is determined by the number, location and type of inclusions it contains')
st.markdown('The GIA (Gemological Institute of America) has designated that clarity of diamonds is graded under the following guidelines (some grades were omitted in dataset):')
st.markdown('''**IF:**\n
Absolutely free from internal faults under 10X magnification. May contain external features that should be so small that they can easily be removed by polishing''')
st.markdown('''**VVS1:**\n
Very, very small inclusions in the stone, very difficult to recognize under 10X magnification. These inclusions can not be in the field of the table''')
st.markdown('''**VVS2:**\n
Very, very small inclusions anywhere in the stone, only smallest external defects allowed''')
st.markdown('''**SI1:**\n
Small internal faults, not visible to the naked eye''')
st.markdown('''**SI2:**\n
Small, easily seen inclusions under magnification in the table, but still not visible to the naked eye''')
st.markdown('''**I1:**\n
Inclusions easily seen under magnification, but difficult to see with the naked eye. Inclusions do not influence brilliance''')
st.bar_chart(df[['clarity', 'price']], x='price', y='clarity')
st.markdown('We can notice that IF and VVS1 (best two grades) starting from higher prices and finished with higher prices too)')

st.subheader('Diamond Grading - Color Grade')
st.markdown('Most commercially available diamonds are classified by color, or more appropriately, the lack of color. The most valuable diamonds are those classified as colorless')
st.line_chart(df[['color', 'price']], x='price', y='color')
st.markdown('Colors from original dataset were grouped in two categories: colorless and near colorless. As we see colorless tends to have higher price')

st.subheader('Diamond Grading - Cut Grade and the Ideal Cut')
st.markdown('The beauty of a diamond resides not only in a favorable body color, but more importantly in its optical properties, in particular the high refractive index and color dispersion')
st.markdown('Cut Scale: Ideal, Premium, Very good, Good, Fair')
st.line_chart(df[['cut', 'price']], x='price', y='cut')
st.markdown('Despite lower scale than Ideal Premium differs the most from others and has higher prices')

st.subheader('Diamond Grading - Carat Weight')
st.markdown('In addition to color, clarity and cut, weight provides a further basis in the valuation of a diamond')
st.area_chart(df[['carat', 'price']], x='price', y='carat')
st.markdown('Visible positive corelation between price and carat')

st.subheader('Diamond Grading - Depth and Table')
st.markdown('Together, the depth and table size of a diamond significantly influence how light is reflected back to the viewer’s eye, thereby affecting its brilliance')
st.markdown('Depth table was dropped due to hight corelation with carat')
st.line_chart(df[['price', 'table']], x='price', y='table')
st.markdown('No significant corelation between price and table')

# add sidebar