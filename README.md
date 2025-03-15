# Testovací program pro hashování hesel

## publikovan v:
https://hashovaniheslatest.streamlit.app/

## Popis projektu
Tento projekt demonstruje bezpečné ukládání a ověřování hesel pomocí **SHA-256** hashování a saltingu. Program je implementován ve **Streamlit** a využívá **SQLite** databázi pro správu uživatelů.

## Funkce aplikace
- **Registrace uživatele**: Umožňuje uživateli vytvořit účet s unikátním uživatelským jménem a heslem.
- **Hashování hesla**: Heslo je zašifrováno pomocí **SHA-256** a uloženo spolu se salt (náhodným řetězcem) pro zvýšení bezpečnosti.
- **Přihlašování uživatele**: Ověřuje heslo porovnáním zadaného hesla s uloženým hashem v databázi.
- **Bezpečné ukládání hesel**: Použití saltu zabraňuje útokům pomocí rainbow tables.
- **Streamlit webové rozhraní**: Jednoduché grafické rozhraní umožňuje snadnou interakci.

## Jak funguje hashování hesla?
1. **Uživatel zadá heslo**.
2. **Program vygeneruje salt** – náhodný řetězec znaků přidaný k heslu, který zvyšuje bezpečnost.
3. **Spojení hesla a saltu** – Heslo je kombinováno se saltem.
4. **SHA-256 hashování** – Výsledný řetězec je zašifrován do jednosměrného hashe.
5. **Uložení do databáze** – Hashované heslo a salt jsou uloženy.
6. **Ověření při přihlášení** – Nový hash zadaného hesla se porovná s uloženým hashem v databázi.

## Technologie
- **Python 3**
- **Streamlit** – Pro webové rozhraní
- **SQLite** – Databáze pro ukládání uživatelů
- **Hashlib** – Knihovna pro hashování

## Instalace
1. Klonujte tento repozitář:
   ```sh
   git clone https://github.com/tvuj-repozitar.git
   cd tvuj-repozitar
   ```
2. Nainstalujte požadované knihovny:
   ```sh
   pip install -r requirements.txt
   ```
3. Spusťte aplikaci:
   ```sh
   streamlit run main.py
   ```

## Použití
1. **Spusťte aplikaci** příkazem `streamlit run main.py`.
2. **Vyberte stránku** v levém menu:
   - **Registrace**: Přidejte nového uživatele.
   - **Přihlášení**: Přihlaste se se stávajícími údaji.
   - **O programu**: Přečtěte si více o fungování aplikace.

## Doporučení pro vylepšení
- Použití **bcrypt** nebo **Argon2** místo SHA-256 pro bezpečnější hashování hesel.
- Přidání **dvoufaktorového ověřování** (2FA).
- Nasazení aplikace na **Heroku** nebo **Streamlit Cloud**.

## Autor
MartyG – 2024


