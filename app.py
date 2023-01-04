import streamlit as st
import streamlit.components.v1 as stc
import requests
from requests.exceptions import Timeout
import base64
import json

st.title("MeCab Web App")
inputText = st.text_input("入力文:", value="今日は良い天気だ")

button = st.button("解析")

if button:
    data = {
        'text':inputText
    }

    isConnectedSuccess = False

    try:
        res = requests.post('http://0.0.0.0:8000/mecab', json.dumps(data), timeout=20.0)
        if res.status_code == 200:
            st.success(f"status_code:{res.status_code}")
            isConnectedSuccess = True
        else:
            st.error(f"status_code:{res.status_code}")
    except Timeout:
        st.error(f"timeout")
    except Exception as e:
        st.error(f"error:{e}")
                
    if isConnectedSuccess:
        res_json = res.json()
        res_result = res_json['result']
        
        st.text(res_result)
