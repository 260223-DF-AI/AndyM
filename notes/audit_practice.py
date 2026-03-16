from pathlib import Path
import random


def do_practice(filepath, num_topics):
    # list all files in audit folder
    folder_path = Path(filepath)
    topics = [file.name for file in folder_path.iterdir() if file.is_file()]
    #print(topics)


    # use .sample() to randomly select some topics
    sample = random.sample(topics, num_topics)

    # get the name (filter out cXXX, .md)
    topics_name = [topic[5:-3] for topic in sample]


    content = []
    for file_path in sample:
        file_path = filepath + "/" + file_path
        try:
            with open(file_path, 'r') as file:
                content.append(file.read())  # append file content as a string
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return (topics_name, content)
        #print(sample)


if __name__ == "__main__":

    topics, content = do_practice("./audit1", 1)
    #print(topics)
    #print("content:",content)

    # this is where you would pipe the notes into chat + topics for questions

    # pipe output into file
    content_lines = content[0].split("\n")
    with open("output.txt","w") as file:
        file.write(f"write interview style questions based off the following topic: {topics[0]}\n")
        file.write(f"the following is the notes to base the questions off:")
        file.writelines(sentence + "\n" for sentence in content_lines)

    print("done")