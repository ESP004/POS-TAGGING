import nltk

REQUIRED_RESOURCES = [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
]


def download_resources():
    for resource in REQUIRED_RESOURCES:
        nltk.download(resource)
        
    print("\nAll NLTK resources are installed.")

if __name__ == "__main__":
    download_resources()