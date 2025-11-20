import base64
import svgwrite

# =====================================================================
# Configuration globale (thème, padding, police…)
# =====================================================================

THEME       = "dark"
PADDING     = [0,10,0,10]
FONT_SIZE   = 12
FONT_FAMILY = "JetBrains Mono"

# Chemins vers les polices
FONT_PATH_REGULAR = "font/JetBrainsMono/JetBrainsMono-Regular.woff2"
FONT_PATH_BOLD    = "font/JetBrainsMono/JetBrainsMono-Bold.woff2"
FONT_PATH_ITALIC  = "font/JetBrainsMono/JetBrainsMono-Italic.woff2"

# =====================================================================
# Texte (chaque variable texte correspond à un morceau de ligne)
# =====================================================================

txt00  = "                "
txt01  = "Hi! I'm Nathan. Welcome to my GitHub profile."
txt_s  = ""
txt1   = "--------------------- Numerical & Computing Environment ---------------------"
txt20  = "Operating systems";     txt21 = " ..................................... "; txt22 = "MacOS, Linux, Windows"
txt30  = "Programming languages"; txt31 = " .................................. ";    txt32 = "Python, Fortran, C++"
txt40  = "Libraries";             txt41 = " .......................... ";            txt42 = "NumPy, SciPy, Matplotlib, Pandas, LAPACK"
txt50  = "Miscellaneous";         txt51 = " .................................... ";  txt52 = "OpenMP, LaTeX, Conda, HDF5"
txt_s  = ""
txt6   = "---------------------------- Theoretical Physics ----------------------------"
txt70  = "Magnetohydrodynamics";  txt71 = " .... ";                  txt72 = "Plasma physics, Fluid dynamics, Maxwell’s equations"
txt80  = "Thermodynamics";        txt81 = " ..................... "; txt82 = "Statistical physics, Transport phenomena"
txt90  = "Classical mechanics";   txt91 = " .............. ";        txt92 = "Celestial mechanics, Hamiltonian mechanics"
txt_s  = ""
txt10  = "----------------------------- Contact & Profile -----------------------------"
txt110 = "Email";                 txt111 = " ......................................... ";                    txt112 = "nathan.zimniak@protonmail.com"
txt120 = "GitHub";                txt121 = " ........................................................ ";     txt122 = "nathanzimniak"
txt130 = "LeetCode";              txt131 = " ............................................................ "; txt132 = "Nathzed"

# =====================================================================
# Couleurs
# =====================================================================

if THEME == "dark":
    color_prim  = "#FFFFFF"
    color_gray  = "#333333"
    color_grey  = "#474747"
    color_subsection    = "#F08369"
    color_subsubsection = "#5A9CF2"
elif THEME == "light":
    color_prim  = "#0D1117"
    color_gray  = "#474747"
    color_grey  = "#333333"
    color_subsection    = "#F68166"
    color_subsubsection = "#2E73D1"
color_bg            = "none"

# Couleurs associées aux morceaux de texte
color0   = color_prim
color1   = color_prim
color20  = color_subsection; color21 = color_gray; color22 = color_subsubsection
color30  = color_subsection; color31 = color_gray; color32 = color_subsubsection
color40  = color_subsection; color41 = color_gray; color42 = color_subsubsection
color50  = color_subsection; color51 = color_gray; color52 = color_subsubsection
color6   = color_prim
color70  = color_subsection; color71 = color_gray; color72 = color_subsubsection
color80  = color_subsection; color81 = color_gray; color82 = color_subsubsection
color90  = color_subsection; color91 = color_gray; color92 = color_subsubsection
color10  = color_prim
color110 = color_subsection; color111 = color_gray; color112 = color_subsubsection
color120 = color_subsection; color121 = color_gray; color122 = color_subsubsection
color130 = color_subsection; color131 = color_gray; color132 = color_subsubsection

# =====================================================================
# Styles
# =====================================================================

if THEME == "dark":    is_bold = False
elif THEME == "light": is_bold = True

bold0   = is_bold
bold1   = is_bold
bold20  = is_bold; bold21 = is_bold; bold22 = is_bold
bold30  = is_bold; bold31 = is_bold; bold32 = is_bold
bold40  = is_bold; bold41 = is_bold; bold42 = is_bold
bold50  = is_bold; bold51 = is_bold; bold52 = is_bold
bold6   = is_bold
bold70  = is_bold; bold71 = is_bold; bold72 = is_bold
bold80  = is_bold; bold81 = is_bold; bold82 = is_bold
bold90  = is_bold; bold91 = is_bold; bold92 = is_bold
bold10  = is_bold
bold110 = is_bold; bold111 = is_bold; bold112 = is_bold
bold120 = is_bold; bold121 = is_bold; bold122 = is_bold
bold130 = is_bold; bold131 = is_bold; bold132 = is_bold

# =====================================================================
# Description structurée du snippet
# =====================================================================

snippet = [
    # Ligne 0
    [{"text": txt00},
     {"text": txt01, "color": color0, "bold": bold0, "typewrite": True, "typewrite_cycle": 2.0},
     {"text": "|", "color": color_bg, "blink": True, "blink_color": color_prim, "blink_cycle": 1.0, "bold": True, "blink_delay": 1.7}],
    # Ligne 1
    [{"text": txt_s}],
    [{"text": txt1, "color": color1, "bold": bold1}],
    # Ligne 2
    [{"text": txt20, "color": color20, "bold": bold20},
     {"text": txt21, "color": color21, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold21},
     {"text": txt22, "color": color22, "bold": bold22}],
    # Ligne 3
    [{"text": txt30, "color": color30, "bold": bold30},
     {"text": txt31, "color": color31, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold31},
     {"text": txt32, "color": color32, "bold": bold32}],
    # Ligne 4
    [{"text": txt40, "color": color40, "bold": bold40},
     {"text": txt41, "color": color41, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold41},
     {"text": txt42, "color": color42, "bold": bold42}],
    # Ligne 5
    [{"text": txt50, "color": color50, "bold": bold50},
     {"text": txt51, "color": color51, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold51},
     {"text": txt52, "color": color52, "bold": bold52}],
    # Ligne 6
    [{"text": txt_s}],
    [{"text": txt6, "color": color6, "bold": bold6}],
    # Ligne 7
    [{"text": txt70, "color": color70, "bold": bold70},
     {"text": txt71, "color": color71, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold71},
     {"text": txt72, "color": color72, "bold": bold72}],
    # Ligne 8
    [{"text": txt80, "color": color80, "bold": bold80},
     {"text": txt81, "color": color81, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold81},
     {"text": txt82, "color": color82, "bold": bold82}],
    # Ligne 9
    [{"text": txt90, "color": color90, "bold": bold90},
     {"text": txt91, "color": color91, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold91},
     {"text": txt92, "color": color92, "bold": bold92}],
    # Ligne 10
    [{"text": txt_s}],
    [{"text": txt10, "color": color10, "bold": bold10}],
    # Ligne 11
    [{"text": txt110, "color": color110, "bold": bold110},
     {"text": txt111, "color": color111, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold111},
     {"text": txt112, "color": color112, "bold": bold112}],
    # Ligne 12
    [{"text": txt120, "color": color120, "bold": bold120},
     {"text": txt121, "color": color121, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold121},
     {"text": txt122, "color": color122, "bold": bold122}],
    # Ligne 13
    [{"text": txt130, "color": color130, "bold": bold130},
     {"text": txt131, "color": color131, "animate_letters": True, "highlight_color": color_grey, "highlight_cycle": 3.0, "bold": bold131},
     {"text": txt132, "color": color132, "bold": bold132}],
]



# =====================================================================
# Fonctions
# =====================================================================

def _embed_font_woff2(path):
    """
    Lit un fichier .woff2 et renvoie son contenu encodé en base64,
    afin de pouvoir l'embarquer directement dans le SVG via @font-face.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

def render_code_svg(lines, filename, font_family, font_size, padding_top, padding_right, padding_bottom, padding_left, bg_color,
                    border_radius=12, default_color="#ffffff", line_height=1.4, font_normal_path=None, font_bold_path=None, font_italic_path=None):
    """
    Rendu principal du "code snippet" en SVG.
    """

    # Nombre de lettres illuminées en même temps
    COMET_WINDOW_SIZE  = 3

    # -----------------------------------------------------------------
    # Calcul des dimensions du SVG (largeur / hauteur)
    # -----------------------------------------------------------------

    max_chars = 0
    for line in lines:
        text_line = "".join(seg.get("text", "") for seg in line)
        max_chars = max(max_chars, len(text_line))

    # Approximation de la largeur moyenne d'un caractère monospace
    char_width = font_size * 0.6

    width = int(padding_left + padding_right + max_chars * char_width)
    lh_px = font_size * line_height
    height = int(padding_top + padding_bottom + len(lines) * lh_px)

    # Création du dessin SVG
    dwg = svgwrite.Drawing(filename, size=(width, height))
    dwg.viewbox(0, 0, width, height)

    # -----------------------------------------------------------------
    # Intégration des polices
    # -----------------------------------------------------------------

    css_rules = []

    if font_normal_path:
        normal_b64 = _embed_font_woff2(font_normal_path)
        css_rules.append(f"""@font-face {{font-family: '{font_family}';
                                          src: url("data:font/woff2;base64,{normal_b64}") format('woff2');
                                          font-weight: 400;
                                          font-style: normal}}""")

    if font_bold_path:
        bold_b64 = _embed_font_woff2(font_bold_path)
        css_rules.append(f"""@font-face {{font-family: '{font_family}';
                                          src: url("data:font/woff2;base64,{bold_b64}") format('woff2');
                                          font-weight: 700;
                                          font-style: normal}}""")

    if font_italic_path:
        italic_b64 = _embed_font_woff2(font_italic_path)
        css_rules.append(f"""@font-face {{font-family: '{font_family}';
                                          src: url("data:font/woff2;base64,{italic_b64}") format('woff2');
                                          font-weight: 400;
                                          font-style: italic}}""")

    if css_rules:
        css_rules.append(f"""text {{font-family: '{font_family}', monospace}}""")
        dwg.defs.add(dwg.style("\n".join(css_rules)))

    # -----------------------------------------------------------------
    # Dessin du background (rectangle avec bords arrondis)
    # -----------------------------------------------------------------

    bg = dwg.rect(insert=(0, 0), size=(width, height), rx=border_radius, ry=border_radius, fill=bg_color)
    dwg.add(bg)

    # -----------------------------------------------------------------
    # Dessin du texte (ligne par ligne, segment par segment)
    # -----------------------------------------------------------------

    # position verticale de la première ligne
    y = padding_top + font_size

    # position horizontale de départ
    x_start = padding_left

    for line in lines:
        x = x_start

        for seg in line:
            text = seg.get("text")
            if not text: continue

            color = seg.get("color", default_color)

            # Style simple
            bold = seg.get("bold", False)
            italic = seg.get("italic", False)
            font_weight = 700 if bold else 400
            font_style = "italic" if italic else "normal"

            # Flags d'animation
            animate_letters = seg.get("animate_letters", False)
            blink = seg.get("blink", False)
            typewrite = seg.get("typewrite", False)

            # Cas : effet machine à écrire (les lettres apparaissent une par une)
            if typewrite:
                # Durée totale pour écrire toute la phrase (en secondes)
                typewrite_cycle = seg.get("typewrite_cycle", 4.0)

                parent_text = dwg.text("", font_size=font_size, font_family=font_family, font_weight=font_weight, font_style=font_style)

                n = len(text)
                dur = typewrite_cycle
                local_x = x

                for i, ch in enumerate(text):
                    # Une lettre = un <tspan>
                    tspan = dwg.tspan(ch, x=[local_x], y=[y], fill=color)
                    tspan.update({"xml:space": "preserve"})

                    # Séquence d'opacité : 0 tant que la lettre n'est pas "tapée",
                    # puis 1 à partir de son tour.
                    steps = []
                    for k in range(n):
                        if k < i: steps.append("0")
                        else:     steps.append("1")

                    values_str = ";".join(steps)

                    animate = dwg.animate(attributeName="fill-opacity", values=values_str, dur=f"{dur}s", repeatCount="1", calcMode="discrete", fill="freeze")
                    tspan.add(animate)

                    parent_text.add(tspan)
                    local_x += char_width

                dwg.add(parent_text)
                x += len(text) * char_width
                continue



            # Cas : vague de couleur lettre par lettre
            if animate_letters:
                highlight_color = seg.get("highlight_color")
                highlight_cycle = seg.get("highlight_cycle")

                parent_text = dwg.text("", font_size=font_size, font_family=font_family, font_weight=font_weight, font_style=font_style)

                n = len(text)
                dur = highlight_cycle
                local_x = x

                for i, ch in enumerate(text):
                    tspan = dwg.tspan(ch, x=[local_x], y=[y], fill=color)
                    tspan.update({"xml:space": "preserve"})

                    steps = []
                    for k in range(n):
                        active_indices = {(k + j) % n for j in range(COMET_WINDOW_SIZE)}
                        if i in active_indices: steps.append(highlight_color)
                        else: steps.append(color)

                    values_str = ";".join(steps)

                    animate = dwg.animate(attributeName="fill", values=values_str, dur=f"{dur}s", repeatCount="indefinite", calcMode="discrete")
                    tspan.add(animate)

                    parent_text.add(tspan)
                    local_x += char_width

                dwg.add(parent_text)
                x += len(text)*char_width
                continue

            # Cas : clignotant
            if blink:
                blink_color = seg.get("blink_color")
                blink_cycle = seg.get("blink_cycle")
                blink_delay = seg.get("blink_delay")  # en secondes, optionnel

                t = dwg.text(text, insert=(x, y), fill=color, font_size=font_size, font_family=font_family, font_weight=font_weight, font_style=font_style)
                t.update({"xml:space": "preserve"})

                animate = dwg.animate(attributeName="fill", values=f"{color};{blink_color};{color}", dur=f"{blink_cycle}s", repeatCount="indefinite", calcMode="discrete")

                # Si un délai est spécifié, on décale le début de l'animation
                if blink_delay is not None: animate["begin"] = f"{blink_delay}s"

                t.add(animate)
                dwg.add(t)

                x += len(text) * char_width
                continue


            # Cas : texte statique
            t = dwg.text(text, insert=(x, y), fill=color, font_size=font_size, font_family=font_family, font_weight=font_weight, font_style=font_style)
            t.update({"xml:space": "preserve"})
            dwg.add(t)

            x += len(text)*char_width

        # Ligne suivante
        y += lh_px

    # Sauvegarde du fichier
    dwg.save()


# =====================================================================
# Appel principal : génération du SVG
# =====================================================================

render_code_svg(snippet,
                filename         = "readme_" + THEME + ".svg",
                font_family      = FONT_FAMILY,
                font_size        = FONT_SIZE,
                bg_color         = color_bg,
                padding_top      = PADDING[0],
                padding_right    = PADDING[1],
                padding_bottom   = PADDING[2],
                padding_left     = PADDING[3],
                font_normal_path = FONT_PATH_REGULAR,
                font_bold_path   = FONT_PATH_BOLD,
                font_italic_path = FONT_PATH_ITALIC)