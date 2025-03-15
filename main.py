import hashlib
import random
import sqlite3
import streamlit as st

class UserDatabase:
    """Třída pro správu databáze uživatelů."""
    def __init__(self, db_name='users.db'):
        """Inicializuje připojení k databázi a vytváří tabulku, pokud neexistuje."""
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Vytvoří tabulku uživatelů, pokud neexistuje."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            salt TEXT
        )
        """)
        self.conn.commit()

    def add_user(self, username, password):
        """Přidá uživatele do databáze, pokud neexistuje."""
        self.cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if self.cursor.fetchone():
            st.error("Uživatel s tímto jménem již existuje.")
            return
        
        salt = self._generate_salt()
        hashed_password = self._hash_password(password, salt)
        self.cursor.execute("INSERT INTO users (username, password, salt) VALUES (?, ?, ?)", 
                            (username, hashed_password, salt))
        self.conn.commit()
        st.success("Uživatel úspěšně přidán.")

    def login_user(self, username, password):
        """Ověří přihlašovací údaje uživatele."""
        self.cursor.execute("SELECT password, salt FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        if user:
            stored_password, salt = user
            if stored_password == self._hash_password(password, salt):
                st.success("Přihlášení úspěšné.")
                return True
        st.error("Neplatné přihlašovací údaje.")
        return False
    
    def _hash_password(self, password, salt):
        """Vrací zahashované heslo se solí."""
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    
    def _generate_salt(self, length=20):
        """Generuje náhodný salt určité délky."""
        return ''.join([chr(random.randint(48, 122)) for _ in range(length)])

    def close(self):
        """Uzavře připojení k databázi."""
        self.conn.close()

# Inicializace databáze
db = UserDatabase()

# Stránky
st.sidebar.title("Navigace")
page = st.sidebar.radio("Vyberte stránku:", ["Přihlášení", "Registrace", "O programu"])

if page == "Přihlášení":
    st.title("Přihlášení uživatele")
    
    login_username = st.text_input("Zadejte uživatelské jméno:", key="login_username")
    login_password = st.text_input("Zadejte heslo:", type="password", key="login_password")

    if st.button("Přihlásit se"):
        db.login_user(login_username, login_password)

elif page == "Registrace":
    st.title("Registrace nového uživatele")
    
    new_username = st.text_input("Zadejte nové uživatelské jméno:", key="new_username")
    new_password = st.text_input("Zadejte heslo:", type="password", key="new_password")

    if st.button("Registrovat"):
        db.add_user(new_username, new_password)

elif page == "O programu":
    st.title("O programu")
    st.write("""
    Tento program slouží k testování hashování hesel a správě uživatelských účtů.
    
    **Funkce programu:**
    - Umožňuje **registraci** nových uživatelů.
    - Uloží hesla **bezpečně** pomocí **SHA-256 hashování** a náhodného **saltingu**.
    - Podporuje **přihlašování** uživatelů ověřením jejich údajů oproti databázi.
    - Používá **SQLite** jako databázi pro ukládání uživatelských údajů.
    - Implementováno ve **Streamlit** pro jednoduché webové rozhraní.
    
    **Jak funguje hashování hesla?**
    1. Uživatel zadá heslo.
    2. Vygeneruje se náhodný **salt**.
    3. Heslo je kombinováno se saltem a hashováno pomocí **SHA-256**.
    4. Výsledek se uloží do databáze.
    5. Při přihlášení se nový hash porovná s uloženým hashem.
    
    Program je navržen tak, aby poskytoval základní úroveň bezpečnosti při práci s hesly.
    """)
