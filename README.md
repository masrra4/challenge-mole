# challenge-mole

Repository: challenge-mole
Type of Challenge: Consolidation
Duration: 8 days
Deadline: 24/05/2022 4:30 (code)
Presentation: 25/05/2022 1:30 PM
Challenge: Solo
contributer:Masrra

The most reason of cancer mole is exposure to the sun .

#Steps to do the project:
1-importlibraries and metadata.
2-Build a mapping between image ids and types of cancer.
3-get the images and clean it .
4-Determin X and y(x is the pixells of the images and y is the types of the cancer)
5-label y from (0 to 6)because we have 7 types of the cancer.
6-Split the data to x_train,x_val,x_test,y_train,y_val,y_test.
7-import the model Resnet50.
8-set the input shape of the model to 224x224 pixels, with 3 color channels.
9-Freeze the imported layers so they cannot be retrained. 
10-Adding flattering and dense layers.
11-Compile and fit the model.
12-save the model.
13-plot the training and the accuracy of the model.
14-Build the app to detect the type of the cancer.


#How to Build the app .
1- import the necessary libraries like(flask,request,render_template)
2-put the name of the app 
3-load the model 
4-get the images and clean them 
5-Convert your image pixels to a numpy array of values .
6-Reshape your image dimensions so that the colour channels correspond to what your model expects.
7-Preprocess your image with preprocess_input.
8-Apply the model and get the prediction.
9-Show the prediction to the user.
10-pass the information from python file to the html file.

