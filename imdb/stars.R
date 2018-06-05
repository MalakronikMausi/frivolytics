library(plyr)
library(dplyr)
library(reshape2)
library(tidyr)
library(stringr)

setwd("~/Desktop/rand/Frivolytics/graphs")
files <- list.files(pattern="*.csv")
data_list <- lapply(files, function(x) { read.csv(x, header=TRUE, sep=',') })
data <- bind_rows(data_list)

setwd("~/Desktop/rand/Frivolytics")
metadata <- read.csv('stars_out.csv', header = TRUE, sep=',')
metadata <- metadata[c(2,4,5)]
metadata[metadata == "&nbsp;"] <- NA

all_data <- full_join(metadata,data)
all_data <- melt(all_data)
all_data <- rename(all_data, c("variable"="date","value"="rank"))
all_data$date <- gsub("X1", "1", all_data$date)
all_data$date <- gsub("X2", "2", all_data$date)
all_data <- all_data %>% separate(date, c("year", "month", "day"), "\\.", remove=FALSE)

write.table(all_data, file = "all_data.csv", sep = ",", row.names = FALSE)
