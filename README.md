# Machine Translation of *Germania* by Tacitus into Bulgarian  

This project aims to machine-translate *Germania*, a classic work by the 1st-century Roman historian **Tacitus**, into Bulgarian.  

The translation is based on **Thomas Gordon’s 18th-century English translation** from Latin, available via [Project Gutenberg](https://www.gutenberg.org/ebooks/2995).  

---

## Workflow  

The translation process is implemented in two Jupyter notebooks:  

1. **`Names Translation.ipynb`**  
   - Extracts names of people, peoples, and places from the text.  
   - Translates them into Bulgarian using GPT-5.  
   - Saves results in a file for human review.  

2. **`Text Translation.ipynb`**  
   - Uses the reviewed names file to build a dictionary for consistent translations.  
   - Splits *Germania* into paragraph-sized chunks.  
   - Translates and saves the original text side-by-side with the Bulgarian version for easy editing.  

At its core, this is a simple **LangGraph workflow** divided into two "pipelines".  

---

## Output  

The completed translation has been compiled into an **eBook**, featuring an **AI-generated cover page** 🙂.  

👉 [Download the eBook (Google Drive link)](https://drive.google.com/file/d/1ZthRRfxg_HKHnVBLinwUJJc5hAgDLnlb/view?usp=sharing)  

---

## Acknowledgments  

- [Project Gutenberg](https://www.gutenberg.org/) for providing Gordon’s translation.