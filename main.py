start_idle = 0
anthem_notes: List[number] = []
anthem_beats: List[number] = []
blink_or_glance = 0

def on_button_pressed_a():
    music.set_volume(music.volume() - 20)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    global start_idle
    while input.sound_level() >= 170:
        start_idle = 0
        basic.show_leds("""
            . # . # .
            # . . . #
            . . . . .
            # . . . #
            . # . # .
            """)
        basic.show_leds("""
            # . # . .
            . . . # .
            . . . . .
            . . . # .
            # . # . .
            """)
        basic.show_leds("""
            . # . # .
            # . . . #
            . . . . .
            # . . . #
            . # . # .
            """)
        basic.show_leds("""
            . . # . #
            . # . . .
            . . . . .
            . # . . .
            . . # . #
            """)
    start_idle = 1
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_b():
    basic.show_leds("""
        # . . . #
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_leds("""
        . . . . .
        . . . # #
        . . . # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global start_idle, anthem_notes, anthem_beats
    start_idle = 0
    anthem_notes = [196,
        165,
        131,
        165,
        196,
        262,
        330,
        294,
        262,
        165,
        185,
        196,
        196,
        196,
        330,
        294,
        262,
        247,
        220,
        247,
        262,
        262,
        196,
        165,
        131]
    anthem_beats = [0.5,
        0.5,
        1,
        1,
        1,
        2,
        0.5,
        0.5,
        1,
        1,
        1,
        2,
        0.5,
        0.5,
        1.5,
        0.5,
        1,
        2,
        0.5,
        0.5,
        1,
        1,
        1,
        1,
        1]
    music.set_tempo(292)
    index = 0
    while index <= len(anthem_notes):
        music.play(music.tone_playable(anthem_notes[index], anthem_beats[index] * music.tempo()),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_leds("""
            . . # . .
            . . # . .
            # # . # #
            . . # . .
            . . # . .
            """)
        index += 1
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# Idle mode.

def on_forever():
    global blink_or_glance
    while start_idle == 1:
        basic.show_leds("""
            . . # # .
            . # # # #
            . # # # #
            . . # # .
            . . . . .
            """)
        basic.pause(randint(10, 2500))
        blink_or_glance = randint(1, 2)
        if blink_or_glance == 1:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . # # # #
                . . . . .
                """)
        else:
            basic.show_leds("""
                . # # . .
                # # # # .
                # # # # .
                . # # . .
                . . . . .
                """)
basic.forever(on_forever)
