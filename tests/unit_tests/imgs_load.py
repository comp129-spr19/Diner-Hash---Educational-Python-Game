import unittest

from os import (
    listdir
)

from pygame import (
    image
)

def isValidImgFile(filename):
    return filename.endswith(".jpg") or filename.endswith(".png")

class TestImagesLoad(unittest.TestCase):
    """
    Test if all images in the imgs directory load correctly

    NOTE: load paths start from the root project directory
    """

    def test_imgs_dir(self):
        print("")
        print("Testing validity of images in img/ directory")
        load_path = "./imgs/"
        for filename in listdir(load_path):
            if isValidImgFile(filename):
                img = image.load(load_path + filename)
                print("assert " + filename + " is loaded")
                self.assertTrue(img is not None)

    def test_imgs_loading_screens_dir(self):
        print("")
        print("Testing validity of images in img/loading_screens/ directory")
        load_path = "./imgs/loading_screens/"
        for filename in listdir(load_path):
            if isValidImgFile(filename):
                img = image.load(load_path + filename)
                print("assert " + filename + " is loaded")
                self.assertTrue(img is not None)
    
if __name__ == '__main__':
    unittest.main()
