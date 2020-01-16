from viola_jones_live_detection import ViolaJonesLiveDetection

resolutions = [
    [1280, 720],
    [960, 540],
    [768, 432],
    [640, 360],
    [426, 240],
    [256, 144]
]

res_index = 5

viola_jones = ViolaJonesLiveDetection(resolutions[res_index][0], resolutions[res_index][1])

viola_jones.start()