
TR:
Bu kod parçası , her resim için imageFov() adlı bir fonksiyonu çağırarak resmin üzerine iki eksen çizgisi ve sıfır koordinatını gösteren bir metin çizmektedir. Bu kod parçası ayrıca tüm resimlerdeki objeleri teker teker dolaşıp her resimdeki objenin koordinatlarına bir çizgi çizer.

Calcdif() fonksiyonunu açı değişimini hesaplamak için kullanabilirsiniz.

iterasyon() fonksiyonu resimdeki objelere ulaşmayı kolaylaştırır.

Bu kod parçasındaki amaç 5'er metre aralıklarla çekilen görüntülerdeki objelerin bir önceki konumdaki objenin koordinatları ve bir sonraki konumdaki objenin koordinatlarını kullanarak açı değişimini hesaplayıp bir sonraki konumda objenin açı değişimine göre konumunu tahmin etmektir.


EN:
This piece of code calls a function called imageFov() for each image and draws text on the image showing the two axis lines and the zero coordinate. This piece of code also traverses the objects in all the images one by one and draws a line to the coordinates of the object in each image.

The purpose of this piece of code is to calculate the angle change of the objects in the images taken at 5 meters intervals, using the coordinates of the object at the previous location and the coordinates of the object at the next location, and to estimate the position of the object at the next location according to the angle change.

You can use the Calcdif() function to calculate the angle change.

The iteration() function makes it easy to reach objects in the picture.