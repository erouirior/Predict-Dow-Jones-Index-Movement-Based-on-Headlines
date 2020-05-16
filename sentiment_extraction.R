library(syuzhet)
news <- read.csv('combined_reddit_dj_2008_2020.csv')
news$movement[news$Label == 'Up'] <- 1
news$movement[news$Label == 'Down'] <- 0

news$tops<-do.call(paste, as.data.frame(news, stringsAsFactors=FALSE))
sentiment <- get_nrc_sentiment(as.character(news$tops))
sent <- cbind(news$Date,news$movement, sentiment)
colnames(sent)<-c('Date',"Movement","Anger", "Anticipation", "Disgust", "Fear", "Joy", "Sadness", "Surprise", "Trust", "Negative", "Positive")

write.csv(sent,'/Users/jeffreylu/Downloads/sentiment_2008_2020.csv',row.names=FALSE)