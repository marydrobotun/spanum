WORDS_TO_NUM = {
    "cero": 0,
    "uno": 1,
    "un": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciséis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "veintiuno": 21,
    "veintidós": 22,
    "veintitrés": 23,
    "veinticuatro": 24,
    "veinticinco": 25,
    "veintiséis": 26,
    "veintisiete": 27,
    "veintiocho": 28,
    "veintinueve": 29,
    "treinta": 30,
    "cuarenta": 40,
    "cincuenta": 50,
    "sesenta": 60,
    "setenta": 70,
    "ochenta": 80,
    "noventa": 90,
    "cien": 100,
    "ciento": 100,
    "doscientos": 200,
    "trescientos": 300,
    "cuatrocientos": 400,
    "quinientos": 500,
    "seiscientos": 600,
    "setecientos": 700,
    "ochocientos": 800,
    "novecientos": 900,
    "mil": 1000,
    "millón": 1_000_000,
    "millones": 1_000_000,
}


def words_to_number(text: str) -> int:
    """
    Converts a Spanish numeral to an integer.

    :param str text: Any Spanish numeral you want to convert.
    :type text: str
    :raises ValueError: Occurs when an unknown word is found in the text.
    :return: The integer value corresponding to the provided Spanish numeral.
    :rtype: int
    
    """
    text = text.lower().replace(" y ", " ")
    words = text.split()
    total = 0
    current = 0
    for w in words:
        if w not in WORDS_TO_NUM:
            raise ValueError(f"Palabra desconocida: {w}")
        val = WORDS_TO_NUM[w]
        if val == 1_000_000:
            current = current or 1
            total += current * val
            current = 0
        elif val == 1000:
            current = current or 1
            total += current * val
            current = 0
        elif val >= 100:
            current += val
        else:
            current += val
    total += current
    return total
