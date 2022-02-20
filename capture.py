import os
import cv2
import time
'''press q to quit the script
    press w to save a picture at any time
'''
image_prefix = 'two{}.jpg'
location = os.path.join(os.getcwd(), 'captureimage')


def save_img(location, img):
    name = os.path.join(location, image_prefix.format(time.time()))
    print(name)
    cv2.imwrite(name, img)


def capture():
    # import the opencv library
    import cv2

    # define a video capture object
    vid = cv2.VideoCapture(0)

    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('w'):
            save_img(location, frame)
            print('saved..')

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture()
