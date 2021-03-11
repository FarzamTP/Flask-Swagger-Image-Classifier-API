from flask import Blueprint, abort, request, jsonify
import requests, os


REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/classify', methods=['POST'])
def get_target_image_url():
    """
    @param url: post : The target image url.
    @returns: 201 : a label (cat / dog) as a flask/response object.
    @raise 400: if unable to download the image.
    """
    if not request.get_json():
        abort(400)
    else:
        data = request.get_json(force=True)
        if not data.get('image_url'):
            abort(400)
        else:
            url = data.get('image_url')
            r = requests.get(url)
            image_dir = f"media/{str(url).split('/')[-1]}"
            if not os.path.exists(image_dir):
                image = open(image_dir, "wb")
                image.write(r.content)
                image.close()
                return jsonify({"image_dir": image_dir,
                                "status": 200})
            else:
                return jsonify({"image_dir": image_dir,
                                "status": 201})