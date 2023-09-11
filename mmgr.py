import json
import os
import requests

class FileClass:
  def __init__(self, filepath, mode="r"):
    self.filepath = filepath
    self.mode = mode
    self.loaded_file = self.open_file()
    self.loaded_dict = self.get_dict()

  def open_file(self):
    try:
      return open(self.filepath, self.mode)
    except FileNotFoundError:
      print("File not found. Creating a new file.")
      new_file = open(self.filepath, "w")
      new_file.write("{}")
      new_file.close()
      return self.open_file()
    else:
      pass

  def get_dict(self):
    return json.load(self.loaded_file)

  def add(self, model_type, link):
    try:
      self.loaded_dict[model_type].append(link)
    except KeyError:
      self.loaded_dict[model_type] = []
      self.loaded_dict[model_type].append(link)
    else:
      pass
    self.save()

  def save(self):
    self.loaded_file = open(self.filepath, "w")
    json.dump(self.loaded_dict, self.loaded_file)
    self.loaded_file.close()
    self.open_file()

  def get_model(self, model_type, link):  
    r = requests.get(link, allow_redirects=True)
    filename = dict(r.headers)['Content-Disposition'].split('="')[1].replace('\"\'', '').replace('"', '')
    try:
      open("models/{}/{}".format(model_type, filename), "wb").write(r.content)
    except FileNotFoundError:
      os.makedirs("models/{}".format(model_type))
      open("models/{}/{}".format(model_type, filename), "wb").write(r.content)
    else:
      pass
  
  def get_all_models(self, model_type):
    for model_link in self.loaded_dict[model_type]:
      self.get_model(model_type, model_link)


