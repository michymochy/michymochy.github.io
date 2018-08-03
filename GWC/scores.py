##import school_scores
##list_of_record = school_scores.get_all()
##
##averages = []
##
##for record in list_of_record:
##    math_score = record["Gender"]["Male"]["Math"]
##    average.append(math_score)
##print(averages)
##sum(averages)


import airlines
import numpy as mp
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
list_of_airline = airlines.get_reports()
with plt.rc_context({'axes.edgecolor':"#bf4080", 'xtick.color':"#bf4080", 'ytick.color':"#bf4080"}):

    whoosh = []

    for fly in list_of_airline:
        sf = fly["Statistics"]["# of Delays"]["Security"]
        whoosh.append(sf)
    print(whoosh)

    plt.hist(whoosh, bins = 10, color = "#ff8080", edgecolor = "#ff6666")
    plt.xlim ([0,50])

    plt.title("Statistics of Airplanes", color ="#bf4080")
    plt.xlabel("# of Delays", color = "#bf4080")
    plt.ylabel("Security Delays", color = "#bf4080")
    plt.show()   

