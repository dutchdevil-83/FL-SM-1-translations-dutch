define narrator = Character(None,           what_style = "narrator_dialogue"                                )
define mc = Character("[mcname]",         color = "#ffffff",                                              )
define mo = Character("You",              color = "#ffffff",                                              )
define mct = Character("[mcname]",         color = "#ffffff",  what_prefix="({i}", what_suffix="{/i})"     )
define mcd = Character("[mcname]",         color = "#000000",  who_style = "dark_character"                )
define hr = Character("Hana",             color = "#bc1ced",                                              )
define arj = Character("Amber-Rose",       color = "#f015a0",                                              )
define mes = Character("Min",              color = "#de25ca",                                              )
define sy = Character("Stacy",            color = "#81c18c",                                              )
define my = Character("Melony",           color = "#0d5c1a",  who_style = "dark_character"                )
define ag = Character("Anna",             color = "#ffedb2",                                              )
define am = Character("April",            color = "#79c18d",                                              )
define cw = Character("Claire",           color = "#dd3376",                                              )
define ns = Character("Nari",             color = "#24e6db",                                              )
define en = Character("Eugene",           color = "#523528",                                              )
define ml = Character("Mrs. Maureen",     color = "#c74317",                                              )
define kv = Character("Kanya",            color = "#1fa281",                                              )
define zh = Character("Zuzana",           color = "#cf9b98",                                              )
define atp = Character("Angela",           color = "#f6cd89",                                              )
define mj = Character("Megan",            color = "#58918a",  who_style = "dark_character"                )
define ed = Character("Elizabeth",        color = "#bfcaa7",                                              )
define tl = Character("Taisia",           color = "#8b4236",                                              )
define ic = Character("Inga",             color = "#682c35",  who_style = "dark_character"                )
define mh = Character("Lyssa",            color = "#945cff",                                              )
define dc = Character("Debbie",           color = "#34a8eb",                                              )
define dvh = Character("Denise",           color = "#381a10",  who_style = "dark_character"                )
define vs = Character("Veronica",         color = "#2a503d",  who_style = "dark_character"                )
define km = Character("Kellie",           color = "#c36c39",                                              )
define sb = Character("Bruce",            color = "#777670",                                              )
define cs = Character("Cecilia",          color = "#342c75",  who_style = "dark_character"                )
define ec = Character("Eileen",           color = "#e7c177",                                              )
define sj = Character("Sue",              color = "#5a4933",  who_style = "dark_character"                )
define jh = Character("Jayden",           color = "#ffffff",                                              )
define lm = Character("Libby",            color = "#ffffff",                                              )
define pm = Character("Peter",            color = "#ffffff",                                              )
define sr = Character("Sienna",           color = "#ffffff",                                              )
define kw = Character("Kai",              color = "#ffffff",                                              )
define ak = Character("Amanda",           color = "#ffffff",                                              )
define bg = Character("Amore",            color = "#dd0019",                                              )
define mcon = Character("Mitch Conner",     color = "#b81c0c",                                              )
define ps = Character("Pepper Storm",     color = "#67447b",                                              )
define fw = Character("Mrs. Watts",       color = "#20447b",  who_style = "dark_character"                )
define chw = Character("Mr. Watts",        color = "#11447b",  who_style = "dark_character"                )
define nj = Character("Jogger",           color = "#dc9d84",                                              )
define dw = Character("Dog Walker",       color = "#dc9d84",                                              )
define cg = Character("Creepy Guy",       color = "#000000",  who_style = "dark_character"                )
define ka = Character("Kennedy",          color = "#000000",  who_style = "dark_character"                )
define ols = Character("Olivia",           color = "#000000",  who_style = "dark_character"                )
define lg = Character("Lauren",           color = "#000000",  who_style = "dark_character"                )
define rd = Character("Ridley",           color = "#dc9d84",                                              )
define jg = Character("Juggsy",           color = "#480f36",                                              )
define be = Character("Bently",           color = "#015002",                                              )
define nr = Character("Nelson Rohr",      color = "#c74317"                                               )
define ms = Character("Maya",             color = "#c74317"                                               )
style dark_character:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [(2, "#e1e1e1", 1, 1)]
style narrator_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox_narrator.png", xalign=0.5, yalign=1.0)
style narrator_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    color "#d1d1d1"
    outlines [(2, "#000000", 1, 1)]