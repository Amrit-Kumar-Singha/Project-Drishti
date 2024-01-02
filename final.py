import cv2
import numpy
from flask import Flask, render_template, Response, stream_with_context, request

video = cv2.VideoCapture(0)
app = Flask('__name__')


def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break;
        else:
            classNames = []
            classFile = "/home/pi/Downloads/Object_Detection_Files/coco.names"
            with open(classFile,"rt") as f:
                classNames = f.read().rstrip("\n").split("\n")

            configPath = "/home/pi/Downloads/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
            weightsPath = "/home/pi/Downloads/Object_Detection_Files/frozen_inference_graph.pb"

            net = cv2.dnn_DetectionModel(weightsPath,configPath)
            net.setInputSize(320,320)
            net.setInputScale(1.0/ 127.5)
            net.setInputMean((127.5, 127.5, 127.5))
            net.setInputSwapRB(True)
            objects=[]
            classIds, confs, bbox = net.detect(frame,confThreshold=0.45,nmsThreshold=0.2)
            #print(classIds,bbox)
            if len(objects) == 0: objects = classNames
            objectInfo =[]
            if len(classIds) != 0:
                for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                    className = classNames[classId - 1]
                    if className in objects:
                        objectInfo.append([box,className])
                        if (True):
                            cv2.rectangle(frame,box,color=(0,255,0),thickness=2)
                            cv2.putText(frame,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                            cv2.putText(frame,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            ret, buffer = cv2.imencode('.jpeg',frame)
            frame = buffer.tobytes()
            yield (b' --frame\r\n' b'Content-type: imgae/jpeg\r\n\r\n' + frame +b'\r\n')


@app.route('/camera')
def camera():
    return render_template('camera.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)