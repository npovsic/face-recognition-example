from google_coral_live_detection import GoogleCoralLiveDetection

resolutions = [
    [1280, 720],
    [960, 540],
    [768, 432],
    [640, 360],
    [426, 240],
    [256, 144]
]

res_index = 5

google_coral = GoogleCoralLiveDetection(resolutions[res_index][0], resolutions[res_index][1])

google_coral.start()
