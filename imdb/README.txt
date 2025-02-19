Get metadata for IMDB top 1000:
- Sign up for trial IMDBPro account
- Go to https://pro.imdb.com/people?ref_=hm_reel_sm_all#sort=ranking (need pro account)
- Right click on table header and select Inspect
- Right click on div with id "results" and select Copy —> Copy Element
- Paste contents into file (starmeter.txt)
- Run parse_stars.py to extract data into a table (output: stars_out.txt)

Get ranking history for IMDB top 1000:
- Now this is the fun part… we're gonna use wget to pull all the data from each star's IMDB page, which includes their ranking history
- Because this info is only available with a pro account, we'll have to supply our credentials
- Add the cookies.txt extension to Chrome
- Navigate to imdb.com and make sure you're logged in
- Click on the cookies.txt extension icon and select the option to download the cookie for this tab; move the file to your working directory
- Run get_graph_data.sh, which will download the data into a directory called pro.imd.com (this will take awhile)

Process ranking history for IMDB top 1000:
- Run parse_graphs.py to extract a the ranking history of each star into a table (output: one csv file per star in the graphs directory)
- Now, we will combine the metadata and rankings data into one big table…
- Open stars.R in RStudio and modify the paths in lines 8 and 14
- Run the script (I do it line by line to make sure everything is going well)
- The output (tableau_data.csv) can be used to do some fun analyses

- Deactivate your IMDBPro trial so you don't get charged!

# Get the positions

Actor, Actress, Writer, Producer, Director