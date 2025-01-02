# About UOS

This is a **kernel** written in [URCL](https://github.com/ModPunchtree/urcl) called "UOS".

***Important:***
> A kernel is **not** an operating system.\
> It only provides the base of an operating system.

## What about... the syscalls?

There are a plethora of syscalls (system calls), expanding based on the needs.\
If you find a syscall to be missing, or want one for your situation, use the Issues tab OR make a PR if you have already written the syscall's code.

Here is a list of the **syscalls**:

```
fn_m0 (freeall, no arguments): Frees all the heap.
fn_m1 (get_free, no arguments): Returns the free memory space MINUS the reserved memory (see below for the memory management).
fn_m2 (free_input, no arguments): Frees the 'input' (also the reserved memory).
fn_g0 (getch, no arguments): Returns the character you just pressed (SYNCHRONOUS!).
fn_g1 (getch_echo, no arguments): Returns AND prints the character you just pressed. (SYNCHRONOUS!).
fn_g2 (parseint, arguments: [number]): Takes in (via stack) one character and returns the number. If it is not a number, returns 127.
fn_v0 (print, no arguments): Prints (and frees!) each character of the reserved memory.
fn_v1 (draw, arguments: [x, y, colour]): Draws one pixel at x, y and of colour.
```

## The memory model.

UOS's memory model is kind of simple.\
It has a working memory of 44 bytes (for now) and a reserved memory of 56 bytes (can be resized using max_print).

The reserved memory, as explained by its name, is reserved for text input or text output and manipulation.\
The working memory can hold anything in contrast.
