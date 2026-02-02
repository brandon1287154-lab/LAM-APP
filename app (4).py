import streamlit as st
import numpy as np
"/mount/src/lam-app/app (4).py"

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
