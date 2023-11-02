[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WSoIsN1S)
# tdd_searching
Searching with Test Driven Development

## fire_gdp library
    get_data(file_name, query_column, query_value, header=True)
*file_name == name of file to get data from <br>
query_column == column index to search in data file <br>
query_value == value to search for in query column<br>
header == includes list of header titles as the first element in return list<br>*
Searches through file for data in query_column that matches query_value.<br>
When the query is found, the row is stored as a list. Returns a list of all rows where the query was found.

    search(list, key)
*list == list to search through<br>
key == value to find in list<br>*
Searches through a given list for key value. Returns a list of indexes in the list where key is found.

    splitter(string, delimiter1, delimiter2)
*string == string to split<br>
delimiter1 == 'higher priority' delimeter<br>
delimeter2 == 'lower priority' delimeter<br>*
Splits a string that contains 2 delimeters, where one is higher priorty and the other is a lower priority.<br>
The low priority will not split the string if it is wrapped between two high priority delimeters, but will split the string otherwise.<br>
For example test,test2,"test,3",test4 will be split as test|test2|test,3|test4<br>
Returns a list of split values

    string_with_comma_to_float(string)
*string == string to convert*<br>
Used for for string representation of floats contain commas (i.e. 1,000,000)<br>
Removes comma from string and then converts it to a float. Returns float value.

    get_fire_gdp_year_data(fires_file, gdp_file, target_country, target_column, year_col)
*fires_file == file containing fires data<br>
gdp_file == file containing GDP data<br>
target_country == country to grab data about in fires_file<br>
target_column == index in fires_file of column with wanted data<br>
year_col == index in fires_file that contain data about the years<br>*
Takes two files where one contains data about fires in countries and the other contains data about country GDPs.<br>
Uses get_data to find the rows containing data about target_country in fires_file and gdp_file.<br>
Uses search to find relevant year in the data from fires_file and grabs information in gdp_file from the corresponding year.<br>
Returns tuple of fire data, gdp data, and corresponding years

    write_to_file(out_file, datas)
*out_file == name of file to output<br>
datas == tuple containing parallel lists*
Takes a tuple containing parallel lists such as the tuple output from get_fire_gdp_year_data.<br>
Writes data to a file, where each entry is delimited by commas. Each has one value from each parallel list.

## Snakemake Presentation
Snakefile is located in the main data directory. Running "snakemake --cores all" will generate: Canada.png, France.png, and Germany.png.
All .png files are scatter plots of the Country's GDP vs Savanna Fires for any given year

### Canada
![alt text](https://github.com/cu-swe4s-fall-2023/assignment-8-searching-and-test-driven-development-kristaphommatha/blob/main/data/Canada.png?raw=true)<br>
**Results**: This graph is skewed very much to the left. This suggests that Canada's Savanna Fires frequency tends to be low compared to its GDP for any given year.<br>
There is one outlier with a very high Savanna Fire count and relatively low GDP.

### France
![alt text](https://github.com/cu-swe4s-fall-2023/assignment-8-searching-and-test-driven-development-kristaphommatha/blob/main/data/France.png?raw=true)<br>
**Results**: This scatter plot is very spread out, which suggests that there is no strong correlation between France's GDP and Savanna Fires frequency.<br>
Compared to Canada, however, its x-axis is on a much smaller scale and its y-axis is on a relatively similar scale. This shows that despite having similar GDP ranges, France still experiences much less Savanna fires. This makes sense, considering France's and Canada's differences in geographic features. 

### Germany
![alt text](https://github.com/cu-swe4s-fall-2023/assignment-8-searching-and-test-driven-development-kristaphommatha/blob/main/data/Germany.png?raw=true)<br>
**Results**: Germany's scatter plot also appears to be skewed to the left, and its x-axis is orders of magnitude smaller than both France and Canada. It's y-axis scale is larger than France and Canada's, which shows that Germany has a higher range of GDP throughout the years and a very low proportion of Savanna fires. Considering Germany's geographic features and size compared to Canada, these numbers make sense. 

#### Methods
All figures were generated using make_data.py, which uses the get_fire_gdp_year_data and write_to_file functions from the fire_gdp library in order to generate .csv files containing<br>
savanna fire and GDP data with the corresponding years. Ths .csv files were then passed into scatter.py to generate the images.
