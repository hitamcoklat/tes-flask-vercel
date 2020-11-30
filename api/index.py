from flask import Flask
from flask import jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(username="septiandwia hoho",
                    email="septiandwianugraH@gmail.com",
                    id="1")

@app.route('/user/bsp')
def get_detail_user():
    return jsonify(username="Bumi SUkagalih Permai",
                   email="bsp@gmail.com",
                   id="2")

@app.route('/scrape/python')
def get_scrape():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://selenium-python.readthedocs.io/locating-elements.html")
    
    textPage = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[5]/p[1]')
    textPage = textPage.text
    
    driver.close()

    return jsonify(msg=textPage)
