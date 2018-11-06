"""
This module captures constants used across the codebase.
"""
MODELS = ["CM", "CM3x3", "CN", "CN3x3", "CSD", "GLRLM", "GLRLM3x3", "HOG", "LBP", "LBP3x3"]
PROCESSED_VISUAL_DESCRIPTORS_DIR_PATH = "../dataset/visual_descriptors/processed/"
VISUAL_DESCRIPTORS_DIR_PATH_REGEX = "../dataset/visual_descriptors/*.csv"
DEVSET_TOPICS_DIR_PATH = "../dataset/textual_descriptors/devset_topics.xml"
VISUAL_DESCRIPTORS_DIR_PATH = "../dataset/visual_descriptors/"
TEXT_DESCRIPTORS_DIR_PATH = "../dataset/textual_descriptors/"
LOCATION_ID_KEY_ERROR = "Wrong input: Location id not found"
GENERIC_EXCEPTION_MESSAGE = "Exception encountered: "
VISUAL_DESCRIPTOR_MODEL_FOR_GRAPH_CREATION = "CN"