import streamlit as st
from PIL import Image
img=Image.open("logo.png")
st.set_page_config(page_title="Anna & Max", page_icon=img)
hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
language = st.radio(
    ('ENG','CZ'), horizontal=True)
st.image("info.png")

st.subheader("Dearest Friends,")
if language == "ENG":
    """
    Please allow us to share further details of our highly-anticipated wedding.
    We hope the following points will give you an idea of the festivities on that glorious day: The date to put down in your calendar is Saturday, September 2, 2023. Please join us at the beautiful Chříč chateau. The address is Chříč 1. The ceremony will commence at 2:00 PM but we ask you to arrive between 12:30 PM and 1:30 PM. Light refreshments will be provided upon your arrival. For those camping enthusiasts, we suggest aiming for the
    start of the arrival window, so you can enjoy the rest of the party without logistical distractions.
    """
else:
    """
    blablablacestina
    """
st.image("spacer.png")

st.subheader("Festivities")
"""
Dear friends, on the same day, another wedding will also take place in the village. Therefore, please follow the navigation marked with our initials A + M. Additionally, the traditional Chříč Rally will also be happening in the village. Yes, this is not a joke. We perceive it as a positive and sincere beginning to our married life, one filled with surprises and challenges. In case the traditional automotive festivities hinder any of the many roads to Chříč, we will keep you informed.
"""
st.image("spacer.png")

st.subheader("Party")
"""
The party will commence with a toast at 3:30 PM. This will also get the ball on the castle terrace rolling. To harmonise with the atmosphere, we invite you to bring something sparkly. It can be jewellery, a piece of clothing, shoes, or anything else. Glitter has no limits.
We kindly ask all guests to avoid clumsy footwear that could lead to unwanted dance mishaps and incidents in the natural landscape. Instead, we recommend stylish and comfortable shoes so you can enjoy the festivities carefree.
"""
st.image("spacer.png")

st.subheader("Gifts")
"""

Due to our scattered possessions across various European lands and beyond, we do not wish for traditional material gifts. However, if you wish to support our newly formed unity, we would gratefully accept a financial contribution towards our journey into the world, which will take place in the winter months. Your assistance will help us explore exotic destinations and build shared memories that will fuel our peaceful marriage during times of conflict and challenge.
"""
st.image("spacer.png")

st.subheader("Overnight:")
"""
The first option is to camp. Space will be allocated for setting up tents on-site. If you prefer the comfort of a roof over your head, you can sleep in a local school, please bring a sleeping mat and a sleeping bag for this option. You will share space with other people. Just 8 minutes away by car, are two camps with cabins. There are beds and bedding. Each cabin accommodates 4 people. We have approximately 50 spots reserved, so please let us know, and we will secure a spot for you. For those who prefer the comfort of a hotel, we will
gladly provide you with recommendations. However, this will have to be at your own expense.

Dearest friends, your presence is the most precious gift to us on this legendary day.

With warmth, love, and excitement,
"""
st.image("signature.png")

with st.expander(":rewd[RSVP Form]"):
    st.markdown(
        """
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeNEAVH0J3Fob8uPX2qJz3puVX5HhE_LTs2CqG5mkcmMSsrOg/viewform?embedded=true", width=100%, height=3200></iframe>
        """,
        unsafe_allow_html=True

    )

st.image("footer.png")

st.button("balonky", on_click=st.balloons)
st.button("snih", on_click=st.snow)



