import pickle
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="IPL Win Predictor",
    page_icon="cricket_bat_and_ball",
    layout="wide",
)

teams = [
    "Sunrisers Hyderabad",
    "Mumbai Indians",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Kings XI Punjab",
    "Chennai Super Kings",
    "Rajasthan Royals",
    "Delhi Capitals",
]

cities = [
    "Hyderabad",
    "Bangalore",
    "Mumbai",
    "Indore",
    "Kolkata",
    "Delhi",
    "Chandigarh",
    "Jaipur",
    "Chennai",
    "Cape Town",
    "Port Elizabeth",
    "Durban",
    "Centurion",
    "East London",
    "Johannesburg",
    "Kimberley",
    "Bloemfontein",
    "Ahmedabad",
    "Cuttack",
    "Nagpur",
    "Dharamsala",
    "Visakhapatnam",
    "Pune",
    "Raipur",
    "Ranchi",
    "Abu Dhabi",
    "Sharjah",
    "Mohali",
    "Bengaluru",
]

model_path = Path(__file__).with_name("pipe.pkl")
pipe = pickle.load(open(model_path, "rb"))

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255, 196, 87, 0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(255, 107, 107, 0.16), transparent 25%),
            linear-gradient(135deg, #0b1728 0%, #102542 45%, #16355c 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1180px;
    }

    .hero-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.06));
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 24px;
        padding: 28px 32px;
        box-shadow: 0 24px 60px rgba(0,0,0,0.22);
        backdrop-filter: blur(8px);
        margin-bottom: 1.25rem;
    }

    .hero-kicker {
        color: #ffd166;
        font-size: 0.92rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    .hero-title {
        color: #f8fbff;
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.05;
        margin-bottom: 0.6rem;
    }

    .section-label {
        color: #ffd166;
        font-size: 0.88rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin: 0.35rem 0 0.75rem 0;
    }

    .panel {
        background: rgba(0, 0, 0, 0.82);
        background: rgba(0, 0, 0, 0.82);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 22px;
        padding: 1.1rem 1.1rem 1.2rem 1.1rem;
        box-shadow: 0 16px 45px rgba(0,0,0,0.18);
        margin-bottom: 1rem;
    }

    .metric-card {
        background: linear-gradient(180deg, rgba(0,0,0,0.92), rgba(20,20,20,0.88));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 18px 20px;
        text-align: center;
        color: white;
        min-height: 128px;
    }

    .metric-card.win-card {
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.96), rgba(16, 185, 129, 0.88));
        border: 1px solid rgba(110, 231, 183, 0.45);
        box-shadow: 0 16px 35px rgba(16, 185, 129, 0.22);
    }

    .metric-card.loss-card {
        background: linear-gradient(135deg, rgba(127, 29, 29, 0.96), rgba(239, 68, 68, 0.88));
        border: 1px solid rgba(252, 165, 165, 0.38);
        box-shadow: 0 16px 35px rgba(239, 68, 68, 0.18);
    }

    .metric-card.rate-card {
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.96), rgba(245, 158, 11, 0.88));
        border: 1px solid rgba(253, 230, 138, 0.35);
        box-shadow: 0 16px 35px rgba(245, 158, 11, 0.18);
    }

    .metric-label {
        color: #c7daee;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.5rem;
    }

    .metric-value {
        font-size: 2.15rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.35rem;
    }

    .metric-caption {
        color: #d9e7f6;
        font-size: 0.92rem;
    }

    .summary-strip {
        background: linear-gradient(90deg, rgba(255,209,102,0.16), rgba(6,214,160,0.16));
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 14px 18px;
        color: #f7fbff;
        margin-top: 0.7rem;
    }

    div[data-testid="stNumberInput"] input,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.96);
        border-radius: 12px;
        color: #111111 !important;
    }

    div[data-testid="stNumberInput"] input {
        -webkit-text-fill-color: #111111 !important;
        font-weight: 700;
    }

    div[data-testid="stSelectbox"] * {
        color: #111111 !important;
    }

    .stButton > button {
        width: 100%;
        border: 0;
        border-radius: 14px;
        padding: 0.8rem 1rem;
        font-weight: 700;
        color: #0b1728;
        background: linear-gradient(90deg, #ffd166 0%, #ff9f1c 100%);
        box-shadow: 0 12px 30px rgba(255, 159, 28, 0.32);
    }

    .stButton > button:hover {
        color: #0b1728;
        transform: translateY(-1px);
    }

    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label {
        color: #ffffff !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-kicker">Match Intelligence</div>
        <div class="hero-title">IPL Win Predictor</div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Match Setup</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox("Batting team", sorted(teams))
    with col2:
        bowling_team = st.selectbox("Bowling team", sorted(teams))

    selected_city = st.selectbox("Host city", sorted(cities))
    target = st.number_input("Target", min_value=1, step=1, value=180)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Live Match State</div>', unsafe_allow_html=True)

    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input("Current score", min_value=0, step=1, value=90)
    with col4:
        overs = st.number_input("Overs completed", min_value=0.1, max_value=20.0, step=0.1, value=10.0)
    with col5:
        wickets_out = st.number_input("Wickets out", min_value=0, max_value=10, step=1, value=3)

    predict = st.button("Predict Winning Probability")
    st.markdown("</div>", unsafe_allow_html=True)


if predict:
    if batting_team == bowling_team:
        st.error("Batting team and bowling team should be different.")
    elif overs <= 0:
        st.error("Overs completed must be greater than 0.")
    elif overs > 20:
        st.error("Overs completed cannot be greater than 20.")
    else:
        balls_left = int(120 - round(overs * 6))
        wickets_left = int(10 - wickets_out)
        runs_left = int(target - score)

        if balls_left <= 0:
            balls_left = 1

        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        input_df = pd.DataFrame(
            {
                "batting_team": [batting_team],
                "bowling_team": [bowling_team],
                "city": [selected_city],
                "runs_left": [runs_left],
                "balls_left": [balls_left],
                "wicket": [wickets_left],
                "total_runs_x": [target],
                "crr": [crr],
                "rrr": [rrr],
            }
        )

        result = pipe.predict_proba(input_df)
        loss = float(result[0][0])
        win = float(result[0][1])

        st.markdown('<div class="section-label">Prediction Result</div>', unsafe_allow_html=True)
        res1, res2, res3 = st.columns(3)

        with res1:
            st.markdown(
                f"""
                <div class="metric-card win-card">
                    <div class="metric-label">{batting_team}</div>
                    <div class="metric-value">{round(win * 100)}%</div>
                    <div class="metric-caption">Win probability</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with res2:
            st.markdown(
                f"""
                <div class="metric-card loss-card">
                    <div class="metric-label">{bowling_team}</div>
                    <div class="metric-value">{round(loss * 100)}%</div>
                    <div class="metric-caption">Defending chance</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with res3:
            st.markdown(
                f"""
                <div class="metric-card rate-card">
                    <div class="metric-label">Pressure Index</div>
                    <div class="metric-value">{rrr:.2f}</div>
                    <div class="metric-caption">Required run rate</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="summary-strip">
                <strong>Chase summary:</strong> {batting_team} need {max(runs_left, 0)} runs from
                {balls_left} balls with {max(wickets_left, 0)} wickets in hand.
                Current run rate is {crr:.2f}, and required run rate is {rrr:.2f}.
            </div>
            """,
            unsafe_allow_html=True,
        )





# python -m streamlit run final_ipl_app.py