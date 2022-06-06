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
1. Clone project: <br>
```git clone https://github.com/marijamilanovic/DSL```
2. Open a terminal as admin and create a virtual environment (for example 'env') <br>
```python -m venv <envName>```
3. Afterwards, activate created virtual environment
   - For Linux: 
    ```source env/bin/active```
   - For Windows:
     ```env\Scripts\activate.bat```
4. Change directory <br>
```cd DSL/menuDSL```
5. Install Python packages from requirements file <br>
```pip install -r requirements.txt```
6. You can check registered languages and generators <br>
``` textx list-languages``` <br>
``` textx list-generators```
7. Create database.ini file: <br>
```
[postgresql]
host=127.0.0.1
database=jsd
user=postgres
password=root
```
and in PostgreSQL create database with name 'jsd' <br>
8. Run script <br>
``` python connect.py```
9. Generate html and pdf <br>
```textx generate example.fdm --target html+pdf```
10. To deactivate virtual environment type <br>
```deactivate```

### Example
![Screenshot 2022-06-06 104045](https://user-images.githubusercontent.com/57723883/172127023-aa529436-5cc6-4b95-a5f1-f4e3f38106dd.png)






