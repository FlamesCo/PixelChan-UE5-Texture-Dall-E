import requests

API_URL = "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"
headers = {"Authorization": "Bearer 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"}
def Startup(self): {
print("Hi, I am beep-o I am a 3d model generator", "Also  do 2d textures  for ue5")

}
def save_obj_model(model_name, model_format, model_path):
    """
    Save a 3d model
    """
    payload = {
        "model_name": model_name,
        "model_format": model_format,
        "model_path": model_path
    }
    response = requests.post(API_URL + "/save_obj_model", headers=headers, json=payload)
    return response.json()

    ## ask if you would like to save the model to a 3d obj file
    print("Thank you for using Beep-0 v0.1x")    


    

 ## use rudalle to generate a image of a 3d model
def generate_3d_model(model_name, model_type, model_size, model_color, model_texture, model_material, model_position, model_rotation, model_scale, model_format):
    """
    Generate a 3d model
    """
    payload = {
        "model_name": model_name,
        "model_type": model_type,
        "model_size": model_size,
        "model_color": model_color,
        "model_texture": model_texture,
        "model_material": model_material,
        "model_position": model_position,
        "model_rotation": model_rotation,
        "model_scale": model_scale,
        "model_format": model_format
    }
    response = requests.post(API_URL + "/generate_3d_model", headers=headers, json=payload)
    return response.json()

    ## ask where to save the model
def save_3d_model(model_name, model_format, model_path):
    """
    Save a 3d model
    """
    payload = {
        "model_name": model_name,
        "model_format": model_format,
        "model_path": model_path
    }
    response = requests.post(API_URL + "/save_3d_model", headers=headers, json=payload)
    return response.json()

    ## ask if you would like to save the model to a 2d png texture split into files for unreal engine 5
def save_2d_model(model_name, model_format, model_path):
    """
    Save a 2d model
    """
    payload = {
        "model_name": model_name,
        "model_format": model_format,
        "model_path": model_path
    }
    response = requests.post(API_URL + "/save_2d_model", headers=headers, json=payload)
    return response.json()
 
print("Starting generator")
print("Hi I am Beep-o v1.0x")
print("Generating 3d model")
print(generate_3d_model())
print("Saving 3d model")
print(save_3d_model())
print("Saving 2d model")
print("Done")