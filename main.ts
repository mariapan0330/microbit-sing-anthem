input.onButtonPressed(Button.A, function () {
    music.setVolume(music.volume() - 20)
})
input.onButtonPressed(Button.B, function () {
    music.setVolume(music.volume() + 20)
})
input.onGesture(Gesture.Shake, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . . . . .
        . . . # #
        . . . # #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # # . . .
        # # . . .
        . . . . .
        . . . . .
        `)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    start_idle = 0
    anthem_notes = [
    196,
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
    131
    ]
    anthem_beats = [
    0.5,
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
    1
    ]
    music.setTempo(292)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . # . #
        . # . # .
        . . # . .
        `)
    for (let index = 0; index <= anthem_notes.length; index++) {
        music.play(music.tonePlayable(anthem_notes[index], anthem_beats[index] * music.tempo()), music.PlaybackMode.UntilDone)
    }
})
let blink_or_glance = 0
let anthem_beats: number[] = []
let anthem_notes: number[] = []
let start_idle = 0
start_idle = 1
// Idle mode.
basic.forever(function () {
    while (start_idle == 1) {
        basic.showLeds(`
            . . # # .
            . # # # #
            . # # # #
            . . # # .
            . . . . .
            `)
        basic.pause(randint(10, 2500))
        blink_or_glance = randint(1, 2)
        if (blink_or_glance == 1) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . # # # #
                . . . . .
                `)
        } else {
            basic.showLeds(`
                . # # . .
                # # # # .
                # # # # .
                . # # . .
                . . . . .
                `)
        }
    }
})
