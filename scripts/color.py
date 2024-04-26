import streamlit as st
from PIL import Image, ImageEnhance

st.title("画像色調調整アプリ")

uploaded_file = st.file_uploader(
    "画像ファイルをアップロードしてください", type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロードされた画像", use_column_width=True)

    # 色調の調整
    enhance_type = st.selectbox(
        "色調を選択してください",
        options=["コントラスト", "明るさ", "シャープネス"],
    )
    factor = st.slider("調整の度合いを選択してください", 0.1, 2.0, 1.0)

    if st.button("色調を調整"):
        if enhance_type == "コントラスト":
            enhancer = ImageEnhance.Contrast(image)
        elif enhance_type == "明るさ":
            enhancer = ImageEnhance.Brightness(image)
        elif enhance_type == "シャープネス":
            enhancer = ImageEnhance.Sharpness(image)

        # 画像を調整
        img_enhanced = enhancer.enhance(factor)
        st.image(img_enhanced, caption="調整後の画像", use_column_width=True)
