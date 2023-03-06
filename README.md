# Facial-Recoginition-By-Siamese-Neural-Network

## I. Introduction: 

This project is to implement facial recognition by siamese neural network for one shot image classification. Deep Convolutional Neural Networks have become the state of the art methods for image classification tasks. However, one of the biggest limitations is they require a lots of labelled data. In many applications, collecting this much data is sometimes not feasible. One shot learning aims to solve this problem. 
![](https://miro.medium.com/max/1400/1*g-561DsAfbU6gcVEk9AC4g.webp)

Siamese network takes two different inputs passed through two similar subnetworks with the same architecture, parameters, and weights. The two subnetworks are a mirror image of each other, just like the Siamese twins. Positive data pair is when both the inputs are the same, and a negative pair is when the two inputs are dissimilar.

### PaperLink: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf

![](https://miro.medium.com/max/1158/1*B7wXpu52WCYgVYz97zXhHA.jpeg)

## II. Project Tasks: 
1.  Collect and Prepare data.
2. Build Siamese neural network.
3. Training Siamese neural network
4. Test, evaluate and predict. 
5. Integrate it with kivy app. 

## III. Project Tools: 

Tensorflow, Keras, OpenCV, Kivy

## IV. Project Architecture:

![](https://bloglunit.files.wordpress.com/2017/05/siamese_nn.png?w=740)

## V. Output 

Precision | 1 |
--- | --- | 
Recall | 1 |

![Screenshot (8)](https://user-images.githubusercontent.com/97932221/217462987-72fa3c85-9558-4d01-ba01-26a7040c8aa4.png)

## VI. Conclusion: 

Siamese neural network model gave high accuracy for facial recognition, If you have Higher version or atleast Nvidia graphics card(GPU is used for Processing Image optimally and also at faster rate), Personal Idea(You can use pretrained model and fit input siamese twin image and siamese layer and train it if you have GPU available, as I have ryzen 5 CPU it took around nearly 2 days to train usage of pretrained model like vgg, inception, efficienet, etc to attain peak accuracy and efficient model for classification). 

Link for pretrained Model: https://keras.io/api/applications/ 

Happy Coding !!!
