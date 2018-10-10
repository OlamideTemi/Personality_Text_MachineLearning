##Written in python 3

#Librariess for analysis
import pandas as pd
import numpy as np
from sklearn import svm,knn

#Libraries for visuals
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale =1.2)

#Read in data
#text = pd.read_csv('path\name.csv')
#text.head()

#plot two features
#sns.lmplot('first_feature', 'second_feature', data = text, hue = 'Type',palette = 'Set1', fit_reg = False,scatter_kws ={"s": 70})

#Specify inputs for the model
#feature_list= text[['first_feature', 'second_feature']].as matrix()
#type_label = np.where(text['Type']=='Neurotic',0,1)

#Fit the SVM model
#model = svm.SVC(kernel = 'linear')
#model.fit(feature_list, type_label)

#Get the separating hyperplane
#w = model.coef_[0]
#a = -w[0]/w[1]
#xx = np.linspace(5,30)
#yy = a* xx - (model.interpret_[0])/w[1]

#Plot the parallels to the separating hyperplane that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a*xx + (b[1] - a*b[0])
b = model.support_vectors_[-1]
yy-up = a*xx + (b[1] - a * b[0])

#Look at the margins and support vectors
sns.lmplot('first_feature', 'second_feature',data = text, hue = 'Type',palette = 'Set1', fit_reg = False,scatter_kws ={"s": 70})
plt.plot(xx,yy, linewidth = 2, color = 'black')
plt.plot()
plt.plot()
plt.scatter()

#Plot the hyperplane
sns.lmplot(('first_feature', 'second_feature',data = text, hue = 'Type',palette = 'Set1', fit_reg = False,scatter_kws ={"s": 70})
plt.plot(xx,yy, linewidth = 2, color = 'black')

#Predict a new case
#Plot the point to see where the point lies visually
sns.lmplot('first_feature', 'second_feature',data = text, hue = 'Type',palette = 'Set1', fit_reg = False,scatter_kws ={"s": 70})
plt.plot(xx,yy, linewidth = 2, color = 'black')
plt.plot(12,12,'yo',mmarkersize='9')
     
