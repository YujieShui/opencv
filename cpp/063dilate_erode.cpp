#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <math.h>
using namespace cv;
using namespace std;
int main(int argc, char** argv)
{
	Mat dresult, eresult;
	Mat src = imread("../images/coins.jpg");

	// 二值化
	Mat gray, binary;
	cvtColor(src, gray, COLOR_BGR2GRAY);
	threshold(gray, binary, 0, 255, THRESH_BINARY | THRESH_OTSU);
	imshow("binary", binary);

	// 使用3x3结构元素进行腐蚀和膨胀操作
	Mat se = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));
	// 腐蚀
	dilate(binary, dresult, se, Point(-1, -1), 1, 0);
	// 膨胀
	erode(binary, eresult, se, Point(-1, -1), 1, 0);

	imshow("dilate", dresult);
	imshow("erode", eresult);
	waitKey(0);
	return 0;
}