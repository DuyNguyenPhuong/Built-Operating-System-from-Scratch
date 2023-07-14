# Nantis

1. Jack Code —> Complier to VM Code (Virtual Machine) —> Translate to Machine Language (Assembly Code)
2. Machine Language: Software tell Hardware to do
3. To code faster: Human write MLanguae in assembly language. And let the Assembly Program change to bit
4. Trade-off:
5. What Hardware can do:
- Add, Subtract
- And , Or
- Got to Instruction X, if C go to instruction Y
1. Difference between Machine Languages
- The richness of set of operations: Some ML don’t have add, subtract but let software made a function to do that
- Data types what data types can Hardware access (64-bits, 8 -bits, floating points)
- Richer DataType Hardware: deal with float, real —> Faster than only integers hardware
- Silicon is the material of choice in the chip industry. Unlike the metals normally used to conduct electrical currents, silicon is a 'semiconductor', meaning that its conductive properties can be increased by mixing it with other materials such as phosphorus or boron.
1. Accessing a memory location is expensive
- Need to supply for a long address
- Getting the memory contents into CPU take time

—> Solution Memory Hierachy

Instead of large box of memory:

- The first part of memory: Smallest: Easy to access —> Get info quickly (Register)
- Cache —> Main Memory —> Disk
- Bigger —> Access Harder
- Register: Reside inside the CPU: Their number, function are central part of ML

**Register**

1. Data Register:
- Add R1, R2
1. Address Register
- Store R1, @A. R1 will be written in Main Memory M[A] = R1

************************Input/Output************************

- Many types: Keyboard, Mouse, Camera, Sensor, printers

Ex: Mouse: when moving, the last movement: write in register —> Access by hardware

- CPU needs some kind of protocol to talk to them: Software Driver know these protocols

—> Mean when read the location : Know what that’ s mean

********************Flow Control********************

- In sequence
- Jump to Ex 102 instruction: to do the for loop
- Jump if …

1. Hack Computer: Hardware
- **16-bit Machine: chunks of 16-bit: take, move, print in chunk**
    - Data Memory (RAM): sequence of chunks: Ram[0], Ram[1]
    - Instruction Memory (ROM): sequence of chunks (16 bits): Ram[0], Ram[1]
    - CPU: Central Processing Unit: A DEVICE perform 16 bits instruction
    - Bus: Move data around: **Highway of 16 lanes moving 16 bist**
        - Data Bus: Connect CPU and data memory
        - Instruction: Move instruction memory to CPU
        - Address Bus:
- Sofware: Program using ML:
    - 16 bit A instruction
    - 16 bit C instruction
    - Hack Program = Sequence of instruction written in the Hack machine Language
- Control:
    - ROM is loaded with Hack program
    - reset button is pushed (used once per program)
    - program starts running
- Hack have 3 registers:
    - D, A
    - M: 16 bit RAM addressed by A
- EXAMPLE:
    - @21: Set A to 21; Make RAM[21]: RAM registered
    - @100 : // A = 100
    - M = -1 // RAM[100] = -1
    - M Refer to RAM[A]
- C instruction:
    - comp = computation
    - dest: destination = M, D, MD
    - jump: = null, JGT, JMP
    
    Ex: 
    
    @300 // A = 300
    
    M = D-1 // RAM[300] = D-1
    
    // If D-1 == 0, Jump to excute instruction stored in ROM[56]
    
    @56 
    
    D-1; JEQ // if (d-1==0) go to 56
    
- Represent in Binary:
    - 1 st bit: 0: A; 1: C

1. Platform
- I/O devices are used for:
    - Getting data from / Display data
- Can do this with High-level approach:
    - libraries, animation, audio
- Low-level approach: Bits
- Keyboard/Screen Memory Map
- Keyboard : Ram[24576]

1. Out
- Screen Memory Map:
    - in RAM, special are for display unit
    - Physical display continuous refresh from the memory map, many times for second
    - Out is affected by manipulates the screen memory map

12.

Low level Programming:

- Work with register and memory
- D: Data register
- A: Data/Address Register
- M: Current selected memory register, M = RAM[A]

@D

D = A 

// D = 10

//D++ 

D= D+1

- ************Note:************ The Computer will run forever (They always do smth) —> Hacker might run some code below

—> Solution: Make a infinte loop

@6

0; JMP

- R?: Virtual Register

// This project is update latest on 4/3/2023

13.
In Multiprogramming, OS manages which job to run(schedule); Protect other memory from others, decide which to resume when CPU available
