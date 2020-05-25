from color_text import *

initColorIt()

def details_block(data_block):
    deaths = data_block['TotalDeaths']
    confirmed = data_block['TotalConfirmed']
    recovered = data_block['TotalRecovered']
    total_active = confirmed - recovered

    print("Total number of dead is : ", color(deaths, colors.RED))
    print("Total number of confirmed is : ", color(confirmed, colors.BLUE))
    print("Total number of recovered is : ", color(recovered, colors.GREEN))
    print("Total number of active is : ", color(total_active, colors.PURPLE))