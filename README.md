# sprints-dashboard
Data Umbrella Open Source Sprints Dashboard

Prep work:  https://github.com/Vancouver-Datajam/dashboard-workshop-dash#setup-prep

## Starting
The layouts for the dashboard were cloned from:  
https://github.com/Vancouver-Datajam/dashboard-workshop-dash

## Conda virtual environment instructions

### Clone the dashboards repo
```
git clone https://github.com/Vancouver-Datajam/dashboard-workshop-dash.git
cd dashboard-workshop-dash/
```

### Set up virtual environment using `conda`
[requirements.txt](https://github.com/Vancouver-Datajam/dashboard-workshop-dash/blob/main/requirements.txt)

#### This didn't work
```bash
# create virtual environment with name "plotlyenv"
conda create -n plotlyenv python=3.9

# activate the virtual environment
conda activate plotlyenv

# install the dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

### Initial graphs were done in Jupyter
```
cd notebooks
jupyter notebook
```

### Use VSCode for development work

```bash
(plotlydash) 
my_repos/data-umbrella-projects/data-umbrella-sprints-dashboard  main ✗                               22m ⚑  
▶ 
```

```
my_repos/data-umbrella-projects/data-umbrella-sprints-dashboard  try_tab2 ✔                              2m  
▶ cd scripts
(plotlydash) 
data-umbrella-projects/data-umbrella-sprints-dashboard/scripts  try_tab2 ✔                               2m  
▶ ls
README.md                 app_1_pie_afme_example.py app_4_try_map_afme.py     old_examples
__init.py__               app_2_bar_afme_example.py app_ter_help.py
app.py                    app_3_funnel_afme.py      app_try_tabs.py
(plotlydash) 
data-umbrella-projects/data-umbrella-sprints-dashboard/scripts  try_tab2 ✔                               2m  
▶ python app.py
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```

#### Testing App
[http://127.0.0.1:8050/](http://127.0.0.1:8050/)

### References
- [tabs on page](https://dash.plotly.com/dash-core-components/tabs)