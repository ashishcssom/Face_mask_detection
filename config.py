import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")).replace("\\", "/")
prototxtPath=path+r"/models/deploy.prototxt" # Face detector model
weightsPath=path+r"/models/res10_300x300_ssd_iter_140000.caffemodel" # Trained face mask detector model
confidence=0.5
model=path+r"/models/mask_detector.model"
fps=35

