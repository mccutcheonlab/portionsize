filename <- commandArgs(trailingOnly=TRUE)

df <- read.csv(filename)

library(ez)

analysis <- ezANOVA(data=df,dv=value,wid=rat,within=amountgiven,type=3)

print(analysis)