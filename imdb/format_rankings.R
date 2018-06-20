library(plyr)
library(dplyr)
library(reshape2)
library(tidyr)
library(stringr)

# Read in the rankings tables
setwd("~/Desktop/frivolytics/imdb/graphs")
files <- list.files(pattern="*.csv")
data_list <- lapply(files, function(x) { read.csv(x, header=TRUE, sep=',') })
ranking_data <- bind_rows(data_list)

# Melt rankings
ranking_data <- melt(ranking_data, id.vars = c("name"))
ranking_data <- plyr::rename(ranking_data, c("variable"="date","value"="rank"))

# Drop empty entries
ranking_data <- ranking_data[!is.na(ranking_data$rank),]

# Format dates
ranking_data$date <- gsub("X1", "1", ranking_data$date)
ranking_data$date <- gsub("X2", "2", ranking_data$date)
ranking_data <- ranking_data %>% separate(date, c("year", "month", "day"), "\\.", remove=FALSE)

# Create condensed version by aggregating data to max ranking per month
ranking_data_agg <- aggregate(rank ~ name + year + month, ranking_data, min)

# Read in metadata
setwd("~/Desktop/frivolytics/imdb")
metadata <- read.csv('metadata_out.csv', header = TRUE, sep=';', quote='')
metadata[metadata == ""] <- NA
metadata <- metadata[c(2:ncol(metadata))] # Drop columns that won't be used in this analysis

# Create table with metadata and ranking info
all_data <- full_join(metadata,ranking_data) # Bind metadata with rankings
all_data$age <- all_data$age - (2018 - as.numeric(all_data$year)) #Adjust age to match age at time of ranking
write.table(all_data, file = "ranking_data_full.csv", sep = ",", row.names = FALSE)

# Do the same with the aggregate rankings
agg_data <- full_join(metadata,ranking_data_agg) # Bind metadata with rankings
agg_data$age <- agg_data$age - (2018 - as.numeric(agg_data$year)) #Adjust age to match age at time of ranking
write.table(agg_data, file = "ranking_data_agg.csv", sep = ",", row.names = FALSE)


