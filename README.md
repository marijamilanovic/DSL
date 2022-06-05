# DSL for Restaurant Menu
DSL for visualization of Restaurant Menu is created for the purpose of the Domain-Specific Languages course at the Faculty of Technical Sciences, University of Novi Sad. 

### Contributors (Team 2):
|  | Student |
| ------ | ------ |
| Student 1 | Kristina Đurić E2 92/2021 | 
| Student 2 | Maja Dragojlović E2 95/2021 | 
| Student 3 | Marija Milanović E2 98/2021 |


### What is purpose of our DSL?
Our DSL enables restaurants to automatically generate menu. Restaurants could easily generate pdf and then print it for usage. Also, they can generate html page for purpose of their website. The main purpose of our DSL is to save employees time and provide them nicely formated and adjustable menu.

### Features
Our DSL enables:
- Tables for every food section (name, price and ingredients)
- Filtering by food type and creating specific menu
- Defining style of the menu
- Images
- Data from PostgreSQL database

### Technologies
- Python 3.6+
- textX
- Jinja2 template engine
- PostgreSQL
- PDFkit

### Instructions
1. Open a terminal as admin and create a virtual environment <br>
```python -m venv <envName>```
2. Afterwards, activate created virtual environment
   - For Linux: 
    ```source env/bin/active```
   - For Windows:
     ```env\Scripts\activate.bat```
3. Change directory <br>
```cd DSL/menuDSL```
5. Generate html and pdf <br>
```textx generate example.fdm --target html+pdf```
6. To deactivate virtual environment type <br>
```deactivate```

### Example
![image](https://user-images.githubusercontent.com/57723883/147284852-4e2e8bec-4be9-4457-8a20-0dd654f8b9ff.png)





