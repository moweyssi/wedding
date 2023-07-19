import streamlit as st
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


t = st.radio("Toggle to see font change", [True, False])

if t:
    st.markdown(
        """
        <style>
@font-face {
  font-family: 'Tangerine';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

    html, body, [class*="css"]  {
    font-family: 'Tangerine';
    font-size: 48px;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )

"# Hello"

"""This font will look different, based on your choice of radio button"""




st.image("info.png")

st.subheader("Dearest Friends,")
"""
Allow us to share with you some more details of the highly-anticipated wedding of the millennium. We hope the following points will give you an idea of the festivities on that glorious day:

Who: Anna and Max

When: Saturday, September 2, 2023

Where: The beautiful Chříč Castle at Chříč 1

Ceremony: Commencing at 2:00 PM

Arrivals: From 12:30 PM to 1:30 PM.


Light refreshments will be provided. For those camping enthusiasts, we suggest aiming for the start of the arrival window.
"""
st.image("spacer.png")

st.subheader("festivities")
"""
Dear friends, on the same day, another wedding will take place in the village. Therefore, please follow the navigation marked with initials A + M. Additionally, the traditional Chříč
Rally will also be happening in the village. Yes, you heard it right. We perceive it as a positive and sincere
start to our married life, one filled with surprises and challenges. In case the traditional automotive
festivities hinder any of the many roads to Chříč, we will keep you informed.
"""
st.image("spacer.png")

st.subheader("and now. the grand evening approaches!")
"""
The party will commence with a toast at approximately 3:30 PM, launching a radiant ball on the castle
terrace. To harmonise with the atmosphere, we urge you to bring something that sparkles. It can be
jewellery, a piece of clothing, flat shoes, or anything else. Glitter has no limits. We kindly ask all guests to avoid clumsy footwear that could lead to unwanted dance mishaps. Instead, we recommend stylish and comfortable shoes so you can enjoy the festivities carefree.
"""
st.image("spacer.png")

st.subheader("gifts")
"""
Due to our scattered possessions across various European lands and beyond, we do not wish for traditional
material gifts. However, if you would be so kind and wish to support us, we would gratefully accept a
financial contribution towards our journey into the world, which will take place in the winter months. Your
assistance will help us explore exotic destinations and build shared memories that will fuel our peaceful
marriage during times of conflict and challenge.
"""
st.image("spacer.png")

st.subheader("accomodation options:")
"""
Camping: Space will be allocated for setting up tents on-site.

Local school: If you prefer the comfort of the school, please bring a sleeping mat and a sleeping bag.

Riverside camps: Just 8 minutes away by car, there are two camps with cabins that have beds and bedding. Each cabin accommodates 4 people. We have approximately 50 spots reserved, so please let us know, and
we will secure a spot for you.

Hotel: For those who prefer the comfort of a hotel, we will gladly provide you with recommendations. However, the costs of the hotel will unfortunately be on your own
Transportation to the hotel and campsites will be arranged. Dearest friends, your presence is the most precious gift to us on this legendary day. With warmth, love, and excitement,
"""
st.image("signature.png")




col1, col2, col3 = st.columns(3)
with col1:
    st.image("footer.png")
with col2:
    st.button("balonky", on_click=st.balloons)
with col3:
    st.button("snih", on_click=st.snow)