import streamlit as st
import random

st.set_page_config(page_title="Pokémon Adventure", layout="centered")
st.title("🎮 Pokémon Adventure Game")

# Initialize session state once
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.step = 0
    st.session_state.user_name = ""
    st.session_state.gender = ""
    st.session_state.town = ""
    st.session_state.starter = ""
    st.session_state.rival_name = "Gary"
    st.session_state.rival_starter = "Eevee"
    st.session_state.user_hp = None
    st.session_state.rival_hp = None
    st.session_state.battle_log = []
    st.session_state.turn = 1
    st.session_state.victory = False

# Pokémon descriptions
def pokedex_description(pokemon):
    descriptions = {
        "Bulbasaur": "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.",
        "Charmander": "The flame on its tail shows its emotions. It burns fiercely when the Pokémon is angry.",
        "Squirtle": "Its shell is not just for protection. Its rounded shape reduces water resistance.",
        "Chikorita": "Loves sunlight. It uses the leaf on its head to find warm places.",
        "Cyndaquil": "Flares flames from its back to protect itself.",
        "Totodile": "Despite its small size, it has powerful jaws that can cause serious injury.",
        "Treecko": "Has small hooks on its feet to climb walls and attacks with its tail.",
        "Torchic": "Stores fire inside its body and is covered in fluffy down.",
        "Mudkip": "Breathes through gills and can crush rocks bigger than itself."
    }
    return descriptions.get(pokemon, "")

# Step 0: Create Trainer
if st.session_state.step == 0:
    st.subheader("📝 Create Your Trainer")
    name = st.text_input("Enter your name (max 10 letters):", max_chars=10)
    gender = st.radio("Choose your gender:", ["boy", "girl"])
    if name and st.button("Next ➡️"):
        st.session_state.user_name = name
        st.session_state.gender = gender
        st.session_state.step = 1
        st.rerun()

# Step 1: Choose Town
elif st.session_state.step == 1:
    st.subheader("🏘️ Choose Your Starting Town")
    town = st.selectbox("Choose your hometown:", ["Kanto", "Johto", "Hoenn"])
    if st.button("Continue ➡️"):
        st.session_state.town = town
        st.session_state.step = 2
        st.rerun()

# Step 2: Choose Starter
elif st.session_state.step == 2:
    st.subheader("🔬 Professor Oak's Lab")
    st.write(f"Professor Oak: Welcome {st.session_state.user_name}, from {st.session_state.town}!")
    starters = {
        "Kanto": ("Bulbasaur", "Charmander", "Squirtle"),
        "Johto": ("Chikorita", "Cyndaquil", "Totodile"),
        "Hoenn": ("Treecko", "Torchic", "Mudkip")
    }
    choice = st.radio("Choose your starter Pokémon:", starters[st.session_state.town])
    st.write(f"📖 {pokedex_description(choice)}")
    if st.button("Choose Starter ✅"):
        st.session_state.starter = choice
        st.session_state.step = 3
        st.rerun()

# Step 3: Rival Encounter
elif st.session_state.step == 3:
    st.subheader("⚔️ Rival Encounter")
    st.write(f"{st.session_state.rival_name}: So you're {st.session_state.user_name}, huh? Let's battle!")
    if st.button("Start Battle 🎮"):
        st.session_state.user_hp = random.randint(18, 25)
        st.session_state.rival_hp = random.randint(10, 15)
        st.session_state.battle_log = []
        st.session_state.turn = 1
        st.session_state.victory = False
        st.session_state.step = 4
        st.rerun()

# Step 4: Battle
elif st.session_state.step == 4:
    st.subheader("🔥 Pokémon Battle")
    st.write(f"Turn {st.session_state.turn}")
    st.write(f"Your {st.session_state.starter} HP: {st.session_state.user_hp}")
    st.write(f"{st.session_state.rival_name}'s {st.session_state.rival_starter} HP: {st.session_state.rival_hp}")

    for log in st.session_state.battle_log:
        st.write(log)

    if st.session_state.user_hp > 0 and st.session_state.rival_hp > 0:
        if st.button("Attack 🔥"):
            # Player attack
            player_hit = random.randint(5, 7)
            st.session_state.rival_hp -= player_hit
            st.session_state.battle_log.append(
                f"{st.session_state.starter} hits! {st.session_state.rival_name}'s {st.session_state.rival_starter} takes {player_hit} damage."
            )

            if st.session_state.rival_hp <= 0:
                st.session_state.battle_log.append(f"🎉 You defeated {st.session_state.rival_name}!")
                st.session_state.victory = True
                st.rerun()

            # Rival attacks
            rival_hit = random.randint(2, 4)
            st.session_state.user_hp -= rival_hit
            st.session_state.battle_log.append(
                f"{st.session_state.rival_name}'s {st.session_state.rival_starter} strikes back! {st.session_state.starter} takes {rival_hit} damage."
            )

            if st.session_state.user_hp <= 0:
                st.session_state.battle_log.append("💀 You lost the battle!")
                st.rerun()

            st.session_state.turn += 1
            st.rerun()

    elif st.session_state.user_hp <= 0:
        st.error(f"You lost! Your {st.session_state.starter} fainted.")
        if st.button("Retry Battle 🔁"):
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.victory:
        st.success(f"You defeated {st.session_state.rival_name}!")
        st.write("🎬 What a battle! That was intense!")
        if st.button("Continue to Next Scene ➡️"):
            st.session_state.step = 5
            st.rerun()

# Step 5: Ending Cutscene
elif st.session_state.step == 5:
    st.balloons()
    st.subheader("🎉 Adventure Begins!")
    st.write(f"{st.session_state.rival_name}: I can't believe I lost! This isn't over, {st.session_state.user_name}!")
    st.write("Professor Oak: Excellent work. You're ready to begin your journey.")
    st.success(f"Good luck in {st.session_state.town}, {st.session_state.user_name}! Become a Pokémon Master!")
    if st.button("🔁 Restart Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
