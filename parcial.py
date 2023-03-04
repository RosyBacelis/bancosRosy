import streamlit as st
import pandas as pd


dfData = pd.read_csv("Herramientas3_2023_banco.csv.csv")
df = dfData.select_dtypes(exclude="number")

dfJobs = dfData.drop_duplicates(subset=["job"])
jobs = dfJobs [["job"]]
jobs = dfJobs ["job"].values.tolist()
print(jobs)
st.header('Crédito bancario')

clearJob = df['job'].unique().tolist()
clearMarital = df['marital'].unique().tolist()
clearEducation = df['education'].unique().tolist()
clearDefault = df['default'].unique().tolist()
clearHousing = df['housing'].unique().tolist()
clearLoan = df['loan'].unique().tolist()
clearContact = df['contact'].unique().tolist()
clearMonth = df['month'].unique().tolist()
clearDay_of_week = df['day_of_week'].unique().tolist()
clearPoutcome = df['poutcome'].unique().tolist()
#clearEmpvarrate = df['emp.var.rate'].unique().tolist()
#clearConspriceidx = df['cons.price.idx'].unique().tolist()
#clearConsconfidx = df['cons.conf.idx'].unique().tolist()
#clearEuribor3m = df['euribor3m'].unique().tolist()
#clearNremployed = df['nr.employed'].unique().tolist()
#clearY = df['y'].unique().tolist()




age = st.number_input('Inserte su edad', value=18)
job = st.selectbox("Seleccione su trabajo", clearJob)
marital = st.selectbox("Seleccione su estado civil", clearMarital)
education = st.selectbox("Seleccione su nivel educativo", clearEducation)
default = st.selectbox("Seleccione una opción", clearDefault)
housing = st.selectbox("Cuenta con vivienda propia", clearHousing)
loan = st.selectbox("Cuenta con Préstamo", clearLoan)
contact = st.selectbox("Seleccione su contacto", clearContact)
month = st.selectbox("Seleccione el mes", clearMonth)
day_of_week = st.selectbox("Seleccione el dia", clearDay_of_week)
duration = st.slider('Elige el duracion', 0, 56, 10)
campaign = st.slider('Elige campaña', 0, 12, 5)
pdays = st.slider('Elige dia', 0, 999, 10)
previous = st.slider('Elige previa', 0, 7, 2)
poutcome = st.selectbox("Seleccione su resultado", clearPoutcome)
#rate = st.slider('Elige el rando de valor ', 3.00,-0.28, -2.00, (3.00, -2.00))
#values = st.slider('Please select a range of values',0.0, 100.0, (40.0, 80.0))
#cons.price.idx
#cons.conf.idx
#euribor3m
#nr.employed = st.selectbox("Seleccione su contacto", clearNremployed)

if st.button('Buscar'):
    st.write('No existe')
else:
    st.write('Si existe')


#################
#option = st.selectbox(
 #   'How would you like to be contacted?',
  #  ('Email', 'Home phone', 'Mobile phone'))

#st.write('You selected:', option)


#number = st.number_input('Insert a number')
#st.write('The current number is ', number)