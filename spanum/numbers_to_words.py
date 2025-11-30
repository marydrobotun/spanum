UNIDADES = [
    "cero", "uno", "dos", "tres", "cuatro", "cinco",
    "seis", "siete", "ocho", "nueve"
]

EXCEPCIONES = {
    10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
    16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
    20: "veinte", 21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro",
    25: "veinticinco", 26: "veintiséis", 27: "veintisiete", 28: "veintiocho", 29: "veintinueve"
}

DECENAS = ["", "", "veinte", "treinta", "cuarenta", "cincuenta",
           "sesenta", "setenta", "ochenta", "noventa"]

CENTENAS = ["", "ciento", "doscientos", "trescientos", "cuatrocientos",
            "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def number_to_words(n:  int) -> str:
    """
    Converts a number to its Spanish word representation.

    :param n: Oany number you want to convert.
    :type n int
    :raise ValueError: If the n is too big.
    :return: The spanish word for provided number.
    :rtype: str
    """
    if n < 0 or n >= 1_000_000_000:
        raise ValueError("Número fuera del rango soportado (0 <= n < 1,000,000,000)")

    if n in EXCEPCIONES:
        return EXCEPCIONES[n]
    if n < 10:
        return UNIDADES[n]
    if n < 100:
        dec, uni = divmod(n, 10)
        if n in EXCEPCIONES:
            return EXCEPCIONES[n]
        return f"{DECENAS[dec]} y {UNIDADES[uni]}" if uni else DECENAS[dec]
    if n < 1000:
        if n == 100:
            return "cien"
        cent, resto = divmod(n, 100)
        return f"{CENTENAS[cent]} {number_to_words(resto)}".strip() if resto else CENTENAS[cent]
    if n < 1_000_000:
        mil, resto = divmod(n, 1000)
        mil_str = "mil" if mil == 1 else f"{number_to_words(mil)} mil"
        return f"{mil_str} {number_to_words(resto)}".strip() if resto else mil_str
    if n < 1_000_000_000:
        millon, resto = divmod(n, 1_000_000)
        millon_str = "un millón" if millon == 1 else f"{number_to_words(millon)} millones"
        return f"{millon_str} {number_to_words(resto)}".strip() if resto else millon_str
