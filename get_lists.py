class SilverLists:
  def self(__init__):
    self.MAIN_LIST = {
      "sd_models": {
        "PMA-inpaint": "https://civitai.com/api/download/models/110119",
        "PMA Regular": "https://civitai.com/api/download/models/110085",
        "RLVZ-Regular": "https://civitai.com/api/download/models/130072",
        "RLVZ-Inpaint": "https://civitai.com/api/download/models/130090"
      }
    }

@property
def sd_models():
  return self.MAIN_LIST['sd_models']

@property
def loras():
  return self.MAIN_LIST['loras']

@property
def embeddings():
  return self.MAIN_LIST['embeddings']

@property
def styles():
  return self.MAIN_LIST['styles']


