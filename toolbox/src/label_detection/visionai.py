import io
from google.cloud import vision

def label_detection(uri: str) -> list:
    """Detects labels in the file."""
    
    # Prepare the img (from local image)
    # image_path = image_path
    # with io.open(image_path, "rb") as image_file:
    #     content = image_file.read()

    # image = vision.Image(content=content)

    # Prepare the img (from remote image)
    image = vision.Image()
    image.source.image_uri = uri

    # Instantiate a client
    client = vision.ImageAnnotatorClient()

    # Lebel detection
    response_label = client.label_detection(image=image)
    labels = response_label.label_annotations
    lab_list = []
    for label in labels:
        # print(label.description)
        lab_list.append(label.description)
    
    if response_label.error.message:
        raise Exception(
            "{}\nFor more info on error messages,check: "
            "https://cloud.google.com/apis/design/errors".format(response_label.error.message)
        )
    
    print(lab_list)
    return lab_list









    # face detection
    # response_face = client.face_detection(image=image)
    # for face_detection in response_face.face_annotations:
    #     d = {
    #         "confidence": face_detection.detection_confidence,
    #          "joy": face_detection.joy_likelihood,
    #          "sorrow": face_detection.sorrow_likelihood,
    #          "surprise": face_detection.surprise_likelihood,
    #          "anger": face_detection.anger_likelihood,
    #         }
    #     print(d)
    
    # img propoerties
    # response_image = client.image_properties(image=image)
    # # print(response_image)
    # for c in response_image.image_properties_annotation.dominant_colors.colors[:3]:
    #     d = {
    #         "color": c.color,
    #         "score": c.score,
    #         "pixel_fraction": c.pixel_fraction
    #     }
    #     print(d)