import pandas as pd
import numpy as np

def problem1(fname):
    return   pd.read_csv(fname, 
                          compression="gzip", 
                          header=None)

def _problem2(fname, skiprows=0, numrows=None):
    return pd.read_csv(fname,
                       compression="gzip", 
                       nrows=numrows,
                       skiprows=skiprows,
                       header=None)

def problem2():
    yob1983_female = _problem2("yob1983.txt.gz", 
                               numrows=12064)
    yob1983_male = _problem2("yob1983.txt.gz", 
                             skiprows=12064)

    yob1883_female = _problem2("yob1883.txt.gz", 
                               numrows=1054)
    yob1883_male = _problem2("yob1883.txt.gz", 
                             skiprows=1054)
    return yob1883_female, yob1883_male, yob1983_female, yob1983_male

def problem3(names1, names2):
    return (len(set(names2[0]).intersection(set(names1[0]))
               ),
           len(set(names2[0]).intersection(set(names1[0])))/\
               len(set(names2[0]).union(set(names1[0]))))

def problem5(name, census_names):
    return name in census_names[0].values

def problem6(fname):
    names = pd.read_csv(fname, compression="gzip", header=None)
    male = names[names[1]=="M"]
    female= names[names[1]=="F"]
    return female, male

def problem7(fname):
    names = problem1(fname)
    female, male = problem6(fname)
    mf_names = set(female[0]).intersection(male[0])
    return names[names[0].isin(mf_names)]

def problem8(fname):
    return pd.read_html(fname, header=None)[0]
