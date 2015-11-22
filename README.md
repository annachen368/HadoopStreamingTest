Z3-str2 is a string theory plug-in built on the powerful Z3 SMT solver.

Z3-str2 treats strings as a primitive type, thus avoiding the inherent limitations 
observed in many existing solvers that encode strings in terms of other primitives.


# Documentations:

Please refer to [https://sites.google.com/site/z3strsolver/](https://sites.google.com/site/z3strsolver/)





# Install Z3-str2

1. Check out the latest version of Z3-str2 from the git repo.


2. Download [the source code of Z3 4.1.1](http://z3.codeplex.com/releases/view/95640)
   
  MD5 SUM: ```c0c2367e4de05614a80b3f62480c23db  z3-src-4.1.1.zip```


3. Unzip "z3-src-4.1.1.zip" and patch the original Z3. Z3-str2 will work with 
   the modified Z3 core.
   * How to patch Z3 core. Suppose the folder name after unzipping is "z3".

     *  $ cp z3.patch z3/
     *  $ cd z3
     *  $ patch -p0 < z3.patch
   
   
4. In the top level folder of Z3 Build the modifed version of Z3
   * $ autoconf
   
   * $ ./configure
   
   * $ make
   
   * $ make a
   
   
5. Build  Z3-str2
   * Modify variable "Z3_path" in the Z3-str2 Makefile to indicate the patched Z3 location.

     * $ make

       
6. Setup Z3-str2 driver script
   * In "Z3-str.py", change the value of the variable "solver" to point to the 
     Z3-str2 binary "str" just built
 
 
7. Run Z3-str2
   *  ```Z3-str.py -f <inputFile>```, e.g 
   
     *  $./Z3-str.py -f tests/concat-002

# Z3 4.1.1 Score code

Z3 is a theorem prover from Microsoft Research.
Z3 is licensed under MSR-LA (Microsoft Research License Agreement). 
See http://z3.codeplex.com/license for more information about this license.
Z3 can be built using Visual Studio Command Prompt, Visual Studio and make/gcc.

1) Building Z3 on Windows using Visual Studio Command Prompt

- Open a Visual Studio Command Prompt, then execute one of the following commands to build the desired component.

- For building all components, execute
    msbuild z3-prover.sln /p:configuration=external 
  All components will be located at /external

- For building all components (64-bit), execute
    msbuild z3-prover.sln /p:configuration=external_64 /p:platform=x64
  All components will be located at /external_64

- For building all components (in debug mode), execute
    msbuild z3-prover.sln 
  All components will be located at /debug

1) Building Z3 using g++/make
Your machine must also have the following commands to be able to build Z3:
autoconf, sed, awk, dos2unix commands


- Open a shell
- For building the z3 executable, execute
 
  autoconf
  ./configure
  make

The z3 executable will be located at bin/external/

- If you want a static library for Z3

  make a

- If you also want the z3 shared library, execute

  make so

  for libz3.so (on Linux)

  make dylib

  for libz3.dylib (on OSX)

Remark: the Z3 makefile imports the source file list from Visual Studio project files.
To add new source files to the Z3 core, you must include them at: lib/lib.vcxproj

