# Read in metadata
setwd("~/Desktop/frivolytics/imdb")
metadata <- read.csv('stars_out.txt', header = TRUE, sep=';', quote='')
metadata[metadata == ""] <- NA


all_roles <- data.frame(matrix(ncol = 100, nrow = nrow(metadata)))
all_roles[,] <- FALSE
colnames(all_roles) <- list(rep("",100))

lapply(1:nrow(metadata)), function(x){
  roles <- strsplit(as.character(metadata[x,'roles']),'|',fixed=TRUE)
  lapply(roles, function(x) {
    if (!(x %in% colnames(all_roles))) {
      all_roles
    }
  })
})