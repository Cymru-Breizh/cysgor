# Cysgor

Cysill wrapper to score Welsh texts' grammaticality. As it connects to the Cysill API, ensure to have a working internet connexion before using it.

## As a CLI
There are two ways to use the CLI, either by entering a text file's path, or directly a text. The CLI returns a string of numbers representing the grammaticality score of the text.

```sh
# With a text as a positional character
cysgor "Mae hen gwlad fy tadau yn annwyl i mi!"
```

```sh
# With a -p or --path flag
cysgor --path src/cysgor/assets/text-sample.txt
```

or alternatively with the pipe operator:

```sh
cat src/cysgor/assets/text-sample.txt | cysgor 
```

## As a library

One can also use this package as a python library:

```py
from cysgor import get_score, get_mistakes

# get the scores
df["scores"] = df["texts"].apply(get_score)
# returns a list of mistakes for each text
df["mistakes"] = df["texts"].apply(get_mistakes)
```


