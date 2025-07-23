import ollama
from PIL import Image
import base64
import streamlit as st
import io

st.title('vision to text generator')

uploaded_image=st.file_uploader('upload ur image',type=['jpg','jpeg','png'])

def image_to_bytes(image_path):
    image=Image.open(image_path)
    buffered=io.BytesIO()
    image.save(buffered,format='PNG')
    encoded_image=base64.b64encode(buffered.getvalue()).decode('utf-8')
    return encoded_image,image

if uploaded_image:
    encoded_img,image=image_to_bytes(uploaded_image)
    st.image(image,'uploaded image',use_column_width=True)

    prompt=st.text_input("ask about the image",value='extract and explain the details from the image')

    with st.spinner('analyzing'):
        try:
            response=ollama.chat(model='gemma3:4b',messages=[{'role':'user','content':prompt,'images':[encoded_img]}])
            answer=response['message']['content']
            st.write(answer)
        except Exception as e:
            st.error(f'error:{e}')





