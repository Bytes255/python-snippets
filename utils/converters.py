"""
Some basic functions to explain how modules work
"""
__lbs_kg_factor = 2.205
__oz_g_factor = 28.35
__ft_m_factor = 3.28084
__in_cm_factor = 2.54


def kg_to_lbs(value : float) -> float: 
    return round(value * __lbs_kg_factor, 2)


def lbs_to_kg(value : float) -> float: 
    return round(value / __lbs_kg_factor, 2) 


def g_to_oz(value : float) -> float: 
    return round(value / __oz_g_factor, 2)
    
    
def oz_to_g(value : float) -> float: 
    return round(value * __oz_g_factor, 2)
        

def m_to_ft(value : float) -> float:
    return round(value * __ft_m_factor, 2)


def ft_to_m(value : float) -> float:
    return round(value / __ft_m_factor, 2)


def cm_to_in(value : float) -> float:
    return round(value / __in_cm_factor, 2)


def in_to_cm(value : float) -> float:
    return round(value * __in_cm_factor, 2 )


# Gets a string and turns every emoticon into emojis
def emoji_converter(message : str) -> str:
    emoji_dict ={
    ":)": chr(128578),
    ":(": chr(128577),
    ">:(": chr(128544),
    ":D": chr(128515)
    }
    
    words = message.split(chr(32))
    ending_message = ""
    for word in words:
        ending_message += emoji_dict.get(word, word) + " "
    return ending_message.strip()