from technique import NonAlteringTechnique
import cv2
import numpy as np

class gausianBlurringAugmentationTechnique(NonAlteringTechnique):

    # Valid values for kernel are 3,5,7,9, and 11
    def __init__(self,parameters):
        NonAlteringTechnique.__init__(self, parameters)
        if 'kernel' in parameters.keys():
            self.kernel = int(parameters["kernel"])
        else:
            self.kernel = 3
        if (not (self.kernel in [3,5,7,9,11])):
            raise NameError("Invalid value for kernel")

    def apply(self, image):
        blurred = cv2.GaussianBlur(image, (self.kernel, self.kernel),0)
        return blurred