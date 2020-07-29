"""
#   File Name: visualization.py
#        Team: visual recognition 2
#  Programmer: littlecsi
               bluehyena
#  Start Date: 07/27/20
# Last Update: July 29, 2020
#     Purpose: Imports image comparison functions from lol_spell_recognition.py file and evaulautes them.
               Evaluation results are saved in 'result' directory.
"""
import lol_spell_recognition as lsr

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from types import FunctionType


def save_graph(compare_function: FunctionType, original_spell_image: np.ndarray, video_frames: list) -> None:
    """
     Make graph with compare_function's return value and save as PNG file

    Args:
        compare_function: Function of image comparison
        original_spell_image: Original image of spell
        video_frames : List of video

    Returns:
        None

    Raises:
        None
    """

    assert callable(compare_function)
    assert isinstance(original_spell_image, np.ndarray)
    assert isinstance(video_frames, list)

    ## Variable Construction
    x_axis = []
    y_axis = []
    in_game_spell = np.array([])

    # Make List of x,y_axis
    for video_frame in video_frames:
        in_game_spell = lsr.extract_spell_images(video_frame, 13)
        y_axis.append(compare_function(in_game_spell, original_spell_image))

    x_axis = list(range(len(video_frames)))

    # Make Graph
    plt.plot(x_axis, y_axis)
    plt.xlabel("Video Time")
    plt.ylabel("Similarity")
    plt.savefig("../result/comparison_result.png", format="png")


def main():
    ## Variable Construction
    frame_count = 0
    frames = []
    in_game_spell = np.array([])
    smite_image = np.array([])
    smite_path = "../resources/summoner_spells/Smite.png"
    video_path = "../resources/smite_test.mp4"

    ## Variable Initialization
    # Read testing file
    frames, frame_count = lsr.video_to_list(video_path)

    # Read smite image
    smite_image = cv.imread(smite_path)
    smite_image = cv.resize(smite_image, (20, 20))
    smite_image = cv.cvtColor(smite_image, cv.COLOR_BGR2RGB)

    ## Begin frame analysis
    save_graph(lsr.compare_images_1, smite_image, frames)


if __name__ == '__main__':
    main()