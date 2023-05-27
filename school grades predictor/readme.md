# Overview
The goal of this project is to predict student performance given various personal, familial, and academic attributes about a student. The end goal of this is to determine what factors are related to the success of students in school.

# Data
The data here came from UCI's Machine Learning Repository. It contains 33 attributes each about 144 students. Each instance represents an individual student's performance in one class, along with the relevant information about that student.

# Methods
This was approached as a classification problem. In the end, I split student's grades into two categories by drawing grade boundaries at a solid C. I then set out to predict whether or not a student scored a C or better in the class. The models I used were random forest classification, logistic regresison, and SVM. Ultimitely, I pick out a few attributes that proved most predictive of class performance and look at them.
