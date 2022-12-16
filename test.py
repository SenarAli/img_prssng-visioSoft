import os, cv2
import math

# Image prediction boxes in order
# Each array containes object in continues matching
PredBoxes = {
  "636.jpg": ([890,1774], [1930, 1347],[2532, 1478], [4508,1680], [4879,1936], [7067,1683]), # First Image Objects
  "637.jpg": ([739,1823], [1573, 1369],[2231, 1436], [4624,1608], [5577,1829], [7460,1781]), # Second Image Objects
  "638.jpg": ([655,1837], [1302, 1434],[1930, 1447], [4764,1535], [6725,1784], [7655,1792]), # Third Image Objects
  "639.jpg": ([545,1860], [1021, 1515],[1542, 1467], [5009,1409], [7445,1867], [7791,1840])  # Forth Image Objects
}

def imageFov (im):
    # FOV lines®®®
    cv2.line(im, (4096, 4096), (0, 0), (224, 224, 224), 10)
    cv2.line(im, (4096, 4096), (8192, 0), (224, 224, 224), 10)
    cv2.putText(im, '0', (4030, 4000), cv2.FONT_HERSHEY_SIMPLEX,
                5, (255, 0, 0), 5, cv2.LINE_AA)


def iterasyon(iterable):
   """This function provides access to objects in the previous
        picture and objects in the next picture.
        If you want to use this function, you can access the objects with this loop.
    for item, next_item in iterasyon(PredBoxes.items()):
      item[1]=([890,1774], [1930, 1347],[2532, 1478], [4508,1680], [4879,1936], [7067,1683])
      next_item[1]=([739,1823], [1573, 1369],[2231, 1436], [4624,1608], [5577,1829], [7460,1781])

"""

      iterator = iter(iterable)
      item = iterator.__next__()

    for next_item in iterator:
        yield item, next_item
        item = next_item

    yield item, None


def calcDiff (current_location):
  index = PredBoxes[img].index(current_location)
  previous = int(img.split('.')[0]) -1

  try:
    previous_location = PredBoxes[str(previous)+'.jpg'][index]
    print('previous location: ',previous_location, 'current_location: ',current_location)

    x1 = previous_location[0]
    y1 = previous_location[1]
    x2 = current_location[0]
    y2 = current_location[1]

    previous_tan = abs((4096-x1))/(4096-y1)
    previous_angle = (math.atan(previous_tan))*(180/math.pi)
    current_tan = abs((4096-x2))/(4096-y2)
    current_angle = (math.atan(current_tan))*(180/math.pi)

    angle_diff = current_angle - previous_angle
    print(angle_diff)

  except:
      print('Angle difference could not be calculated because this is the first photo.')
      angle_diff = 0
  
  return angle_diff

for img in PredBoxes: #or  use  for item, next_item in iterasyon(PredBoxes.items()):
    image_path = os.path.join("../imgs/", img)
    im = cv2.imread(image_path)
    imageFov(im)
    for obj in PredBoxes[img]:
        angle_diff = calcDiff(obj)
        cv2.line(im, (4096, 4096), obj, (255, 255, 120), 10)
        cv2.putText(im, str(round(angle_diff,2)), (obj[0] , obj[1]), cv2.FONT_HERSHEY_SIMPLEX,
                     5, (0, 0, 255), 5, cv2.LINE_AA)
        
    cv2.imshow("panoptic prediction", im)
    cv2.waitKey(0)