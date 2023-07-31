// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

@R2
M = 0

@R1
D = M

@temp
M = D

@product
M = 0

(LOOP)
    @temp
    D = M

    @END
    D; JEQ

    @R0
    D = M

    @product
    M = M+D

    @temp
    M = M-1

    @LOOP
    0; JMP

(END)
    @product
    D =M
    @R2
    M = D

    @END
    0; JMP

