# Cysgor

Cysill wrapper to score Welsh texts' grammaticality. As it connects to the Cysill API, ensure to have a working internet connexion before using it.

## As a CLI
There are two ways to use the CLI, either by entering a text file's path, or directly a text. The CLI returns a string of numbers representing the grammaticality score of the text.

```
# With a text as a positional character
cysgor "Mae hen gwlad fy tadau yn annwyl i mi!"
```

```
# With a -p or --path flag
cysgor --path src/cysgor/assets/text-sample.txt
```

or alternatively with the pipe operator:

```
cat src/cysgor/assets/text-sample.txt | cysgor 
```

## As a library

<!-- TODO -->
