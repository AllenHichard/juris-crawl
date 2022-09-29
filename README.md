<h1 align="center">
📄<br>Courtroom Crawler
</h1>

<h1 align="center">
  <img src="image/spy.jpg">
</h1>

This system was developed to be able to search standard **CNJ** cases in Brazilian courts. Currently, it is able to process the states of **Alagoas** and **Ceará**, both in the first and second degree.

Courts where data will be collected:

- TJAL
  - 1º degree - https://www2.tjal.jus.br/cpopg/open.do
  - 2º degree - https://www2.tjal.jus.br/cposg5/open.do
- TJCE
  - 1º degree - https://esaj.tjce.jus.br/cpopg/open.do
  - 2º degree - https://esaj.tjce.jus.br/cposg5/open.do 

Were tested:

- **1347** lawsuits in the court of Alagoas
- **7842** lawsuits in the court of Ceará

Data to be collected:

- class
- area
- Subject
- distribution date
- judge
- action value
- parts of the process
- list of transactions (date, movement and complement)


## 💈 Installation

If you want to run the project locally, you will need to follow these steps:

- `clone`- run the following command in terminal or use your preferred IDE to clone.
  - git clone https://github.com/AllenHichard/crawler.git


- `libraries` - run the command below to install the libraries, use the cloned repository directory.
  - pip install -r requirements.txt
  

- `main` - run the main program file.
  - 'main.py' 

## 💻 ️Local API

The system has a local API, so you can test the local API by running the main.py file.

- `api link`- Get method was used for testing convenience, so no need to configure payloads or headers to run the application.
  - http://127.0.0.1:5000/api/consult/{{cnj}}

- `example` - Algorithm will accept full cnj patterns (25 characters) or just numbers (20 characters)
  - http://127.0.0.1:5000/api/consult/00703379120088060001
  - http://127.0.0.1:5000/api/consult/0070337-91.2008.8.06.0001


## ☑️How to test the robot?

- run the file **pdf/general.py**.
  - General.py reads two documents from the official journal (Alagoas and Ceará), and applies a parser to capture the cnj numbers and then runs the crawler on the processes collected from the pdf;
- run the file **main.py**.
  - Will run the api made with flask

## ☑️ comments

- The system is in its MVP version;
- The system is not free of flaws, as eventualities may arise that did not arise in the test, but the algorithm is easily editable to capture data from the courts in question;
- The crawler has been tested with more than 9000 processes, running the pdf/general.py file, it will parser and capture the processes and run the system for each of the processes found

