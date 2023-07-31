// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(START)
    @SCREEN
    D = A

    @address
    M = D

    @8192
    D = A
    @pixelLeftToPainted
    M = D

    @keyboard
    M = 0

(CHECK)
    @pixelLeftToPainted
    D = M

    @START   // If there is no pixel left, go to Start
    D, JEQ

    @KBD
    D = M

    @BLACKSC
    D, JNE // IF there is a key, go to BLACKSC

    @WHITESC
    D, JEQ // If no key is pressed, go to WHITESC



    (CHECK2)
        @pixelLeftToPainted
        D = M

        @BLACKSC
        D, JNE // IF there is a key, go to BLACKSC

        @START
        D, JEQ



    (BLACKSC)
        @address
        A = M
        M = -1

        @address
        M = M + 1

        @pixelLeftToPainted
        M = M - 1

        @CHECK2
        0; JMP

    (WHITESC)
        @address
        A = M
        M = 0

        @address
        M = M + 1

        @pixelLeftToPainted
        M = M -1

        @CHECK
        0; JMP





