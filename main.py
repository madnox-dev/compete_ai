import streamlit as st

def header():
    st.title("Amazon Competitor Analysis")
    st.caption("Enter your ASIN to get product analysis")

def input():
    asin = st.text_input("ASIN",placeholder="B0CXSE23DW")

    geo = st.text_input("Zip/Postal Code",placeholder="600069")
    domain = st.text_input("Domain" )
    return asin.strip(), geo.strip(), domain.strip()

def main():
    st.set_page_config(page_title="Amazon Comp Analysis",page_icon = "💻")
    header()
    asin, geo, domain = input()

    if st.button("Scrape Product") and asin:
        with st.spinner("Scraping product..."):
            st.write("Scrape")
        st.success("Product scraped successfully ")    

if __name__ == "__main__":
    main()