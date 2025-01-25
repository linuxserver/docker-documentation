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
            if not header and line.strip().startswith("---"):
                header = True
            elif header and line.strip().startswith("---"):
                break
            elif line.strip().startswith("description:"):
                description = line.replace("description: ", "").replace("\\n", " ").replace("\"", "").strip(' \t\n\r')
                image_to_description[image] = description if description else "No description"
            elif line.rstrip() == "tags:":
                found = True
            elif not line.strip().startswith("-"):
                found = False
            elif found:
                tag = line.replace("-", "").strip(' \t\n\r')
                if tag == "Internal":
                    continue
                category_to_images[tag].append(image)

def generate_output(image_to_description, category_to_images):
    with open(OUTPUT_PATH, "w") as output:
        output.write("# Images by Category\n\n")

        for category in sorted(category_to_images.keys()):
            if not category:
                continue
            output.write(f"## {category}\n\n")
            output.write(f"| Container | Description |\n")
            output.write(f"| --------- | ----------- |\n")
            for image in sorted(category_to_images[category]):
                output.write(f"| [{image}](images/docker-{image}/) | {image_to_description[image]} |\n")
            output.write("\n")
        output.write("\n")

if __name__ == "__main__":
    main()
