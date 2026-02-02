import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
# ==================================================
# Exponential Speed Model (Algebra 2)
# Clean, Safe, and Deployment-Ready
# ==================================================

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Exponential Speed Model",
    page_icon="🚗",
    layout="centered"
)

# ------------------------------
# Title and Description
# ------------------------------
st.title("Exponential Speed Model")
st.subheader("Interactive Algebra 2: Exponential Growth & Decay")

st.write(
    "This app uses an **exponential equation** to model how speed changes over time. "
    "Students can adjust the initial speed, rate of change, and time to explore "
    "**exponential growth and decay**."
)

# ------------------------------
# Sidebar Controls
# ------------------------------
st.sidebar.header("Model Parameters")

initial_speed = st.sidebar.slider(
    "Initial Speed (mph)",
    min_value=30,
    max_value=120,
    value=90,
    step=5
)

rate_percent = st.sidebar.slider(
    "Rate of Change (% per hour)",
    min_value=-20,
    max_value=20,
    value=8,
    step=1
)

# Convert percent to decimal
rate = rate_percent / 100.0

time_hours = st.sidebar.slider(
    "Time (hours)",
    min_value=0,
    max_value=24,
    value=2,
    step=1
)

# ------------------------------
# Exponential Model Function
# ------------------------------
# S(t) = S₀(1 + r)ᵗ

def speed_model(t, s0, r):
    return s0 * (1 + r) ** t

# ------------------------------
# Data Generation (Error-Safe)
# ------------------------------
if time_hours == 0:
    t = np.array([0])
else:
    t = np.linspace(0, time_hours, 200)

speeds = speed_model(t, initial_speed, rate)
final_speed = speed_model(time_hours, initial_speed, rate)

# ------------------------------
# Numerical Output
# ------------------------------
st.markdown("### Result")
st.write(
    f"After **{time_hours} hours**, the speed is approximately "
    f"**{final_speed:.2f} mph**."
)

# ------------------------------
# Graph
# ------------------------------
fig, ax = plt.subplots()
ax.plot(t, speeds)
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Speed (mph)")
ax.set_title("Speed vs. Time")
ax.grid(True)

st.pyplot(fig)

# ------------------------------
# Interpretation
# ------------------------------
st.markdown("### Interpretation")

if rate > 0:
    st.write("- The speed increases over time (exponential growth).")
elif rate < 0:
    st.write("- The speed decreases over time (exponential decay).")
else:
    st.write("- The speed remains constant.")

# ------------------------------
# Model Limitations
# ------------------------------
st.markdown("### Model Limitations")
st.warning(
    "This model is **theoretical** and not realistic for real driving conditions. "
    "It is intended for learning exponential functions only."
)

# ------------------------------
# In-App Chatbox (Student Helper)
# ------------------------------
# This chatbox lets students ask questions about the model and get instant help.

st.markdown("### 💬 Ask the Model")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Ask me questions about the exponential model, the graph, or what the results mean."
        }
    ]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Simple rule-based responses (safe & offline)
    question = user_input.lower()

    if "equation" in question or "model" in question:
        response = (
            "The equation used is **S(t) = S₀(1 + r)ᵗ**. "
            "S₀ is the initial speed, r is the rate of change (as a decimal), and t is time in hours."
        )
    elif "growth" in question:
        response = "Growth happens when the rate is positive, meaning the speed increases each hour by a percentage."
    elif "decay" in question:
        response = "Decay happens when the rate is negative, meaning the speed decreases each hour by a percentage."
    elif "graph" in question:
        response = "The graph shows how speed changes over time. A curve upward means growth; a curve downward means decay."
    elif "real" in question or "safe" in question:
        response = (
            "This model is not realistic for real driving. It is only for learning how exponential functions work."
        )
    else:
        response = (
            "Good question! Try asking about the equation, growth vs decay, the graph, or what the numbers mean."
        )

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)

