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

### Start working in Jupyter
```
cd notebooks
jupyter notebook
```

---

```bash
(plotlydash) 
my_repos/data-umbrella-projects/data-umbrella-sprints-dashboard  main ✗                               22m ⚑  
▶ 
```
