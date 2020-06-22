## BOOKINGS CANCELLATION PREDICTION

About the Project
-----------------
This project is created as final assignment to fullfil the requirements tograduate from Job Connector DataScience Program in Purwadhika Digital
School. I use machine learning classification model to predict hotel bookings cancellation in Resort and City Hotel in Portugal.

Research Background
-----
Hotels are vulnerable to demand and cancellation uncertainty (Chen et al., 2011).
This can lead to sudden increases and decreases in pickup which is why hotel revenue managers -within the context of
regular booking patterns -tend to closely monitor the booking pace at both total and segmented level.

Based on 240,000 booking records, Morales and Wang (2010) find that several guest-, booking-and room-specific characteristics
are relevant in forecasting cancellation rates. Antonio, de Almeida, and Nunes (2017) show that booking channel, arrival month, room type, booking lead time, and country of origin are the most important predictors.

Dataset
----
The dataset contains data from two different hotels. One Resort hotel and one City hotel.

From the publication (https://www.sciencedirect.com/science/article/pii/S
2352340918315191) we know that both hotels are located in Portugal (southern Europe).

The data contains "bookings due to arrive between the
1st of July of 2015 and the 31st of August 2017". The data also contains 32 features with total 119,390
bookings that need to be selected and cleaned.

Research Problem & Motivation
----
The aim of this research project is to predict whether a guest of Resort and City Hotel in
Portugal will cancel the booking and identify the variables that influence this activity. This
project has the potential to improve cancellation policy, cost efficiency, and
revenue maximization efforts relating to hotels in Portugal.

Determining whether and why a guest maycancel the booking is a challenging and
imperfect science. Our interpretable modelswill be correlational and cannot pinpoint causality.

Model
-----
I compare 3 machine learning models in this project, those are Logistic Regression, K-Nearest Neighbors, and Random Forest Classifier. Then I find the best default model is Random Forest Classifier, so I tuned the model with GridSearchCV but turned out, the deafult model is slightly better than the tuned one. So, I pick the default model as our prediction model. Here is the score of the model:

| Recall Score | f1-Score |
|--------------|----------|
|        0.836 |    0.846 |

Dashboard
---
#### 1. Home
![alt text](https://github.com/rifkimputra/FINAL_PROJECT/dashboard/static/images/home.png "Dashboard Home")
