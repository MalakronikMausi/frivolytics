library(plyr)
library(dplyr)
library(reshape2)
library(tidyr)
library(stringr)

# Read in the rankings tables
setwd("~/Desktop/frivolytics/imdb/graphs")
files <- list.files(pattern="*.csv")
data_list <- lapply(files, function(x) { read.csv(x, header=TRUE, sep=',') })
data <- bind_rows(data_list)

# Read in metadata
setwd("~/Desktop/frivolytics/imdb")
metadata <- read.csv('stars_out.txt', header = TRUE, sep=';', quote='')
metadata[metadata == ""] <- NA
metadata <- metadata[c(2,4,5,6)] # Drop columns that won't be used in this analysis

# Bind metadata with rankings
tableau_data <- full_join(metadata,data)
tableau_data <- melt(tableau_data, id.vars = c("name","age","height","roles"))
tableau_data <- plyr::rename(tableau_data, c("variable"="date","value"="rank"))

#Drop empty entries
tableau_data <- tableau_data[!is.na(tableau_data$rank),]

#Drop all but the first role
tableau_data$roles <- gsub("\\|.*", "", tableau_data$roles)

#Format dates
tableau_data$date <- gsub("X1", "1", tableau_data$date)
tableau_data$date <- gsub("X2", "2", tableau_data$date)
tableau_data <- tableau_data %>% separate(date, c("year", "month", "day"), "\\.", remove=FALSE)

#Adjust age to match age at time of ranking
tableau_data$age <- tableau_data$age - (2018 - as.numeric(tableau_data$year))


write.table(tableau_data, file = "tableau_data.csv", sep = ",", row.names = FALSE)
