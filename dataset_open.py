import numpy as np
import cv2
import time
from glob import glob
from natsort import natsorted


#3rd_person

DATASET = "/home/bencevic/Desktop/out"

# images = np.load("_out/dataset0.npy")
file_names = glob(f'{DATASET}/dataset*')
file_names = natsorted(file_names)
file_names = file_names[:17]
arrays = [np.load(f) for f in file_names]
images = np.concatenate(arrays)
del arrays
print(images.shape)

# angle = []
# with open(f"{DATASET}/data.txt") as file:
#     for line in file:
#         angle.append(float(line.split(",")[1]))

# for index in range(1, len(angle)-5):
#         angle[index] = (angle[index-1] + angle[index - 2] + angle[index+1] + angle[index + 2] + angle[index])/5.0

# wheel = cv2.imread('/opt/carla-simulator/PythonAPI/examples/steering_wheel_image.jpg', 0)
# rows, cols = wheel.shape

#counter = 0


for i, img in enumerate(images):
   cv2.imwrite(f"/home/bencevic/Desktop/out/{i}.png", img)


# while cv2.waitKey(23) != ord('q'):


#     frame = images[counter]
#     cv2.imshow("frame", frame)
#     #cv2.imwrite(f"{counter}.png", frame)
#     # real_angle = angle[counter] * 520

#     # print(f"FRAME: {counter} \tGROUND TRUTH: {round(real_angle, 2)}")

#     # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), - real_angle, 1)
#     # dst = cv2.warpAffine(wheel, M, (cols, rows))
#     # cv2.imshow("Ground Truth", dst)

#     # if counter == 10:
#     #     cv2.imwrite(f"{counter}.png", frame)
#     #     print("Saved")


#     counter += 1
#     if counter >= len(images):
#         print("Done.")
#         break

# cv2.destroyAllWindows()
