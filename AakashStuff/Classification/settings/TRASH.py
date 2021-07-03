from . import load_datasets
scaleFactor = 4
config = {
    "models_dir": "models",
    "DATASET": "TRASH",
    "target_learning_rate": 0.001,
    "target_model_epochs": 50,
    "target_batch_size": 64,
    "model_name": "TRASH-KerasModel.model",

    "LOAD_TARGET_WEIGHTS": False,

    "IMG_W": 512 // scaleFactor,
    "IMG_H": 384 // scaleFactor,
    "CHANNELS": 1,
    "IMG_SHAPE": (384 // scaleFactor, 512 // scaleFactor, 1),
    "N_CLASSES": 10,
    "DATA_LOADER": load_datasets.load_data_garbage_classification,
    "mode": "train",
}
