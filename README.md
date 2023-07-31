# Built a Computer From Scratch
<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![MIT License][license-shield]][license-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Emergency Alert Global Version </h3>

  <p align="center">
    An app that contacts you to the authority in just 1 click!
    <br />
    <a href="https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/issues">Report Bug</a>
    ·
    <a href="https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## :high_brightness: About the project

I have had that question since the first day I participated in Competitive Trading in high school. How can my laptop read those C++ or Python lines and just “do it”?

Or how does the computer know what is 1+1? (I initially thought somehow it searched the internet and sent us the result lol). But actually, every single thing comes from the Computer or the CPU.

In this project, I will build a computer from scratch, from CPU to high-level language to gain an understanding of how computer work but also how we can increase efficiency in a low-level scope.

Specifically, I implemented:

1. Operating System Classes: Math, Sys, Memory, Array, Linked List Classes
2. Basic Arithmetic Function: Add, Multiply by Assembly
3. Basic Computer Function: Draw a Line, Circle, or a Character by Assembly

By implementing these essential functions of the computer, I understood how a computer allocates or deallocates memory efficiently, how it does multiply in log time.

## 📟 Code Example

This code accounts for Add Implementation

```asm
// Computes R0 = 2 + 3  (R0 refers to RAM[0])
@2
D=A
@3
D=D+A
@0
M=D
```

##### Add 2 constant in Virtual Machine

```
// Pushes and adds two constants.
push constant 7
push constant 8
add
```

##### Array Class Implementation:

```
class Array {

    /** Constructs a new Array of the given size. */
    function Array new(int size) {
      return Memory.alloc(size);

    }

    /** Disposes this array. */
    method void dispose() {
      // we need an Array for deAlloc(). So get the this
      //var Array that;
      //let that = Memory.peek(4);
      do Memory.deAlloc(this);
      return;
    }
}
```




## Intro to Hack Assembly

The Hack Assembly Language mainly consists of 3 types of instructions. It ignores whitespace and allows programs to declare symbols with a single symbol declaration instruction. Symbols can either be labels or variables.

### Predefined Symbols

- **A**: Address Register.
- **D**: Data Register.
- **M**: Refers to the register in Main Memory whose address is currently stored in **A**.
- **SP**: RAM address 0.
- **LCL**: RAM address 1.
- **ARG**: RAM address 2.
- **THIS**: RAM address 3.
- **THAT**: RAM address 4.
- **R0**-**R15**: Addresses of 16 RAM Registers, mapped from 0 to 15.
- **SCREEN**: Base address of the Screen Map in Main Memory, which is equal to 16384.
- **KBD**: Keyboard Register address in Main Memory, which is equal to 24576.

### Types of Instructions

1. A-Instruction: Addressing instructions.
2. C-Instruction: Computation instructions.
3. L-Instruction: Labels (Symbols) declaration instructions.

#### A-INSTRUCTIONS

##### Symbolic Syntax of an A-Instruction

`@value`, where value is either a decimal non-negative number or a Symbol.

Examples:

- `@21`
- `@R0`
- `@SCREEN`

##### Binary Syntax of an A-Instruction

`0xxxxxxxxxxxxxxx`, where `x` is a bit, either 0 or 1. A-Instructions always have their MSB set to 0.

Examples:

- `000000000001010`
- `011111111111111`

##### Effects of an A-Instruction

Sets the contents of the **A** register to the specified value. The value is either a non-negative number (i.e. 21) or a Symbol. If the value is a Symbol, then the contents of the **A** register is set to the value that the Symbol refers to but not the actual data in that Register or Memory Location.

#### L-INSTRUCTIONS

Symbols can be either variables or labels. Variables are symbolic names for memory addresses to make remembering these addresses easier. Labels are instructions addresses that allow multiple jumps in the program easier to handle. Symbols declaration is not a machine instruction because machine code doesn't operate on the level of abstraction of that of labels and variables, and hence it is considered a pseudo-instruction.

##### Declaring Variables

Declaring variables is a straightforward A-Instruction, example:

```asm
@i
M=0
```

The instruction `@i` declares a variable "i", and the instruction `M=0` sets the memory location of "i" in Main Memory to 0, the address "i" was automatically generated and stored in **A** Register by the instruction.

##### Declaring Labels

To declare a label we need to use the command `(LABEL_NAME)`, where "LABEL_NAME" can be any name we desire to have for the label, as long as it's wrapped between parentheses. For example:

```asm
(LOOP)
  // ...
  // instruction 1
  // instruction 2
  // instruction 3
  // ...
  @LOOP
  0;JMP
```

The instruction `(LOOP)` declares a new label called "LOOP", the assembler will resolve this label to the address of the next instruction (A or C instruction) on the following line.

The instruction `@LOOP` is a straight-forward A-Instruction that sets the contents of **A** Register to the instruction address the label refers to, whereas the `0; JMP` instruction causes an unconditional jump to the address in **A** Register causing the program to execute the set of instructions between `(LOOP)` and `0; JMP` infinitely.

#### C-INSTRUCTIONS

##### Symbolic Syntax of a C-Instruction

*dest* = *comp* ; *jmp*, where:

1. *dest*: Destination register in which the result of computation will be stored.
2. *comp*: Computation code.
3. *jmp*: The jump directive.

Examples:

- `D=0`
- `M=1`
- `D=D+1;JMP`
- `M=M-D;JEQ`

##### Binary Syntax of a C-Instruction

`1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3`, where:

- `111` bits: C-Instructions always begin with bits `111`.
- `a` bit: Chooses to load the contents of either **A** register or **M** (Main Memory register addressed by **A**) into the ALU for computation.
- Bits `c1` through `c6`: Control bits expected by the ALU to perform arithmetic or bit-wise logic operations.
- Bits `d1` through `d3`: Specify which memory location to store the result of ALU computation into: **A**, **D** or **M**.
- Bits `j1` through `j3`: Specify which JUMP directive to execute (either conditional or uncoditional).

##### Effects of a C-Instruction

Performs a computation on the CPU (arithmetic or bit-wise logic) and stores it into a destination register or memory location, and then (optionally) JUMPS to an instruction memory location that is usually addressed by a value or a Symbol (label).


## 🔧 Built With

I built this project by Assembly Language

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## :dizzy: Getting Started

### Prerequisites

Get used to Assembly Language and Operating System

### Installation

1. Clone the repo
   ```sh
   git clone [https://github.com/your_username_/Project-Name.git](https://github.com/DuyNguyenPhuong/Low-latency-Trading-Program.git)
   ```
2. Check the repo named features

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## :mortar_board: Usage

You can run this project by clicking the Make Project Button (Green Arrow) in the top right of the project or type this in the terminal

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## :mountain_cableway: Roadmap

- [x] Finish the Product
- [x] Add back to top links
- [x] Add Additional Templates w/ Examples
- [x] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Vietnamese
    - [ ] Spanish

See the [open issues](https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- CONTRIBUTING -->
## :dancer: Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- LICENSE -->
## :lock: License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- ACKNOWLEDGMENTS -->
## :closed_book: Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)
* [Github Bagde](https://github.com/Ileriayo/markdown-badges)

<p align="right">(<a href="#readme-top">back to top</a>)</p>









<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DuyNguyenPhuong/Emergency-Alert-Global-Version.svg?style=for-the-badge
[contributors-url]: https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DuyNguyenPhuong/Emergency-Alert-Global-Version.svg?style=for-the-badge
[forks-url]: https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/network/members
[stars-shield]: https://img.shields.io/github/stars/DuyNguyenPhuong/Emergency-Alert-Global-Version.svg?style=for-the-badge
[stars-url]: https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Versionstargazers
[issues-shield]: https://img.shields.io/github/issues/DuyNguyenPhuong/Emergency-Alert-Global-Version.svg?style=for-the-badge
[issues-url]: https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/issues
[license-shield]: https://img.shields.io/github/license/DuyNguyenPhuong/Emergency-Alert-Global-Version.svg?style=for-the-badge
[license-url]: https://github.com/DuyNguyenPhuong/Emergency-Alert-Global-Version/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/duyngp/


[product-screenshot]: images/CallDemo.jpg

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[Kotlin]: https://img.shields.io/badge/kotlin-%237F52FF.svg?style=for-the-badge&logo=kotlin&logoColor=white
[Kotlin-url]: https://kotlinlang.org/

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
