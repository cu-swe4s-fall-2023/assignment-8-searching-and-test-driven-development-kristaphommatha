# Homework 9
## Data Presentation
![alt text](https://github.com/cu-swe4s-fall-2023/assignment-8-searching-and-test-driven-development-kristaphommatha/blob/main/data/Homework9.png?raw=true)<br>
CO2 emissions contribute greatly to global warming. Understanding the trends and correlations of CO2 emissions overtime allows us to predict CO2 emissions in countries and identify the largest contributors to these emissions in each country. In this report, the CO2 emissions of some North American countries are studied. <br>
### Figure A
Figure A shows the average temperature recorded every year from 1990 to 2020. The four countries shown, United States, Mexico, Canada, Guatemala, all show a slight increase in average temperature over the course of 20 years.<br>
### Figure B
Figure B shows the total emissions of each country over the same time span of 1990 to 2020. Both the United States and Mexico show an increase of emissions over time. Canada's emissions appear to increase then decrease, while Guatemala's emissions stay at a steady level throughout the years. The increase of emissions and average temperature over time in some of the countries may suggest positive relationship between CO2 emissions and average temperature.<br>
### Figure C
Figure C shows the total emissions vs. GDP of each country over the same 20 years. This figure shows a positive trend in total emissions and GDP. This figure shows an increase of both total emissions and GDP in all of the countries shown, which could suggest that as GDP increases, so does total emissions.<br>
### Figure D
Figure D shows GDP vs urban population with a colorbar representing total emissions. From the colorbar we can see that the United States has the highest GDP, urban population, and total emissions out of the four countries, which lines up with the data from Figure B and Figure C. <br>
### For next year
Given more time and access to data, I would also be interested in looking at the relationship between CO2 emissions and the autoindustry and oil & gas industries in these countries. I would expect a positive relationship between car manufacturing, car usage, and CO2 emissions.<br>

## Using Libraries
### dataFunctions.py
    collect_fire_years_data(file_name, country_col, country, target_stats)
Collects data about of target_stats about specific country in a file. Returns the data as a dataframe that also contains the years.<br>
file_name == name of file containing fires data<br>
country_col == string input for the name of the country column (In Agrofood_co2_emission.csv, country_col = "Area")<br>
country == string input for the country of interest<br>
target_stats == array of strings for the name of statistics to collect data about<br>
    
    destroy_commas(x)
Takes in a string containing numbers and commas and converts the string to a float.<br>
x == string input containing commas.

    clean_data(file_name)
Parses through a .csv file and replaces '...' and '-' with None values. Writes to a new .csv file titles CLEAN_file_name.<br>
file_name == name of file to be cleaned.

    get_fire_gdp_year_data(fires_file, gdp_file, country, target_stats)
Calls collect_fire_years_data with fires_file, country, and target_stats to return a dataframe about fires. Then, opens gdp_file and adds gdp data to the dataframe and returns the new dataframe.<br>
fires_file == file containing data about fires<br>
gdp_file == file contianing data about GDP<br>
country == country of interest<br>
target_stats == array of strings for the name of statistics to collect data about<br>

    find_total_range(df1, df2, df3, df4, target_stat)
Finds the overall minimum and maximum of a target_stat across 4 data frames. Returns the minimum and maximum as a tuple.<br>
df1, df2, df3, df4 == dataframes to parse through<br>
target_stat == string input for the stat of interest<br>

### data_plotting.py and snakemake
Produces the figure shown above as Homework9.png inside the data folder in main directory  from CLEAN_IMF_GDP.csv and Agrofood_co2_emission.csv. <br>

### cleaning_data.py (Inside data folder in main directory)
    python cleaning_data.py --f {file_name}
Takes user input for file_name and outputs a cleaned version of the file under CLEAN_file_name<br>

    
