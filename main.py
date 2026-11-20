from pyscript import document

non_metals = {
    "Hydrogen": ['H', 'Hydrogen', '1', '1.008'],
    "Helium": ['He', 'Helium', '2', '4.0026'],
    "Nitrogen": ['N', 'Nitrogen', '7', '14.007'],
    "Carbon": ['C', 'Carbon', '6', '12.011'],
    "Oxygen": ['O', 'Oxygen', '8', '15.999'],
    "Fluorine": ['F', 'Fluorine', '9', '18.998'],
    "Neon": ['Ne', 'Neon', '10', '20.180'],
    "Phosphorus": ['P', 'Phosphorus', '15', '30.974'],
    "Sulfur": ['S', 'Sulfur', '16', '32.06'],
    "Chlorine": ['Cl', 'Chlorine', '17', '35.45'],
    "Argon": ['Ar', 'Argon', '18', '39.95'],
    "Selenium": ['Se', 'Selenium', '34', '78.971'],
    "Bromine": ['Br', 'Bromine', '35', '79.904'],
    "Krypton": ['Kr', 'Krypton', '36', '83.798'],
    "Iodine": ['I', 'Iodine', '53', '126.90'],
    "Xenon": ['Xe', 'Xenon', '54', '131.29'],
    "Radon": ['Rn', 'Radon', '86', '[222]']
}

def adding_numbers(e):
    document.getElementById('result').innerHTML = ""
    element1 = document.getElementById('elements').value.strip().title()

    # Using .get() - no if statement
    info = non_metals.get(
        element1,
        ("-", "Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b> Symbol: </b> {info[0]} <br>
    <b> Element: </b> {info[1]} <br>
    <b> Atomic Number: </b> {info[2]} <br>
    <b> Atomic Mass: </b> {info[3]} <br>
    """