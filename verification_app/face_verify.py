# Kivy Dependencies
# Import UI/UX components

import tensorflow as tf
import cv2
import os
import numpy as np
from layers import L1Dist
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger


class CamApplication(App):


    def build(self):
        # Main Layout Components
        self.web_cam = Image(size_hint=(1,.8))
        self.button = Button(text="Verify",on_press= self.verify ,size_hint=(1,.1))
        self.verification_label = Label(text="Verification Uninitiated",size_hint=(1,.1))

        # Add Items to layout
        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)


        # Video Capture
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update,1.0/33.0)

        return layout
    # Run Continuously to get webcam feed
    def update(self,*args):
        # Open and read from Open CV
        ret, frame = self.capture.read()
        frame = frame[30:40 + 240, 300:550,:]

        # Flip Horizontal and convert image to texture
        buf = cv2.flip(frame,0).tostring()
        img_texture = Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt="bgra")
        img_texture.blit_buffer(buf,colorfmt="bgr",bufferfmt="ubyte")
        self.web_cam.texture = img_texture
    # Preprocess Function
    def preprocess(self,file_path):
            byte_img = tf.io.read_file(file_path)
            img = tf.io.decode_jpeg(byte_img)
            img = tf.image.resize(img, (105, 105))
            img = img / 255.0
            return img

    # Validate Function to verify person
    def verify(self,*args):
        detection_threshold = 0.99
        verification_threshold = 0.8

        # Capture Input image from webcam
        SAVE_PATH = os.path.join("application_data","input_images","input_images.jpg")
        ret,frame = self.capture.read()
        frame = frame[30:40 + 240, 300:550,:]
        cv2.imwrite(SAVE_PATH,frame)
        # Load Tensorflow model
        self.model = tf.keras.models.load_model('siamesemodel.h5',custom_objects={'L1Dist': L1Dist})

        # Build results array
        results = []
        for image in os.listdir(os.path.join('application_data', 'verification_images')):
            input_img = self.preprocess(os.path.join('application_data', 'input_images', 'input_images.jpg'))
            validation_img = self.preprocess(os.path.join('application_data', 'verification_images', image))

            # Make Predictions
            result = self.model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
            results.append(result)

        # Detection Threshold: Metric above which a prediciton is considered positive
        detection = np.sum(np.array(results) > detection_threshold)

        # Verification Threshold: Proportion of positive predictions / total positive samples
        verification = detection / len(os.listdir(os.path.join('application_data', 'verification_images')))
        verified = verification > verification_threshold


        # Set Verification Text
        self.verification_label.text = "Verified" if verified == True else "Unverified"

        # Log out Details
        Logger.info(results)
        Logger.info(detection)
        Logger.info(verification)
        Logger.info(verified)

        return results, verified

        # Log out Details



if __name__ == "__main__":
    CamApplication().run()





