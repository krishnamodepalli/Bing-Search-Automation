
# Bing Search Automation

This is a simple python selenium browser automation project, which is solely 
developed for making the process of earning bing reward points easier and 
quicker.

## Usage:

### Installation
> We highly recommend you using a virtual-env for this project separately
```bash
git clone git@github.com:/krishnamodepalli/Bing-Search-Automation.git
cd Bing-Search-Automation/
pip3 install -r requirements.txt      # install the requirements for python
python3 main.py                       # relax, the rest is taken care...
```

### Running the script
You can modify some of the settings like no. of searches and the browser to 
open in the script itself.  

Please kindly refer to the `app_configurations` in `main.py:54` for script 
setting like no. of searches and chrome profiles and browser paths.

#### For Chrome & Brave
> **We highly recommend you reading this before working with chrome in our 
> project.**

Working with chrome had become an issue since the start of this project. 
Working with various chrome profiles and keeping the bing (Microsoft) 
Account logged in and having the browser history saved, all this was a big 
trouble in the start. To solve this issue, we can create an empty chrome 
profile and start the browser in the `remote-debugging-mode` and then attach 
our selenium driver to the browser. This way, we can store the new chrome 
profile data and also match our requirement.

It is recommended that you create a new folder anywhere in your 
drive and assign this as the new chrome profile for the chrome and then 
modify the setting in the `app_configurations`

> These setting configurations will be made easier and simpler in the 
> upcoming releases.

#### Types of searches
There are 2 types of searches provided with the bundle, one is just a simple 
one with a lot of keywords in a single file and randomly searching those 
keywords, Or You can have a [`NEWS-API`](https://newsapi.org)'s API_KEY and 
provided it with the configuration of the app, you will be searching the 
latest news on the internet in the bing searches.


### Compatible browsers
1. Edge
2. Chrome
3. Brave

Will be adding support to other browsers as well soon.

> Disclaimer: This project is still under-developed and works well with above
> specified browsers  
> ***Note**: This project is safe to use and is completely working well.*

## TODO:
- [ ] Convert this python script into a fully functioning console automation 
  script
- [ ] Enable customization of configurations with local user level config files
- [ ] Add command-line arguments and flags for run-time configuration settings
- [ ] Adding profiles for the configurations and settings, for more than one 
  use-cases and more than one bing accounts
- [ ] Add clear documentation for the project
