// yolov4_object_detection.cpp
#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>

class YOLOv4ObjectDetector {
public:
    YOLOv4ObjectDetector(const std::string& model_path) {
        // Load YOLOv4 model
        net = cv::dnn::readNetFromDarknet(model_path, model_path);
    }

    std::vector<cv::Rect> detectObjects(cv::Mat& frame){
        // Pre-process frame
        cv::Mat blob;
        cv::dnn::blobFromImage(frame, blob, 1/255.0, cv::Size(416, 416), cv::Scalar(0,0,0), true, false);

        // Set input blob
        net.setInput(blob);

        // Run object detection
        std::vector<cv::Mat> outs;
        net.forward(outs);

        // Parse output
        std::vector<cv::Rect> objects;
        for (size_t i = 0; i < outs.size(); ++i) {
            float* data = (float*)outs[i].data;
            for (int j = 0; j < outs[i].rows; ++j, data += outs[i].cols) {
                cv::Mat scores = outs[i].row(j).colRange(5, outs[i].cols);
                cv::Point classIdPoint;
                double confidence;
                cv::minMaxLoc(scores, 0, &confidence, 0, &classIdPoint);
                if (confidence > 0.5) {
                    int centerX = (int)(data[0] * frame.cols);
                    int centerY = (int)(data[1] * frame.rows);
                    int width = (int)(data[2] * frame.cols);
                    int height = (int)(data[3] * frame.rows);
                    cv::Rect object(centerX, centerY, width, height);
                    objects.push_back(object);
                }
            }
        }

        return objects;
    }

private:
    cv::dnn::Net net;
};

int main() {
    YOLOv4ObjectDetector detector("yolov4.cfg", "yolov4.weights");
    cv::VideoCapture cap(0);
    cv::Mat frame;

    while (true) {
        cap >> frame;
        if (frame.empty()) break;

        std::vector<cv::Rect> objects = detector.detectObjects(frame);
        for (const auto& obj : objects) {
            cv::rectangle(frame, obj, cv::Scalar(0, 255, 0), 2);
        }

        cv::imshow("Object Detection", frame);
        if (cv::waitKey(1) == 27) break;
    }

    return 0;
}
