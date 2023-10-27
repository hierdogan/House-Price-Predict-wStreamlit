import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="HousePrice Prediction App",
    page_icon="🏠",
    layout="wide"
    )


app_mode = st.sidebar.selectbox('Select Page',['Welcome','Prediction','About Project','Team'])
if app_mode=='Welcome':
    st.title("Let's Find The Dream House")
    st.image('./vis/welcome.png')
    st.write('App designed by HIErdogan with ❤️')
    st.divider()
    st.subheader('This project was prepared as a final project for Miuul&VBO Data Analytics Bootcamp, DA02 semester.')


############## PREDICTION PAGE ##############

# TODO add an explanation and specify feature range and explain

elif app_mode =='Prediction':
    #st.balloons()

    container = st.container()

    col1, col2 = container.columns([1,1])

    with col1:
        def main():
            style = """<div style='background-color:pink; padding:12px'>
                    <h1 style='color:black'>House Price Prediction</h1>
            </div>"""
            st.markdown(style, unsafe_allow_html=True)
            st.header('How to make it?')
            st.write('You can make an approximate price estimate by updating the values you see below in accordance with the \
                    features of the house you are looking for - at the specified intervals. \
                    This will enable customers to make informed decisions when buying or selling properties.')
            st.divider()
            left, right = st.columns((2,2))
            OverallQual = left.number_input('Rates the overall material and finish of the house(1-10)', step=1, format='%d', value= 1, min_value=1, max_value=10)
            GrLivArea = right.number_input('Above grade (ground) living area square feet(1-5650)',  step=1, format='%d', value= 0, max_value=5650)
            TotalBsmtSF = left.number_input('Total square feet of basement area', step=1, format='%d', value=0, max_value=2070)
            GarageCars = right.number_input('Size of garage in car capacity', step=1, format='%d', value=0, max_value=5)
            AgeBuilt = left.number_input('Original construction age', step=1, format='%d', value=0, max_value=73)
            BsmtFinSF1 = right.number_input('Rating of Type 1 basement finished area square feet', step=1, format='%d', value=0, max_value=1833)
            LotArea = left.number_input('Lot size in square feet',  step=1, format='%d', value=0, max_value=17729)
            OverallCond = right.number_input('Rates the overall condition of the house', step=1, format='%d', value=0, max_value=10)
            button = st.button('Predict')
            # if button is pressed
            if button:
                # make prediction
                result = predict(OverallQual, GrLivArea, TotalBsmtSF, GarageCars, AgeBuilt, BsmtFinSF1, LotArea, OverallCond)
                st.success(f'The value of the house is ${result}')

        # load the train model
        #with open('./xgb_model.pkl', 'rb') as rf:
        model = pickle.load(open('./xgb_model.pkl', 'rb'))

        def predict(OverallQual, GrLivArea, TotalBsmtSF, GarageCars, AgeBuilt, BsmtFinSF1, LotArea, OverallCond):
            lists = [OverallQual, GrLivArea, TotalBsmtSF, GarageCars, AgeBuilt, BsmtFinSF1, LotArea, OverallCond]
            df = pd.DataFrame(lists).transpose()
        #     # scaling the data
        #    scaler.transform(df)
            # making predictions using the train model
            prediction = model.predict(df)
            result = int(prediction)
            return result

        if __name__ == '__main__':
            main()

    # Görsel
    with col2:
        image = st.image('./vis/predict.jpg', caption="Let's Calculate")

############## ABOUT  PROJECT ##############
elif app_mode =='About Project':
    st.title('Define the objective')
    st.write('The objective of the project is to develop a house price prediction model that can provide accurate estimates for customers. \
             This will enable customers to make informed decisions when buying or selling properties.')
    
    st.title('Identify the target audience')
    st.write('The target audience includes potential home buyers and sellers who require reliable price estimates.')

    st.title('Understand the requirements')
    st.write('The house price prediction model should be built using a dataset comprising 2,919 observations and 80 variables, \
             including the target variable (house prices). The model should consider various features that are likely to impact house prices, such as property characteristics, \
             location data, and other relevant information.')
    
    st.title('Identify key performance indicators (KPIs)')
    st.write('The success of the prediction model will be evaluated using several KPIs, including Mean Squared Error (MSE), Root Mean Squared Error (RMSE), \
             Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), and R-squared. These metrics will provide insights into the accuracy and performance of the model.')


############## TEAM ##############

elif app_mode =='Team':
    st.header("Team Members 👩‍💻‍👨‍💻")

    # Ekip üyelerinin isimleri ve LinkedIn profillerinin linkleri
    ekip_uyeleri = {

        "Halil İbrahim Erdoğan" : "https://www.linkedin.com/in/hierdogan",
        "Zeliha V.A. Toraman": "https://www.linkedin.com/in/zeliha-v-a-toraman"
    }

    for isim, profil_linki in ekip_uyeleri.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [LinkedIn]({profil_linki})")
    st.header(" ")
    st.divider()
    st.header("Educators 👨‍🔬")
    educators = {

        "Educator : Atilla Yardımcı, Ph.D." : "https://www.linkedin.com/in/atillayardimci",
        "Mentor Teacher : Caner Gündüz" : "https://www.linkedin.com/in/cgunduz"
    }

    for isim, profil_linki in educators.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [LinkedIn]({profil_linki})")

    st.header(" ")
    st.divider()
    st.header("Education Platform 🏫")
    company = {

        "Miuul": "https://miuul.com",
        "Veri Bilimi Okulu" : "https://www.veribilimiokulu.com"
    }

    for isim, profil_linki in company.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [Web Site]({profil_linki})")
