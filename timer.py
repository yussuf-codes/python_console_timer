from time import sleep


def timer(timeSeconds):
    while timeSeconds:
        remainMinutes = timeSeconds // 60
        remainSeconds = timeSeconds % 60

        if remainMinutes == 0:
            minutes = "00"
        elif remainMinutes < 10:
            minutes = f"0{remainMinutes}"
        elif remainMinutes > 9:
            minutes = f"{remainMinutes}"

        if remainSeconds == 0:
            seconds = "00"
        elif remainSeconds < 10:
            seconds = f"0{remainSeconds}"
        elif remainSeconds > 9:
            seconds = f"{remainSeconds}"
        
        timer = f" Timer: {minutes}:{seconds}"
        print(timer, end="\r")

        sleep(1)
        timeSeconds -= 1