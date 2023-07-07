from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from showcase.models import Gallery
from .models import AI_Model
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import imageio
import requests
import base64
import json
import random
import string
import os


@login_required
def home(request):
    # Retrieves all AI_Model objects from the database
    models_data = AI_Model.objects.all()
    return render(request, "generator/home.html", {"models": models_data})


@login_required
def generator(request):
    if request.method == "POST":
        # Get the input data from the request
        model_checkpoint = request.POST.get("model_checkpoint")
        prompt_ps = request.POST.get("prompt_ps")
        prompt_ng = request.POST.get("prompt_ng")
        sampler = request.POST.get("sampler")
        seed = request.POST.get("seed")
        steps = request.POST.get("steps")
        height = request.POST.get("height")
        width = request.POST.get("width")
        cfg_scale = request.POST.get("cfg_scale")

        # Make a request to the API with the input data
        api_url = os.getenv("STABLE_DIFFUSION_URI")
        api_payload = {
            "prompt": prompt_ps,
            "negative_prompt": prompt_ng,
            "steps": steps,
            "seed": seed,
            "sampler_name": sampler,
            "width": width,
            "height": height,
            "cfg_scale": cfg_scale,
            "override_settings": {
                "sd_model_checkpoint": model_checkpoint
            },
        }
        response = requests.post(url=f"{api_url}/sdapi/v1/txt2img", json=api_payload)

        if response.status_code == 200:
            # Process the response to obtain the image data
            res = response.json()
            base64_img = res["images"][0]
            base64_img = base64_img.replace("data:image/png;base64,", "")
            img_bytes = base64.b64decode(base64_img)

            # Generate a random string as the image filename
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            img_filename = f"{random_string}.png"

            # Specify the path to save the image
            save_path = os.path.join("media", "temp", img_filename)

            # Save the image to the specified path
            with open(save_path, "wb") as img_file:
                img_file.write(img_bytes)

            # Get the URL for the saved image
            img_url = request.build_absolute_uri(f"/media/temp/{img_filename}")

            return JsonResponse({"status": 200, "data": img_url}, status=200)
        else:
            return JsonResponse({"status": 400, "data": "API request failed!"}, status=400)

    return JsonResponse({"status": 400, "data": "invalid request!"}, status=400)


def save_to_gallery(request):
    if request.method == "POST":
        # Get the image URL from the request
        image_url = request.POST.get("image_url")

        # Make a request to download the image
        response = requests.get(image_url)
        if response.status_code == 200:
            # Generate a random string as the image filename
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            img_filename = f"{random_string}.png"

            # Specify the path to save the image
            save_path = os.path.join(settings.MEDIA_ROOT, "showcase", img_filename)

            # Save the image content to disk
            with open(save_path, "wb") as img_file:
                img_file.write(response.content)

            # Open the image using imageio
            image = imageio.imread(save_path)

            # Convert the image to PIL format
            image = Image.fromarray(image)

            # Add watermark text
            watermark_text = "Musicai.Art"
            font_size = 50
            font = ImageFont.load_default()
            draw = ImageDraw.Draw(image)
            text_width, text_height = draw.textsize(watermark_text, font=font)
            x = image.width - text_width - 10
            y = image.height - text_height - 10
            draw.text((x, y), watermark_text, fill=(255, 255, 255), font=font)

            # Save the image with the watermark
            image.save(save_path)

            # Get the URL for the saved image
            saved_image_url = "showcase/" + img_filename

            # Save the image URL and logged user's email to the Gallery model
            gallery_entry = Gallery.objects.create(user=request.user, image=saved_image_url)

            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error"})
    else:
        return JsonResponse({"status": "error"})