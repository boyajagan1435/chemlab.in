st.set_page_config(page_title="Virtual Chemistry Lab", page_icon="🧪") 
^^
st.title("🧪 Virtual Chemistry Lab")

tab1, tab2, tab3, tab4 = st.tabs(
    ["⚗️ Mix", "🌈 pH Tester", "🧮 Molarity", "📓 Notebook"]
)

# ---------- Tab 1: Mix chemicals ----------
with tab1:
    reactions = {
        ("HCl", "NaOH"): "NaCl + H2O (neutralization, heat released)",
        ("HCl", "Zn"): "ZnCl2 + H2 (hydrogen gas bubbles)",
        ("AgNO3", "NaCl"): "AgCl + NaNO3 (white precipitate)",
        ("CuSO4", "Zn"): "ZnSO4 + Cu (solution fades, copper forms)",
    }
    chemicals = ["HCl", "NaOH", "Zn", "AgNO3", "NaCl", "CuSO4"]
    a = st.selectbox("Chemical 1", chemicals, key="c1")
    b = st.selectbox("Chemical 2", chemicals, index=1, key="c2")
    if st.button("Mix"):
        result = reactions.get((a, b)) or reactions.get((b, a))
        if result:
            st.success(f"{a} + {b} → {result}")
            st.balloons()
        else:
            st.info("No visible reaction.")

# ---------- Tab 2: pH tester ----------
with tab2:
    ph = st.slider("Solution pH", 0.0, 14.0, 7.0, 0.1)
    if ph < 7:
        kind = "Acidic"
    elif ph > 7:
        kind = "Basic"
    else:
        kind = "Neutral"
    if ph < 3:
        color = "🔴 Red"
    elif ph < 6:
        color = "🟠 Orange"
    elif ph < 8:
        color = "🟢 Green"
    elif ph < 11:
        color = "🔵 Blue"
    else:
        color = "🟣 Purple"
    st.subheader(f"{kind} solution")
    st.write(f"Universal indicator color: {color}")
    st.write(f"[H⁺] = {10 ** -ph:.2e} mol/L")

# ---------- Tab 3: Molarity calculator ----------
with tab3:
    st.write("Molarity = moles ÷ volume (L)")
    mass = st.number_input("Mass of solute (g)", min_value=0.0, value=5.85)
    molar_mass = st.number_input("Molar mass (g/mol)", min_value=0.01, value=58.5)
    volume = st.number_input("Volume of solution (mL)", min_value=0.1, value=100.0)
    moles = mass / molar_mass
    molarity = moles / (volume / 1000)
    st.metric("Moles", f"{moles:.4f} mol")
    st.metric("Molarity", f"{molarity:.4f} M")

# ---------- Tab 4: Lab notebook ----------
with tab4:
    if "notes" not in st.session_state:
        st.session_state.notes = []
    title = st.text_input("Experiment title")
    obs = st.text_area("Observations")
    if st.button("Save entry") and title:
        st.session_state.notes.append((title, obs))
    for t, o in reversed(st.session_state.notes):
        with st.expander(t):
            st.write(o)
    if st.session_state.notes:
        report = "\n\n".join(f"{t}\n{o}" for t, o in st.session_state.notes)
        st.download_button("Download report", report, "lab_report.txt")
