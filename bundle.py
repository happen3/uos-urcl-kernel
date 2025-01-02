"""
Simple program to insert an OS with the kernel.
If you have an OS and want to bundle it with the kernel, use that!
"""
import sys
import os

REPLACE_AT = 0 # Default to avoid problems
argv = sys.argv

if len(argv) != 3:
    print(f"\033[1;38;2;255;255;0;48;2;0;0;0mUsage: {os.path.basename(argv[0])} <kernel_location> <os_location>\033[0m")
    print("\033[1;38;2;255;99;71mNot enough arguments.\033[0m")
    exit(1)

if not os.path.exists("build"):
    os.mkdir("build")
if os.path.exists(argv[1]):
    if os.path.exists(argv[2]):
        if os.path.isfile(argv[1]):
            if os.path.isfile(argv[2]):
                with open(argv[1], 'r', encoding="utf-8") as kernelc:
                    kernel = kernelc.read()
                with open(argv[2], 'r', encoding="utf-8") as osc:
                    os_code = osc.read()

                # Process OS tag
                print("\033[38;2;0;127;255mProcessing OS import...\033[0m")

                for ln, line in enumerate(kernel.split("\n")):
                    if line == "[IMPORT \"OS\"]":
                        REPLACE_AT = ln

                new_kernel = kernel.split("\n")
                new_kernel[REPLACE_AT] = os_code

                # Write the OS
                print("\033[38;2;0;127;255mWriting the final build...\033[0m")

                with open("build/bundle.urcl", "w", encoding="utf-8") as final:
                    final.write("\n".join(new_kernel))
            else:
                print(f"\033[1;38;2;255;99;71;48;2;0;0;0m\"{argv[2]}\" is not a file.\033[0m")
                exit(4)
        else:
            print(f"\033[1;38;2;255;99;71;48;2;0;0;0m\"{argv[1]}\" is not a file.\033[0m")
            exit(3)
    else:
            print(f"\033[1;38;2;255;99;71;48;2;0;0;0mOS \"{argv[2]}\" does not exist.\033[0m")
            exit(2)
else:
    print(f"\033[1;38;2;255;99;71;48;2;0;0;0mkernel \"{argv[1]}\" does not exist.\033[0m")
    exit(1)

exit(0)
