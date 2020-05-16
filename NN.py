from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
import pandas as pd
from sklearn.model_selection import train_test_split


sentiment = pd.read_csv('/Users/jeffreylu/Downloads/sentiment_2008_2020.csv')
sentiment.drop('Date',axis=1,inplace=True)


x_train, x_test, y_train, y_test = train_test_split(sentiment.loc[:, sentiment.columns != 'Movement'], \
                                                    sentiment['Movement'], test_size=0.2)


model = Sequential()

model.add(Dense(8,input_dim=10,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train,y_train,epochs=20,batch_size = 50,validation_data=(x_test,y_test),shuffle=True)
