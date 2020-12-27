#!/usr/bin/python

import ctypes
import numpy
import cv2




def main():
    TestLib = ctypes.cdll.LoadLibrary('./OV580Lib/Release/libOV580Lib.so')
    
    image_array = numpy.zeros((800,1280,1),numpy.uint16)

    class OV580_Handle(ctypes.Structure):
        _fields_ = [("impl", ctypes.c_void_p)]
    impl=0
    handle = OV580_Handle(impl)
	
    TestLib.openOV580Camera(ctypes.byref(handle))
	
    print( "Python: camera started")
	
	#Processing Loop:
    for i in range(0,100):
        TestLib.OV580Camera_getCamImage(ctypes.byref(handle),numpy.ctypeslib.as_ctypes(image_array))
        cv2.imshow("Test",image_array)
        cv2.waitKey(1)
        print(i)

    TestLib.closeOV580Camera(ctypes.byref(handle))
    print ("Python: camera closed")

if __name__ == '__main__':
        main()
