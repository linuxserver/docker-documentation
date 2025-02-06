import collections
import glob
import os

INPUT_PATH = "docs/images/*.md"
OUTPUT_PATH = "docs/images-by-category.md"


def main():
    image_to_description = {}
    category_to_images = collections.defaultdict(list)
    files = glob.glob(INPUT_PATH)
    for file in files:
        process_input(image_to_description, category_to_images, file)
    generate_output(image_to_description, category_to_images)

def process_input(image_to_description, category_to_images, file):
    filename = os.path.basename(file)
    image = filename.replace("docker-", "").replace(".md", "")
    with open(file) as input:
        header = False
        found = False
        for line in input:
            line = line.strip(" \t\n\r")
            if not header and line.startswith("---"):
                header = True
            elif header and line.startswith("---"):
                break
            elif line.startswith("description:"):
                description = line.replace("description: ", "").replace("\\n", " ").replace("\"", "").strip(" \t\n\r")
                image_to_description[image] = description if description else "No description"
                found = False
            elif line == "tags:":
                found = True
            elif not line.startswith("-"):
                found = False
            elif found:
                tag = line.replace("-", "", 1).strip(" \t\n\r")
                if tag == "Internal":
                    continue
                category_to_images[tag].append(image)

def generate_output(image_to_description, category_to_images):
    with open(OUTPUT_PATH, "w") as output:
        output.write("<!--- DO NOT CHANGE THIS FILE MANUALLY, IT IS AUTOMATICALLY GENERATED -->")
        output.write("<!--- GENERATED FROM https://github.com/linuxserver/docker-documentation/scripts/generate-images-by-category.py -->")
        output.write("# Images by Category\n\n")

        for category in sorted(category_to_images.keys()):
            if not category:
                continue
            output.write(f"## {category}\n\n")
            output.write(f"| Container | Description |\n")
            output.write(f"| --------- | ----------- |\n")
            for image in sorted(category_to_images[category]):
                output.write(f"| [{image.capitalize()}](images/docker-{image}.md) | {image_to_description[image]} |\n")
            output.write("\n")
        output.write("\n")

if __name__ == "__main__":
    main()
