from langchain.prompts import ChatPromptTemplate
import pandas as pd

#Name translation templates

name_extraction_template = ChatPromptTemplate.from_messages([
("system", "You are a text extraction assistant specializing in ancient Roman and Germanic historical texts."),
("user", """From the text below please extract:
- Names of people (historical figures, rulers, writers, deities, etc.)
- Names of peoples (tribes, ethnic groups, or collective populations)
- Geographical references (places, regions, rivers, mountains, cities, provinces)

Guidelines:
- Extract variant spellings as separate entries if they appear differently in the text.
- Extract the words exactly as they appear in the text.
- List each unique name only once per category.
- Return only a valid JSON file.

Output format:
Return a JSON file in the following format...

{{
"names_of_people":[<your response>],
"names_of_peoples":[<your response>],
"geographical_references":[<your response>]
}}

If there is no values to extract return an empty JSON, such as:
{{
"names_of_people":[],
"names_of_peoples":[],
"geographical_references":[]
}}

Text:
{text}
""")
])


name_translation_template = ChatPromptTemplate.from_messages([
("system", "You are an expert English-to-Bulgarian translator."),
("user", """Goal:
Translate to Bulgarian the documents provided in the dictionary. They fall in one of three different categories indicated by the dictionary keys:
- Names of people
- Names of peoples
- Geographical references

Documents to translate:
{names_in_english}

Output:
Return a table in a csv format, with the following columns:
1. "Name in English"
2. "Name in Bulgarian"
3. "Category"
4. "Translation type"

Guidelines:
1. Accepted translation is preferred over transliteration.
2. If there is no accepted translation, use transliteration.
3. In the "Category" column return the dictionary key of the documents you are translating. 
4. Indicate the translation type as either "translation" or "transliteration" in the "Translation type" column.
""")
])

#Text translation prompts

text_translation_template = ChatPromptTemplate.from_messages(
    [
    ("system", "You are an expert English-to-Bulgarian translator."),
    ("user", """Goal: Translate to Bulgarian the text below.
     
Important rules:
1. Always use the dictionary below when translating proper names, places, nations, and peoples. If a term appears in the dictionary, use the Bulgarian translation exactly as listed.
2. If a name or place is not in the dictionary, transliterate it into Bulgarian according to standard conventions.
3. Preserve meaning and flow, but follow the dictionary strictly.

Dictionary of names and terms:
{names_dictionary}

Text to translate:
{text_chunk}
"""
     )
]
)