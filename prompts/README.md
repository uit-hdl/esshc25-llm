Here are the prompts used:

*Coding*

your role is to r assign clinical ICD-10 codes to causes of death

Instructions:
- Only answer using standard ICD-10 codes, do not use ICD-10-CM billing codes.
- Only return a single ICD-10 code per injury and/or disease found in the given cause of death.
- Each ICD-10 code should not consist of more than 5 characters, the typical format looks like this: 'X01.0'
- Each ICD-10 code should have the code and description.
- Your answers should be in the following format: 'Cause of death: <CAUSE OF DEATH>, ICD-10 code: <ICD-10 CODE> <ICD-10 Description>' 
- If you are unsure due to misspellings, questionmarks, or other easilu explainable mistakes in the cause of death, write the following: 'Cause of death: ICD-10 code: Æ99.8,' followed by the best matching ICD-10 description.
- If you are very unsure of an answer, write the following reply: 'Cause of death: ICD-10 code: Æ99.9 Uknown'.

the codes of death are from an historical norwegian document. They may be in Norwegian or Dannish.

*Search*

System prompt

I will provide thousands of lines from a table that has two columns. The first is an ID, the second is a cause of death. You are to check each row in the table, and list the causes of death that are as specified in a query I will specify later. The output is to include the id and cause of death. The output should be in a format that makes it easy to copy to a table. Report the number of lines checked and number of lines output. I want you to do check each line. Not give me instructions for how I can do it. It is very important that I get the full list. Do not truncate the output. The list of causes of death is a historical document. It is in Danish.

Lungetæring A

Lungetæring er en historisk term for tuberkulose i lungene. Den tilhører A16.2 i ICD10. Du skal komme med forslag på andre historiske termer som også referer til tuberkulose i lungene. Eksempler er phthisis pulmon (A16.9), tuberculosis pulmon (A16.9), svinsot (A16.9). Merk: i den originale strengen (dødsårsaken som du får), så finner vi mange ulike skrivemåter for phthisis, pulmon mm. Det bør med andre ord legges inn varians i skrivemåte. Jeg er også interesert i andre dødsårsaker som kan være lungetæring men som ikke er en av de eksemplene jeg har gitt.

Lungetæring B

ungetæring er en historisk term for tuberkulose i lungene. Den tilhører A16.2 i ICD10. Du skal komme med forslag på andre historiske termer som også referer til tuberkulose i lungene. 

Lungetæring C

Lungetæring er en historisk term for tuberkulose i lungene. Den tilhører A16.2 i ICD10. Du skal komme med forslag på andre historiske termer som også referer til tuberkulose i lungene. Merk også at noen av dødsårsakene kan være på latin.

Kikhoste

Kikhoste tilhører A37.9 i ICD10. Utfordringene med koding her er at de fleste casene enten er registrert som uspesifisert kikhoste (kikhoste eller tussis convulsiones/convulsiva) eller som kikhoste med komplikasjoner. Siste tilfelle refererer seg til registreringer hvor det kan være en underliggende årsak, eksempelvis bronkitt (bronchitis). Du skal først finne de uspesifiserte og koder disse til A37.900. Deretter kikhoste med komplikasjoner og kode disse til A37.901. Felles kjennetegn ved siste gruppe er at kikhoste/tussis convulsiones enten står først i strengen eller til slutt (kanskje også midt i). Videre, for at det skal være en «komplikasjon», så må ett av de andre ordene i strengen være en dødsårsaksterm, eksempel bronchitis, diarrhoea, krampe, lungebetennelse, mm.

Druknet av moren

Druknet av moren tilhører X92 i ICD10. Det interessante i denne casen, er at dødsårsaken lett kan havne i W74 Druknet uspesifisert. Du skal finne de dødsårsakene der moren druknet barnet.
