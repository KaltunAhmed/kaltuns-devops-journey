## Binary, Octal and String Representation


| String Representation | Binary Representation | Octal Representation   | Permission Description       |
|-----------------------|-----------------------|------------------------|------------------------------|
| `---`                 | `000`                 | `0 (000)`              | No permissions               |
| `--x`                 | `001`                 | `1 (001)`              | Execute                      |
| `-w-`                 | `010`                 | `2 (010)`              | Write                        |
| `-wx`                 | `011`                 | `3 (011)`              | Write and execute            |
| `r--`                 | `100`                 | `4 (100)`              | Read                         |
| `r-x`                 | `101`                 | `5 (101)`              | Read and execute             |
| `rw-`                 | `110`                 | `6 (110)`              | Read and write               |
| `rwx`                 | `111`                 | `7 (111)`              | Read, write, and execute     |