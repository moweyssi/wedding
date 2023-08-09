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
    "Choose your language",
    ('CZ','ENG'), horizontal=True,label_visibility="hidden")
st.image("info.png")

with st.expander(":rewd[RSVP Form]"):
    st.markdown(
        """
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeNEAVH0J3Fob8uPX2qJz3puVX5HhE_LTs2CqG5mkcmMSsrOg/viewform?embedded=true", width=100%, height=2200></iframe>
        """,
        unsafe_allow_html=True

    )

st.image("footer.png")
if language == "ENG":
    st.subheader("Dearest Friends,")
    """
    Please allow us to share further details of our highly-anticipated wedding.
    We hope the following points will give you an idea of the festivities on that glorious day: The date to put down in your calendar is **Saturday, September 2, 2023**. Please join us at the beautiful Chříč chateau. The address is **Chříč 1**. The ceremony will commence at **2:00 PM** but we ask you to arrive between 12:30 PM and 1:30 PM. Light refreshments will be provided upon your arrival. For those camping enthusiasts, we suggest aiming for the
    start of the arrival window, so you can enjoy the rest of the party without logistical distractions.

    We humbly ask you for a singular favor: bestow upon us but a scant ten seconds of your precious time on the **RVSP form above**. In doing so, you will greatly aid us with preparations for this grand event, ensuring its resplendent success for all who partake.
    """
    st.image("spacer.png")

    st.subheader("Festivities")
    """
    Dear friends, on the same day, another wedding will also take place in the village. Therefore, please follow the **navigation marked with our initials A + M**. Additionally, the traditional Chříč Rally will also be happening in the village. Yes, this is not a joke. We perceive it as a positive and sincere beginning to our married life, one filled with surprises and challenges. In case the traditional automotive festivities hinder any of the many roads to Chříč, we will keep you informed.
    """
    st.image("spacer.png")

    st.subheader("Party")
    """
    The party will commence with a toast at 3:30 PM. This will also get the ball on the castle terrace rolling. To harmonise with the atmosphere, we invite you to **bring something sparkly**. It can be jewellery, a piece of clothing, shoes, or anything else. **Glitter has no limits.**
    We kindly ask all guests to **avoid clumsy footwear** that could lead to unwanted dance mishaps and incidents in the natural landscape. Instead, we recommend stylish and comfortable shoes so you can enjoy the festivities carefree.
    """
    st.image("spacer.png")

    st.subheader("Gifts")
    """

    Due to our scattered possessions across various European lands and beyond, we do not wish for traditional material gifts. However, if you wish to support our newly formed unity, we would gratefully accept a financial contribution towards our journey into the world, which will take place in the winter months. Your assistance will help us explore exotic destinations and build shared memories that will fuel our peaceful marriage during times of conflict and challenge.
    """
    col1, col2, col3 = st.columns(3)
    col1.code(
        "UK bank account\nName: Maxim Oweyssi\nAccount number: 04817931\nSort code: 04-00-75")
    col2.image("Revolut.jpg", width=220)
    col3.code(
        "EU bank account\nName: Maxim Oweyssi\nIBAN: GB71 REVO 0099 7031 6159 48\nBIC: REVOGB21")
    st.image("spacer.png")

    st.subheader("Overnight:")
    """
    The first option is to camp. Space will be allocated for setting up tents on-site. If you prefer the comfort of a roof over your head, you can sleep in a local school, please bring a sleeping mat and a sleeping bag for this option. You will share space with other people. Just 8 minutes away by car, are two camps with cabins. There are beds and bedding. Each cabin accommodates 4 people. We have approximately 50 spots reserved, so please let us know, and we will secure a spot for you. For those who prefer the comfort of a hotel, we will
    gladly provide you with recommendations. However, this will have to be at your own expense.

    Dearest friends, your presence is the most precious gift to us on this legendary day.

    With warmth, love, and excitement,
    """
    st.image("signature.png")
    col1,col2,col3,col5,col5,col6,col7 = st.columns(7)
    with col1:
        st.button("balloon", on_click=st.balloons)
    with col7:
        st.button("snow", on_click=st.snow)
else:
    st.subheader("Nejmilejší rodino a přátelé,")
    """
    Dovolte nám, abychom vás s radostí pozvali na naší avizovanou zámeckou svatbu. Doufáme, že vám následující body poskytnou představu o dění onoho slavnostního dne. Svatba se uskuteční v sobotu **2. září 2023** na krásném Chříčském zámku, který najdete na adrese **Chříč 1**. Začátek obřadu je ve **14.00**. Prosím přijeďte mezi 12.30 a 13.30. Pro stanaře doporučujeme mířit na začátek příjezdového okna.
    
    S úctou vás prosíme o jednu laskavost: obdařte nás deseti vteřinami Vašeho cenného času a vyplňte prosím náš **RVSP formulář výše**. Tím nám umožníte pokračovat se složitými přípravami onoho velkolepého dne.
    """
    st.image("spacer.png")

    st.subheader("Srandy kopec")
    """
    Drazí přátelé, ve stejný den se ve vesnici koná i další svatba. Proto prosím sledujte **navigační cedule** s iniciály A + M. Kromě druhé svatby se ve vesnici bude také konat tradiční chříčské rally. Ano, je to tak. Vnímáme to jako pozitivní a upřímný začátek manželského soužití, které bude jistě plné překvapení a výzev. V případě, že by tradiční automobilové slavnosti měly blokovat jednu z mnoha cest do Chříče, dáme vědět.    """
    st.image("spacer.png")

    st.subheader("Bál na zámecké terase")
    """
    Párty začíná přípitkem v 15.30. Poté vás zveme na bál na zámecké terase. Abyste se dokonale sladili s atmosférou, vyzýváme vás, abyste si přinesli **něco, co se třpytí**. Může to být šperk, kus oděvu, střevíce bez podpatku či něco jiného. Kreativitě se meze nekladou. Také prosíme všechny hosty, aby se vyhnuli **neohrabaným botám**, které by mohly způsobit nechtěné taneční eskapády. Místo toho doporučujeme stylovou a pohodlnou obuv, abyste se mohli bezstarostně bavit v exotickém chříském terénu.
    """
    st.image("spacer.png")

    st.subheader("Dary")
    """
    Vzhledem k našim majetkovým dispozicím rozmístěným po různých evropských zemích (i za jejich hranicemi), si nepřejeme předměty. Avšak, pokud byste měli tu laskavost a chtěli nás podpořit, přijmeme s pokorou a vděkem finanční příspěvek na naší cestu do světa, která se uskuteční v zimních měsících. Tím nám pomůžete objevovat cizí kraje a budovat společné vzpomínky, které nám v období konfliktu a jiných těžkých chvil dodají energii na pohodové manželství. V případě, že byste se chtěli podílet na přípravách měsíce/týdny/dny předtím, prosím ozvěte se. Pomoc bude potřeba s dekoracemi, jídlem a dalšími položkami.    """
    
    col1, col2, col3 = st.columns(3)
    col2.image("QR_code.jpg", width=220)

    st.image("spacer.png")

    st.subheader("Nocleh:")
    """
    Na místě bude pro Vás a vaše blízké vyhrazeno místo pro postavení stanů. Pokud upřednostňujete střechu nad hlavou, je tu možnost spaní v hromadné místnosti místní školy Pivoňka. V tom případě vám stačí spacák a karimatka. Vzdálené pouhých 8 minut jízdy se nachází dva kempy s chatičkami. Jsou vybaveny postelemi a povlečením. Každá chatička je určena pro 4 osoby. Máme zamluveno cca 50 míst. V případě zájmu nám dejte vědět a zamluvíme vám místo. Pro ty, kteří preferují komfort hotelu, rádi poskytneme tipy, kde se ubytovat. Avšak náklady na hotel budou bohužel na vás.
    Drazí svatebčané, vaše přítomnost je pro nás tím nejcennějším darem tohoto legendárního dne.

    Těšíme se!

    S úctou, láskou a nadšením,
    """

    st.image("signature.png")

    col1,col2,col3,col5,col5,col6,col7 = st.columns(7)
    with col1:
        st.button("balónky", on_click=st.balloons)
    with col7:
        st.button("sníh", on_click=st.snow)



