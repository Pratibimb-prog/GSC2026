import os
from pathlib import Path

import gdown
import tensorflow as tf
from keras.layers import Dense

FILE_ID = "1o_jinpmPFLad1iGhAyapBbtpUT39d7Hy"

MODEL_PATH = Path(__file__).resolve().with_name("cnn_lstm_new_model.keras")

original_init = Dense.__init__


def _patched_init(self, *args, **kwargs):
    kwargs.pop("quantization_config", None)
    original_init(self, *args, **kwargs)


Dense.__init__ = _patched_init

# Force download if file not present OR corrupted
if not MODEL_PATH.exists() or MODEL_PATH.stat().st_size < 10_000:
    print("Downloading model...")

    gdown.download(id=FILE_ID, output=str(MODEL_PATH), quiet=False)

# Validate file after download
if not MODEL_PATH.exists():
    raise FileNotFoundError("Download failed: file not created")

if MODEL_PATH.stat().st_size < 10_000:
    raise ValueError("Downloaded file is corrupted or incomplete")

print("Loading model...")

model = tf.keras.models.load_model(str(MODEL_PATH), compile=False)

print(f"Model loaded successfully from {MODEL_PATH}")
print(f"Input shape: {model.input_shape}")
print(f"Output shape: {model.output_shape}")
