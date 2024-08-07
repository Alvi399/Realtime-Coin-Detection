import cv2
import cvzone
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


class VideoTransformer(VideoTransformerBase):
    def __init__(self, threshold1, threshold2, coin_areas):
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        self.coin_areas = coin_areas

    def preProcessing(self, img):
        imgPre = cv2.GaussianBlur(img, (5, 5), 3)
        imgPre = cv2.Canny(imgPre, self.threshold1, self.threshold2)
        kernel = np.ones((3, 3), np.uint8)
        imgPre = cv2.dilate(imgPre, kernel, iterations=1)
        imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
        return imgPre

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        jumlahKoin = 0
        totalKoin = 0
        imgCount = np.zeros((480, 640, 3), np.uint8)

        imagePre = self.preProcessing(img)
        imageContours, conFound = cvzone.findContours(img, imagePre, minArea=20)

        if conFound:
            for con in conFound:
                peri = cv2.arcLength(con['cnt'], True)
                approx = cv2.approxPolyDP(con['cnt'], 0.02 * peri, True)

                if len(approx) > 7:
                    area = con['area']
                    # print(f'Area: {area}')
                    if area > 1000:
                        for value, range_ in self.coin_areas.items():
                            if range_[0] <= area < range_[1]:
                                totalKoin += value
                                jumlahKoin += 1
                                break

        cvzone.putTextRect(imgCount, f"Jumlah koin: {jumlahKoin}", [10, 30], 2, 2, colorR=(0, 255, 0))
        cvzone.putTextRect(imgCount, f"Total koin: {totalKoin}", [10, 70], 2, 2, colorR=(0, 255, 0))
        imageStacked = cvzone.stackImages([img, imagePre, imageContours, imgCount], 2, 1)

        return imageStacked


st.title("Proyek Deteksi Koin dengan Streamlit dan OpenCV")
# Sidebar for thresholds and coin area settings
st.sidebar.title("Pengaturan")
threshold1 = st.sidebar.slider("Threshold 1", 0, 255, 255)
threshold2 = st.sidebar.slider("Threshold 2", 0, 255, 160)
coin_areas = {
    100: (st.sidebar.slider("100 Rupiah - Min Area", 0, 5000, 3000), st.sidebar.slider("100 Rupiah - Max Area", 0, 5000, 3500)),
    200: (st.sidebar.slider("200 Rupiah - Min Area", 0, 5000, 3800), st.sidebar.slider("200 Rupiah - Max Area", 0, 5000, 4600)),
    500: (st.sidebar.slider("500 Rupiah - Min Area", 0, 5000, 4600), st.sidebar.slider("500 Rupiah - Max Area", 0, 5000, 5000)),
    1000: (st.sidebar.slider("1000 Rupiah - Min Area", 0, 5000, 3500), st.sidebar.slider("1000 Rupiah - Max Area", 0, 5000, 3800)),
}

# Create an instance of the VideoTransformer class with the sidebar settings
transformer = VideoTransformer(threshold1, threshold2, coin_areas)

# Streamlit webrtc streamer
webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=lambda: transformer)

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: black;
        text-align: center;
        padding: 10px;
        color: white;
        border-top: 1px solid #ddd;
    }
    </style>
    <div class="footer">
        <p>© 2024 Muhammad Alvi Kirana Zulfan Nazal. Semua hak cipta dilindungi.</p>
    </div>
    """,
    unsafe_allow_html=True
)
