import joblib
import streamlit as st
import pandas as pd


def main():
    
    model = joblib.load("model.pkl")
    dct = joblib.load('dct_map_cat_data.pkl')
    
    
        
    st.title('Churn prediction')
    
    REGION = st.selectbox('Choose your region from the list below:', ['FATICK', 'DAKAR', 'KAOLACK', 'SAINT-LOUIS', 'THIES', 'TAMBACOUNDA', 'LOUGA', 'DIOURBEL', 'KOLDA', 'KAFFRINE', 'ZIGUINCHOR', 'MATAM', 'SEDHIOU', 'KEDOUGOU'])
    
    REGION = dct['dct_region'][REGION]
    
    TENURE = st.selectbox('How long have you been with present on the network', ['K > 24 month', 'I 18-21 month', 'G 12-15 month', 'H 15-18 month','F 9-12 month', 'J 21-24 month', 'D 3-6 month', 'E 6-9 month'])
    
    TENURE = dct['dct_tenure'][TENURE]
    
    MONTANT = st.number_input('Enter a top-up amount:', 100, 235000)
    
    FREQUENCE_RECH = st.slider('Select the number of time you made a recharge', 1, 140)
    
    REVENUE = st.number_input('Enter your monthly income:', 1, 532177)
    
    ARPU_SEGMENT = (float(REVENUE) / 3)
    
    FREQUENCE = FREQUENCE_RECH
    
    TOP_PACK = st.selectbox('Select an intent pack from the list below', ['On net 200F=Unlimited _call24H', 'Data:1000F=5GB,7d','All-net 500F=2000F;5d', 'Data: 100 F=40MB,24H',
                                                                          'MIXT: 200mnoff net _unl on net _5Go;30d', 'Jokko_Daily','MIXT:500F= 2500F on net _2500F off net;2d',
                                                                          'Data: 200 F=100MB,24H', 'Data:490F=1GB,7d', 'Data:1000F=2GB,30d','On-net 500F_FNF;3d', 'IVR Echat_Daily_50F', 'Pilot_Youth4_490',
                                                                          'Mixt 250F=Unlimited_call24H', 'On-net 500=4000,10d','Data:200F=Unlimited,24H', 'All-net 500F =2000F_AllNet_Unlimited',
                                                                          'All-net 600F= 3000F ;5d', 'Data:3000F=10GB,30d','Twter_U2opia_Daily', 'All-net 1000=5000;5d',
                                                                          'Data:150F=SPPackage1,24H', 'Yewouleen_PKG', 'Twter_U2opia_Weekly','New_YAKALMA_4_ALL', 'Jokko_promo', 'On-net 1000F=10MilF;10d',
                                                                          'Facebook_MIX_2D', 'All-net 500F=1250F_AllNet_1250_Onnet;48h','Data:500F=2GB,24H', '200=Unlimited1Day', 'On-net 200F=60mn;1d',
                                                                          'YMGX 100=1 hour FNF, 24H/1 month', 'On net 200F= 3000F_10Mo ;24H','Data:1500F=3GB,30D', 'VAS(IVR_Radio_Daily)', 'SUPERMAGIK_5000',
                                                                          'MIXT: 590F=02H_On-net_200SMS_200 Mo;24h\t\t','Data:DailyCycle_Pilot_1.5GB', 'Twter_U2opia_Monthly',
                                                                          'Data: 490F=Night,00H-08H', 'Data:50F=30MB_24H','On-net 300F=1800F;3d', 'Data:700F=1.5GB,7d',
                                                                          'CVM_on-net bundle 500=5000', 'Data:300F=100MB,2d','Pilot_Youth1_290', 'MROMO_TIMWES_RENEW', 'All-net 300=600;2d',
                                                                          'Jokko_Monthly', 'All-net 1000F=(3000F On+3000F Off);5d','Data:30Go_V 30_Days', 'All-net 5000= 20000off+20000on;30d',
                                                                          'All-net 500F=4000F ; 5d', '500=Unlimited3Day','MROMO_TIMWES_OneDAY', 'MIXT: 390F=04HOn-net_400SMS_400 Mo;4h\t',
                                                                          'SUPERMAGIK_1000','MIXT:1000F=4250 Off net _ 4250F On net _100Mo; 5d','MIXT: 5000F=80Konnet_20Koffnet_250Mo;30d\t\t', 'FNF2 ( JAPPANTE)',
                                                                          'EVC_500=2000F', 'EVC_JOKKO30', 'TelmunCRBT_daily','APANews_weekly', 'EVC_100Mo', 'Jokko_Weekly',
                                                                          'Internat: 1000F_Zone_1;24H\t\t', 'DataPack_Incoming','Data:1500F=SPPackage1,30d', '200F=10mnOnNetValid1H',
                                                                          'MIXT: 500F=75(SMS, ONNET, Mo)_1000FAllNet;24h\t\t','Internat: 1000F_Zone_3;24h\t\t','MIXT:10000F=10hAllnet_3Go_1h_Zone3;30d\t\t',
                                                                          'Data:700F=SPPackage1,7d', 'CVM_200f=400MB','Mixt : 500F=2500Fonnet_2500Foffnet ;5d','Internat: 2000F_Zone_2;24H\t\t',
                                                                          'On-net 2000f_One_Month_100H; 30d', 'FIFA_TS_daily','IVR Echat_Weekly_200F', '305155009','MIXT: 4900F= 10H on net_1,5Go ;30d', 'Data: 200F=1GB,24H',
                                                                          '1000=Unlimited7Day', '1500=Unlimited7Day', 'pack_chinguitel_24h','VAS(IVR_Radio_Monthly)', 'EVC_Jokko_Weekly',
                                                                          'Incoming_Bonus_woma', 'CVM_100f=200 MB', 'VAS(IVR_Radio_Weekly)','EVC_4900=12000F', 'CVM_500f=2GB', 'Go-NetPro-4 Go', 'EVC_700Mo',
                                                                          'CVM_100F_unlimited', 'FNF_Youth_ESN', 'CVM_On-net 400f=2200F','NEW_CLIR_PERMANENT_LIBERTE_MOBILE', 'EVC_MEGA10000F','Data_EVC_2Go24H', 'EVC_1Go'] )
    TOP_PACK = dct['dct_top_pack'][TOP_PACK]
    
    FREQ_TOP_PACK = st.number_input('Enter the number of times you have activated the top pack packages', 1, 713)
    
    DATA_VOLUME = st.slider('Choose the the amount of data in (Mo) from the barre below', 0, 500)
    
    ON_NET = st.number_input('Enter the number of calls made to ON_NET',1, 50809)
    
    ORANGE = st.number_input('Enter the number of calls made to ORANGE',1, 21323)
    
    TIGO = st.number_input('Enter the number of calls made to TIGO', 1, 4174)
    
    REGULARITY = st.number_input('How many times have you been active for the last 90 days on the network',1, 62)
    
    # DataFrame reconstruction
    input_data = pd.DataFrame({'REGION': [REGION], 'TENURE': [TENURE],'MONTANT':[MONTANT], 'FREQUENCE_RECH': [FREQUENCE_RECH],'REVENUE':[REVENUE], 'ARPU_SEGMENT':[ARPU_SEGMENT],
                               'FREQUENCE':[FREQUENCE],'DATA_VOLUME': [DATA_VOLUME], 'ON_NET':[ON_NET], 'ORANGE': [ORANGE],'TIGO': [TIGO], 'REGULARITY': [REGULARITY],
                               'TOP_PACK': [TOP_PACK],'FREQ_TOP_PACK':[FREQ_TOP_PACK] }, index=[0])
    
    
    
    

    
    button = st.button('Make Prediction')
    
    if button:
        st.write('Based on the information provided')
        predict = model.predict(input_data)
        if predict == 1:
            st.error('The client will probably churn')
        else:
            st.success('The client will probably stay')


main()
