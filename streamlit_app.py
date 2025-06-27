
import streamlit as st

# App-Titel
st.title("🧠 Pausenideen für das Studienseminar")

# Beschreibung
st.markdown("Teile hier deine Ideen für eine aktive, entspannende oder kreative Pausengestaltung am Studienseminar.")

# Formular zur Ideeneingabe
with st.form("ideenformular"):
    titel = st.text_input("💡 Name der Idee")
    ziel = st.text_area("🎯 Ziel oder Zweck")
    ort = st.text_input("📍 Möglicher Ort")
    material = st.text_area("🧰 Benötigtes Material")
    nutzen = st.text_area("💬 Was bringt die Idee den anderen?")
    bereit = st.radio("👤 Wärst du bereit, das selbst umzusetzen?", ["Ja", "Nein", "Vielleicht"])
    abgeschickt = st.form_submit_button("✅ Idee einreichen")

# Speicher (Session State)
if "ideenliste" not in st.session_state:
    st.session_state["ideenliste"] = []

# Idee übernehmen
if abgeschickt and titel:
    neue_idee = {
        "Titel": titel,
        "Ziel": ziel,
        "Ort": ort,
        "Material": material,
        "Nutzen": nutzen,
        "Bereitschaft": bereit
    }
    st.session_state["ideenliste"].append(neue_idee)
    st.success("✅ Deine Idee wurde aufgenommen!")

# Anzeige aller bisherigen Ideen
if st.session_state["ideenliste"]:
    st.subheader("📋 Eingereichte Ideen")
    for i, idee in enumerate(st.session_state["ideenliste"], 1):
        with st.expander(f"Idee {i}: {idee['Titel']}"):
            st.markdown(f"- **Ziel:** {idee['Ziel']}")
            st.markdown(f"- **Ort:** {idee['Ort']}")
            st.markdown(f"- **Material:** {idee['Material']}")
            st.markdown(f"- **Nutzen:** {idee['Nutzen']}")
            st.markdown(f"- **Umsetzungsbereitschaft:** {idee['Bereitschaft']}")
else:
    st.info("Noch keine Ideen eingetragen.")
