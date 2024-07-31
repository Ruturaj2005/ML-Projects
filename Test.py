import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def set_page_config():
    st.set_page_config(
        page_title="Investment Recommendation System",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
        body {
        font-family: 'Roboto', sans-serif;
        color: #333;
        background-color: #f0f4f8;
    }
    .stApp {
        max-width: 100%;
        padding: 1rem;
    }
    h1, h2, h3 {
        color: #1e3a8a;
        font-weight: 700;
    }
    .sidebar .sidebar-content {
        background-color: #1e3a8a;
        background-image: linear-gradient(315deg, #1e3a8a 0%, #3b82f6 74%);
    }
    .sidebar h2 {
        color: white;
        text-align: center;
        padding: 20px 0;
        font-size: 1.5em;
    }
    .stRadio > div {
        flex-direction: column;
    }
    .stRadio label {
        width: 100%;
        padding: 12px;
        margin: 8px 0;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 8px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stRadio label:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #1e40af;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    footer {
        color: white;
        text-align: center;
        padding: 20px 0;
        font-size: 0.9em;
        position: absolute;
        bottom: 0;
        width: 100%;
    }
    a {
        color: #3b82f6;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    a:hover {
        color: #1e40af;
        text-decoration: underline;
    }
    .card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .profile-links {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .profile-links a {
        margin: 10px;
        padding: 10px 20px;
        background-color: #3b82f6;
        color: white;
        border-radius: 20px;
        transition: all 0.3s ease;
    }
    .profile-links a:hover {
        background-color: #1e40af;
        text-decoration: none;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        margin: 0 10px;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 160px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -80px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    .mutual-fund-btn {
        background-color: #1e40af;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px;
        cursor: pointer;
    }
    .mutual-fund-btn:hover {
        background-color: #1d4ed8;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .sip-btn {
        background-color: #ff006e;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        cursor: pointer;
    }
    .sip-btn:hover {
        background-color: #d4006c;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .metric-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    .metric-card:hover {
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: translateY(-5px);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 600;
        color: #3a86ff;
    }
    
    .metric-label {
        font-size: 1rem;
        color: #555;
        margin-top: 0.5rem;
    }
    
    .stSlider {
        padding: 1rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
                
    .stProgress > div > div > div > div {
        background-color: #3a86ff;
    }            
    
    .stSlider > div > div > div > div {
        height: 10px;
        border-radius: 5px;
    }

    .stSlider > div > div > div > div {
        background-color: #3a86ff;
    }                        
    
    .stSlider > div > div > div > div > div {
        height: 20px;
        width: 20px;
        border-radius: 50%;
        background-color: #3a86ff;
        border: 2px solid white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 140px;
        background-color: #6c757d;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position the tooltip above the text */
        left: 50%;
        margin-left: -75px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }

    .title-container {
        text-align: center;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #3a86ff, #ff006e);
    }            


    .mutual-fund-btn {
        background-color: #3a86ff;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px;
        cursor: pointer.
    }
    .mutual-fund-btn:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .title1 {
        font-weight: 700;
        font-size: 3rem;
        color: white;
        margin-bottom: 0.5rem;
    }
     .subtitle1 {
        font-weight: 300;
        font-size: 1.2rem;
        color: #f0f0f0;
    }
                            
    .sip-btn {
        background-color: #ff006e;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        cursor: pointer;
    }
    .sip-btn:hover {
        background-color: #cc0059;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)

def future_value(invested_monthly, yrs, annual_roi=12):
    compounded_roi = annual_roi/100/12
    fv = float(invested_monthly) * ((1+compounded_roi)**(yrs*12)-1) * (1+compounded_roi)/compounded_roi 
    fv = round(fv, 0)
    return fv

def total_invested(invested_monthly, yrs):
    total_money = invested_monthly * 12 * yrs
    total_money = round(total_money, 0)
    return total_money

def main():
    set_page_config()
    local_css()
    
    

    with st.sidebar:
        st.image("Final-logo.jpg", width=100)
        st.markdown("<h2>Team Hurricane</h2>", unsafe_allow_html=True)
        
        page = st.radio("Navigation", 
            ["Home", "Suggest Me a Plan", "Mutual Funds", "Stock Market", 
             "Gold Investment", "Real Estate", "Crypto (coming soon)"])
        
        # st.markdown(
        #     "<footer>© 2024 Team Hurricane. All rights reserved.</footer>",
        #     unsafe_allow_html=True
        # )

    if page == "Home":
        home_page()
    elif page == "Suggest Me a Plan":
        suggest_plan_page()
    elif page == "Mutual Funds":
        mutual_funds_page(), sip_calculator()
        


def home_page():
    st.title("Investment Recommendation System")
    
    with st.container():
        st.markdown("""
        <div class="card">
        An investment recommendation system helps create a customized investment plan tailored to individual financial goals and risk
        tolerance. It analyzes personal financial data and market trends to suggest a balanced portfolio. This includes a mix of mutual
        funds, stocks, Systematic Investment Plans (SIPs), gold, Cryptocurrency and real estate. The system provides diversified investment
        options to maximize returns and minimize risks. It continuously monitors and adjusts the portfolio based on market performance
        and user preferences. This personalized approach ensures that investments align with the user's long-term financial objectives.
        Overall, it offers a comprehensive solution for effective wealth management.
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Our LinkedIn Profiles:")
    st.markdown("""
    <div class="profile-links">
        <a href="https://www.linkedin.com/in/prithviraj44//" target="_blank">Prithviraj More</a>
        <a href="https://www.linkedin.com/in/om-deshmukh-928a282a6//" target="_blank">Om Deshmukh</a>
        <a href="https://www.linkedin.com/in/darshannair74//" target="_blank">Darshan Nair</a>
        <a href="https://www.linkedin.com/in/ruturaj-pandharkar-265a6228b/" target="_blank">Ruturaj Pandharkar</a>
        <a href="https://www.linkedin.com/in/akhilesh-mohorir-9150b6292//" target="_blank">Akhilesh Mohorir</a>
    </div>
    """, unsafe_allow_html=True)

def suggest_plan_page():
    st.title("Suggest Me a Plan")
    
    with st.form("investment_form"):
        amount = st.number_input("Enter your monthly income:", min_value=5000, step=5000)
        age = st.number_input("Enter your age:", min_value=1, step=1)
        occupation = st.selectbox("Enter your occupation:", ["Student", "Professional", "Business", "Retired"])
        
        submit_button = st.form_submit_button("Generate Plan")
        
    if submit_button:
        str1 = ""
        invested = 0  # Initialize invested variable
        
        def isfloat(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        if not amount or not age:
            str1 += "Dear User,\nPlease fill all the fields.\n\nYou may press RESET to reset fields."
        elif not isfloat(amount) or not isfloat(age):
            str1 += "Dear User,\nPlease enter appropriate values for amount and age.\n\n\t>> Income    =>    Integer or Float\n\t>> Age         =>    Preferably an Integer"
        elif float(amount) < 0 or int(age) <= 0:
            str1 += "Dear User,\nPlease enter a positive value for amount and age.\n\nYou may press RESET to reset fields."
        else:
            age = int(age)
            amount = float(amount)
            per50 = round(amount * 0.5, 0)
            per40 = round(amount * 0.4, 0)
            per30 = round(amount * 0.3, 0)
            per20 = round(amount * 0.2, 0)
            
            if age < 1 or age > 130:
                str1 += "Dear User,\nPlease enter an appropriate age.\nAge should be between 1 year and 130 years.\n\nYou may press RESET to reset fields."
            else:
                if age < 18:
                    str1 += "Dear user,\nAs your age is below 18 years,\nIt won't be possible for you to invest in Stocks or Mutual Funds.\nBut you may study about stock market to get a basic idea about the same.\n\nYou may read the following books to increase your knowledge.\n\n1. The Intelligent Investor\n2. Rich Dad Poor Dad"
                elif 18 <= age <= 35:
                    str1 += f"Dear user,\nAs you are young, we recommend you the following investment strategies.\n\n>> 50% - For your needs (food, rent, EMI, etc.)\n\t[50 %    =>    ~ {per50}    INR]\n\n>> 30% - For your wants (vacations, gadgets, etc.)\n\t[30 %    =>    ~ {per30}    INR]\n\n>> 20% - Savings and Investments (Stocks, Mutual Funds, FD, etc.)\n\t[20 %    =>    ~ {per20}    INR]\n"
                    invested = round(amount * 0.2, 0)
                else:
                    str1 += f"Dear user,\nAs you are older, we recommend you the following investment strategies.\n\n>> 40% - For your needs (food, rent, EMI, etc.)\n\t[40 %    =>    ~ {per40}    INR]\n\n>> 20% - For your wants (vacations, gadgets, etc.)\n\t[20 %    =>    ~ {per20}    INR]\n\n>> 40% - Savings and Investments (Stocks, Mutual Funds, FD, etc.)\n\t[40 %    =>    ~ {per40}    INR]\n"
                    invested = round(amount * 0.4, 0)

                str1 += f"\n\n>> If you follow this Financial Discipline, \nEstimated Returns (at 12% Compound Interest) :"
                str1 += f"\nInvested/month      =>      {invested} INR"
                str1 += "\n\nPeriod\tInvested (INR)\t\tFuture Value (INR)\n---------------------------------------------------------------"
                for year in [2, 5, 10]:
                    str1 += f"\n{year} yrs\t~ {total_invested(invested, year)}\t\t~ {future_value(invested, year)}"

                if occupation == "Student":
                    str1 += "\n\n\n>> As a student, dedicating your time and energy to learning is one of the most valuable investments you can make. Online courses offer a convenient and flexible way to enhance your skills and knowledge. We highly recommend exploring courses on these platforms:\n1. www.coursera.com\n2. www.udemy.com"

                elif occupation == "Professional":
                    str1 += "\n\n\n>> As a professional, dedicating your time and energy to learning is one of the most valuable investments you can make. Whether through online courses, reading books, or other resources, continuous learning can significantly boost your career prospects. Investing in your education not only increases your chances of promotion but also offers the greatest returns for your professional growth. Embrace the opportunity to enhance your skills and unlock new career opportunities!"

                elif occupation == "Business":
                    str1 += "\n\n\n>> As a business professional, investing your time in reading books that can help grow your business is invaluable. We recommend the following books:\nThink and Grow Rich\nZero to One\nRich Dad Poor Dad\nReading these books will surely increase your chances of growing your business and provide the greatest returns on your investment!"

                elif occupation == "Retired":
                    str1 += "\n\n\n>> As a retiree, you might want to focus on preserving your wealth and generating stable returns. Consider exploring conservative investment options and retirement planning strategies. Books on personal finance for retirees can be particularly helpful."

                str1 += "\n\n\n>> You may also explore these books to guide you on your investment journey:\nGetting Things Done\nThe 7 Habits of Highly Effective People\nThink and Grow Rich"
        st.text_area("Your Personalized Investment Plan:", str1, height=600)

def mutual_funds_page():
    st.markdown("""
    <div style="text-align: center;">
        <h1>Mutual Fund Recommender</h1>
        <hr style="border:1px solid #b0b0b0; width:50%; margin:auto;">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card paragraph-spacing">
    Mutual funds are a type of investment where many people pool their money together to invest in a variety of assets, such as stocks, bonds, and other securities. This collective money is managed by a professional fund manager who invests it in a way that aims to earn the highest possible returns while minimizing risk. By investing in a mutual fund, individuals can benefit from diversification, which means their money is spread across different types of investments, reducing the risk of losing money. Mutual funds offer a convenient and affordable way for people to invest in the stock market and other assets, making it a popular choice for those looking to grow their savings over time.
    </div>
    
    <div class="bullet-points bullet-spacing">
        <ul>
            <li>Equity Mutual Funds: These invest primarily in stocks and aim for high returns, suitable for long-term investors.</li>
            <li>Debt Mutual Funds: These invest in fixed-income securities and are ideal for conservative investors seeking regular income.</li>
            <li>Hybrid Mutual Funds: These funds invest in a mix of equity and debt instruments, offering balanced risk and return.</li>
            <li>Index Funds: These track a particular market index, providing returns similar to the market performance.</li>
            <li>Sectoral/Thematic Funds: These focus on specific sectors or themes, offering higher risk and reward potential.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # st.markdown("""
    # <div style="text-align: center; margin-top: 2rem;">
    #     <div class="tooltip">
    #         <button class="mutual-fund-btn" onclick="window.location.href='https://www.example.com/mutual-funds'">Know Mutual Funds</button>
    #         <span class="tooltiptext">Learn more about different types of mutual funds and top 10 from each category.</span>
    #     </div>
    #     <div class="tooltip">
    #         <button class="mutual-fund-btn" onclick="window.location.href='https://www.example.com/start'">Start Mutual Funds</button>
    #         <span class="tooltiptext">Begin your investment journey.</span>
    #     </div>
    #     <div class="tooltip">
    #         <button class="mutual-fund-btn" onclick="window.location.href='https://docs.google.com/document/d/1TsphK11gov3eY1mHTOnVGQ5tuaGDaR8c/edit?usp=sharing&ouid=111333235595321752961&rtpof=true&sd=true'">Why Mutual Funds</button>
    #         <span class="tooltiptext">Why shoud you invest inmutual funds.</span>
    #     </div>
    # </div>
    # """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <div class="tooltip">
            <a href="https://docs.google.com/document/d/1iq5z_UPg9syUZcXku-EfxSQAWcI-EIdf/edit?usp=sharing&ouid=111333235595321752961&rtpof=true&sd=true" target="_blank">
                <button class="mutual-fund-btn">Know Mutual Funds</button>
            </a>
            <span class="tooltiptext">Learn more about different types of mutual funds and top 10 from each category.</span>
        </div>
        <div class="tooltip">
            <a href="https://www.youtube.com/watch?v=L0yTgTagvL8" target="_blank">
                <button class="mutual-fund-btn">Start Mutual Funds</button>
            </a>
            <span class="tooltiptext">Begin your investment journey.</span>
        </div>
        <div class="tooltip">
            <a href="https://docs.google.com/document/d/1TsphK11gov3eY1mHTOnVGQ5tuaGDaR8c/edit?usp=sharing&ouid=111333235595321752961&rtpof=true&sd=true" target="_blank">
                <button class="mutual-fund-btn">Why Mutual Funds</button>
            </a>
            <span class="tooltiptext">Why should you invest in mutual funds.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def calculate_sip(lumpsum, monthly_sip, rate, years):
    monthly_rate = rate / (12 * 100)
    months = years * 12
    total_investment = lumpsum + (monthly_sip * months)
    future_value = lumpsum * (1 + rate/100)**years
    for i in range(months):
        future_value += monthly_sip * ((1 + monthly_rate)**(months - i))
    return total_investment, future_value - total_investment, future_value

def create_yearly_data(lumpsum, monthly_sip, rate, years):
    return pd.DataFrame([
        {
            'Year': year,
            'Invested Amount': calculate_sip(lumpsum, monthly_sip, rate, year)[0],
            'Total Amount': calculate_sip(lumpsum, monthly_sip, rate, year)[2]
        } for year in range(years + 1)
    ])

def sip_calculator():
    st.markdown("""
    <div class="title-container">
        <p class="title1">SIP Calculator</p>
        <p class="subtitle1">Plan your financial future with precision</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        lumpsum = st.slider('Lumpsum Investment (₹)', 0, 1000000, 100000, step=10000, format="%d")
        monthly_sip = st.slider('Monthly SIP (₹)', 0, 100000, 10000, step=1000, format="%d")
    with col2:
        rate = st.slider('Annual Interest Rate (%)', 1.0, 30.0, 12.0, step=0.1)
        years = st.slider('Investment Period (Years)', 1, 30, 10)

    invested, gains, total = calculate_sip(lumpsum, monthly_sip, rate, years)

    st.markdown("<br>", unsafe_allow_html=True)  # Add some space

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">₹{invested:,.0f}</div>
            <div class="metric-label">Total Invested</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">₹{gains:,.0f}</div>
            <div class="metric-label">Total Gains</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">₹{total:,.0f}</div>
            <div class="metric-label">Total Amount</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add some space

    yearly_data = create_yearly_data(lumpsum, monthly_sip, rate, years)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yearly_data['Year'], y=yearly_data['Invested Amount'], name='Invested', fill='tozeroy', line=dict(color='#3a86ff')))
    fig.add_trace(go.Scatter(x=yearly_data['Year'], y=yearly_data['Total Amount'], name='Total', fill='tonexty', line=dict(color='#ff006e')))

    fig.update_layout(
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        title='Investment Growth Over Time',
        xaxis_title='Year',
        yaxis_title='Amount (₹)',
        legend_title='',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Poppins, sans-serif", size=12),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Poppins, sans-serif")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div style="font-size: 0.8rem; color: #777; text-align: center; margin-top: 2rem;">
        Disclaimer: This calculator provides estimates based on the given inputs. 
        Actual returns may vary depending on market conditions and other factors.
    </div>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()