# Probability and Statistics Notes

This is a series of notes on probability and statistics. The notes are organised into 
jupyter notebooks. As the name suggests these are just notes, so many topics will lack the
rigorousness that a formal treatment of the subject would deliver.


## Creating a book

You can create a book from the notes using <a href="https://quarto.org/">Quarto</a>. 
You can preview the book by using the following on the top level directory of the project.

```
quarto preview

```

You can create a PDF document from the notebooks using

```
quarto render --to pdf
```

## Requirements

The notes depend on a set of requirements. You can use ```pip``` in order to
install what is needed.

```
pip install -r requirements.txt

```

In addition, the notes use the <a href="https://github.com/pockerman/mlutils">mlutils</a> package.
Follow the instructions therein on how to install.


