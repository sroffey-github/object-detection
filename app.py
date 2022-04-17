from imageai.Detection import ObjectDetection
import sys, os

filename = sys.argv[1]
execution_path = f'{os.getcwd()}/imgs'

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(os.getcwd() , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , filename), output_image_path=os.path.join(execution_path , f'{filename.split(".")[0]}-new.{filename.split(".")[1]}'))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )