# Module that handles hotkey button screen
#

init python:

    # function to hide buttons
    def HKBHideButtons():
        # RUNTIME ONLY
        # Hides the hkb buttons
        #
        config.overlay_screens.remove("hkb_overlay")
        renpy.hide_screen("hkb_overlay")


    # function to show buttons
    def HKBShowButtons():
        # RUNTIME ONLY
        # Shows the hkb buttons
        #
        config.overlay_screens.append("hkb_overlay")

# TODO all of these shield functions need aadjusting with keymaps
    def mas_HKBRaiseShield():
        """RUNTIME ONLY
        Disables the hotkey buttons
        """
        store.hkb_button.enabled = False


    def mas_HKBDropShield():
        """RUNTIME ONLY
        Enables the hotkey buttons
        """
        store.hkb_button.enabled = True


    def mas_HKBRaiseShield_AD():
        """RUNTIME ONLY
        Disables the hotkey buttons EXCEPT for Music
        """
        store.hkb_button.ad_enabled = False


    def mas_HKBDropShield_AD():
        """RUNTIME ONLY
        Enables the hotkey buttons EXCEPT for Music
        """
        store.hkb_button.ad_enabled = True


    def mas_HKBRaiseShield_M():
        """RUNTIME ONLY
        Disables the Music hotkey button
        """
        store.songs.enabled = False

    
    def mas_HKBDropShield_M():
        """RUNTIME ONLY
        Enables the Music hotkey button
        """
        store.songs.enabled = True


    def mas_HKBIsEnabled():
        """
        RETURNS: True if all the buttons are enabled, False otherwise
        """
        return store.hkb_button.enabled and store.hkb_button.ad_enabled

        # function to hide buttons
    def MovieOverlayHideButtons():
        #
        # Hides the movie buttons
        #
        if "movie_overlay" in config.overlay_screens:
            config.overlay_screens.remove("movie_overlay")
            renpy.hide_screen("movie_overlay")

    # function to show buttons
    def MovieOverlayShowButtons():
        #
        # Shows the movie buttons
        #
        config.overlay_screens.append("movie_overlay")


init -1 python in hkb_button:

    # new property to disable buttons
    # set to False to disable buttons
    enabled = True

    # property for disabling only Talk and Play (basically this wont disable
    # music)
    ad_enabled = True
    movie_buttons_enabled = False


# HOTKEY BUTTON SCREEN ========================================================
# Literally just hotkey buttons

# properties for these new buttons
# again copied from choice
define gui.hkb_button_width = 120
define gui.hkb_button_height = None
define gui.hkb_button_tile = False
#define gui.hkb_button_borders = Borders(0, 5, 0, 5)
define gui.hkb_button_text_font = gui.default_font
define gui.hkb_button_text_size = gui.text_size
define gui.hkb_button_text_xalign = 0.5
#define gui.hkb_button_text_xanchor = 0.5
define gui.hkb_button_text_idle_color = "#000"
define gui.hkb_button_text_hover_color = "#fa9"
define gui.hkb_button_text_kerning = 0.2

# starting with a new style: hkb (hotkey button)
# most of this is copied from choice
style hkb_vbox is vbox
style hkb_button is button
style hkb_button_text is button_text

style hkb_vbox:
    spacing 0

style hkb_button is default:
    properties gui.button_properties("hkb_button")
    idle_background  "mod_assets/hkb_idle_background.png"
    hover_background "mod_assets/hkb_hover_background.png"
    ypadding 5

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_text is default:
    properties gui.button_text_properties("hkb_button")
    outlines []

# and a disabled varient of the button
style hkbd_vbox is vbox
style hkbd_button is button
style hkbd_button_text is button_text

style hkbd_vbox:
    spacing 0

style hkbd_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/hkb_disabled_background.png"
    hover_background "mod_assets/hkb_disabled_background.png"

style hkbd_button_text is default:
#    properties gui.button_text_properties("hkb_button")
    font gui.default_font
    size gui.text_size
    idle_color "#000"
    hover_color "#000"
    kerning 0.2
    outlines []

style hkb_text is default:
    xalign 0.5
    size gui.text_size
    font gui.default_font
    color "#000"
    kerning 0.2
    outlines []

screen hkb_overlay():

    zorder 50

    style_prefix "hkb"

    vbox:
        xpos 0.05
#        xalign 0.05
        ypos 0.80
#        yalign 0.95

        if store.hkb_button.enabled and store.hkb_button.ad_enabled:
            textbutton _("Talk") action Jump("prompt_menu")
        else:
            frame:
                ypadding 5
                xsize 120

                background Image("mod_assets/hkb_disabled_background.png")
                text "Talk"

# NOTE: disabled until we have additoinal content
#if allow_dialogue and store.hkb_button.enabled:
#            textbutton _("Movies") action Jump("ch30_monikamovie")
#        else:
#            textbutton _("Movies"):
#                action NullAction()
#                style "hkbd_button"


        if store.hkb_button.enabled:
            textbutton _("Music") action Function(select_music)
        else:
            frame:
                ypadding 5
                xsize 120

                background Image("mod_assets/hkb_disabled_background.png")
                text "Music"
           

        if store.hkb_button.enabled and store.hkb_button.ad_enabled:
            textbutton _("Play") action Jump("pick_a_game")
        else:
            frame:
                ypadding 5
                xsize 120

                background Image("mod_assets/hkb_disabled_background.png")
                text "Play"
           

screen movie_overlay():

    zorder 50

    style_prefix "hkb"

    vbox:
        xalign 0.95
        yalign 0.95

        if watchingMovie:
            textbutton _("Pause") action Jump("mm_movie_pausefilm")
        else:
            textbutton _("Pause") action NullAction() style "hkbd_button"

        if watchingMovie:
            textbutton _("Time") action Jump("mm_movie_settime")
        else:
            textbutton _("Time"):
                action NullAction()
                style "hkbd_button"

init python:
    HKBShowButtons()
