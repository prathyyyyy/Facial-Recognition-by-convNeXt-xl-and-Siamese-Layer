llt# Facial-Recognition-By-Siamese-Neural-Network and Convnext XL pretrained Model

## I. Introduction: 

One-shot learning aims to solve the problem of requiring a lot of labeled data for image classification tasks. This project will leverage one-shot learning using Convnext XL and Siamese layers. ConVNeXt XL is a recently proposed CNN architecture that has been shown to be very effective for image classification tasks. Siamese layers are used to measure the similarity between two images. The Siamese network will be trained to minimize the contrastive loss between images of the same class and maximize the contrastive loss between images of different classes. 

- The project will leverage one-shot learning using Convnext XL and Siamese layers.
- ConVneXt XL is a recently proposed CNN architecture that has been shown to be very effective for image classification tasks.
- Siamese layers are used to measure the similarity between two images.
- The Siamese network will be trained to minimize the contrastive loss between images of the same class and maximize the contrastive loss between images of different classes.

![](https://miro.medium.com/max/1400/1*g-561DsAfbU6gcVEk9AC4g.webp)

The ConvNeXt Xl + siamese layer takes two different inputs passed through two similar subnetworks with the same architecture, parameters, and weights. The two subnetworks are a mirror image of each other, just like the Siamese twins. Positive data pair is when both the inputs are the same, and a negative pair is when the two inputs are dissimilar.

### PaperLink: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf

![](https://miro.medium.com/max/1158/1*B7wXpu52WCYgVYz97zXhHA.jpeg)

## II. Project Tasks: 
1.  Collect and Prepare data.
2. Build a ConvNeXt XL and Siamese layer.
3. Training pretrained model with siamese layer
4. Test, evaluate, and predict. 
5. Integrate it with the kivy app. 

## III. Project Tools: 

Tensorflow, Keras, OpenCV, Kivy

## IV. Project Architecture:

![](https://bloglunit.files.wordpress.com/2017/05/siamese_nn.png?w=740)
### ConvNexT XL architecture: 
![image](https://github.com/prathyyyyy/Facial-Recognition-by-siamese-neural-network/assets/97932221/301bfe8b-5c1e-4e2d-8881-c31dabf66ba1)



## V. Output 

Precision | 0.99 |
--- | --- | 
Recall | 0.985 |

![Screenshot (8)](https://user-images.githubusercontent.com/97932221/217462987-72fa3c85-9558-4d01-ba01-26a7040c8aa4.png)

## VI. Conclusion: 

I utilized the ConvNextXL + siamese layer for my project, resulting in high precision and recall values. Impressively, it only took 15 epochs to achieve these results. To aid in training the heavy image processing model, I employed the use of the NVIDIA Tesla P100 GPU, which allowed for faster processing time. In the near future, I plan to update my code to include YOLO V8 or Nas for live tracking of facial objects. For more information on the updated pretrained model, please refer to the Keras documentation.

Link for pretrained Model: https://keras.io/api/applications/ 

Happy Coding !!!
