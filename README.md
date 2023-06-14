# Embedding-a-Machine-Learning-Model-in-A-Web-Applications
This is project that throws lights on the method of developing a web application for machine learning models


<img alt="Sepsis Prediction Project" src="sepsis.jpg"> </img>

# Introduction/Project Description 🎰

Sepsis is the body's extreme response to an infection. The use of AI and machine learning in disease prediction is very useful to the modern health industry since early prediction/ detection of disease is instrumental in avoid certain unseen bad events with patients. This project describes the use of machine learning to build a model that predict the sepsis status of a patient. The model is built on a historic patient data with identified sepsis status.
# Knowledge On Dataset 👨🏽‍💻
The datasets has ten features about a patient as seen below, including the sepsis feature that classifies a person with sepsis or not
- [ID: number to represent patient ID]
- [PRG: Plasma glucose]
- [PL: Blood Work Result-1 (mu U/ml)]
- [PR: Blood Pressure (mm Hg)]
- [SK: Blood Work Result-2 (mm)]
- [TS: Blood Work Result-3 (mu U/ml)]
- [M11: Body mass index (weight in kg/(height in m)^2]
- [BD2: Blood Work Result-4 (mu U/ml)]
- [Age: patients age (years)]
- [Insurance: If a patient holds a valid insurance card]
- [Sepsis: Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise]

# Project Method and Setup 🚀
Install the required packages to be able to run the evaluation locally. All recommended packages are in the requirement.txt file

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**):

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol ` ; ` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI

- Run the demo apps:
        
  FastAPI:
    
    - Demo

          uvicorn main:app --reload 

    <!-- - Sepsis prediction

          uvicorn main:app --reload  -->


  - Go to your browser at the following address, to explore the api's documentation :
        
      http://127.0.0.1:8000/docs
## Resources
Here are some ressources you would read to have a good understanding of FastAPI :
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)

# Conclusion
Machine learning is useful in solving real life problems in the world. Sepsis prediction project is useful for early detection of patient's sepsis status. Kindly reach out for contribution 

#### Author
Winifred Kwakye
