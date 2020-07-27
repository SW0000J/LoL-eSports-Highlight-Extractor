"""
#   File Name: finding_ultimate.py
#        Team: visual recognition 2
#  Programmer: SW0000J
#  Start Date: 07/08/20
# Last Update: July 20, 2020
#     Purpose: to find ultimate skill
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
Ultimate Skill's center(x, y) coordinate
radius : 12

# left-side player
# player 1 [x, y] -> [71, 165]
# player 2 [x, y] -> [71, 268]
# player 3 [x, y] -> [71, 371]
# player 4 [x, y] -> [71, 473]
# player 5 [x, y] -> [71, 577]

# right-side player
# player 1 [x, y] -> [1847, 165]
# player 2 [x, y] -> [1847, 268]
# player 3 [x, y] -> [1847, 371]
# player 4 [x, y] -> [1847, 473]
# player 5 [x, y] -> [1847, 577]

Champions icon's coordinate
len : 40

# left-side player
# player 1 [x, y] -> [31, 160]
# player 2 [x, y] -> [31, 263]
# player 3 [x, y] -> [31, 366]
# player 4 [x, y] -> [31, 468]
# player 5 [x, y] -> [31, 572]

# right-side player
# player 1 [x, y] -> [1847, 160]
# player 2 [x, y] -> [1847, 263]
# player 3 [x, y] -> [1847, 366]
# player 4 [x, y] -> [1847, 468]
# player 5 [x, y] -> [1847, 572]
"""

def draw_circle_on_ultimate(circle_x : int, circle_y : int) -> None:
    """
    Draw circle on ultimate skill to get ultimate skill's coordinate

    Args:
        circle_x: x-coordinate of the center of the circle
        circle_y: y-coordinate of the center of the circle

    Returns:
        Just draw circle on ultimate skill

    Raises:
        None
    """
    img = cv.imread("test.jpeg")

    img = cv.circle(img, (circle_x, circle_y), 12, (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def draw_rectangle_on_champion(rectangle_x : int, rectangle_y : int) -> None:
    """
    Draw rectangle on champion to get champions icon's coordinate

    Args:
        rectangle_x: x-coordinate of the center of the circle
        rectangle_y: y-coordinate of the center of the circle

    Returns:
        Draw rectangle on champions icon

    Raises:
        None
    """
    img = cv.imread("test.jpeg")

    img = cv.rectangle(img, (rectangle_x, rectangle_y), (rectangle_x + 40, rectangle_y + 40), (0, 0, 255), 1)

    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def compare_champion_icon_with_champion_icon_data(champion_image_path : str, test_image_path : str,
                                                  champion_icon_file_list : list) -> int:
    """
        Compare two images(champion icon & champion icon data) using 'SIFT' similarity
        match_list mean how similar images they are

        Args:
            champion_image_path : champion image path
            test_image_path : test image path

        Returns:
            match list's length

        Raises:
            None
    """
    matched_list = []
    for index in range(len(champion_icon_file_list)):

        img1 = cv.imread(champion_image_path + champion_icon_file_list[index])
        img2 = cv.imread(test_image_path)

        sift = cv.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        match_list = []
        for m, n in matches:
            if m.distance < 0.3 * n.distance:
                match_list.append([m])
        matched_list.append(len(match_list))
        print('{} done'.format(index))

    best_matched_index = matched_list.index(max(matched_list))

    return best_matched_index
    #img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
    #plt.imshow(img3), plt.show()


def main() -> None:
    #draw_circle_on_ultimate(1847, 165)
    #draw_rectangle_on_champion(1847, 160)

    champion_icon_data = []
    ultimate_skills_data = []

    in_game_champion_icon = []
    in_game_ultimate_skills = []

    champion_icon_files = ["Aatrox.png", "Ahri.png", "Akali.png", "Alistar.png", "Amumu.png", "Anivia.png",
                            "Annie.png", "Aphelios.png", "Ashe.png", "Aurelionsol.png", "Azir.png", "Bard.png",
                            "Blitzcrank.png", "Brand.png", "Braum.png", "Caitlyn.png", "Camille.png",
                            "Cassiopeia.png", "Chogath.png", "Corki.png", "Darius.png", "Diana.png", "Dr_mundo.png",
                            "Draven.png", "Ekko.png", "Elise.png", "Evelynn.png", "Ezreal.png", "Fiddlesticks.png",
                            "Fiora.png", "Fizz.png", "Galio.png", "Gangplank.png", "Garen.png", "Gnar.png",
                            "Gragas.png", "Graves.png", "Hecarim.png", "Heimerdinger.png", "Illaoi.png", "Irelia.png",
                            "Ivern.png", "Janna.png", "Jarvan.png", "Jax.png", "Jayce.png", "Jhin.png", "Jinx.png",
                            "Kaisa.png", "Kalista.png", "Karma.png", "Karthus.png", "Kassadin.png", "Katarina.png",
                            "Kayle.png", "Kayn.png", "Kennen.png", "Khazix.png", "Kindred.png", "Kled.png",
                            "Kogmaw.png", "Leblanc.png", "Leesin.png", "Leona.png", "Lillia.png", "Lissandra.png",
                            "Lucian.png", "Lulu.png", "Lux.png", "Malphite.png", "Malzahar.png", "Maokai.png",
                            "Masteryi.png", "Missfortune.png", "Mordekaiser.png", "Morgana.png", "Nami.png",
                            "Nasus.png", "Nautilus.png", "Neeko.png", "Nidalee.png", "Nocturne.png", "Nunu.png",
                            "Olaf.png", "Orianna.png", "Ornn.png", "Pantheon.png", "Poppy.png", "Pyke.png",
                            "Qiyana.png", "Quinn.png", "Rakan.png", "Rammus.png", "Reksai.png", "Renekton.png",
                            "Rengar.png", "Riven.png", "Rumble.png", "Ryze.png", "Sejuani.png", "Senna.png",
                            "Sett.png", "Shaco.png", "Shen.png", "Shyvana.png", "Singed.png", "Sion.png",
                            "Sivir.png", "Skarner.png", "Sona.png", "Soraka.png", "Swain.png", "Sylas.png",
                            "Syndra.png", "Tahmkench.png", "Taliyah.png", "Talon.png", "Taric.png", "Teemo.png",
                            "Thresh.png", "Tristana.png", "Trundle.png", "Tryndamere.png", "Twistedfate.png",
                            "Twitch.png", "Udyr.png", "Urgot.png", "Varus.png", "Vayne.png", "Veigar.png", "Velkoz.png",
                            "Vi.png", "Viktor.png", "Vladimir.png", "Volibear.png", "Warwick.png", "Wukong.png",
                            "Xayah.png", "Xerath.png", "Xinzhao.png", "Yasuo.png", "Yorick.png", "Yuumi.png", "Zac.png",
                            "Zed.png", "Ziggs.png", "Zilean.png", "Zoe.png", "Zyra.png"]

    champion_image_path = "../resources/champions_image/"
    test_image = "test.jpeg"

    # Load champion icon images
    for index in range(len(champion_icon_files)):
        champion_icon = cv.imread(champion_image_path + champion_icon_files[index])
        champion_icon_data.append(champion_icon)

        champion_icon_data[index] = cv.cvtColor(champion_icon_data[index], cv.COLOR_BGR2RGB)

    # Resize champion icon images(40 x 40)
    for index in range(len(champion_icon_data)):
        champion_icon_data[index] = cv.resize(champion_icon_data[index], (40, 40))

    # find best match index

    print(compare_champion_icon_with_champion_icon_data(champion_image_path, test_image, champion_icon_files))




if __name__ == "__main__":
    main()