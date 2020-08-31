"""
#   File Name: cognition_inGame.py
#        Team: standardization
#  Programmer: tjswodud
#  Start Date: 07/07/20
<<<<<<< HEAD
# Last Update: August 02, 2020
#     Purpose: Determine the game is (Playing) or (not Playing) and cut Full_Video not in_game
=======
# Last Update: August 18, 2020
#     Purpose: Full video of LCK will be given in this program.
#              And compare frame and minimap image (template) per frame, using sift_algorithm.
#              (if it success for compare, that frame is ingame, if not, that frame is not ingame.)
#              Finally, this program will return edited video, except for frame that is not ingame.
>>>>>>> origin/feature-standardization-minimap
"""

import cv2 as cv
import numpy as np
<<<<<<< HEAD
import time


def cut_video(capture, temp):
    # fps, codec, output
    fps = capture.get(cv.CAP_PROP_FPS)
    total_frame_count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    output = cv.VideoWriter("../results/output" + ".mp4", fourcc, fps, (1920, 1080), 1)

    # Playing Video, writing output
    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        current_frame = int(capture.get(cv.CAP_PROP_POS_FRAMES))
        print("{}/{} - {}%".format(current_frame, total_frame_count, round(current_frame/total_frame_count, 2)))

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if capture.get(cv.CAP_PROP_POS_FRAMES) % fps == 0:
            # template matching
            res = cv.matchTemplate(gray_frame, temp, cv.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.4)

            if loc[::-1][0].size != 0:  # playing
                # print('writing')
                output.write(frame)
            else:
                # print('not writing')
                continue

    capture.release()
    output.release()
    cv.destroyAllWindows()


def main():
    start_time = time.time()

    # Full Videos
    cap = cv.VideoCapture("../resources/APKvsSB.mp4")

    # Template Image (minimap)
    template = cv.imread("../resources/minimap_templ.png", cv.IMREAD_GRAYSCALE)

    cut_video(cap, template)

    print('time:', time.time() - start_time)

=======
import os
from matplotlib import pyplot as plot
import time

def match_template(video_capture: np.ndarray, template: np.ndarray, video_file: str, video_path: str) -> None:
    """
        Compare captured video and template image (minimap image) with sift_algorithm
        , and then write video frame that is in_game

        Args:
            video_capture: captured video using VideoCapture in __main__
            template: a template image (minimap image) to compare with video_capture
            video_file: name of video file in string type
            video_path: path of output_video (output_video will be stored this path)

        Returns:
            None

        Raises:
            N/A
    """
    is_writing = False

    file_name = video_file.replace('.mp4', '')

    width = int(video_capture.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    fps = video_capture.get(cv.CAP_PROP_FPS)
    output = cv.VideoWriter((video_path + '/' + file_name + '_output' + '.mp4'), fourcc, fps, (width, height), 1)

    # sift_ans = False
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        width_end, height_end = frame_gray.shape

        width_start = round(780 / 1080 * width_end)
        height_start = round(1620 / 1920 * height_end)

        frame_resize = frame_gray[width_start: width_end, height_start: height_end]

        total_frames = int(video_capture.get(cv.CAP_PROP_FRAME_COUNT))

        if video_capture.get(cv.CAP_PROP_POS_FRAMES) % int(fps) == 0:
            current_frame = int(video_capture.get(cv.CAP_PROP_POS_FRAMES))
            percentage = int((current_frame / total_frames) * 100)
            print('{}/{} - {}%'.format(current_frame, total_frames, percentage))
            sift_ans = sift_algorithm(frame_resize, template)
            if sift_ans:
                is_writing = True
            else:
                is_writing = False

        if is_writing:
            output.write(frame)
        else:
            continue

    output.release()
    video_capture.release()
    cv.destroyAllWindows()

def sift_algorithm(frame_resize: np.ndarray, template: np.ndarray) -> bool:
    """
        Compare video's frame and template image, using sift_algorithm

        Args:
            frame_resize: each of video's frame that is resized to template image
            template: a template image (minimap image) to compare with video_capture

        Returns:
            [bool type]
            if frame_resize and template match more than 15 points, return True (this frame is ingame.)
            if not, return False (this frame is not ingame.)

        Raises:
            N/A
    """
    sift = cv.xfeatures2d.SIFT_create()

    keypoint_1, descriptor_1 = sift.detectAndCompute(frame_resize, None)
    keypoint_2, descriptor_2 = sift.detectAndCompute(template, None)

    bf_matcher = cv.BFMatcher()
    match = bf_matcher.knnMatch(descriptor_1, descriptor_2, 2)

    success_match = []
    for m, n in match:
        if m.distance < n.distance * 0.75:
            success_match.append([m])

    # plot_image = cv.drawMatchesKnn(frame_resize, keypoint_1, template, keypoint_2, success_match, None, flags=2)
    # plot.imshow(plot_image)
    # plot.show()

    if len(success_match) > 15:
        print('this frame is ingame.')
        return True
    else:
        print('this frame is not ingame.')
        return False

def create_capture(path: str):
    return cv.VideoCapture(path)

def main() -> None:
    start_time = time.time()

    resource_path = "D:/video/resources"
    output_path = "D:/video/outputs"
    video_list = os.listdir(resource_path)
    template_image = cv.imread("../resources/minimap_templ.png", cv.COLOR_BGR2GRAY)

    video_num = 1
    for video_file in video_list:
        new_video_path = resource_path + '/' + video_file
        video_capture = create_capture(new_video_path)
        print('[No.{} video is editing...]'.format(video_num))
        match_template(video_capture, template_image, video_file, output_path)
        video_num += 1

    end_time = time.time()
    exe_time = round((end_time - start_time), 1)
    print('time : {} s.'.format(exe_time))
>>>>>>> origin/feature-standardization-minimap

if __name__ == '__main__':
    main()