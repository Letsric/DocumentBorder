import asyncio
import os
from datetime import datetime
from io import BytesIO

from PIL import Image
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from starlette.responses import StreamingResponse

app = FastAPI()

# define allowed connections
origins = [
    'http://127.0.0.1:3001',
    'http://localhost:3001',
    'http://192.168.178.105:3001',
    'http://asusserver:3001',
    '*',
]

# add these to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allows all origins
    allow_credentials=True,
    allow_methods=['*'], # Allows all methods
    allow_headers=['*'], # Allows all headers
)


@app.post(
    "/makeborder/{paperType}/{orientation}/{imageSize}/{padding}/{numberOfImagesH}/"
    "{numberOfImagesV}")
async def makeBorder(file: UploadFile, paperType: str, orientation: str, imageSize: str,
                     padding: str, numberOfImagesH: str, numberOfImagesV: str):
    """
    makes a pretty border out of an image for
    e.g. an invitation to a birthday party

    file                 = Image for the border

    paperType            = The type of the paper (Can be: [ A3 | A4 | A5 | letter ] )

    orientation          = The orientation of the paper (Can be: [ vertical | horizontal ] )

    imageSize            = The size of the images for the border (Can be: any integer)

    padding              = How much space between the edge of the paper and the border
                           should there be (Can be: any integer)

    numberOfImagesV      = The number of images you want vertically

    numberOfImagesH      = THe number of images you want horizontally         """

    # ____________________________________________________________________
    """
    Generate variables
    ==================
      timestampStr = timestamp in a nice String format
                     with all the columns replaced with
                     dots (because of filename limitations
                     in Windows)
      img          = Pillow Image uploaded by the user
                     (Pillow Image format)
      imgDraw      = Pillow ImageDraw object for drawing
                     onto the Image uploaded by the user             """
    timestamp = datetime.now()
    timestampStr = str(timestamp)
    timestampStr = timestampStr.replace(":", ".")
    imageSize = int(imageSize)
    padding = int(padding)
    numberOfImagesH = int(numberOfImagesH)
    numberOfImagesV = int(numberOfImagesV)
    file = file.file
    img = Image.open(file)
    numberOfImagesV -= 1
    numberOfImagesH -= 1
    # ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

    # ___________________________________________
    """
    Validate all of the user controlled arguments
    =============================================        """
    if not paperType in {"A3", "A4", "A5", "letter"}:
        return HTMLResponse(f"<h1>Error!</h1><hl><p>The paper"
                            f"type {paperType} is not supported!</p>")
    if not orientation in {"horizontal", "vertical"}:
        return HTMLResponse(f"<h1>Error!</h1><hl><p>The paper"
                            f"type {paperType} is not supported!</p>")
    # ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

    # _________________________________________________________________
    """
    Create and process the image for the border
    ===========================================                      """
    # Create borderImg for A3 paper format
    if paperType == "A3":
        if orientation == "vertical":
            borderImg = Image.new("RGB", (3508, 4960), "WHITE")
        if orientation == "horizontal":
            borderImg = Image.new("RGB", (4960, 3508), "WHITE")

    # Create borderImg for A4 paper format
    elif paperType == "A4":
        if orientation == "vertical":
            borderImg = Image.new("RGB", (2480, 3508), "WHITE")
        if orientation == "horizontal":
            borderImg = Image.new("RGB", (3508, 2480), "WHITE")

    # Create borderImg for A5 paper format
    elif paperType == "A5":
        if orientation == "vertical":
            borderImg = Image.new("RGB", (1748, 2480), "WHITE")
        if orientation == "horizontal":
            borderImg = Image.new("RGB", (2480, 1748), "WHITE")

    # Create borderImg for US letter paper format
    elif paperType == "letter":
        if orientation == "vertical":
            borderImg = Image.new("RGB", (2550, 3300), "WHITE")
        if orientation == "horizontal":
            borderImg = Image.new("RGB", (3300, 2550), "WHITE")

    imgW = img.width  # old width of the user image
    imgH = img.height  # old height of the user image
    newImgW = imageSize  # new width of the user image determent by the imageSize parameter
    newImgH = int(imgH / imgW * imageSize)  # new height of the user image
    resizedImg = img.resize((newImgW, newImgH))  # the scaled user image
    imagesPastedV = 0
    imagesPastedH = 0

    while imagesPastedV < numberOfImagesV:
        whereToPaste = (
                               borderImg.height - padding * 2 - newImgH) / numberOfImagesV * \
                       imagesPastedV + padding

        borderImg.paste(resizedImg, (padding, int(whereToPaste)))
        borderImg.paste(resizedImg, (borderImg.width -
                                     newImgW - padding, int(whereToPaste)))
        imagesPastedV += 1

    while imagesPastedH < numberOfImagesH + 1:
        whereToPaste = (
                               borderImg.width - padding * 2 - newImgW) / numberOfImagesH * \
                       imagesPastedH + padding

        borderImg.paste(resizedImg, (int(whereToPaste), padding))
        borderImg.paste(resizedImg, (int(whereToPaste),
                                     borderImg.height - newImgH - padding))
        imagesPastedH += 1
    # ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

    # _________________________________________________________
    """
    Save the new image and return it
    ================================                 """
    finalImage = BytesIO()
    borderImg.save(finalImage, "PNG")
    finalImage.seek(0)
    return StreamingResponse(finalImage, media_type="image/png")
    # ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾